package com.example.android_client;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class ControlFragment extends Fragment {

  private Button buttonTurnAirConditioner, buttonGetAirConditionerStatus;
  private Button buttonTurnHeater, buttonGetHeaterStatus;

  private final String rpi = "http://192.168.0.3:8000";

  @Nullable
  @Override
  public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
    View view = inflater.inflate(R.layout.fragment_control, container, false);

    // Кнопки кондиционера
    buttonTurnAirConditioner = view.findViewById(R.id.buttonTurnAirConditioner);
    buttonGetAirConditionerStatus = view.findViewById(R.id.buttonAirConditionerStatus);

    // Кнопки печки
    buttonTurnHeater = view.findViewById(R.id.buttonTurnHeater);
    buttonGetHeaterStatus = view.findViewById(R.id.buttonHeaterStatus);

    // Обработчики для кондиционера
    buttonTurnAirConditioner.setOnClickListener(v -> toggleAirConditioner());
    buttonGetAirConditionerStatus.setOnClickListener(v -> getAirConditionerStatus());

    // Обработчики для печки
    buttonTurnHeater.setOnClickListener(v -> toggleHeater());
    buttonGetHeaterStatus.setOnClickListener(v -> getHeaterStatus());

    return view;
  }

  // Кондиционер
  private void toggleAirConditioner() {
    String requestBody = "{ \"state\": \"toggle\" }";
    sendRequest(rpi + "/air-conditioner/turn", requestBody);
  }

  private void getAirConditionerStatus() {
    sendRequest(rpi + "/air-conditioner/status", "");
  }

  // Печка
  private void toggleHeater() {
    String requestBody = "{ \"state\": \"toggle\" }";
    sendRequest(rpi + "/heater/turn", requestBody);
  }

  private void getHeaterStatus() {
    sendRequest(rpi + "/heater/status", "");
  }

  private void sendRequest(String urlString, String requestBody) {
    new Thread(() -> {
      try {
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        if (requestBody.isEmpty()) {
          connection.setRequestMethod("GET");
        } else {
          connection.setRequestMethod("POST");
        }
        connection.setDoOutput(true);
        connection.setRequestProperty("Content-Type", "application/json");

        if (!requestBody.isEmpty()) {
          OutputStream os = connection.getOutputStream();
          os.write(requestBody.getBytes());
          os.flush();
          os.close();
        }

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) {
          getActivity().runOnUiThread(() -> Toast.makeText(getActivity(), "Запрос выполнен", Toast.LENGTH_SHORT).show());
        } else {
          getActivity().runOnUiThread(() -> Toast.makeText(getActivity(), "Ошибка: " + responseCode, Toast.LENGTH_SHORT).show());
        }
      } catch (Exception e) {
        getActivity().runOnUiThread(() -> Toast.makeText(getActivity(), "Ошибка: " + e.getMessage(), Toast.LENGTH_SHORT).show());
      }
    }).start();
  }
}
