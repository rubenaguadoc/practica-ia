import json
import sys
sys.path.append('src')
from aEstrella import algoritmo as aStar

def lambda_handler(event, context):
    if event["httpMethod"] == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
            }
        }
    
    data = json.loads(event["body"])
    result, lines = aStar(int(data["inicio"]), int(data["fin"]), bool(data["transbordos"]))

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(
            {
                "result": result,
                "lines": lines
            }
        )
    }
