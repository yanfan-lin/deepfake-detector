import os
import json
import requests

def lambda_handler(event, context):

    # Retrieve query parameters from the event.
    query_params = event.get('queryStringParameters') or {}
    image_url = query_params.get('image_url')
    
    if not image_url:
        return {
            'statusCode': 400,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Missing image_url parameter'})
        }
    
    # Retrieve API credentials from environment variables.
    api_user = os.environ.get('API_USER')
    api_secret = os.environ.get('API_SECRET')
    
    if not api_user or not api_secret:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'API credentials not set in environment'})
        }
    
    # Set up parameters for the external API call.
    params = {
        'models': 'genai',
        'api_user': api_user,
        'api_secret': api_secret,
        'url': image_url
    }
    
    try:
        # Perform the API call to SightEngine.
        response = requests.get("https://api.sightengine.com/1.0/check.json", params=params)
        response.raise_for_status()  # Raise exception for HTTP errors.
        result = response.json()
        
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(result)
        }
    except requests.RequestException as req_err:
        # Handle exceptions related to the API call.
        return {
            'statusCode': 502,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': f'Error calling external API: {str(req_err)}'})
        }
    except Exception as e:
        # Catch any other exceptions.
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
