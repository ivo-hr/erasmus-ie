package com.example.h8fulalarmclock;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.widget.Button;
import android.widget.TextView;

import java.time.format.DateTimeFormatter;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        //Set current time in 24h to textview
        TextView currentTime = (TextView) findViewById(R.id.current_time);
        currentTime.setText(java.time.LocalTime.now().toString());
        //Set current date to textview
        TextView currentDate = (TextView) findViewById(R.id.current_date);
        DateTimeFormatter wdmyFormat = DateTimeFormatter.ofPattern("EEE, d MMM yyyy");
        String formattedDate = java.time.LocalDate.now().format(wdmyFormat);
        currentDate.setText(formattedDate);

        //Update date and time every minute
        final Handler handler = new Handler(Looper.getMainLooper());
        Runnable runnable = new Runnable() {
            @Override
            public void run() {
                currentTime.setText(java.time.LocalTime.now().toString());
                String formattedDate = java.time.LocalDate.now().format(wdmyFormat);
                currentDate.setText(formattedDate);
                handler.postDelayed(this, 60000); // 60 seconds delay
            }
        };

        handler.post(runnable); // start the updates


        //Set alarm time to textview
        TextView alarmTime = (TextView) findViewById(R.id.next_alarm);
        //TODO: Get alarm time from database
        alarmTime.setText("07:00");

        //Set reminder text to textview
        TextView reminderText = (TextView) findViewById(R.id.next_reminder);
        //TODO: Get reminder text from database
        reminderText.setText("take your medicine!");

        //Set reminder date/time to textview
        TextView reminderTime = (TextView) findViewById(R.id.reminder_time);
        //TODO: Get reminder time from database
        reminderTime.setText("12 dec 12:00");

        //BUTTONS
        Button alarmButton = (Button) findViewById(R.id.but_alarm);
        Button reminderButton = (Button) findViewById(R.id.but_reminder);
        Button settingsButton = (Button) findViewById(R.id.but_settings);

        //go to alarm activity
        alarmButton.setOnClickListener(v -> {
            //Go to alarm activity
            Intent intent = new Intent(this, AlarmsActivity.class);
            startActivity(intent);

        });

        //go to reminder activity
        reminderButton.setOnClickListener(v -> {
            //TODO: Go to reminder activity
        });

        //go to settings activity
        settingsButton.setOnClickListener(v -> {
            //TODO: Go to settings activity

        });
    }
}
