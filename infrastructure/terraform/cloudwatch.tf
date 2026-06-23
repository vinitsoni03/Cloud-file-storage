resource "aws_cloudwatch_log_group" "lambda_logs" {
  name              = "/aws/lambda/cloud-file-storage"
  retention_in_days = 30
}

resource "aws_cloudwatch_metric_alarm" "lambda_errors" {
  alarm_name          = "lambda-errors"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = "2"
  metric_name         = "Errors"
  namespace           = "AWS/Lambda"
  period              = "60"
  statistic           = "Sum"
  threshold           = "1"
  alarm_description   = "Alarm when Lambda errors exceed threshold"
}
