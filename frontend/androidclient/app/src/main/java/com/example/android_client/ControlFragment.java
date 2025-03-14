import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class ControlFragment extends Fragment {

  private EditText editTextDelay;
  private Button buttonStartStop, buttonSetDelay;
  private Button buttonTurnAirConditioner, buttonGetAirConditionerStatus;
  private Button buttonTurnHeater, buttonGetHeaterStatus;

  private final String rpi = "http://192.168.0.3:8000";

  @Override
  public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
    View view = inflater.inflate(R.layout.fragment_control, container, false);
    editTextDelay = view.findViewById(R.id.editTextDelay);
    buttonStartStop = view.findViewById(R.id.buttonStartStop);
    buttonSetDelay = view.findViewById(R.id.buttonSetDelay);

    buttonStartStop.setOnClickListener(v -> startStopEngine());
    buttonSetDelay.setOnClickListener(v -> setDelay());
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

  private void startStopEngine() {
    sendRequest(rpi + "/startstop", "");
  // Кондиционер
  private void toggleAirConditioner() {
    String requestBody = "{ \"state\": \"toggle\" }";
    sendRequest(rpi + "/air-conditioner/turn", requestBody);
  }

  private void setDelay() {
    String delayStr = editTextDelay.getText().toString();
    int delay;
    try {
      delay = Integer.parseInt(delayStr);
      if (delay < 1 || delay > 44200) { // 44200 минут = 30 дней
        Toast.makeText(getActivity(), "Время должно быть от 1 до 44200 минут", Toast.LENGTH_SHORT).show();
        return;
      }
      sendRequest(rpi + "/delay?minutes=" + delay, "");
    } catch (NumberFormatException e) {
      Toast.makeText(getActivity(), "Введите корректное число", Toast.LENGTH_SHORT).show();
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
      try {
        URL url = new URL(urlString);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        if (requestBody.isEmpty()) {
          connection.setRequestMethod("GET");
        } else {
          connection.setRequestMethod("POST");
        }
        connection.setDoOutput(true);
        connection.setRequestProperty("Content-Type", "application/json");

        OutputStream os = connection.getOutputStream();
        os.write(requestBody.getBytes());
        os.flush();
        os.close();
        if (!requestBody.isEmpty()) {
          OutputStream os = connection.getOutputStream();
          os.write(requestBody.getBytes());
          os.flush();
          os.close();
        }

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) {
          getActivity().runOnUiThread(() -> Toast.makeText(getActivity(), "Запрос отправлен", Toast.LENGTH_SHORT).show());
          getActivity().runOnUiThread(() -> Toast.makeText(getActivity(), "Запрос выполнен", Toast.LENGTH_SHORT).show());
        } else {
          getActivity().runOnUiThread(() -> Toast.makeText(getActivity(), "Ошибка: " + responseCode, Toast.LENGTH_SHORT).show());
        }
