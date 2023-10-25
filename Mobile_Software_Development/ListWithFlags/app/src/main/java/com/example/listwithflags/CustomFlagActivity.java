package com.example.listwithflags;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;

public class CustomFlagActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_custom_flag);

        Bundle b = getIntent().getExtras();
        String country = b.getString("country");
        String capital = b.getString("city");

        TextView disp_country = (TextView) findViewById(R.id.country_text);
        TextView disp_capital = (TextView) findViewById(R.id.city_text);
        disp_capital.setText(capital);
        disp_country.setText(country);
        Button but = (Button) findViewById(R.id.search_button);

        but.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String query = capital + ", " + country;
                try {
                    String enc_query = URLEncoder.encode(query, "UTF-8");
                    Uri uri = Uri.parse("https://www.google.com/search?q=" + enc_query);
                    Intent intent = new Intent(Intent.ACTION_VIEW, uri);
                    startActivity(intent);
                } catch (UnsupportedEncodingException e) {
                    throw new RuntimeException(e);
                }
            }
        });


    }
}