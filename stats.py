import pymongo
import datetime
from config import *

client = pymongo.MongoClient(ATLAS_URI)
db = client.get_database("terabox_downloader")

def get_today_key():
    return datetime.date.today().strftime("%Y-%m-%d")

# Message and User Tracking
def track_message(user_id):
    """Tracks a processed message and updates relevant statistics."""
    db.stats.update_one({}, {"$inc": {"total_messages": 1}}, upsert=True)

    today = get_today_key()
    db.new_users.update_one({"date": today}, {"$addToSet": {"users": user_id}}, upsert=True)
    db.active_users.update_one({"user_id": user_id}, {"$inc": {"score": 1}}, upsert=True)

# Statistics Retrieval
def get_message_count():
    stat = db.stats.find_one()
    return stat["total_messages"] if stat else 0

def get_new_user_count_today():
    today = get_today_key()
    new_user = db.new_users.find_one({"date": today})
    return len(new_user["users"]) if new_user else 0

def get_top_active_users(limit=5):
    return list(db.active_users.find().sort("score", pymongo.DESCENDING).limit(limit))

def get_file_type_stats():
    return db.file_types.find_one() or {}
