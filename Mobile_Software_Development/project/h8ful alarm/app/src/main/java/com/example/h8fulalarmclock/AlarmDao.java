package com.example.h8fulalarmclock;

import androidx.room.Dao;
import androidx.room.Delete;
import androidx.room.Insert;
import androidx.room.Query;
import androidx.room.Update;

import java.util.List;

@Dao
public interface AlarmDao {
    @Query("SELECT * FROM AlarmEntity")
    List<AlarmEntity> getAll();

    @Query("SELECT * FROM AlarmEntity WHERE id = :id")
    AlarmEntity getById(int id);
    @Insert
    void insert(AlarmEntity alarm);

    @Delete
    void delete(AlarmEntity alarm);

    @Update
    void update(AlarmEntity alarm);
}