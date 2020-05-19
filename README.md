aws cloudformation create-stack --stack-name SM-ID-0520 --template-body file://CF/sm-studio-id.yaml --capabilities CAPABILITY_NAMED_IAM  --parameters ParameterKey=SMPassword,ParameterValue=<SET THIS> --region us-east-1

aws cloudformation update-stack --stack-name SM-ID-0520 --template-body file://CF/sm-studio-id.yaml --capabilities CAPABILITY_NAMED_IAM  --parameters ParameterKey=SMPassword,UsePreviousValue=true --region us-east-1

aws cloudformation delete-stack --stack-name SM-ID-0520 

aws cloudformation describe-stacks  --stack-name SM-ID-0520

Custom test
===========
aws cloudformation create-stack --stack-name SM-Customer --template-body file://./sm-custom.yaml  --region us-west-2

References:
https://aws.amazon.com/cloudformation/resources/templates/

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html

S3 Lambda setup
https://aws.amazon.com/blogs/infrastructure-and-automation/deploying-aws-lambda-functions-using-aws-cloudformation-the-portable-way/

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html

API Gateway
https://bl.ocks.org/magnetikonline/c314952045eee8e8375b82bc7ec68e88

https://volkanpaksoy.com/archive/2019/01/18/AWS-Security-Best-Practices-Use-IAM-instead-of-root/
https://aws.nz/best-practice/cloudformation-service-roles/


Custom Resource
https://www.alexdebrie.com/posts/cloudformation-custom-resources/

