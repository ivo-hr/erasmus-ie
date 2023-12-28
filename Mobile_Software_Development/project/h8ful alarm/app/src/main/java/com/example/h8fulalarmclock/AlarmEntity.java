package com.example.h8fulalarmclock;

import android.annotation.SuppressLint;
import android.app.AlarmManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Build;
import android.util.Log;

import java.util.Calendar;
import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity
public class AlarmEntity {
    @PrimaryKey(autoGenerate = true)
    public int id;

    public String time;
    public String days;
    public boolean isEnabled;

    public float speed;

    public String ringtone;

    public AlarmEntity(String time, String days, boolean isEnabled, float speed, String ringtone) {
        this.time = time;
        this.days = days;
        this.isEnabled = isEnabled;
        this.speed = speed;
        this.ringtone = ringtone;
    }

    public int getId() {
        return id;
    }

    public void setEnabled(boolean isChecked) {
        isEnabled = isChecked;
    }


    public void scheduleAlarm(Context context) {
        AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
        Intent intent = new Intent(context, AlarmReceiver.class);
        intent.putExtra("ALARM_ID", id);

        // Get the days of the week that the alarm should repeat on
        boolean[] days = new boolean[7];
        for (int i = 0; i < 7; i++) {
            days[i] = this.days.charAt(i) == '1';
        }

        //if no days are selected, set the alarm to go off today/tomorrow
        if (!days[0] && !days[1] && !days[2] && !days[3] && !days[4] && !days[5] && !days[6]) {
            Calendar calendar = Calendar.getInstance();
            calendar.set(Calendar.HOUR_OF_DAY, Integer.parseInt(time.split(":")[0]));
            calendar.set(Calendar.MINUTE, Integer.parseInt(time.split(":")[1]));
            calendar.set(Calendar.SECOND, 0);
            if (calendar.before(Calendar.getInstance())) {
                calendar.add(Calendar.DAY_OF_YEAR, 1);
            }
            // Set an alarm to go off at that time
            PendingIntent pendingIntent = PendingIntent.getBroadcast(context, id, intent, PendingIntent.FLAG_IMMUTABLE);
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
                if (alarmManager.canScheduleExactAlarms())
                    alarmManager.setExact(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
                else
                    alarmManager.set(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
            }
            else
                try {
                    alarmManager.setExact(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
                }
                catch (Exception e) {
                    alarmManager.set(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
                }
            Log.d("AlarmEntity", "scheduledAlarm: " + calendar.toString());
        }
        // For each day of the week
        else {
            for (int i = 0; i < 7; i++) {
                if (days[i]) {
                    // Calculate the time in milliseconds since the epoch for the next occurrence of that day at the alarm time
                    Calendar calendar = Calendar.getInstance();
                    calendar.set(Calendar.DAY_OF_WEEK, i + 1);
                    calendar.set(Calendar.HOUR_OF_DAY, Integer.parseInt(time.split(":")[0]));
                    calendar.set(Calendar.MINUTE, Integer.parseInt(time.split(":")[1]));
                    calendar.set(Calendar.SECOND, 0);
                    if (calendar.before(Calendar.getInstance())) {
                        calendar.add(Calendar.WEEK_OF_YEAR, 1);
                    }

                    // Set an alarm to go off at that time
                    PendingIntent pendingIntent = PendingIntent.getBroadcast(context, id * 10 + i, intent, PendingIntent.FLAG_IMMUTABLE);
                    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S) {
                        if (alarmManager.canScheduleExactAlarms())
                            alarmManager.setExact(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
                        else
                            alarmManager.set(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
                    }
                    else
                        try {
                            alarmManager.setExact(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
                        }
                        catch (Exception e) {
                            alarmManager.set(AlarmManager.RTC_WAKEUP, calendar.getTimeInMillis(), pendingIntent);
                        }



                    Log.d("AlarmEntity", "scheduledRepeatingAlarm: " + calendar.toString());
                }
            }
        }
    }

    public void cancelAlarm(Context context) {
        AlarmManager alarmManager = (AlarmManager) context.getSystemService(Context.ALARM_SERVICE);
        Intent intent = new Intent(context, AlarmReceiver.class);
        PendingIntent pendingIntent = PendingIntent.getBroadcast(context, id, intent, PendingIntent.FLAG_IMMUTABLE);

        alarmManager.cancel(pendingIntent);
    }

    public boolean isEnabled() {
        return isEnabled;
    }

    public String getRingtone() {
        return ringtone;
    }

    public int getSpeed() {
        return (int) speed;
    }
}
