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
