import pandas as pd
import json
from pymongo import MongoClient
from os.path import join

# Load the dataset
df = pd.read_csv(join('./Datasets/', 'Swimming database 2.csv'), encoding='latin-1')
df.columns = list(map(lambda x: x.replace(" ", "_"), df.columns))

# Convert date and time columns to string
df['Athlete_birth_date'] = pd.to_datetime(df['Athlete_birth_date'], format='%m/%d/%Y').dt.date.astype("string")
df['Swim_date'] = pd.to_datetime(df['Swim_date'], format='%m/%d/%Y').dt.date.astype("string")

# Rename and drop columnsj
df = df.rename(columns={"Duration_(hh:mm:ss:ff)": "Duration"})
df = df.drop(columns=['Swim_time'])

# Handle missing values
df["City"].fillna("Not Specified", inplace=True)

# Extract unique athlete information
adf = df[['Athlete_Full_Name', 'Gender', 'Athlete_birth_date']].drop_duplicates()

# Connect to MongoDB
uri = 'mongodb://admin:Sp00ky!@localhost:27017/?AuthSource=admin'

client = MongoClient(uri)

# Create a database and collection
mydb = client["Swimming"]
mycol = mydb["Athlete"]
mycol.drop()

# Loop through each athlete to create a document
for row in adf.itertuples():
    their_swims = df[df.Athlete_Full_Name == row.Athlete_Full_Name][['Event_Name',
                                                                      'Event_description',
                                                                      'Swim_date',
                                                                      'Team_Code',
                                                                      'Team_Name',
                                                                      'Rank_Order',
                                                                      'City',
                                                                      'Country_Code',
                                                                      'Duration']]
    entries = json.dumps({
        "Name": row.Athlete_Full_Name,
        "Birth_Date": row.Athlete_birth_date,
        "Gender": row.Gender,
        "Swims": their_swims.to_dict('records')
    })
    x = mycol.insert_one(json.loads(entries))

# Close the MongoDB connection
client.close()
