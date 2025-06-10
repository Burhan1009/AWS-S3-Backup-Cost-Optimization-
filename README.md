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

* click on Close after install all packages in Python
![image](https://github.com/user-attachments/assets/a5b3f389-d0fc-4a92-8978-9c8a7bf12b4f)
