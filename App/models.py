from django.shortcuts import render
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
def get_subscribers(query=None):
    # If a query is provided, return subscribers matching the query (case-insensitive)
    if query:
        return list(subscribers.find({"fullname": {"$regex": query, "$options": "i"}}))
    return list(subscribers.find())  # Return all subscribers if no query is provided

# Function to get a single subscriber by ID
def get_subscriber_by_id(subscriber_id):
    return subscribers.find_one({"_id": ObjectId(subscriber_id)})

# Function to update a subscriber's info
def update_subscriber(subscriber_id, update_data):
    return subscribers.update_one({"_id": ObjectId(subscriber_id)}, {"$set": update_data})

# Function to delete a subscriber
def delete_subscriber(id):
    return subscribers.delete_one({"_id": ObjectId(id)})

# View to handle the subscriber list and search
def subscriber_list(request):
    query = request.GET.get('q', '')  # Get the search query from the GET request
    subs = get_subscribers(query)  # Fetch the subscribers (with or without search)
    return render(request, 'subscriber_list.html', {'subscribers': subs})

