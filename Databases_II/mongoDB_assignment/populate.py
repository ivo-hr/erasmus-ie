import pandas as pd
import json
from pymongo import MongoClient
from os.path import join


# Load the new dataset
new_df = pd.read_csv(join('./', 'database.csv'), encoding='latin-1', low_memory=False)

# Print column names to identify the correct one
print("Column Names:", new_df.columns)

# Convert date columns to datetime
date_columns = ['Incident Year', 'Incident Month', 'Incident Day']
new_df[date_columns] = new_df[date_columns].astype(str)
new_df['Incident_Date'] = pd.to_datetime(new_df[date_columns].agg('-'.join), format='%Y-%m-%d', errors='coerce')


# Handle mixed types in 'Record ID' column
new_df['Record ID'] = new_df['Record ID'].astype(str)

# Connect to MongoDB
uri = 'mongodb://admin:Sp00ky!@localhost:27017/?AuthSource=admin'
client = MongoClient(uri)

# Create a database and collection
mydb = client["AirIncidents"]
mycol = mydb["Incident"]
mycol.drop()

# Loop through each incident to create a document
# Check if the correct column name is in the DataFrame
if 'Record ID' in new_df.columns:
    # Loop through each incident to create a document
    for index, row in new_df.iterrows():
        incident_data = {
            "Record_ID": str(row['Record ID']),
            "Incident_Year": str(row['Incident Year']),
            "Incident_Month": str(row['Incident Month']),
            "Incident_Day": str(row['Incident Day']),
            "Operator_ID": str(row['Operator ID']),
            "Operator": str(row['Operator']),
            "Aircraft": str(row['Aircraft']),
            "Aircraft_Type": str(row['Aircraft Type']),
            "Aircraft_Make": str(row['Aircraft Make']),
            "Aircraft_Model": str(row['Aircraft Model']),
            "Aircraft_Mass": str(row['Aircraft Mass']),
            "Engine_Make": str(row['Engine Make']),
            "Engine_Model": str(row['Engine Model']),
            "Engines": str(row['Engines']),
            "Engine_Type": str(row['Engine Type']),
            "Engine1_Position": str(row['Engine1 Position']),
            "Engine2_Position": str(row['Engine2 Position']),
            "Engine3_Position": str(row['Engine3 Position']),
            "Engine4_Position": str(row['Engine4 Position']),
            "Airport_ID": str(row['Airport ID']),
            "Airport": str(row['Airport']),
            "State": str(row['State']),
            "FAA_Region": str(row['FAA Region']),
            "Warning_Issued": str(row['Warning Issued']),
            "Flight_Phase": str(row['Flight Phase']),
            "Visibility": str(row['Visibility']),
            "Precipitation": str(row['Precipitation']),
            "Height": str(row['Height']),
            "Speed": str(row['Speed']),
            "Distance": str(row['Distance']),
            "Species_ID": str(row['Species ID']),
            "Species_Name": str(row['Species Name']),
            "Species_Quantity": str(row['Species Quantity']),
            "Flight_Impact": str(row['Flight Impact']),
            "Fatalities": str(row['Fatalities']),
            "Injuries": str(row['Injuries']),
            "Aircraft_Damage": str(row['Aircraft Damage']),
            "Radome_Strike": str(row['Radome Strike']),
            "Radome_Damage": str(row['Radome Damage']),
            "Windshield_Strike": str(row['Windshield Strike']),
            "Windshield_Damage": str(row['Windshield Damage']),
            "Nose_Strike": str(row['Nose Strike']),
            "Nose_Damage": str(row['Nose Damage']),
            "Engine1_Strike": str(row['Engine1 Strike']),
            "Engine1_Damage": str(row['Engine1 Damage']),
            "Engine2_Strike": str(row['Engine2 Strike']),
            "Engine2_Damage": str(row['Engine2 Damage']),
            "Engine3_Strike": str(row['Engine3 Strike']),
            "Engine3_Damage": str(row['Engine3 Damage']),
            "Engine4_Strike": str(row['Engine4 Strike']),
            "Engine4_Damage": str(row['Engine4 Damage']),
            "Engine_Ingested": str(row['Engine Ingested']),
            "Propeller_Strike": str(row['Propeller Strike']),
            "Propeller_Damage": str(row['Propeller Damage']),
            "Wing_or_Rotor_Strike": str(row['Wing or Rotor Strike']),
            "Wing_or_Rotor_Damage": str(row['Wing or Rotor Damage']),
            "Fuselage_Strike": str(row['Fuselage Strike']),
            "Fuselage_Damage": str(row['Fuselage Damage']),
            "Landing_Gear_Strike": str(row['Landing Gear Strike']),
            "Landing_Gear_Damage": str(row['Landing Gear Damage']),
            "Tail_Strike": str(row['Tail Strike']),
            "Tail_Damage": str(row['Tail Damage']),
            "Lights_Strike": str(row['Lights Strike']),
            "Lights_Damage": str(row['Lights Damage']),
            "Other_Strike": str(row['Other Strike']),
            "Other_Damage": str(row['Other Damage']),
        }

        x = mycol.insert_one(incident_data)

    # Close the MongoDB connection
    client.close()
else:
    print("Record ID not found in DataFrame. Please check the CSV file and try again.")
