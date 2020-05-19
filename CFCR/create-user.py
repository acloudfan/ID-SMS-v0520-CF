import boto3

# This will create the user
region="us-west-2"

session = boto3.Session(profile_name='work',region_name=region)
sm = session.client("sagemaker")

# get the domain id 
domainID='d-jgfq7yoda8y4'

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_user_profile

response = sm.create_user_profile(DomainId=domainID,
    UserProfileName='smuser')

print(response)

