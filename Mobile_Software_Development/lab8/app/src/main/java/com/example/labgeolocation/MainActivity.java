package com.example.labgeolocation;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.annotation.SuppressLint;
import android.content.Intent;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.util.Log;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class MainActivity extends AppCompatActivity implements LocationListener {

    private TextView mLocationText;   // TextView to display the raw location data
    private TextView locality;         // TextView to display the location address
    private LocationManager locationManager;    // Manages location services
    private long minTime = 500;              // Minimum time interval between location updates (in milliseconds)
    private float minDistance = 1;           // Minimum distance between location updates (in meters)
    private static final int MY_PERMISSION_GPS = 1;   // Request code for GPS permission

    Button setMinButton;  // Button to set the minimum time and distance between location updates
    Button showListButton;  // Button to show the list of locations
    EditText minTimeInput;  // EditText to get the minimum time between location updates
    EditText minDistanceInput;  // EditText to get the minimum distance between location updates

    ArrayList<String> locationList = new ArrayList<>();  // ArrayList to store location data

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mLocationText = (TextView) findViewById(R.id.location);   // Initialize mLocationText
        locality = (TextView) findViewById(R.id.locality);         // Initialize locality TextView
        setUpLocation();  // Set up location services

        setMinButton = (Button) findViewById(R.id.updateMinsBut);  // Initialize setMinButton
        showListButton = (Button) findViewById(R.id.showListBut);  // Initialize showListButton
        minTimeInput = (EditText) findViewById(R.id.minTimeTxt);  // Initialize minTimeInput
        minDistanceInput = (EditText) findViewById(R.id.minDistTxt);  // Initialize minDistanceInput



        // Set onClickListener for setMinButton
        setMinButton.setOnClickListener(v -> {
            // Set the minimum time and distance between location updates
            if (minTimeInput.getText().toString().equals("")) {
                minTimeInput.setText("500");
                Toast.makeText(this, "Resetting minimum time...", Toast.LENGTH_SHORT).show();
            }
            if (minDistanceInput.getText().toString().equals("")) {
                minDistanceInput.setText("1");
                Toast.makeText(this, "Resetting minimum distance...", Toast.LENGTH_SHORT).show();
            }
            //Set the minimum time and distance between location updates in int
            minTime = Integer.parseInt(minTimeInput.getText().toString());
            minDistance = Integer.parseInt(minDistanceInput.getText().toString());
            Toast.makeText(this, "Minimum time and distance updated!", Toast.LENGTH_SHORT).show();
            setUpLocation();
        });

        // Set onClickListener for showListButton
        showListButton.setOnClickListener(v -> {
            // Show the list of locations
            if (locationList.isEmpty()) {
                Toast.makeText(this, "No locations to show!", Toast.LENGTH_SHORT).show();
            } else {
                // Create a new intent to start the ListActivity
                Intent intent = new Intent(MainActivity.this, ListActivity.class);
                // Pass the locationList to the ListActivity
                intent.putExtra("locationList", locationList);
                // Start the ListActivity
                startActivity(intent);
            }
        });
    }

    private void setUpLocation() {
        locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);

        // Check if the app has permission to access GPS
        if (ActivityCompat.checkSelfPermission(MainActivity.this,
                Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            // Request permission if not granted
            ActivityCompat.requestPermissions(MainActivity.this,
                    new String[]{Manifest.permission.ACCESS_FINE_LOCATION},
                    MY_PERMISSION_GPS);
        } else {
            // Start listening for location updates
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, minTime, minDistance, this);
            Log.i("Lab9", "started location updates");
            Location location = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
            onLocationChanged(location);
        }
    }


    @SuppressLint("DefaultLocale")
    public void onLocationChanged(Location location) {
        String latestLocation = "";

        Log.d("GPSLOCATION", "LOCATION CHANGED!"); // Log location change event

        if (location != null) {
            // Format the location data
            latestLocation = String.format(
                    "Current Location: Latitude %f Longitude : %f",
                    location.getLatitude(), location.getLongitude());
            Log.d("GPSLOCATION", "LOCATION formatted for text view!");
        }
        mLocationText.setText("GPS Location" + "\n" + latestLocation);  // Set the raw location data

        try {
            // Use Geocoder to get address information from latitude and longitude
            Geocoder geo = new Geocoder(MainActivity.this.getApplicationContext(), Locale.getDefault());
            List<Address> addresses = geo.getFromLocation(location.getLatitude(), location.getLongitude(), 1);

            if (addresses.isEmpty()) {
                locality.setText("Waiting for Location");
            } else {
                // Set the address information in the locality TextView
                if (addresses.size() > 0) {
                    int size = addresses.size() - 1;
                    String address = addresses.get(size).getFeatureName() + ", " +
                            addresses.get(size).getLocality() + ", " +
                            addresses.get(size).getAdminArea() + ", " +
                            addresses.get(size).getCountryName();
                    locality.setText(address);
                    locationList.add(address);
                }
            }
        } catch (Exception e) {
            // Handle exceptions related to Geocoder
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        // Handle permission request result
        switch (requestCode) {
            case MY_PERMISSION_GPS:
                if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    // All good!
                } else {
                    Toast.makeText(this, "Need your location!", Toast.LENGTH_SHORT).show();
                }
                break;
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        setUpLocation();  // Restart location updates when the activity resumes
        Log.i("Lab9", "restarted location updates");
    }

    @Override
    protected void onPause() {
        super.onPause();
        locationManager.removeUpdates(this);  // Stop location updates when the activity is paused
        Log.i("Lab9", "stopped location updates");
    }
}
