package com.example.volleyv1;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    // TextView to display the results
    private TextView mTextViewResult;

    // RequestQueue for handling network requests
    private RequestQueue mQueue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize UI components
        mTextViewResult = findViewById(R.id.text_view_result);
        Button buttonJSON = findViewById(R.id.buttonJSON);
        Button buttonString = findViewById(R.id.buttonString);

        // Initialize Volley RequestQueue
        mQueue = Volley.newRequestQueue(this);

        // Set click listeners for the buttons
        buttonJSON.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Trigger JSON parsing method when JSON button is clicked
                jsonParse();
            }
        });
        buttonString.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Trigger string parsing method when String button is clicked
                stringParse();
            }
        });
    }

    // Method to perform a String request
    private void stringParse() {
        // URL for the String request
        String url = "https://www.youtube.com";

        // Create a StringRequest for the specified URL
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    public void onResponse(String response) {
                        // Display the first 500 characters of the response in the TextView
                        mTextViewResult.setText("Response is: " + response.substring(0, 500));
                    }
                },
                new Response.ErrorListener() {
                    public void onErrorResponse(VolleyError error) {
                        // Handle errors in the network request
                        Log.d("Error", "Some kind of Error");
                    }
                });

        // Add the StringRequest to the RequestQueue
        mQueue.add(stringRequest);
    }

    // Method to perform a JSON request
    private void jsonParse() {
        // URL for the JSON request
        String url = "https://raw.githubusercontent.com/luismirallesp/JsonObjects/main/Employees.json";

        // Create a JsonObjectRequest for the specified URL
        JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            // Extract 'employees' array from the JSON response
                            JSONArray jsonArray = response.getJSONArray("employees");

                            for (int i = 0; i < jsonArray.length(); i++) {
                                // Extract information for each employee and display in the TextView
                                JSONObject employee = jsonArray.getJSONObject(i);
                                String firstName = employee.getString("firstname");
                                int age = employee.getInt("age");
                                String mail = employee.getString("mail");

                                // Append employee details to the TextView
                                mTextViewResult.append(firstName + ", " + String.valueOf(age) + ", " + mail + "\n\n");
                            }
                        } catch (JSONException e) {
                            // Handle JSON parsing errors
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // Handle errors in the JSON request
                        error.printStackTrace();
                    }
                });

        // Add the JsonObjectRequest to the RequestQueue
        mQueue.add(request);
    }
}
