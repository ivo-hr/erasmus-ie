package com.example.h8fulalarmclock;
import androidx.room.Database;
import androidx.room.RoomDatabase;

@Database(entities = {AlarmEntity.class, ReminderEntity.class}, version = 1)
public abstract class AppDatabase extends RoomDatabase {
    public abstract AlarmDao alarmDao();
    public abstract ReminderDao reminderDao();
}