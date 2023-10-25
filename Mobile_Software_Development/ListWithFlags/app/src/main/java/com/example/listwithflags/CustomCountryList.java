package com.example.listwithflags;
import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class CustomCountryList extends ArrayAdapter {
    private String[] countryNames;
    private String[] capitalNames;
    private Integer[] imageid;
    private Activity context;
    public CustomCountryList(Activity context, String[] countryNames, String[]
            capitalNames, Integer[] imageid) {
        super(context, R.layout.row_item, countryNames);
        this.context = context;
        this.countryNames = countryNames;
        this.capitalNames = capitalNames;
        this.imageid = imageid;
    }
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        View row=convertView;
        LayoutInflater inflater = context.getLayoutInflater();
        if(convertView==null)
            row = inflater.inflate(R.layout.row_item, null, true);
        TextView textViewCountry = (TextView)
                row.findViewById(R.id.textViewCountry);
        TextView textViewCapital = (TextView) row.findViewById(R.id.textViewCapital);
        ImageView imageFlag = (ImageView) row.findViewById(R.id.imageViewFlag);
        textViewCountry.setText(countryNames[position]);
        textViewCapital.setText(capitalNames[position]);
        imageFlag.setImageResource(imageid[position]);

        textViewCountry.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String msg = "You clicked the country label of " + countryNames[position];
                Toast t = Toast.makeText(context, msg, Toast.LENGTH_SHORT);
                t.show();
            }
        });

        textViewCapital.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String msg = "You clicked the capital label of " + capitalNames[position];
                Toast t = Toast.makeText(context, msg, Toast.LENGTH_SHORT);
                t.show();
            }
        });

        imageFlag.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String msg = "You clicked the flag of " + countryNames[position];
                Toast t = Toast.makeText(context, msg, Toast.LENGTH_SHORT);
                t.show();

                Intent intent = new Intent(context, CustomFlagActivity.class);
                Bundle b = new Bundle();
                b.putString("country",countryNames[position]);
                b.putString("city", capitalNames[position]);

                intent.putExtras(b);

                getContext().startActivity(intent);
            }
        });

        return row;
    }

}

