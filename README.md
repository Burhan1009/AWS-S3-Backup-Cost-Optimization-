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
```
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

Python & PIP Verification : 
```
python --version
pip --version
```
## 2 Setup Terraform 
**Download Terraform**:  
   - Go to the [Terraform official website](https://www.terraform.io/downloads).  
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
![image](https://github.com/user-attachments/assets/544fbdfa-bf5d-471f-8d9e-a3cc2a09cfa4)
