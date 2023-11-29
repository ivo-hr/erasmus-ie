package com.example.last_lab;

import android.content.Intent;
import android.os.Bundle;
import android.os.SystemClock;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.ImageRequest;
import com.android.volley.toolbox.Volley;
import androidx.appcompat.app.AppCompatActivity;


public class MainActivity extends AppCompatActivity {

    private ImageView imageView;
    private Button buttonLoadImage;
    private TextView textViewTime;
    private RequestQueue requestQueue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize UI components
        imageView = findViewById(R.id.imageView);
        buttonLoadImage = findViewById(R.id.buttonLoadImage);
        textViewTime = findViewById(R.id.textViewTime);

        // Initialize Volley RequestQueue
        requestQueue = Volley.newRequestQueue(this);

        // Set click listener for the button
        buttonLoadImage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Record start time
                long startTime = SystemClock.elapsedRealtime();

                // Load and display the image using Volley
                loadImage();

                // Calculate and display the time taken
                long elapsedTime = SystemClock.elapsedRealtime() - startTime;
                textViewTime.setText("Time taken: " + elapsedTime + " ms");
            }
        });

        // Set click listener for the "Show Images" button
        Button buttonShowImages = findViewById(R.id.buttonShowImages);
        buttonShowImages.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Navigate to the new screen to show images
                Intent intent = new Intent(MainActivity.this, ImageListActivity.class);
                startActivity(intent);
            }
        });
    }

    private void loadImage() {
        // URL of the image to be loaded (replace with your image URL)
        String imageUrl = "https://www.196flavors.com/wp-content/uploads/2021/10/croquetas-de-pollo-2fp.jpg";

        // Create an ImageRequest for the specified URL
        ImageRequest imageRequest = new ImageRequest(
                imageUrl,
                new Response.Listener<android.graphics.Bitmap>() {
                    @Override
                    public void onResponse(android.graphics.Bitmap response) {
                        // Display the loaded image in the ImageView
                        imageView.setImageBitmap(response);
                    }
                },
                0,
                0,
                ImageView.ScaleType.CENTER_CROP,
                null,
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Handle errors in the image request
                        error.printStackTrace();
                    }
                });

        // Add the ImageRequest to the RequestQueue
        requestQueue.add(imageRequest);
    }
}
