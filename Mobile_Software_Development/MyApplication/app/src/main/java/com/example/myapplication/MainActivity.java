package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    int surpriseCounter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        surpriseCounter = 0;
        TextView counter = (TextView)findViewById(R.id.surpriseCounter);
        counter.setText("NUMBER OF SURPRISES: " +  surpriseCounter);
        //button ID storage in variable
        Button surprise = (Button)findViewById(R.id.surprise);

        //Button interaction
        if (surprise != null){
            surprise.setOnClickListener((View.OnClickListener)
                    (new View.OnClickListener() {
                public final void onClick(View it) {
                    //Toast message
                    Toast.makeText((Context) MainActivity.this, "Surprise!🎊", Toast.LENGTH_LONG).show();
                    surpriseCounter++;
                    counter.setText("NUMBER OF SURPRISES: " +  surpriseCounter);
                }
            }));
        }

        Button unsurprise = (Button)findViewById(R.id.unsurprise);

        //Button interaction
        if (unsurprise != null){
            unsurprise.setOnClickListener((View.OnClickListener)
                    (new View.OnClickListener() {
                        public final void onClick(View it) {
                            //Toast message
                            Toast.makeText((Context) MainActivity.this, "oh...", Toast.LENGTH_LONG).show();
                            if (surpriseCounter > 0) surpriseCounter--;
                            counter.setText("NUMBER OF SURPRISES: " + surpriseCounter);
                        }
                    }));
        }
    }
}