
package com.example.last_lab;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.last_lab.ImageAdapter;

import java.util.ArrayList;
import java.util.List;

public class ImageListActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_image_list);

        // Sample list of image titles
        List<String> imageTitles = generateImageTitles();

        // Set up RecyclerView
        RecyclerView recyclerView = findViewById(R.id.recyclerViewImages);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        ImageAdapter imageAdapter = new ImageAdapter(this, imageTitles);
        recyclerView.setAdapter(imageAdapter);
    }

    private List<String> generateImageTitles() {
        List<String> imageTitles = new ArrayList<>();
        for (int i = 1; i <= 10; i++) {
            imageTitles.add("Image " + i);
        }
        return imageTitles;
    }
}
