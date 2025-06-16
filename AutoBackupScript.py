import os
import datetime
import shutil
import boto3
from pathlib import Path
from botocore.exceptions import NoCredentialsError

def filter_previous_day_files(source_path):
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y_%m_%d')
    return [
        file for file in os.listdir(source_path)
        if yesterday in file and file.endswith('.txt')
    ]

def clean_old_backups(destination_path, allowed_date):
    try:
        for file in os.listdir(destination_path):
            file_path = os.path.join(destination_path, file)
            if file.endswith('.zip') and allowed_date not in file:
                os.remove(file_path)
                print(f"Deleted old backup file: {file_path}")
    except Exception as e:
        print(f"Error during old backup cleanup: {e}")

def create_backup(files, source_path, destination_path):
    date_name = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    backup_dir = os.path.join(destination_path, date_name)
    os.makedirs(backup_dir, exist_ok=True)

    try:
        for file in files:
            source_file = os.path.join(source_path, file)
            destination_file = os.path.join(backup_dir, file)
            shutil.copy2(source_file, destination_file)
            print(f"Copied: {file} to {destination_file}")

        zip_file = shutil.make_archive(backup_dir, 'zip', backup_dir)
        print("Backup Complete..! Created zip archive.")
        shutil.rmtree(backup_dir)
        print(f"Removed temporary folder: {backup_dir}")

        return zip_file
    except Exception as e:
        print(f"Error during backup creation: {e}")
        return None

def upload_to_s3(file_path, bucket_name, s3_folder, aws_access_key, aws_secret_key, region_name):
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region_name
    )

    try:
        file_name = os.path.basename(file_path)
        s3_key = f"{s3_folder}/{file_name}"
        s3.upload_file(file_path, bucket_name, s3_key)
        print(f"File uploaded successfully to S3: {s3_key}")
        return True
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"Error during S3 upload: {e}")
    return False

def send_sns_notification(subject, message, topic_arn, aws_access_key, aws_secret_key, region_name):
    sns = boto3.client(
        'sns',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region_name
    )
    try:
        sns.publish(
            TopicArn=topic_arn,
            Subject=subject,
            Message=message
        )
        print("SNS notification sent successfully.")
    except Exception as e:
        print(f"Error sending SNS notification: {e}")

# === USER CONFIGURATION ===
source_path = Path(r"D:\\DevOps Projects\\AWS-S3-Backup-Cost-Optimization-\\source")
destination_path = Path(r"D:\\DevOps Projects\\AWS-S3-Backup-Cost-Optimization-\\destination")
bucket_name = "burhandemotws"
s3_folder = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
aws_access_key = "####"
aws_secret_key = "###"
region_name = "us-east-1"
sns_topic_arn = "###"  # Replace with your SNS topic ARN

# === MAIN PROCESS ===
previous_day_files = filter_previous_day_files(source_path)

if previous_day_files:
    zip_file = create_backup(previous_day_files, source_path, destination_path)
    allowed_date = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    clean_old_backups(destination_path, allowed_date)

    if zip_file:
        success = upload_to_s3(zip_file, bucket_name, s3_folder, aws_access_key, aws_secret_key, region_name)
        if success:
            subject = "Backup Upload Successful"
            message = f"The backup file {os.path.basename(zip_file)} was uploaded to S3 bucket '{bucket_name}' on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
            send_sns_notification(subject, message, sns_topic_arn, aws_access_key, aws_secret_key, region_name)
else:
    print("No files found for yesterday's date.")
