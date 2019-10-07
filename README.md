# Deployment of a REST API  hosted on Azure Function, Azure App Service, Azure Virtual Machine, Azure Container Instance and Azure Kubernetes Service

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fflecoqui%2FTestPythonAzFunc%2Fmaster%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fflecoqui%2FTestPythonAzFunc%2Fmaster%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

This repository contains sample to deploy :
- Python Azure Function based on Python 3.6
- Python Azure Container based on Python 3.7 
The source code of the Azure Function and the Container are stored on this repository as well.
Both Azure Function Azure Container expose a REST API.

The REST API (api/HttpTriggerPythonFunction) is actually an JSON echo service, if you send a Json string in the http content, you will receive the same Json string in the http response.
Below a curl command line to send the request:


          curl -d "{\"param1\":\"0123456789\",\"param2\":\"abcdef\"}"  -H "Content-Type: application/json"  -X POST   "https://<hostname>/api/HttpTriggerPythonFunction"

          curl -H "Content-Type: application/json"  -X GET   "https://<hostname>/api/HttpTriggerPythonFunction?param1=0123456789&param2=abcdef"



![](https://raw.githubusercontent.com/flecoqui/TestPythonAzFunc/master/Docs/1-architecture.png)


# DEPLOYING THE REST API ON AZURE SERVICES

This chapter describes how to deploy the rest API automatically on :</p>
* **Python Azure Function**</p>
* **Python Azure Container Instance**</p>
in **3 command lines**.

## PRE-REQUISITES
First you need an Azure subscription.
You can subscribe here:  https://azure.microsoft.com/en-us/free/ . </p>
Moreover, we will use Azure CLI v2.0 to deploy the resources in Azure.
You can install Azure CLI on your machine running Linux, MacOS or Windows from here: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest 

The first Azure CLI command will create a resource group.
The second  Azure CLI command will deploy an Azure Function, an Azure App Service and a Virtual Machine using an Azure Resource Manager Template.
In order to deploy Azure Container Instance or Azure Kubernetes Service a Service Principal is required to pull the container image from Azure Container Registry, unfortunately as today it's not possible to create Azure Service Principal with an Azure Resource Manager Template, we will use a PowerShell script on Windows or a Bash script on Linux to deploy the Azure Container Instance and  Azure Kubernetes Service.  


## CREATE RESOURCE GROUP:
First you need to create the resource group which will be associated with this deployment. For this step, you can use Azure CLI v1 or v2.

* **Azure CLI 1.0:** azure group create "ResourceGroupName" "RegionName"

* **Azure CLI 2.0:** az group create an "ResourceGroupName" -l "RegionName"

For instance:

    azure group create TestPythonAzFuncrg eastus2

    az group create -n TestPythonAzFuncrg -l eastus2

## DEPLOY THE SERVICES:

### TESTING THE PYTHON AZURE FUNCTION LOCALLY:
You can test your Python Azure Function locally provided you install Python 3.6 on your machine. 

Run the followig commands:

1. Open a Command Shell and change directory "C:\git\me\TestPythonAzFunc\PythonFunction".
2. Run the command : 


        C:\git\me\TestPythonAzFunc\PythonFunction> python -m venv .venv


3. Run the command : 


        C:\git\me\TestPythonAzFunc\PythonFunction> .venv\scripts\activate


4. Run the command : 


        (.venv) C:\git\me\TestPythonAzFunc\PythonFunction> func host start


5. The function will run locally using a TCP port to receive the REST API requsts: 
For instance:


        HttpTriggerPythonFunction: [GET,POST] http://localhost:7071/api/HttpTriggerPythonFunction


6. Use curl command to test the  REST API:


        curl -d "{\"param1\":\"0123456789\",\"param2\":\"abcdef\"}" -H "Content-Type: application/json"   -X POST "http://localhost:7071/api/HttpTriggerPythonFunction"



### DEPLOYING THE PYTHON AZURE FUNCTION TO AZURE:
Follow the instructions on the link below to deploy the Python Azure Function to Azure:

[Deploy to Azure with Visual Studio Code](https://docs.microsoft.com/en-us/azure/python/tutorial-vs-code-serverless-python-05) 


[Deploy to Azure with Azure DevOps](https://docs.microsoft.com/en-us/azure/azure-functions/functions-how-to-azure-devops)

Unfortunaltely, currently it's not possible a Python Azure Function with an ARM Template like for a .Net Core Azure Function here:

[Deploy .Net Core Azure Function to Azure withARM Template](https://github.com/flecoqui/TestRESTAPIServices/tree/master/Azure/101-function)  





### DEPLOY REST API ON AZURE CONTAINER INSTANCE:

In order to deploy the REST API on Azure Container Instance or Azure Kubernetes you will use a Powershell script on Windows and a Bash script on Linux with the following parameters:</p>
* **ResourceGroupName:**						The name of the resource group used to deploy Azure Function, Azure App Service and Virtual Machine</p>
* **namePrefix:**						The name prefix which has been used to deploy Azure Function, Azure App Service and Virtual Machine</p>
* **cpuCores:**						The number of CPU cores used by the containers on Azure Container Instance or Kubernetes, for instance : 1, by default 0.4 </p>
* **memoryInGB:**				The amount of memory in GB used by the containers on Azure Container Instance or Kubernetes, for instance : 2, by defauylt 0.3 </p>
</p>
</p>

This Azure Container Instance does support Python 3.7 whereas Python Azure Function only support Python 3.6.
 
Below the command lines for Windows and Linux:

* **Powershell Windows:** .\install-containers-windows.ps1  "ResourceGroupName" "NamePrefix" "cpuCores" "memoryInGB"

* **Bash Linux:** ./install-containers.sh "ResourceGroupName" "NamePrefix" "cpuCores" "memoryInGB" 


For instance:

    ./install-containers.sh TestPythonAzFuncrg testrest 2 7 

    .\install-containers-windows.ps1 TestPythonAzFuncrg testrest 2 7

Once deployed, the following services are available in the resource group:


![](https://raw.githubusercontent.com/flecoqui/TestPythonAzFunc/master/Docs/1-deploy.png)


The services has been deployed with 3 command lines.

If you want to deploy the REST API on only one single service, you can use the resources below:</p>

* **Azure Function:** Template ARM to deploy Azure Function https://github.com/flecoqui/TestPythonAzFunc/tree/master/Azure/101-function </p>
* **Azure Container Instance:** Template ARM and scripts to deploy Azure Container Instance  https://github.com/flecoqui/TestPythonAzFunc/tree/master/Azure/101-aci</p>


# TEST THE SERVICES:

## TEST THE SERVICES WITH CURL
Once the services are deployed, you can test the REST API using Curl. You can download curl from here https://curl.haxx.se/download.html 
For instance :

     curl -d  "{\"param1\":\"0123456789\",\"param2\":\"abcdef\"}" -H "Content-Type: application/json"  -X POST   https://<namePrefix>function.azurewebsites.net/api/HttpTriggerPythonFunction
     curl -d  "{\"param1\":\"0123456789\",\"param2\":\"abcdef\"}" -H "Content-Type: application/json"  -X POST   http://<namePrefix>aci.<Region>.azurecontainer.io/api/HttpTriggerPythonFunction

</p>


# DELETE THE REST API SERVICES 

## DELETE AZURE CONTAINER REGISTRY SERVICE PRINCIPAL :

**Azure CLI 2.0:** az ad sp  delete --id "ServicePrincipalUrl"

For instance:

    az ad sp delete --id http://testrestacrsp


## DELETE THE RESOURCE GROUP:

* **Azure CLI 1.0:**      azure group delete "ResourceGroupName" "RegionName"

* **Azure CLI 2.0:**  az group delete -n "ResourceGroupName" "RegionName"

For instance:

    azure group delete TestPythonAzFuncrg eastus2

    az group delete -n TestPythonAzFuncrg 




# Next Steps

1. Add ARM Tempalte for Python Azure Function when it will be supported  
