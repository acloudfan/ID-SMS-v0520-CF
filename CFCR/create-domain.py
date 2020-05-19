import boto3
import sys

# This will create the domain
region="us-west-2"

session = boto3.Session(profile_name='work',region_name=region)
sm = session.client("sagemaker")

# Gets default VPC and Subnets
def get_vpc_subnets() :
    clt = session.client('ec2')
    vpcs = clt.describe_vpcs()
    vpc_id = vpcs['Vpcs'][0]['VpcId']

    sn_list = []
    subnet_list = clt.describe_subnets()
    for subnet in subnet_list['Subnets']:
        if subnet['VpcId'] == vpc_id:
            sn_list.append(subnet['SubnetId'])
    return vpc_id, sn_list

# Create the studio domain
def create_domain():
    vpc_id, sn_list = get_vpc_subnets()

    try:
        response = sm.create_domain(
            DomainName='SSMID052020',
            AuthMode='IAM',
            DefaultUserSettings={
                'ExecutionRole': 'arn:aws:iam::837510115097:role/service/sm-studio-role',
                'SharingSettings': {
                    'NotebookOutputOption': 'Allowed' 
                }     
            } ,
            SubnetIds=sn_list,
            VpcId=vpc_id
        )
    except:
        print("suck")
        print(sys.exc_info())
        response="error"


    return response

response = create_domain()
print(response)

# response = sm.create_domain(
#     DomainName='SSMID052020',
#     AuthMode='IAM',
#     DefaultUserSettings={
#         'ExecutionRole': 'arn:aws:iam::837510115097:role/service/sm-studio-role',
#         'SharingSettings': {
#             'NotebookOutputOption': 'Allowed' 
#         }     
#     } ,
#     SubnetIds=[
#         'subnet-188f8853',
#         'subnet-1afb0f47',
#         'subnet-22b9a35b',
#         'subnet-76f9955d'
#     ],
#     VpcId='vpc-59961e21'
# )


