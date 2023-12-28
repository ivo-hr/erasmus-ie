package com.example.h8fulalarmclock;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

import androidx.room.Room;

public class AlarmReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        Intent serviceIntent = new Intent(context, AlarmService.class);
        int alarmId = intent.getIntExtra("ALARM_ID", -1);
        serviceIntent.putExtra("ALARM_ID", alarmId);
        context.startService(serviceIntent);
        Log.d("AlarmReceiver", "Alarm with id " + alarmId + " received");
        // Reschedule the alarm
        if (alarmId != -1) {
            AppDatabase db = Room.databaseBuilder(context, AppDatabase.class, "database-name").build();
            new Thread(() -> {
                AlarmEntity alarm = db.alarmDao().getById(alarmId);
                if (alarm != null && alarm.isEnabled()) {
                    alarm.scheduleAlarm(context);
                }
            }).start();
        }
    }
}