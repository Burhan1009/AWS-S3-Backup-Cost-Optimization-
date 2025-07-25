# AWS-S3-Backup-Cost-Optimization-
AWS S3 Backup Cost Optimization with Python (boto3): Automatically Move Old Backups to Glacier & Send Notifications via SNS Using Lifecycle Policies

![image](https://github.com/user-attachments/assets/b40b6158-970c-4014-8e39-352c2b0ff7bc)

# 📄 Project Description:
This project demonstrates how to automate backups from an on-premises server to Amazon S3 and optimize storage costs by moving older backups to Amazon S3 Glacier using Lifecycle Policies. The solution is built using Python (Boto3) for automation and Terraform for AWS infrastructure provisioning.

By compressing and uploading user and database directories to S3 and using AWS Lifecycle Policies, you can reduce your storage costs by up to 80%.

## On-Premise Server
   └──> [Database/User Directory] -> Convert to ZIP with Date Folders -> Python Boto3 Script -> Upload to S3 -> Lifecycle Policy: Auto Move to Glacier
## AWS Infrastructure:
   └──> IAM Access Keys -> Terraform Configuration -> S3 Bucket with Lifecycle Rules
## Automation Flow 
Local data → Compressed ZIPs → Uploaded via Python → AWS S3 → Glacier (via Policy)

# ✅ Features

🔐 Secure IAM access with Access & Secret Keys

📦 Compresses backup data into ZIP format with timestamps

☁️ Uploads ZIP files to Amazon S3

🔁 Automatically applies Lifecycle Policies to move files to Glacier

💵 Optimizes cost (Glacier ~$0.004/GB vs Standard ~$0.023/GB)

🛠️ Terraform-managed infrastructure

# 🔧 System Software & Setup:

1. On Your Local Machine (Linux or Windows):
* Python 3.13 [ Download ](https://surli.cc/bianoi)
* pip (Python package installer)
* AWS CLI configured
* Terraform 1.0+
* Git

2. AWS
* An AWS account with : **IAM user with programmatic access & S3** and **Glacier permissions**

## If you have Windows 10 or Windows 11 Home edition and want to run a Windows simulation on your current system using Hyper-V, follow these steps:
* Create a batch file and run it in your Windows Command Prompt.
* Wait for the required software to install.
* Check the Windows Features to ensure that Hyper-V has been enabled on your Home edition.
```powershell
@echo off
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt

for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do (
    dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
)

del hyper-v.txt

dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /LimitAccess /ALL

echo.
echo Hyper-V should now be enabled. Please restart your computer.
pause
```
## Watch This video 
https://youtu.be/y9Vh8OMRS1k

## Project Setup 

Fist Step Need to install Python Software & Setup Enviornment 

* Run as Administrator
![image](https://github.com/user-attachments/assets/78ad918a-742d-46bc-9d93-cbce5311e29f)

* click on Close after install all packages
![image](https://github.com/user-attachments/assets/a5b3f389-d0fc-4a92-8978-9c8a7bf12b4f)

* Verify
![image](https://github.com/user-attachments/assets/c1fd77cc-b248-4b39-a713-569083b00386)

## 1 Setting Python Environment Path on Windows
1. Locate Your Python Installation
2. Your Python is installed at -> C:\Users\Hensex\AppData\Local\Programs\Python\Python313
## 2. Add Python to System PATH (Permanent Solution)

## Method 1: Through System Properties
* Press Win + R, type sysdm.cpl and hit Enter
* Go to Advanced tab → Environment Variables
* Under System variables, find Path and click Edit
* Click New and add these paths:
```
C:\Users\Hensex\AppData\Local\Programs\Python\Python313
C:\Users\Hensex\AppData\Local\Programs\Python\Python313\Scripts
```
## Method 2: Using PowerShell (Admin) 
```powershell
[Environment]::SetEnvironmentVariable(
    "Path",
    [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::Machine) + 
    ";C:\Users\Hensex\AppData\Local\Programs\Python\Python313;" +
    "C:\Users\Hensex\AppData\Local\Programs\Python\Python313\Scripts",
    [EnvironmentVariableTarget]::Machine
)
```
## Verify the Path on PowerShell
```
$env:Path -split ';' | Select-String "Python313"
```
![image](https://github.com/user-attachments/assets/94aabc6e-62cf-4e58-9a12-0a662d5a9ace)

## To install the boto3 library in Python, run the following command in your terminal or command prompt:
```
pip install boto3
```
Python & PIP Verification : 
```
python --version
pip --version
pip show boto3
```
## 2 Setup Terraform 
**Download Terraform**:  
   - Go to the [Terraform official website](https://releases.hashicorp.com/terraform/1.12.1/terraform_1.12.1_windows_amd64.zip).  
   - Download the Windows 64-bit ZIP file.  

**Extract the ZIP File**:  
   - Extract the downloaded ZIP file to a folder (e.g., `C:\terraform`).  

**Add Terraform to the System PATH**:  
   - Open **Start Menu**, search for "Environment Variables," and select "Edit the system environment variables."  
   - Click **Environment Variables** under the System Properties dialog.  
   - Under **System variables**, select `Path` and click **Edit**.  
   - Click **New** and add the folder path where you extracted Terraform (e.g., `C:\terraform`).  
   - Click **OK** to save changes.  

**Verify Installation**:  
   - Open Command Prompt or PowerShell and type:  
     ```bash
     terraform --version
     ```
![image](https://github.com/user-attachments/assets/9293e483-645e-476c-b656-567844796365)

## 3 **Configure AWS CLI**
1. **Download AWS CLI**:  
   - - Go to the [Official Website](https://awscli.amazonaws.com/AWSCLIV2.msi).  
   - Download the MSI installer for Windows.  

2. **Run the Installer**:  
   - Double-click the downloaded MSI file.  
   - Follow the installation wizard to complete the process.  

3. **Verify Installation**:  
   - Open Command Prompt or PowerShell and type:  
     ```bash
     aws --version
     ```
   - It should display the installed version of the AWS CLI.  

4. **Set Up AWS CLI**:  
   - Open Command Prompt or PowerShell and run:  
     ```bash
     aws configure
     ```
   - Enter your AWS Access Key, Secret Key, Region, and output format when prompted.  

5. **Test AWS CLI**:  
   - Run a simple command to verify connectivity:  
     ```bash
     aws s3 ls
     ```
## Create IAM Credentials
- Login AWS Account
- Specify user details
  
![image](https://github.com/user-attachments/assets/5f9d034c-83c7-49ab-b53a-910c9accf706)

## How to Apply
- Go to IAM Console → Policies → Create Policy
- Paste this JSON
- Attach to the specific user via Users → Add permissions
- Select AmazonS3FullAccess & AmazonSNSFullAccess

![image](https://github.com/user-attachments/assets/98595b48-163e-4d6c-8c5c-62d180668a08)

## Even Follow This Steps Both are same 
- Go to IAM Console → Policies → Create Policy
- Paste this JSON
- Attach to the specific user via Users → Add permissions
```powershell
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3BucketAccess",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObject",
                "s3:PutObject",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::YOUR-BUCKET-NAME",
                "arn:aws:s3:::YOUR-BUCKET-NAME/*"
            ]
        },
        {
            "Sid": "SNSCloudWatchAccess",
            "Effect": "Allow",
            "Action": [
                "sns:Publish",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*"
        }
    ]
}
```
![image](https://github.com/user-attachments/assets/87607182-5c11-4fdc-b042-6e5498b35d14)

## Create Security credentials For access CLI Mode 
- Click On User Which is created Few Mints ago
- Select on Security credentials
![image](https://github.com/user-attachments/assets/b101622e-e13a-4274-90b4-32e4cbe03d70)

- Click on Create access key
- Access key best practices & alternatives | Command Line Interface (CLI)
- Confirmation : Check I understand the above recommendation and want to proceed to create an access key.
- Give a Description tag value
- click on create as you can see Access keys (1) created
- CLI Configuration Done
##### I used my AWS Access Key and Secret Key to provision infrastructure using Terraform (IaC) and automate cloud operations with Python Boto3 SDK. This enabled secure, code-driven management of AWS services like S3

## AWS CLI Configuration on Windows
1. Install AWS CLI
```powershell
# Download and run the MSI installer from:
https://aws.amazon.com/cli/

# Verify installation:
aws --version
```

2. Basic Configuration | Run in Command Prompt or PowerShell
```powershell
aws configure
```
3 You'll be prompted for
```powershell
AWS Access Key ID [None]: AKIAXXXXXXXXXXXXXXXX  <-- Your IAM user's access key
AWS Secret Access Key [None]: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  <-- Your IAM user's secret key
Default region name [None]: us-east-1  <-- Preferred region (e.g., us-west-2, eu-central-1)
Default output format [None]: json  <-- (json/text/table)
```
4 AWS S3 Listing Commands
```powershell
aws s3 ls
```
![image](https://github.com/user-attachments/assets/45e71ddf-890e-45e9-b188-75572dde6646)

# Terraform AWS S3 Bucket with Lifecycle Policy Automation
- This repository uses Terraform to provision an AWS S3 bucket with automated lifecycle policies for cost-effective storage management.

### Explanation of the code (point by point):

## main.tf file 

```hcl
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "6.0.0-beta3"
    }
  }
}

```

1 terraform { ... } Declares the start of the Terraform configuration block.

2 required_providers { ... } Specifies which providers are required for this Terraform project.

3 aws = { ... } Defines the AWS provider configuration.

4 source = "hashicorp/aws" Indicates that the AWS provider should be sourced from HashiCorp’s official provider registry.

5 version = "6.0.0-beta3" Specifies the exact version (6.0.0-beta3) of the AWS provider to use.

### Summary:
- This block ensures Terraform uses the specified version of the AWS provider from HashiCorp’s registry for managing AWS resources.

## s3bucket.tf file
```hcl
provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "example_bucket" {
  bucket        = var.bucket_name
  force_destroy = true

  tags = var.bucket_tags

  lifecycle {
    prevent_destroy = false
  }
}

resource "aws_s3_bucket_versioning" "example" {
  bucket = aws_s3_bucket.example_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "example" {
  bucket = aws_s3_bucket.example_bucket.id

  rule {
    id = "transition-to-glacier"
    filter {}

    transition {
      days          = 30
      storage_class = "GLACIER"
    }

    noncurrent_version_transition {
      noncurrent_days = 30
      storage_class   = "GLACIER"
    }

    noncurrent_version_expiration {
      noncurrent_days = 90
    }

    status = "Enabled"
  }
}

resource "aws_s3_bucket_public_access_block" "example" {
  bucket                  = aws_s3_bucket.example_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# SNS topic
# resource "aws_sns_topic" "s3_notifications" {
#   name = "s3-backup-notify-topic"
# }

# SNS topic subscription (email)
resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.s3_notifications.arn
  protocol  = "email"
  endpoint  = var.notification_email
}

# S3 bucket notification to SNS
resource "aws_s3_bucket_notification" "s3_event_notification" {
  bucket = aws_s3_bucket.example_bucket.id

  topic {
    topic_arn = aws_sns_topic.s3_notifications.arn
    events    = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_s3_bucket.example_bucket, aws_sns_topic.s3_notifications]
}
resource "aws_sns_topic" "s3_notifications" {
  name = "s3-backup-notify-topic"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Sid       = "AllowS3Publish",
        Effect    = "Allow",
        Principal = {
          Service = "s3.amazonaws.com"
        },
        Action    = "SNS:Publish",
        Resource  = "*",
        Condition = {
          ArnLike = {
            "aws:SourceArn" = "arn:aws:s3:::${var.bucket_name}"
          }
        }
      }
    ]
  })
}

```
### Explanation of the selected code (point by point)
- Lifecycle Rule Block (rule { ... }) Defines a lifecycle rule for the S3 bucket to manage object storage and cost.
- Transition to Glacier (transition { ... }) Moves current objects to the GLACIER storage class after 30 days to save costs.
- Noncurrent Version Transition (noncurrent_version_transition { ... }) Moves previous versions of objects (noncurrent versions) to GLACIER after 30 days.
- Noncurrent Version Expiration (noncurrent_version_expiration { ... }) Permanently deletes noncurrent object versions after 90 days.
- Status Enabled (status = "Enabled") Activates this lifecycle rule.
- Public Access Block Resource (aws_s3_bucket_public_access_block) Configures the S3 bucket’s public access settings.
- All Public Access Allowed All four settings (**block_public_acls, block_public_policy, ignore_public_acls, restrict_public_buckets**) are set to false, meaning public access is not restricted for this bucket.

## variable.tf file 
```hcl
variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
  default     = "burhandemotws"
}

variable "bucket_tags" {
  description = "Tags for the S3 bucket"
  type = map(string)
  default = {
    Name        = "BurhanDemoTWS"
    Environment = "Production"
  }
}

variable "region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "notification_email" {
  description = "Email address to receive S3 notifications"
  type        = string
  default     = "job.khanburhan503@gmail.com"  # 👈 Yahan apna email daalein
}

```
### Explanation of the code (point by point)
- variable "bucket_name" { ... } <br/>
  1 Declares a variable for the S3 bucket name <br/>
  2 Sets a description for documentation <br/>
  3 Specifies the type as a string. <br/>
  4 Provides a default value: "burhandemotws". <br/>

- variable "bucket_tags" { ... } <br/>
  1 Declares a variable for S3 bucket tags <br/>
  2 Sets a description for documentation. <br/>
  3 Specifies the type as a map of strings. <br/>
  4 Provides default tags : Name = "BurhanDemoTWS" | Environment = "Production" <br/>

- variable "region" { ... } <br/>
  1 Declares a variable for the AWS region. <br/>
  2 Sets a description for documentation. <br/>
  3 Specifies the type as a string. <br/>
  4 Provides a default value: "us-east-1". <br/>

### Summary
- These variable blocks define configurable values for your Terraform project, making it easy to change the S3 bucket name, tags, and AWS region without modifying the main code.

## Output.tf File

```hcl
output "bucket_name" {
  description = "The name of the created S3 bucket"
  value       = aws_s3_bucket.example_bucket.id
}

output "region" {
  description = "The AWS region used"
  value       = var.region
}

output "sns_notification_email" {
  description = "SNS email address to receive S3 upload notifications"
  value       = var.notification_email
}
output "sns_topic_arn" {
  description = "ARN of the SNS topic for S3 notifications"
  value       = aws_sns_topic.s3_notifications.arn
}
```
## Standard Terraform Workflow
1 terraform init
- Initializes your working directory containing Terraform configuration files.
- Downloads required provider plugins and modules.
- Should be run first whenever you start with new Terraform code or clone existing code.

2 terraform plan
- Creates an execution plan showing what actions Terraform will take to achieve the desired state.
- Shows what resources will be created, modified, or destroyed.
- Does not make any actual changes to your infrastructure.
- Always review the plan before applying!

3 terraform apply
- Executes the actions proposed in the **terraform plan**.
- Actually creates/modifies/destroys infrastructure resources.
- Will prompt for confirmation unless run with **-auto-approve flag**

4 terraform destroy
- Destroys all resources managed by your Terraform configuration.
- Should be used carefully as it removes infrastructure.

## Example Workflow
```hcl
# Initialize Terraform
terraform init

# Review what will be created
terraform plan

# Apply the changes (after verifying the plan looks correct)
terraform apply

# When finished, to clean up (if desired)
terraform destroy
```
![image](https://github.com/user-attachments/assets/c3c51019-c0a6-480e-acce-0f4c0fa69d9d)

# Prerequisites for Running the Python Script

- 🔧 1. Install Python (Recommended: Python 3.8+)
```script
python --version
```
- 📦 2. Install Required Python Package
```script
pip install boto3
```
- 📂 3. Setup Your File Paths
- Source Path: This is where your .bak or txt ya any other  files are stored:
```script
source_path = Path(r"D:\\DevOps Projects\\AWS-S3-Backup-Cost-Optimization-\\source")
```
- Destination Path: Where the .zip backup will be temporarily stored
```script
destination_path = Path(r"D:\\DevOps Projects\\AWS-S3-Backup-Cost-Optimization-\\destination")
```
- 🔐 4. AWS Credentials (IAM User)
- You'll need
```script
aws_access_key
aws_secret_key
```
- Make sure this IAM user has permissions for
```script
s3:PutObject
sns:Publish
```
- 5. S3 Bucket and SNS Topic Must Exist
```script
S3 Bucket Name: Example — burhandemotws
SNS Topic ARN: Example — arn:aws:sns:us-east-1:123456789012:s3-backup-topic
```
- 📧 6. SNS Email Subscription Must Be Confirmed
- Once the SNS topic is created (via Terraform or AWS Console), you must confirm the email subscription by clicking the link received in your inbox. Like I have atteched screenshort
![image](https://github.com/user-attachments/assets/8681b49f-f689-462a-8357-3629b75a8cd9)


## Step-by-Step Flow of the Script
- ✅ Step 1: Filter Yesterday’s .bak Files
```python
filter_previous_day_files(source_path)
```
- ✅ Step 2: Create a Backup (.zip)
```python
create_backup(filtered_files, source_path, destination_path)
```
- ✅ Step 3: Upload the ZIP File to S3
```python
upload_to_s3(zip_file, bucket_name, s3_folder, aws_access_key, aws_secret_key, region_name)
```
- ✅ Step 4: Send SNS Email Notification After Upload
```python
send_sns_notification(
    sns_topic_arn,
    aws_access_key,
    aws_secret_key,
    region_name,
    subject="Backup Notification",
    message="✅ Your database has been uploaded on S3. Please check."
)
```
- ✅ Final Variables You Need in Your Script
```python
source_path = Path(r"D:\\DevOps Projects\\AWS-S3-Backup-Cost-Optimization-\\source")
destination_path = Path(r"D:\\DevOps Projects\\AWS-S3-Backup-Cost-Optimization-\\destination")

bucket_name = "burhandemotws"
s3_folder = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

aws_access_key = "YOUR_AWS_ACCESS_KEY"
aws_secret_key = "YOUR_AWS_SECRET_KEY"
region_name = "us-east-1"
sns_topic_arn = "arn:aws:sns:us-east-1:YOUR_ACCOUNT_ID:YOUR_TOPIC_NAME"
```

## Python Code 
```python
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
region_name = "us-east-1"
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
```
# 🕒 Schedule with Windows Task Scheduler
1 Step-by-Step Guide 
- Open Task Scheduler
- Press Windows + R → Type taskschd.msc → Press Enter

2 Create a Basic Task 
- Click “Create Basic Task…” Name: **Daily S3 Backup **, Description: ```powershell ** Backup .txt files to S3 and send email** ```

3 Set Trigger
- Choose Daily
- Start time: ```powershell 1:00 AM ```

4 Set Action
- Choose Start a Program
- Program/script: **python**
- Add arguments: ```txt "D:\DevOps Projects\AWS-S3-Backup-Cost-Optimization-\daily_backup.py" ```

5 Finish 
- Confirm and click Finish
- ✅ Task is now scheduled to run daily at 1:00 AM.

6 📧 Email Notification Format
- The SNS email you receive will contain this message:
```hcl
Subject: Daily S3 Backup

✅ Your database has been uploaded on S3. Please check.
```
![image](https://github.com/user-attachments/assets/a58e83c7-3f5c-4aee-9621-3c42ade3b5fa)

![image](https://github.com/user-attachments/assets/a6cc6a53-5d31-4fc5-977b-fcc358b803c7)

![image](https://github.com/user-attachments/assets/ddf547ef-ee52-4af2-8a73-c3c6fc661184)


# ⚠ Important Notice
- This project (and upcoming ones) is made only for learning.
- ✅ You can share it on LinkedIn for learning.
- ❌ You cannot use this on personal YouTube or other learning platforms.
- 👨‍💻 This is made for beginners and new learners—please respect the work.
- Only the TWS Community is allowed to share this.
Thanks for understanding!<br/>
## Burhan

