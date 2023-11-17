from pymongo import MongoClient
import pandas as pd
from os.path import join

# Connect to MongoDB
uri = 'mongodb://admin:Sp00ky!@localhost:27017/?AuthSource=admin'
client = MongoClient(uri)
mydb = client["Swimming"]

# Load the DataFrame like before
df = pd.read_csv(join('./Datasets/', 'Swimming Database 2.csv'), encoding='latin-1')
df.columns = list(map(lambda x: x.replace(" ", "_"), df.columns))
df[['Event_Name', 'Event_description', 'Team_Code', 'Team_Name', 'Athlete_Full_Name', 'Gender', 'City', 'Country_Code']] = \
    df[['Event_Name', 'Event_description', 'Team_Code', 'Team_Name', 'Athlete_Full_Name', 'Gender', 'City',
        'Country_Code']].astype("string")
df = df.rename(columns={"Duration_(hh:mm:ss:ff)": "Duration"})
df = df.drop(columns=['Swim_time'])
df['Athlete_birth_date'] = pd.to_datetime(df['Athlete_birth_date'], format='%m/%d/%Y').dt.date
df['Athlete_birth_date'] = df['Athlete_birth_date'].astype("string")
df['Swim_date'] = pd.to_datetime(df['Swim_date'], format='%m/%d/%Y').dt.date
df['Swim_date'] = df['Swim_date'].astype("string")

# Team collection
mycol_team = mydb["Team"]
mycol_team.drop()  # Drop existing data (if any)

# Loop through each team to create a document
for team_name in sorted(df["Team_Name"].dropna().unique()):
    team_swims = df[df["Team_Name"] == team_name][
        ['Event_Name', 'Event_description', 'Athlete_Full_Name', 'Gender', 'Athlete_birth_date', 'Swim_date',
         'Team_Code', 'Rank_Order', 'City', 'Country_Code', 'Duration']]
    team_entry = {
        "Team_Name": team_name,
        "Swims": team_swims.to_dict('records')
    }
    mycol_team.insert_one(team_entry)

# Team collection
mycol_team = mydb["Team"]

# Find all documents in the Team collection
all_teams = mycol_team.find()

# Print the data for each document
for team in all_teams:
    print(team)

# Close connection
client.close()
