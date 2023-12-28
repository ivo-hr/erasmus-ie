package com.example.h8fulalarmclock;

import androidx.room.Entity;
import androidx.room.PrimaryKey;


@Entity
public class ReminderEntity {
    @PrimaryKey(autoGenerate = true)
    public int id;

    public String time;
    public String message;
    public int notificationFrequency;
    public boolean exponentialNotification;
}
