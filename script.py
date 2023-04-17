import boto3
import yaml

myclient = boto3.client('s3',region_name='us-east-2')

with open('cf.yml','r') as f:
    mydata = yaml.load(f,Loader=yaml.FullLoader)

myclient.create_bucket(**mydata)










