package com.example.jasonproject2;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    EditText editText;
    RadioButton radio1;
    RadioButton radio2;
    RadioButton radio3;

    @SuppressLint("WrongViewCast")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        editText=findViewById(R.id.editTextPhone);
        radio1=findViewById(R.id.radioRumah);
        radio2=findViewById(R.id.radioMobile);
        radio3=findViewById(R.id.radioKantor);

        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
    }

    public void showText(View view) {
        String phone =editText.getText().toString();
        String pilih="";
        if(radio1.isChecked()) {
            pilih="Telp Rumah";
        } else if(radio2.isChecked()) {
            pilih="Mobile";
        } else if (radio3.isChecked()) {
            pilih="Telp Kantor";
        }
        Toast.makeText(this, pilih+ ":" + phone, Toast.LENGTH_SHORT).show();
    }
}