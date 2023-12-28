package com.example.h8fulalarmclock;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.Switch;
import android.widget.TextView;

import java.util.List;

public class ListAlarmAdapter extends BaseAdapter {
    private Context context;
    private List<AlarmEntity> alarms;
    private AppDatabase db;

    public ListAlarmAdapter(Context context, List<AlarmEntity> alarms, AppDatabase db) {
        this.context = context;
        this.alarms = alarms;
        this.db = db;
    }

    @Override
    public int getCount() {
        return alarms.size();
    }

    @Override
    public Object getItem(int position) {
        return alarms.get(position);
    }

    @Override
    public long getItemId(int position) {
        return alarms.get(position).id;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        if (convertView == null) {
            convertView = LayoutInflater.from(context).inflate(R.layout.list_item_alarm, parent, false);
        }

        TextView alarmText = convertView.findViewById(R.id.alarm_text);
        String alarmTime = alarms.get(position).time;
        //Add day initials to alarm time
        if (alarms.get(position).days.charAt(0) == '1') alarmTime += " Sun";
        if (alarms.get(position).days.charAt(1) == '1') alarmTime += " Mon";
        if (alarms.get(position).days.charAt(2) == '1') alarmTime += " Tue";
        if (alarms.get(position).days.charAt(3) == '1') alarmTime += " Wed";
        if (alarms.get(position).days.charAt(4) == '1') alarmTime += " Thu";
        if (alarms.get(position).days.charAt(5) == '1') alarmTime += " Fri";
        if (alarms.get(position).days.charAt(6) == '1') alarmTime += " Sat";
        //alarmTime.trim();
        alarmTime.replace(" ", ", ");

        alarmText.setText(alarmTime); // Set the text of the TextView to the alarm time
        alarmText.setOnClickListener(v -> {
            AlarmEntity clickedAlarm = alarms.get(position);
            clickedAlarm.setEnabled(!clickedAlarm.isEnabled);
            //open edit alarm activity
            Intent intent = new Intent(context, EditAlarmActivity.class);
            intent.putExtra("ALARM_ID", clickedAlarm.getId());
            context.startActivity(intent);
        });
        ImageView deleteAlarm = convertView.findViewById(R.id.delete_alarm);
        deleteAlarm.setOnClickListener(v -> {
            AlarmEntity alarmToDelete = alarms.get(position);
            alarms.remove(position);
            notifyDataSetChanged();

            new Thread(() -> {
                db.alarmDao().delete(alarmToDelete);
            }).start();

        });
        Switch alarmSwitch = convertView.findViewById(R.id.alarm_switch);
        alarmSwitch.setChecked(alarms.get(position).isEnabled);

        alarmSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
            AlarmEntity alarmToUpdate = alarms.get(position);
            alarmToUpdate.setEnabled(isChecked);

            if (isChecked) {
                alarmToUpdate.scheduleAlarm(context);
            } else {
                alarmToUpdate.cancelAlarm(context);
            }
            new Thread(() -> {
                db.alarmDao().update(alarmToUpdate);
            }).start();
        });

        return convertView;
    }
}