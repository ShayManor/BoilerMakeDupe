import os
import logging
from pymongo import MongoClient
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load environment variables
load_dotenv()

# Get MongoDB connection string
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    logging.error("❌ MONGO_URI is missing in .env file!")
    exit(1)

# Connect to MongoDB
try:
    with MongoClient(MONGO_URI) as client:
        db = client["test1"]
        # Test connection
        client.admin.command("ping")
        logging.info("✅ Successfully connected to MongoDB Atlas!")
except Exception as e:
    logging.error(f"❌ Connection failed: {e}")
