# Set up AWS secrets manager client

import boto3
import json
from functools import lru_cache

@lru_cache
def secrets_client():
    return boto3.client("secretsmanager")

def get_secret(secret_name: str) -> dict:
    client = secrets_client()
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])
