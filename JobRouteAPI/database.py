from pymongo import MongoClient

try:
    # Connect to MongoDB server
    client = MongoClient("mongodb://localhost:27017/")
    db = client["JobRouteDB"]
    
    # Collections
    users_collection = db["users"]
    skills_collection = db["skills"]
    careers_collection = db["careers"]

    # Check connection
    server_status = client.admin.command("ping")
    print("Database Connected Successfully")

except Exception as e:
    print(f"Database Connection Failed: {e}")
