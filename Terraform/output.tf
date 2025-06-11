output "bucket_name" {
  description = "The name of the created S3 bucket"
  value       = aws_s3_bucket.example_bucket.id
}

output "region" {
  description = "The AWS region used"
  value       = var.region
}
