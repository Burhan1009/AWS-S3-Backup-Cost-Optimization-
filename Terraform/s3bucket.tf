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
