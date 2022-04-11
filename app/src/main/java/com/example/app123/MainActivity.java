package com.example.app123;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
//<<<<<<< HEAD
        setContentView(R.layout.main);
//=======
//        setContentView(R.layout.activity_main);
//>>>>>>> 706b965e2764b43a3f70dd09d131a5429b94c807
    }
}