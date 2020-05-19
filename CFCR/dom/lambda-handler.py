## This is invoked by the CF template for
## Creating the domain

import boto3
import sys
from crhelper import CfnResource

helper = CfnResource()

# This will create the domain
region="us-west-2"
session = boto3.Session(region_name=region)
sm = session.client("sagemaker")

# Gets default VPC and Subnets
def get_vpc_subnets(session) :
    clt = session.client('ec2')
    vpcs = clt.describe_vpcs()
    vpc_id = vpcs['Vpcs'][0]['VpcId']

    sn_list = []
    subnet_list = clt.describe_subnets()
    for subnet in subnet_list['Subnets']:
        if subnet['VpcId'] == vpc_id:
            sn_list.append(subnet['SubnetId'])

    print("VPC={}".format(vpc_id))
    print(sn_list)

    return vpc_id, sn_list

# Create the studio domain
def create_domain_boto3(session, execution_role):

    # Get the default VPC & Subnets
    vpc_id, sn_list = get_vpc_subnets(session)

    sm = session.client("sagemaker")

    response = sm.create_domain(
        DomainName='SSMID052020',
        AuthMode='IAM',
        DefaultUserSettings={
            'ExecutionRole': execution_role,
            'SharingSettings': {
                'NotebookOutputOption': 'Allowed' 
            }     
        } ,
        SubnetIds=sn_list,
        VpcId=vpc_id
    )

    print(response)

    return response

@helper.create
def  create_domain(event, _):
    studio_execution_role=event['ResourceProperties']['StudioExecutionRole']
    region=event['ResourceProperties']['StudioDomainRegion']
    session = boto3.Session(region_name=region)

    try:
        response = create_domain_boto3(session, studio_execution_role)
        helper.Data['response'] = response
        helper.Data['StackId'] = response['StackId']
        print(response)
        domainArn = response['DomainArn']
        domainId =  domainArn.partition('domain/')[2] 
    except:
        print(sys.exc_info())
        domainId =  "Domain Creation Failed!!!"

    helper.Data['domainId'] = domainId
    

@helper.update
def  dom_update(event, _):
    pass

@helper.delete
def  dom_delte(event, _):
    pass


def handler(event, context):
    helper(event, context)