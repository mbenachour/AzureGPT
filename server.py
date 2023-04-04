from flask import Flask, request, jsonify
import openai
from flask_cors import CORS 
import subprocess
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for the Flask application

# load env variables from .env 

load_dotenv()

# read env variables

GPT_API_KEY = os.getenv('GPT_API_KEY')


# # GPT-4 API key
# GPT_API_KEY =   os.getenv('GPT_API_KEY')

# # Azure credentials
AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID')
AZURE_CLIENT_SECRET =  os.getenv('AZURE_CLIENT_SECRET')
AZURE_TENANT_ID = os.getenv('AZURE_TENANT_ID')
AZURE_SUBSCRIPTION_ID = os.getenv('AZURE_SUBSCRIPTION_ID')

# Set up OpenAI credentials
openai.api_key = GPT_API_KEY

# Azure CLI authentication command (using a service principal)
authentication_command = f"az login --service-principal -u {AZURE_CLIENT_ID} -p {AZURE_CLIENT_SECRET} --tenant {AZURE_TENANT_ID} "

@app.route('/azure', methods=['POST'])
def create_azure_environment():
    # Get description from frontend
    description = request.json.get('description')

    # Call GPT-3 API to generate Bash code for Azure CLI commands using the "davinci" engine
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f'Generate Bash code for Azure CLI commands to create an environment based on the following description:\n{description}\n\nBash code:',
            max_tokens=200
        )
        generated_code = response.choices[0].text.strip()

        # Authenticate with Azure CLI using a service principal and specifying subscription
        try:
            subprocess.check_output(authentication_command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            return jsonify({'message': f'Authentication Error: {str(e.output)}'})

        # Execute the generated Bash code and get summary from GPT-3
        try:
            output = subprocess.check_output(generated_code, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            print(output)

            # delete all null from output
            output = output.replace('\x00', '')
            print(output)
            # Request a summary of the results from GPT-3
            summary_response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f'Please orgnize the results in stable format and show them as html table :\n{output}\n\nSummary:',
                max_tokens=500
            )
            summary = summary_response.choices[0].text.strip()
            message = 'Summary:\n' + summary
        except subprocess.CalledProcessError as e:
            message = f'Error: {str(e.output)}'
    except Exception as e:
        message = f'Error: {str(e)}'

    return jsonify({'message': message})

if __name__ == '__main__':
    # Run the Flask app on port 8081
    app.run(port=8081)


