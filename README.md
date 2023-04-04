# AzureGPT

AzureGPT is a web application that allows users to create an Azure cloud environment based on a textual description. The application uses the OpenAI API to generate Azure CLI commands and executes them to create the described environment. The results of the execution are displayed in the user interface and summarized using the OpenAI API.

## Features

- Web-based user interface for describing Azure cloud environments.
- Backend service that interacts with the OpenAI API to generate Bash code for Azure CLI commands.
- Execution of generated Bash code to create the described environment in Azure.
- Summarization of execution results using the OpenAI API.

## Setup and Requirements

### Requirements

- Python 3.7 or higher.
- Flask.
- Flask-CORS.
- OpenAI Python library.
- Azure CLI.

### Configuration

1. Set up an Azure service principal with appropriate permissions and obtain an OpenAI API key.
2. Update the `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`, and `GPT_API_KEY` variables in the Python script with your actual credentials.

### Installation

1. Install the required Python packages:
``` python

pip install flask flask-cors openai

```

2. Install the Azure CLI:
https://docs.microsoft.com/en-us/cli/azure/install-azure-cli


## Running the Application

1. Start the backend service by running the Python script:


python server.py


2. Open the `index.html` file in your web browser to access the user interface.

## Usage

1. Enter a description of the Azure cloud environment you wish to create in the text box.
2. Click the "Submit" button to generate and execute the Azure CLI commands.
3. View the summarized results of the execution in the result area.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer

This application executes arbitrary code generated by the OpenAI API. Use it with caution and consider additional security measures, such as input validation and sandboxing, in a production environment.

## Contributing

Contributions are welcome! Please submit pull requests or open issues to contribute to this project.
# AzureGPT
