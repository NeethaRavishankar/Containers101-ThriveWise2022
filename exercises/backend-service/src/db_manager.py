import boto3
from datetime import datetime
from botocore.exceptions import ClientError

class DBManager:
    dynamo_client = None
    table = None
    pk_attribute = ''
    sk_attribute = ''
    
    def __init__(self, database_table='example', pk_attribute_name='pk_attribute', sk_attribute_name='sk_attribute', endpoint=None):
        self.dynamo_client = boto3.resource('dynamodb', region_name='us-west-2', aws_access_key_id='', aws_secret_access_key='', endpoint_url=endpoint)
        self.table = self.dynamo_client.Table(database_table)

        try:
            self.table.table_status
        except ClientError:
            self.dynamo_client.create_table(
                AttributeDefinitions=[
                    {
                        'AttributeName': pk_attribute_name,
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': sk_attribute_name,
                        'AttributeType': 'S'
                    },
                ],
                TableName=database_table,
                KeySchema=[
                    {
                        'AttributeName': pk_attribute_name,
                        'KeyType': 'HASH',
                    },
                    {
                        'AttributeName': sk_attribute_name,
                        'KeyType': 'RANGE',
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 20,
                    'WriteCapacityUnits': 20
                },
            )

        self.pk_attribute = pk_attribute_name
        self.sk_attribute = sk_attribute_name
        
    
    def put_item_into_db(self, item):
        # Put item into DynamoDB
    
    def get_items(self):
        # Scan to get all items from DynamoDB