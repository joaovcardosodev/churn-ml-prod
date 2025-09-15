import pandas as pd
import boto3
from tqdm import tqdm

dynamodb = boto3.resource('rds', region_name='us-east-1')
table = dynamodb.Table('Customer')