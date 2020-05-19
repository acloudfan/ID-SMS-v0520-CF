aws cloudformation create-stack --stack-name SM-ID-0520 --template-body file://CF/sm-studio-id.yaml --capabilities CAPABILITY_NAMED_IAM  --parameters ParameterKey=SMPassword,ParameterValue=***SET This*** --region us-east-1

aws cloudformation update-stack --stack-name SM-ID-0520 --template-body file://CF/sm-studio-id.yaml --capabilities CAPABILITY_NAMED_IAM  --parameters ParameterKey=SMPassword,UsePreviousValue=true --region us-east-1

aws cloudformation delete-stack --stack-name SM-ID-0520 

aws cloudformation describe-stacks  --stack-name SM-ID-0520