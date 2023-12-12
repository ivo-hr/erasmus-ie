package com.example.h8fulalarmclock;

import android.app.Service;
import android.content.Intent;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.IBinder;

import androidx.annotation.Nullable;
import androidx.room.Room;

public class AlarmService extends Service {
    private MediaPlayer mediaPlayer;

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        int alarmId = intent.getIntExtra("ALARM_ID", -1);
        if (alarmId != -1) {
            new Thread(() -> {
                AppDatabase db = Room.databaseBuilder(getApplicationContext(),
                        AppDatabase.class, "database-name").build();
                AlarmEntity alarm = db.alarmDao().getById(alarmId);
                if (alarm != null) {
                    try {
                        mediaPlayer = MediaPlayer.create(this, Uri.parse(alarm.getRingtone()));
                    }
                    catch (Exception e) {
                        mediaPlayer = MediaPlayer.create(this, R.raw.alarm);
                    }
                    mediaPlayer.start();
                }
            }).start();
        }

        // Start the alarm screen activity
        Intent alarmScreenIntent = new Intent(this, AlarmScreenActivity.class);
        alarmScreenIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        startActivity(alarmScreenIntent);

        return START_STICKY;
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        if (mediaPlayer != null) {
            mediaPlayer.stop();
            mediaPlayer.release();
        }
    }
}