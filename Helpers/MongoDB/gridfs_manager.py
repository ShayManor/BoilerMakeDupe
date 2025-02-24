import gridfs
import os
from config import db

fs = gridfs.GridFS(db)


def store_file(file_path):
    """Uploads a file to GridFS and returns the file_id."""
    with open(file_path, "rb") as f:
        file_id = fs.put(f, filename=os.path.basename(file_path))
    return file_id


def retrieve_file(file_id, download_dir="./agents"):
    """Retrieves a file from GridFS and saves it locally."""
    os.makedirs(download_dir, exist_ok=True)
    file_data = fs.get(file_id)
    file_path = os.path.join(download_dir, file_data.filename)

    with open(file_path, "wb") as f:
        f.write(file_data.read())

    return file_path
