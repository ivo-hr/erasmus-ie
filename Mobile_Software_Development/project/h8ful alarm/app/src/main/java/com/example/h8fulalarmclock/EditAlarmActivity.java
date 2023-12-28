package com.example.h8fulalarmclock;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.media.RingtoneManager;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.SeekBar;
import android.widget.TimePicker;

import androidx.appcompat.app.WindowDecorActionBar;
import androidx.room.Room;

public class EditAlarmActivity extends AppCompatActivity {

    String ringtonePath = "select ringtone";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_alarm);

        TimePicker timePicker = findViewById(R.id.alarm_time_picker);
        timePicker.setIs24HourView(true); // Set the TimePicker to 24-hour mode
        //Get the cheboxes
        CheckBox sundayCheckbox = findViewById(R.id.sunday_checkbox);
        CheckBox mondayCheckbox = findViewById(R.id.monday_checkbox);
        CheckBox tuesdayCheckbox = findViewById(R.id.tuesday_checkbox);
        CheckBox wednesdayCheckbox = findViewById(R.id.wednesday_checkbox);
        CheckBox thursdayCheckbox = findViewById(R.id.thursday_checkbox);
        CheckBox fridayCheckbox = findViewById(R.id.friday_checkbox);
        CheckBox saturdayCheckbox = findViewById(R.id.saturday_checkbox);
        //Get the ringtone button
        Button ringtoneButton = findViewById(R.id.ringtone_button);
        //Get the save button
        Button saveButton = findViewById(R.id.save_alarm_button);
        //Get the speed seekbar
        SeekBar speedSeekBar = findViewById(R.id.speed_seek_bar);



        // If the activity was started with an alarm ID, load the alarm data from the database
        int alarmId = getIntent().getIntExtra("ALARM_ID", -1);
        if (alarmId != -1) {
            // Fetch the alarm from the database in a background thread
            new Thread(() -> {
                AppDatabase db = Room.databaseBuilder(getApplicationContext(),
                        AppDatabase.class, "database-name").build();
                AlarmEntity alarm = db.alarmDao().getById(alarmId);

                // Populate the UI with the alarm data in the main thread
                runOnUiThread(() -> {
                    String[] timeParts = alarm.time.split(":");
                    timePicker.setHour(Integer.parseInt(timeParts[0]));
                    timePicker.setMinute(Integer.parseInt(timeParts[1]));
                    //Set the checkboxes
                    sundayCheckbox.setChecked(alarm.days.charAt(0) == '1');
                    mondayCheckbox.setChecked(alarm.days.charAt(1) == '1');
                    tuesdayCheckbox.setChecked(alarm.days.charAt(2) == '1');
                    wednesdayCheckbox.setChecked(alarm.days.charAt(3) == '1');
                    thursdayCheckbox.setChecked(alarm.days.charAt(4) == '1');
                    fridayCheckbox.setChecked(alarm.days.charAt(5) == '1');
                    saturdayCheckbox.setChecked(alarm.days.charAt(6) == '1');
                    //Set the speed
                    speedSeekBar.setProgress((int) alarm.speed);

                });
            }).start();
        }

        // Set the onClickListener for the ringtone button
        ringtoneButton.setOnClickListener(v -> {
            Intent intent = new Intent(RingtoneManager.ACTION_RINGTONE_PICKER);
            intent.putExtra(RingtoneManager.EXTRA_RINGTONE_TYPE, RingtoneManager.TYPE_ALARM);
            intent.putExtra(RingtoneManager.EXTRA_RINGTONE_TITLE, "Select Ringtone");
            startActivityForResult(intent, 999);
        });


        // Set the onClickListener for the save button
        saveButton.setOnClickListener(v -> {
            // Get the selected time from the TimePicker
            int hour = timePicker.getHour();
            int minute = timePicker.getMinute();
            String time = hour + ":" + minute;


            // Get the selected days from the CheckBoxes
            String days = "";
            days += sundayCheckbox.isChecked() ? "1" : "0";
            days += mondayCheckbox.isChecked() ? "1" : "0";
            days += tuesdayCheckbox.isChecked() ? "1" : "0";
            days += wednesdayCheckbox.isChecked() ? "1" : "0";
            days += thursdayCheckbox.isChecked() ? "1" : "0";
            days += fridayCheckbox.isChecked() ? "1" : "0";
            days += saturdayCheckbox.isChecked() ? "1" : "0";


            // Get the speed from the SeekBar
            float speed = speedSeekBar.getProgress();

            // Get the ringtone from the Button
            String ringtone = ringtoneButton.getText().toString();

            // Create a new AlarmEntity
            AlarmEntity alarm = new AlarmEntity(time, days, true, speed, ringtone);

            // Save the alarm to the database in a background thread
            new Thread(() -> {
                AppDatabase db = Room.databaseBuilder(getApplicationContext(),
                        AppDatabase.class, "database-name").build();

                if (alarmId != -1) {
                    alarm.id = alarmId;
                    Log.d("EditAlarmActivity", "Updating alarm with ID: " + alarm.id);
                    db.alarmDao().update(alarm);

                }
                else{
                    //Get a new alarm id different from -1 and from the ones already in the database
                    int newId = 0;
                    while(db.alarmDao().getById(newId) != null || newId == -1){
                        newId++;
                    }
                    alarm.id = newId;
                    db.alarmDao().insert(alarm);
                    Log.d("EditAlarmActivity", "Creating new alarm with ID: " + alarm.id);
                }
                alarm.scheduleAlarm(EditAlarmActivity.this);
            }).start();

            // Go back to the AlarmsActivity
            Intent intent = new Intent(this, AlarmsActivity.class);
            startActivity(intent);
        });
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == 999 && resultCode == RESULT_OK) {
            Uri uri = data.getParcelableExtra(RingtoneManager.EXTRA_RINGTONE_PICKED_URI);
            Button ringtoneButton = findViewById(R.id.ringtone_button);
            if (uri != null) {
                ringtonePath = uri.toString();
                ringtoneButton.setText("ringtone selected");
            } else {
                ringtoneButton.setText("select ringtone");
            }
        }
    }
}