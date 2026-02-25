import json  # Used to convert Python data into JSON format and vice versa
import os    # Used to interact with the operating system (not used here but imported)
import boto3 # AWS SDK for Python to interact with AWS services like DynamoDB

def lambda_handler(event, context):  # Main function that AWS Lambda calls
    try:
        # Calls page_router function and passes HTTP method, query parameters, and body
        mypage = page_router(event['httpMethod'], event['queryStringParameters'], event['body'])
        return mypage  # Returns the response back to API Gateway
    except Exception as e:
        # If any error happens, return 500 error with message
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})  # Convert error into JSON format
        }

def page_router(httpmethod, querystring, formbody):  # Function to handle GET and POST requests
    if httpmethod == 'GET':  # If request method is GET
        try:
            # Open index.html file in read mode
            with open('index.html', 'r') as htmlFile:
                htmlContent = htmlFile.read()  # Read HTML content
            return {
                'statusCode': 200,  # Success response
                'headers': {"Content-Type": "text/html"},  # Tell browser content is HTML
                'body': htmlContent  # Send HTML page as response
            }
        except Exception as e:
            # If error while reading file
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }

    elif httpmethod == 'POST':  # If request method is POST
        try:
            insert_record(formbody)  # Insert form data into DynamoDB
            # Open success.html file in read mode
            with open('success.html', 'r') as htmlFile:
                htmlContent = htmlFile.read()  # Read success page content
            return {
                'statusCode': 200,
                'headers': {"Content-Type": "text/html"},
                'body': htmlContent  # Send success page after inserting record
            }
        except Exception as e:
            # If any error during insert
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }

def insert_record(formbody):  # Function to insert form data into DynamoDB
    formbody = formbody.replace("=", "' : '")  # Replace = with : for DynamoDB format
    formbody = formbody.replace("&", "', '")   # Replace & to separate fields properly
    # Create PartiQL insert statement (Replace table name if needed)
    formbody = "INSERT INTO nikii value {'" + formbody + "'}"   # Replace with DynamoDB Table name(My table name is yaswanth)

    client = boto3.client('dynamodb')  # Create DynamoDB client
    response = client.execute_statement(Statement=formbody)  # Execute insert query
    # Assuming the execute_statement call returns successfully
    return response  # Return DynamoDB response
