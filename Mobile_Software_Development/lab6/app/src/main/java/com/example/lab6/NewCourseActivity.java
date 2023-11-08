package com.example.lab6;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class NewCourseActivity extends AppCompatActivity {

    // creating a variables for our button and edittext.
    private EditText nameEdt, surnameEdt, emailEdt, phoneEdt;
    private Button courseBtn;

    // creating a constant string variable for our
    // course name, description and duration.
    public static final String EXTRA_ID = "com.gtappdevelopers.gfgroomdatabase.EXTRA_ID";
    public static final String EXTRA_NAME = "com.gtappdevelopers.gfgroomdatabase.EXTRA_NAME";
    public static final String EXTRA_SURNAME = "com.gtappdevelopers.gfgroomdatabase.EXTRA_SURNAME";
    public static final String EXTRA_EMAIL = "com.gtappdevelopers.gfgroomdatabase.EXTRA_EMAIL";

    public static final String EXTRA_PHONE = "com.gtappdevelopers.gfgroomdatabase.EXTRA_PHONE";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_course);

        // initializing our variables for each view.
        nameEdt = findViewById(R.id.idEdtName);
        surnameEdt = findViewById(R.id.idEdtSurname);
        emailEdt = findViewById(R.id.idEdtEmail);
        phoneEdt = findViewById(R.id.idEdtPhone);
        courseBtn = findViewById(R.id.idBtnSaveCourse);

        // below line is to get intent as we
        // are getting data via an intent.
        Intent intent = getIntent();
        if (intent.hasExtra(EXTRA_ID)) {
            // if we get id for our data then we are
            // setting values to our edit text fields.
            nameEdt.setText(intent.getStringExtra(EXTRA_NAME));
            surnameEdt.setText(intent.getStringExtra(EXTRA_SURNAME));
            emailEdt.setText(intent.getStringExtra(EXTRA_EMAIL));
            phoneEdt.setText(intent.getStringExtra(EXTRA_PHONE));
        }
        // adding on click listener for our save button.
        courseBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // getting text value from edittext and validating if
                // the text fields are empty or not.
                String name = nameEdt.getText().toString();
                String surname = surnameEdt.getText().toString();
                String email = emailEdt.getText().toString();
                String phone = phoneEdt.getText().toString();
                if (name.isEmpty() || surname.isEmpty() || email.isEmpty() || phone.isEmpty()) {
                    Toast.makeText(NewCourseActivity.this, "Please enter valid user details.", Toast.LENGTH_SHORT).show();
                    return;
                }
                else if (!phone.matches("^[0-9]+$")) {
                    Toast.makeText(NewCourseActivity.this, "Please enter a valid phone number.", Toast.LENGTH_SHORT).show();
                    return;
                }
                else if (!email.contains("@")){
                    Toast.makeText(NewCourseActivity.this, "Please enter a valid email address.", Toast.LENGTH_SHORT).show();
                    return;
                }
                else if (!name.matches("^[a-zA-Z ]+$") || !surname.matches("^[a-zA-Z]+$") ){
                    Toast.makeText(NewCourseActivity.this, "Please enter a valid name and surname.", Toast.LENGTH_SHORT).show();
                    return;
                }
                // calling a method to save our course.
                saveCourse(name, surname, email, phone);
            }
        });
    }

    private void saveCourse(String name, String surname, String email, String phone) {
        // inside this method we are passing
        // all the data via an intent.
        Intent data = new Intent();

        // in below line we are passing all our course detail.
        data.putExtra(EXTRA_NAME, name);
        data.putExtra(EXTRA_SURNAME, surname);
        data.putExtra(EXTRA_EMAIL, email);
        data.putExtra(EXTRA_PHONE, phone);
        int id = getIntent().getIntExtra(EXTRA_ID, -1);
        if (id != -1) {
            // in below line we are passing our id.
            data.putExtra(EXTRA_ID, id);
        }

        // at last we are setting result as data.
        setResult(RESULT_OK, data);

        // displaying a toast message after adding the data
        Toast.makeText(this, "Contact has been saved to Room Database. ", Toast.LENGTH_SHORT).show();
    }
}
