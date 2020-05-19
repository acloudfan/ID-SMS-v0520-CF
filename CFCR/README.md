https://aws.amazon.com/blogs/infrastructure-and-automation/aws-cloudformation-custom-resource-creation-with-python-aws-lambda-and-crhelper/


aws lambda create-function --function-name "crhelper-sum-resource" --handler "lambda_function.handler" --timeout 900 --zip-file fileb://./sum.zip --runtime python3.7 --role "arn:aws:iam::837510115097:role/SM-ID-0520-SMLambdaExecutionRole-1EUSYKLR5X5SM" --region us-west-2

aws cloudformation create-stack --stack-name SM-Custom-Test --template-body file://sum-stack.yaml  --region us-west-2

Test
====
1. Create the domain
