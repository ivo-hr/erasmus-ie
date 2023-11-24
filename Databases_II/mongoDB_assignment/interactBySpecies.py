import argparse
from pymongo import MongoClient
import json

# Function to query and print a list of all document ids in the "BirdSpecies" collection
def query_all_cases(database):
    count = 0
    all_documents = database.BirdSpecies.find()
    for document in all_documents:
        for incident in document["Incidents"]:
            print(incident["Record_ID"])
            count += 1
    print(f"Number of records: {count}")
    
# Function to query and print the number of records for each species
def query_all_species(database):
    species_records = {}

    # Aggregate the number of records for each species
    all_species = database.BirdSpecies.find()
    for species_document in all_species:
        species_name = species_document["Species_Name"]
        record_count = len(species_document["Incidents"])

        # Merge records for the same species
        if species_name in species_records:
            species_records[species_name] += record_count
        else:
            species_records[species_name] = record_count

    # Print the aggregated results
    for species_name, record_count in species_records.items():
        print(f"Species: {species_name}, Number of Records: {record_count}")

# Function to query and print a list of document ids matching a specified species name
def query_species_documents(database, species_name):
    count = 0
    species_documents = database.BirdSpecies.find({"Species_Name": species_name})
    for document in species_documents:
        for incident in document["Incidents"]:
            print(incident["Record_ID"])
            count += 1
    print(f"Number of records with {species_name} hit: {count} ")

# Function to query and print a list of all document ids with specified fields (projection)
def query_projection_documents(database, fields):
    # If fields doesn't include Record_ID, add it
    fields["Record_ID"] = 1

    count = 0
    projection_documents = database.BirdSpecies.find({}, fields)
    for document in projection_documents:
        for incident in document["Incidents"]:
            output_fields = list(fields.keys()) if fields else []  # Use specified fields or an empty list
            print(', '.join("{}: {}".format(field, incident.get(field, 'N/A')) for field in output_fields))
            count += 1
    print(f"Number of records: {count}")

# Function to query and print a list of all document ids sorted by a specified field and order
def query_sorted_documents(database, sort_field, sort_order):
    count = 0
    sorted_documents = database.BirdSpecies.find().sort(sort_field, sort_order)
    for document in sorted_documents:
        for incident in document["Incidents"]:
            print(incident["Record_ID"])
            count += 1
    print(f"Number of records: {count} sorted by {sort_field} in {sort_order} order")

# Function to perform an aggregation query using match criteria and print a matching list of document ids
def query_aggregation_documents(database, match_criteria):
    count = 0
    aggregation_pipeline = [{"$unwind": "$Incidents"}, {"$match": match_criteria}]
    aggregation_result = database.BirdSpecies.aggregate(aggregation_pipeline)
    for document in aggregation_result:
        print(document["Incidents"]["Record_ID"], "matches the criteria of", match_criteria)
        count += 1
    print(f"Number of records: {count}")

# Function to query and print a specific document based on the provided record ID
def query_specific_document(database, record_id):
    specific_document = database.BirdSpecies.find({"Incidents.Record_ID": record_id})
    for document in specific_document:
        for incident in document["Incidents"]:
            if incident["Record_ID"] == record_id:
                # Convert ObjectId to string
                document["_id"] = str(document["_id"])
                print(json.dumps(incident, indent=2))

# Function to add a new document to the database
def add_document(database, new_document):
    # Insert the document into the database
    result = database.BirdSpecies.insert_one(new_document)
    print("Inserted Record ID:", result.inserted_id)

# Function to update a document in the database
def update_document(database, record_id, updated_document):
    # Update the document in the database
    result = database.BirdSpecies.update_one({"Incidents.Record_ID": record_id}, {"$set": {"Incidents.$": updated_document}})
    print("Updated", result.modified_count, "record(s)")

# Function to delete a document from the database
def delete_document(database, record_id):
    # Delete the document from the database
    result = database.BirdSpecies.update({}, {"$pull": {"Incidents": {"Record_ID": record_id}}}, multi=True)
    print("Deleted", result["nModified"], "record(s)")

# Main block for command-line argument parsing and query execution
if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="MongoDB Query Program")
    # Create a mutually exclusive group for --query and --modify
    group = parser.add_mutually_exclusive_group(required=True)
    # Add --query argument
    group.add_argument("--query", choices=["all", "allspecies", "specific", "species", "projection", "sorted", "aggregation"],
                        help="Type of query to perform")
    # Add --modify argument
    group.add_argument("--modify", choices=["add", "update", "delete"], help="Type of modification to perform")
    # Add arguments for each query type
    parser.add_argument("--species_name", help="With --query. Species name for species query")
    parser.add_argument("--fields", help="With --query. Fields for projection query")
    parser.add_argument("--sort_field", help="With --query. Field for sorting")
    parser.add_argument("--sort_order", choices=["asc", "desc"], help="With --query. Sort order")
    parser.add_argument("--match_criteria", help="With --query. Match criteria for aggregation query")
    parser.add_argument("--record_id", help="With --query. Record ID of a specific document")
    parser.add_argument("--new_document", help="With --modify. New document to add to the database, in JSON format")
    parser.add_argument("--update_document", help="With --modify. Updated parameters to replace the old ones, in JSON format")
    parser.add_argument("--delete_document", help="With --modify. Record ID of the document to delete")

    args = parser.parse_args()

    # Handle spaces in species name

    # Connect to MongoDB
    client = MongoClient('mongodb://admin:Sp00ky!@localhost:27017/?AuthSource=admin')
    db = client["AirIncidents"]

    # Perform the selected query
    if args.query:
        if args.query == "all":
            query_all_cases(db)
        elif args.query == "allspecies":
            query_all_species(db)
        elif args.query == "species" and args.species_name:
            args.species_name = args.species_name.replace('"', '')
            query_species_documents(db, args.species_name)
        elif args.query == "projection" and args.fields:
            fields = json.loads(args.fields.replace("'", "\""))
            query_projection_documents(db, fields)
        elif args.query == "sorted" and args.sort_field and args.sort_order:
            query_sorted_documents(db, args.sort_field, 1 if args.sort_order == "asc" else -1)
        elif args.query == "aggregation" and args.match_criteria:
            match_criteria = json.loads(args.match_criteria.replace("'", "\""))
            query_aggregation_documents(db, match_criteria)
        elif args.query == "specific" and args.record_id:
            query_specific_document(db, args.record_id)
        else:
            print("Invalid query parameters")
            exit()

    elif args.modify:
        if args.modify == "add" and args.new_document:
            new_document = json.loads(args.new_document.replace("'", "\""))
            add_document(db, new_document)
        elif args.modify == "update" and args.record_id and args.update_document:
            updated_document = json.loads(args.update_document.replace("'", "\""))
            update_document(db, args.record_id, updated_document)
        elif args.modify == "delete" and args.record_id:
            delete_document(db, args.record_id)
        else:
            print("Invalid modification parameters")
            exit()
