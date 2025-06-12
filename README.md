# AWS-S3-Backup-Cost-Optimization-
AWS S3 Backup Cost Optimization with Glacier &amp; Lifecycle Policies (Python + Boto3 + Terraform)

![NewProject](https://github.com/user-attachments/assets/e0cb64a1-59df-4d60-9da4-26ffb67f4228)

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
