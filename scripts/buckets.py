
import boto3
import pprint

s3 = boto3.client('s3')

response = s3.list_objects(
    Bucket='daftpunkbucket',
    Delimiter='string',
    EncodingType='url',
    Marker='string',
    MaxKeys=123,
    Prefix='string',
    RequestPayer='requester'
)

print(pprint.pprint(response))
