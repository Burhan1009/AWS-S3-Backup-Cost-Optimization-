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
