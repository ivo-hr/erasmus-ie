package com.example.h8fulalarmclock;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ListView;

import androidx.room.Room;

import java.util.List;

public class AlarmsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_alarms);

        ListView alarmsList = findViewById(R.id.alarms_list);

        // Get a database instance
        AppDatabase db = Room.databaseBuilder(getApplicationContext(),
                AppDatabase.class, "database-name").build();

        // Get the alarms from the database in a background thread
        new Thread(() -> {
            List<AlarmEntity> alarms = db.alarmDao().getAll();

            // Update the ListView in the main thread
            runOnUiThread(() -> {
                ListAlarmAdapter adapter = new ListAlarmAdapter(this, alarms, db);
                alarmsList.setAdapter(adapter);
            });
        }).start();

        alarmsList.setOnItemClickListener((parent, view, position, id) -> {
            AlarmEntity clickedAlarm = (AlarmEntity) parent.getItemAtPosition(position);
            Intent intent = new Intent(AlarmsActivity.this, EditAlarmActivity.class);
            intent.putExtra("ALARM_ID", clickedAlarm.getId());
            startActivity(intent);
        });

        Button addAlarmButton = findViewById(R.id.add_alarm);
        addAlarmButton.setOnClickListener(v -> {
            Intent intent = new Intent(AlarmsActivity.this, EditAlarmActivity.class);
            startActivity(intent);
        });



    }

    @Override
    public void onBackPressed() {
        super.onBackPressed();
        Intent intent = new Intent(AlarmsActivity.this, MainActivity.class);
        startActivity(intent);
    }
}