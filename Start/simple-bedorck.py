import json
import boto3
import os

os.environ['AWS_PROFILE'] = 'innovation'

def lambda_handler(event, context=None):
    print("Lambda function started")  # Debugging statement

    # Set up AWS session
    session = boto3.Session(region_name='us-east-1')
    bedrock = session.client('bedrock-runtime')
    print("AWS client initialized")  # Debugging statement

    # Model and prompt details
    bedrock_model_id = 'amazon.titan-text-express-v1'
    prompt = "What is the difference between a Lambda function and a serverless function?"
    print("Prompt prepared:", prompt)  # Debugging statement

    # Prepare the request body
    body = json.dumps({
        "inputText": prompt,
        "textGenerationConfig": {
            "temperature": 0,
            "topP": 0.5,
            "maxTokenCount": 1024,
            "stopSequences": []
        }
    })

    print("Request body prepared")  # Debugging statement

    # Invoke the Bedrock model
    try:
        response = bedrock.invoke_model(
            modelId=bedrock_model_id,
            body=body,
            contentType='application/json',
            accept='application/json'
        )
        print("Model invoked successfully")  # Debugging statement

        # Read the response body from StreamingBody
        response_body = json.loads(response['body'].read().decode('utf-8'))
        print("Response body received:", response_body)  # Debugging statement

        # Extract text from response
        response_text = response_body["results"][0]["outputText"]
        print("Extracted text from response:", response_text)
        return response_text
    except Exception as e:
        print("Error occurred:", e)  # Debugging statement
        return None

# Simulate event and context for local testing
mock_event = {}
mock_context = None

lambda_handler(mock_event, mock_context)

