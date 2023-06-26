import os
from google.cloud import storage
from google.auth import compute_engine

# Define the GCS bucket and file information
BUCKET_NAME = "YOUR_BUCKET_NAME"
FILE_NAME = "YOUR_FILE_NAME"

# Create a client using the provided credentials
client = storage.Client()

# Get the bucket and blob (file) references
bucket = client.get_bucket(BUCKET_NAME)
blob = bucket.blob(FILE_NAME)

# Check if the file exists in the bucket
if blob.exists():
    # Download the file
    blob.download_to_filename(FILE_NAME)
    # Delete the file from the bucket
    blob.delete()
