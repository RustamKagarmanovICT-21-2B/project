package com.example.android_client;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentTransaction;

public class MainActivity extends AppCompatActivity implements LoginFragment.OnLoginListener {

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    // Загружаем LoginFragment при старте приложения
    if (savedInstanceState == null) {
      loadLoginFragment();
    }
  }

  private void loadLoginFragment() {
    LoginFragment loginFragment = new LoginFragment();
    FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
    transaction.replace(R.id.fragment_container, loginFragment);
    transaction.commit();
  }

  @Override
  public void onLoginSuccess() {
    // Загружаем ControlFragment после успешного входа
    ControlFragment controlFragment = new ControlFragment();
    FragmentTransaction transaction = getSupportFragmentManager().beginTransaction();
    transaction.replace(R.id.fragment_container, controlFragment);
    transaction.commit();
  }
}
