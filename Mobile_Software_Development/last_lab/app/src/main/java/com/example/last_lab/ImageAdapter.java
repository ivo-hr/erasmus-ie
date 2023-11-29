
package com.example.last_lab;

import android.content.Context;
import android.os.SystemClock;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.ImageRequest;
import com.android.volley.toolbox.Volley;
import java.util.List;

public class ImageAdapter extends RecyclerView.Adapter<ImageAdapter.ImageViewHolder> {

    private List<String> imageTitles;
    private Context context;
    private RequestQueue requestQueue;

    public ImageAdapter(Context context, List<String> imageTitles) {
        this.context = context;
        this.imageTitles = imageTitles;
        this.requestQueue = Volley.newRequestQueue(context);
    }

    @NonNull
    @Override
    public ImageViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_image, parent, false);
        return new ImageViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull ImageViewHolder holder, int position) {
        holder.bindData(imageTitles.get(position));
    }

    @Override
    public int getItemCount() {
        return imageTitles.size();
    }

    class ImageViewHolder extends RecyclerView.ViewHolder {

        private ImageView imageView;
        private TextView textViewTitle;
        private TextView textViewLoadTime;

        ImageViewHolder(@NonNull View itemView) {
            super(itemView);
            imageView = itemView.findViewById(R.id.imageViewItem);
            textViewTitle = itemView.findViewById(R.id.textViewTitle);
            textViewLoadTime = itemView.findViewById(R.id.textViewLoadTime);
        }

        void bindData(String title) {
            // Record start time
            long startTime = SystemClock.elapsedRealtime();

            // Load and display the image using Volley
            loadImage();

            // Calculate and display the time taken
            long elapsedTime = SystemClock.elapsedRealtime() - startTime;
            textViewLoadTime.setText("Time taken: " + (elapsedTime) + " miliseconds");

            // Set the title
            textViewTitle.setText(title);
        }

        private void loadImage() {
            // URL for dynamically fetching images
            String imageUrl = "https://picsum.photos/200?" + System.currentTimeMillis();

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
}
