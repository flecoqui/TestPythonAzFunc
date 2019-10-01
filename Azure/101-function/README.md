# Deployment of a REST API  hosted on Azure Function

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fflecoqui%2FTestPythonAzFunc%2Fmaster%2FAzure%2F101-function%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fflecoqui%2FTestPythonAzFunc%2Fmaster%2FAzure%2F101-function%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

This template allows you to deploy from Github a Python REST API hosted on Azure Function. Moreover, the REST API service will be directly deployed from github towards Azure Function.

The REST API (api/HttpTriggerPythonFunction) is actually an JSON echo service with two paramaters (param1, param2), if you send a Json string in the http content, you will receive the same Json string in the http response.
Below a curl command line to send the request.
POST Request:


          curl -d "{\"param1\":\"0123456789\",\"param2\":\"abcdef\"}' -H "Content-Type: application/json"  -X POST   https://<hostname>/api/HttpTriggerPythonFunction


GET Request:


          curl -H "Content-Type: application/json"  -X GET   https://<hostname>/api/HttpTriggerPythonFunction?param1=0123456789&param2=abcdef







# DEPLOYING THE REST API ON AZURE SERVICES

## PRE-REQUISITES
First you need an Azure subscription.
You can subscribe here:  https://azure.microsoft.com/en-us/free/ . </p>
Moreover, we will use Azure CLI v2.0 to deploy the resources in Azure.
You can install Azure CLI on your machine running Linux, MacOS or Windows from here: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest 



## CREATE RESOURCE GROUP:
First you need to create the resource group which will be associated with this deployment. For this step, you can use Azure CLI v1 or v2.

* **Azure CLI 1.0:** azure group create "ResourceGroupName" "RegionName"

* **Azure CLI 2.0:** az group create an "ResourceGroupName" -l "RegionName"

For instance:

    azure group create testpythonazfuncrg eastus2

    az group create -n testpythonazfuncrg -l eastus2

## DEPLOY THE SERVICES:

### DEPLOY REST API ON AZURE FUNCTION, APP SERVICE, VIRTUAL MACHINE:
You can deploy Azure Function, Azure App Service and Virtual Machine using ARM (Azure Resource Manager) Template and Azure CLI v1 or v2

* **Azure CLI 1.0:** azure group deployment create "ResourceGroupName" "DeploymentName"  -f azuredeploy.json -e azuredeploy.parameters.json*

* **Azure CLI 2.0:** az group deployment create -g "ResourceGroupName" -n "DeploymentName" --template-file "templatefile.json" --parameters @"templatefile.parameter..json"  --verbose -o json

For instance:

    azure group deployment create testpythonazfuncrg testpythonazfuncdep -f azuredeploy.json -e azuredeploy.parameters.json -vv

    az group deployment create -g testpythonazfuncrg -n testpythonazfuncdep --template-file azuredeploy.json --parameter @azuredeploy.parameters.json --verbose -o json


When you deploy the service you can define the following parameters:</p>
* **namePrefix:** The name prefix which will be used for all the services deployed with this ARM Template</p>
* **azFunctionAppSku:** The Azure Function App Sku Capacity, by defualt S1</p>
* **storageSku:** The Azure Storage Sku Capacity, by default Standard_LRS</p>
* **repoURL:** The github repository url</p>
* **branch:** The branch name in the repository</p>
* **repoFunctionPath:** The path to the Azure Function code, by default "TestFunctionApp"</p>


The services has been deployed with 2 command lines.


# TEST THE SERVICES:

## TEST THE SERVICES WITH CURL
Once the services are deployed, you can test the REST API using Curl. You can download curl from here https://curl.haxx.se/download.html 
For instance :

     curl -d "{\"param1\":\"0123456789\",\"param2\":\"abcdef\"}" -H "Content-Type: application/json"  -X POST   "https://<namePrefix>function.azurewebsites.net/api/HttpTriggerPythonFunction"
     curl -H "Content-Type: application/json"  -X GET   "https://<namePrefix>function.azurewebsites.net/api/HttpTriggerPythonFunction?param1=0123456789&param2=abcdef"

</p>


# DELETE THE REST API SERVICES 


## DELETE THE RESOURCE GROUP:

* **Azure CLI 1.0:**      azure group delete "ResourceGroupName" "RegionName"

* **Azure CLI 2.0:**  az group delete -n "ResourceGroupName" "RegionName"

For instance:

    azure group delete testpythonazfuncrg eastus2

    az group delete -n testpythonazfuncrg 





# Next Steps

1. More advanced Python Azure Function using Azure Storage, Azure Data Lake  
