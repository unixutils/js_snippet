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
        if open(FILE_NAME, 'rb').read() != open(FILE_NAME + ".new", 'rb').read():
            # Contents are different, replace the existing file
            os.replace(FILE_NAME + ".new", FILE_NAME)
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


import os
from dotenv import dotenv_values, set_key

def update_project_id(env_file_path, new_value):
    env = dotenv_values(env_file_path)
    if 'project_id' in env:
        current_value = env['project_id']
        if current_value != new_value:
            set_key(env_file_path, 'project_id', new_value)
            print(f"Updated project_id in {env_file_path} from {current_value} to {new_value}")
    else:
        print(f"No project_id found in {env_file_path}")

# Provide the folder path where the .env files are located
folder_path = '/path/to/env/files'

# Provide the new value for project_id
new_project_id = 'some_new_value'

# Iterate over all .env files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.env'):
        file_path = os.path.join(folder_path, file_name)
        update_project_id(file_path, new_project_id)
