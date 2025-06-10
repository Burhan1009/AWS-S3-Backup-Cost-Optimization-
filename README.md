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
