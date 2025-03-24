# from pymongo import MongoClient

# client = MongoClient('mongodb+srv://harshithasamudrala2000:dj7rsiAhJD9iCCM1@cluster0.t27i3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
# db = client['data_base1']
# collection = db['collection1']

# document = {'name':'abc','city':'Bengaluru'}
# inserted_document = collection.insert_one(document)

# print(f'Inserted document Id:{inserted_document.inserted_id}')
# client.close()


from pymongo import MongoClient

# Connect to MongoDB Atlas (Replace with your connection string)
client = MongoClient("mongodb+srv://harshithasamudrala2000:dj7rsiAhJD9iCCM1@cluster0.t27i3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Select your database and collection
db = client["user_database"]
collection = db["user_details"]

print("Connected to MongoDB Atlas!\n")


# Collect user data
user_data = {
    "name": input("Enter name: "),
    "age": int(input("Enter age: ")),
    "email": input("Enter email: "),
    "address": input("Enter address: ")
}

# Insert data into MongoDB
result = collection.insert_one(user_data)
print(f" User inserted with ID: {result.inserted_id}")

# Display the inserted user
print("\n User Details in the Database:")
user = collection.find_one({"_id": result.inserted_id})
print(user)

# def get_user_input():
#     user_data = {}
#     user_data["name"] = input("Enter name: ")
#     user_data["age"] = int(input("Enter age: "))
#     user_data["email"] = input("Enter email: ")
#     user_data["address"] = input("Enter address: ")
#     return user_data

# # Insert multiple users dynamically
# while True:
#     user = get_user_input()
#     result = collection.insert_one(user)
#     print(f" User inserted with ID: {result.inserted_id}")

#     more = input("Do you want to add another user? (yes/no): ").strip().lower()
#     if more != "yes":
#         break

# print("\n All Users in the Database:")
# for user in collection.find():
#     print(user)



# from pymongo import MongoClient
# from bson import ObjectId

# # Connect to MongoDB Atlas (Replace with your connection string)
# client = MongoClient("mongodb+srv://harshithasamudrala2000:dj7rsiAhJD9iCCM1@cluster0.t27i3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# # Select your database and collection
# db = client["user_database"]
# collection = db["user_details"]

# print("Connected to MongoDB Atlas!\n")

# # Input: User provides the ObjectId to search
# user_id = input("Enter the user ID to fetch: ")

# try:
#     # Convert user_id to ObjectId and fetch the record
#     user = collection.find_one({"_id": ObjectId(user_id)})

#     # Check if the user exists
#     if user:
#         print("\n User Found:")
#         print(user)
#     else:
#         print("\n No user found with that ID.")

# except Exception as e:
#     print(f"\n Error: {e}")
