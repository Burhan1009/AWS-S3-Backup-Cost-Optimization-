import os
import datetime
import shutil
import boto3
from pathlib import Path
from botocore.exceptions import NoCredentialsError

def filter_previous_day_files(source_path):
    """
    Filters the files in the source directory to include only those related to yesterday's date.
    """
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y_%m_%d')
    return [
        file for file in os.listdir(source_path)
        if yesterday in file and file.endswith('.bak')
    ]


def clean_old_backups(destination_path, allowed_date):
    """
    Deletes zip files in the destination_path that do not match the allowed_date.
    """
    try:
        for file in os.listdir(destination_path):
            file_path = os.path.join(destination_path, file)
            # Check if the file is a zip archive and does not match the allowed_date
            if file.endswith('.zip') and allowed_date not in file:
                os.remove(file_path)
                print(f"Deleted old backup file: {file_path}")
    except Exception as e:
        print(f"Error during old backup cleanup: {e}")

def create_backup(files, source_path, destination_path):
    """
    Copies the filtered files to the destination folder and creates a zip archive.
    Deletes the intermediate folder after zipping.
    """
    # Get yesterday's date for folder and zip name
    date_name = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    backup_dir = os.path.join(destination_path, date_name)

    # Ensure the folder exists
    os.makedirs(backup_dir, exist_ok=True)

    try:
        # Copy files to the temporary backup folder
        for file in files:
            source_file = os.path.join(source_path, file)
            destination_file = os.path.join(backup_dir, file)
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {file} to {destination_file}")

        # Create a ZIP archive of the folder
        zip_file = shutil.make_archive(backup_dir, 'zip', backup_dir)
        print("Backup Complete..! Created zip archive.")

        # Remove the temporary backup folder
        shutil.rmtree(backup_dir)
        print(f"Removed temporary folder: {backup_dir}")

        return zip_file  # Return the path of the ZIP file
    except Exception as e:
        print(f"Error during backup creation: {e}")
        return None

def upload_to_s3(file_path, bucket_name, s3_folder, aws_access_key, aws_secret_key, region_name):
    """
    Uploads the zip file to the specified S3 bucket.
    """
    # Initialize the S3 client with region_name
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region_name
    )

    try:
        file_name = os.path.basename(file_path)
        s3_key = f"{s3_folder}/{file_name}"

        # Upload the zip file to the S3 bucket
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to S3: {s3_key}")
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"Error during S3 upload: {e}")

# User-defined paths and credentials
source_path = Path(r"\\192.22.54.4\\d$\\DAILYBACKUP")  # Use a raw string
destination_path = Path(r"D:\\CloudBackup\\Zip\\ProManager")

bucket_name = "burhandemotws"  # Replace with your S3 bucket name
s3_folder = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')  # Yesterday's date for S3 folder
aws_access_key = ""  # Replace with your AWS access key
aws_secret_key = ""  # Replace with your AWS secret key
region_name = "us-east-1"  # Replace with your S3 bucket region

# Filter files for the previous date
previous_day_files = filter_previous_day_files(source_path)

if previous_day_files:
    # Create backup
    zip_file = create_backup(previous_day_files, source_path, destination_path)

    # Clean up old backups
    allowed_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    clean_old_backups(destination_path, allowed_date)

    # Upload to S3 if backup is successful
    if zip_file:
        upload_to_s3(zip_file, bucket_name, s3_folder, aws_access_key, aws_secret_key, region_name)
else:
    print("No files found for yesterday's date.")
