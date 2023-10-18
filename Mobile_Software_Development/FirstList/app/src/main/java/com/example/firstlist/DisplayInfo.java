package com.example.firstlist;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class DisplayInfo extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_info);
// Read the variables from the bundle
        Bundle b = getIntent().getExtras();
        String city = b.getString("city");
        String country = b.getString("country");
        int city_population = b.getInt("city_population");
        int metro_population = b.getInt("metro_population");
// Link our widget to the variables
        TextView display_country = (TextView) findViewById(R.id.display_country);
        TextView display_city = (TextView) findViewById(R.id.display_city);
        TextView display_population = (TextView)
                findViewById(R.id.display_population);
        TextView display_metropolitan = (TextView)
                findViewById(R.id.display_metropolitan);
// Display the values on the screen
        display_country.setText(country);
        display_city.setText(city);
        display_population.setText(Integer.toString(city_population));
        display_metropolitan.setText(Integer.toString(metro_population));
    }
}