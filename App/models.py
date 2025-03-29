from django.db import models
from .mongodb import subscribers
from bson import ObjectId
from datetime import datetime

# Function to insert a new subscriber
def insert_subscriber(fullname, phone, category):
    subscriber = {
        "fullname": fullname,
        "phone": phone,
        "category": category,
        "inscriptionDate": datetime.utcnow()
    }
    return subscribers.insert_one(subscriber).inserted_id

# Function to get all subscribers
def get_subscribers():
    return list(subscribers.find())

# Function to get a single subscriber by ID
def get_subscriber_by_id(subscriber_id):
    return subscribers.find_one({"_id": ObjectId(subscriber_id)})

# Function to update a subscriber's info
def update_subscriber(subscriber_id, update_data):
    return subscribers.update_one({"_id": ObjectId(subscriber_id)}, {"$set": update_data})

# Function to delete a subscriber
def delete_subscriber(fullname):
    return subscribers.delete_one({"fullname":fullname})

