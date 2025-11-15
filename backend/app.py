from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://aditya:vTpKR1QEMhzbU3CW@cluster0.qwqqxw5.mongodb.net/?retryWrites=true&w=majority")
db = client["todoDB"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")
    itemID = request.form.get("itemID")


    data = {
        "itemName": itemName,
        "itemDescription": itemDescription,
        "itemID": itemID

    }

    result = collection.insert_one(data)

    # Add _id manually
    data["_id"] = str(result.inserted_id)

    return jsonify({"message": "To-Do Item Saved Successfully", "data": data})

if __name__ == "__main__":
    app.run(debug=True)
