import os
from google.cloud import storage
from google.auth import compute_engine
import filecmp

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
    # Check if the existing file exists
    if os.path.exists(FILE_NAME):
        # Download the file to compare
        blob.download_to_filename(FILE_NAME + ".new")

        # Compare the contents with the existing file
        if not filecmp.cmp(FILE_NAME, FILE_NAME + ".new"):
            # Contents are different, replace the existing file
            os.rename(FILE_NAME + ".new", FILE_NAME)
            print("File replaced.")
        else:
            # Contents are the same, log a message
            os.remove(FILE_NAME + ".new")
            print("Same file exists, not replaced.")
    else:
        # Download the file as there is no existing file
        blob.download_to_filename(FILE_NAME)
        print("File downloaded.")
else:
    print("File not found in the bucket.")
