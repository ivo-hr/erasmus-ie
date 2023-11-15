package com.example.lab7;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Bitmap;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MainActivity extends AppCompatActivity {
    private TextView outputText;
    private static final String TAG = "IT472";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        outputText = findViewById(R.id.outputText);
    }
    public void runTask(View v){
// VERSION 0
// Running a task on the UI Thread
        Log.i(TAG, "Blocking Task Started");
        try {
// simulate a long-running task
            Thread.sleep(10000); // Waits 10 seconds
            outputText.setText("Task Complete");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        Log.i(TAG, "Blocking Task Finished");
    }
    public void generateContent(View view) {
        outputText.setText("Random number: \n"+ Math.random());
    }

    public void loadImageInBackground(View v) {
        // Creates a service to execute threads
        ExecutorService service = Executors.newSingleThreadExecutor();
        // Creates a handle to recover the result from the
        Handler handler = new Handler(Looper.getMainLooper());
        service.execute(new Runnable() {
            @Override
            public void run() {
                Bitmap bitmap = webImageReader.readImage("https://www.lecturas.com/medio/2020/09/30/jesus-calleja_d2d07677_800x800.jpg");
                        handler.post(new Runnable() {
                            @Override
                            public void run() {
                                // Fill this function to set the image
                                // For example, you can update an ImageView with the loaded bitmap
                                ImageView img = findViewById(R.id.imageView);

                                img.setImageBitmap(bitmap);
                            }
                        });
            }
        });
    }
}

/*Advantages of using threads in Android:

1. **Concurrent Efficiency:**
   - Threads enable multiple tasks simultaneously, keeping the app responsive during operations.

2. **Performance Boost:**
   - Threads speed up tasks, enhancing overall app performance, especially for time-consuming operations.

3. **Resource Optimization:**
   - Threads allow different app components to work independently, making better use of device resources.

Disadvantages of using threads in Android:

1. **Coding Complexity:**
   - Thread management adds complexity to code, requiring careful handling to avoid issues like freezing or data conflicts.

2. **Potential Memory Impact:**
   - Threads consume extra memory, and excessive threads can lead to increased memory usage, impacting app performance over time.*/