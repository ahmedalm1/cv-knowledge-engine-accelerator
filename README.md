# CV Knowledge Engine Solution Accelerator

## About this accelerator
The CV Knowledge Engine solution accelerator aims to provides a quick way of creating an intelligent search engine, that enables searching and filtering through CV and resume documents. It leverages Knowledge Mining and Cognitive Services technologies, to extract all the valuable information and insights from the CV documents, like names, contact information, years of experience, skills and qualifications, ..etc. It also creates an intuitive, easy-to-navigate user interface, that allows for a full search experience with capabilities like searching with search terms, customized filters, and informative result cards. Moreover, the extracted information can also be exported to Power BI and used to create informative dashboards, to give a high level overview of the information extracted. 

### Business Use Case 
The process of screening and searching through CV documents submitted by job seekers is a long and costly process, where the recruiters teams usually have to go through each submitted CV manually, to find the best candidates suited for the job opening. This accelerator will help extract all the essential information from CVs and resumes and simplify the process of searching and filtering through applicants, which will significantly reduce costs and time to isights. 

### Demo Website
You can demo the accelerator by visiting this website [CV Knowledge Engine](https://cvknowledgeengine.azurewebsites.net/).

### Resources and Architecture 
- Storage Account 
- Cognitive Search 
- Cognitive Services
- Azure Function 
- App Service

![Architecture](https://user-images.githubusercontent.com/88718044/139073235-eb6b8b2c-3577-405e-b974-82bc951676dc.png)

### Sample Documents 
The sample documents used in this accelerator to create the demo were 223 dummy CV documents, acquired from [Resume Krafts](https://resumekraft.com/resume-examples/) website.

### Extracted Information
The information and isights extracted from the CV documents can be grouped into three categories: 

#### PII Information
- Name 
- Email
- Phone number
- Location 
- LinkedIn 
#### Professional Information
- Years of experience
- Qualifications
- Languages
- Organizations
- Skills 
#### Other Insights
- Key phrases

### Web App Interface
The first interface created to display the extracted insights is a website interface, that can be used to search and filter through the CV documents.

#### Home Page
![Home Page](https://user-images.githubusercontent.com/88718044/139071306-6595000e-a33c-4dca-85eb-ed6c475d66cf.jpeg)

#### Search Results
![Search Results](https://user-images.githubusercontent.com/88718044/139071348-131db6aa-f11b-4857-88b4-cbe61bae5fb6.jpeg)

### PowerBI Dashboard
COMING SOON

## Deployemnt Process
Deploying the accelerator can be done in seven simple steps, that cover every aspect from deploying the resources, creating the search service elements, and conecting to the web interface. 

### Prerequisites
In order to deploy the accelerator, clone or download this repository, and make sure the following requirements are met:
- Azure Subscription 
- Visual Studio 2019 or later
- VS Code with Azure Functions extension
- Sample CV documents
- Postman 

### Step 0: Deploy the resources
Using the provided ARM template, create all the required Azure resources by clicking on this button: 

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAhmedAlmu%2Fcv-knowledge-engine-accelerator%2Fmain%2FAssets%2FARM%2520Template%2Ftemplate.json)

### Step 1: Setup the Environemnt 
After deploying the resources successfully, navigate to the newly created Storage Account in Azure, and upload the sample documents in a new blob container.

The sample documents can be found in [Assets/Sample Documents](https://github.com/AhmedAlmu/cv-knowledge-engine-accelerator/tree/main/Assets/Sample%20Documents) folder. 

Next, navigate to the folder [Assets/Postman Script](https://github.com/AhmedAlmu/cv-knowledge-engine-accelerator/tree/main/Assets/Postman%20Script) to find the Postman collection that will be used to create the Search Service elements. 

In Postman, import the collection and fill in the global variables with the proper values. To do that, click on the collection's name and navigate to the "Variables" tab. Modify the values in the "CURRENT VALUE" column according to the following table: 

| CURRENT VALUE | Value to replace |
| ------ | ------ |
| <SEARCH_SERVICE_NAME> | Name of Search Service |
| <SEARCH_SERVICE_ADMIN_KEY> | Admin Key of Search Service |
| <COGNATIVE_SERVICE_KEY> | Key of Cognitive Services |
| <STORAGE_ACCOUNT_NAME> | Name of Storage Account |
| <STORAGE_ACCOUNT_CONTAINER_NAME> | Name of Storage Container |
| <STORAGE_CONTAINER_FOLDER_NAME> | Name of Storage Folder, only if used, otherwise replace with empty space |
| <STORAGE_ACCOUNT_CONNECTION_STRING> | Connection String of Storage Account  |
| <CUSTOM_SKILL_URL_ONE> | Azure Function URL of Text Extraction Skill |
| <CUSTOM_SKILL_URL_TWO> | Azure Function URL of Years of Experience Skill |
| <LOOKUP_TABLE_URL_ONE> | Lookup table URL of Qualifications |
| <LOOKUP_TABLE_URL_TWO> | Lookup table URL of Languages |
| <DATASOURCE_NAME> | Name of Datasource |
| <INDEX_NAME> | Name of Index |
| <SKILLSET_NAME> | Name of Skillset |
| <INDEXER_NAME> | Name of Indexer |

### Step 2: Create the Datasource
In Postman, navigate to Create Datasource and run the request. 

This will create a Datasource in the Search Service from the container that has the sample documents. 

### Step 3: Create the Skillset 
#### Step 3a: Custom Skill
In VS Code, create an HTTP Trigger Azure Function in Python, and replace the code in the "init" file with the code provided in [Assets/Function Script](https://github.com/AhmedAlmu/cv-knowledge-engine-accelerator/tree/main/Assets/Function%20Script). 

This process should be done twice to create two functions, one for Text Extraction and the other for Years of Experience. 

In Text Extraction, make sure to add the values for the Cognitive Services Key and Endpoint in the script, and add "requests" in the requirments file.

To deploy the function, you can follow the instructions provided in here: [Develop Azure Functions by using Visual Studio Code](https://docs.microsoft.com/en-us/azure/azure-functions/functions-develop-vs-code?tabs=python).

After deploying both custom skill functions, we can procceed to create the Skillset. 

#### Step 3b: Built-in Skills
In Postman, navigate to Create Skillset request. 

For the "Custom Entity Lookup" skills, we need to provide the URL for the CSV lookup tables. You can upload the two files in [Assets/Lookup Tables](https://github.com/AhmedAlmu/cv-knowledge-engine-accelerator/tree/main/Assets/Lookup%20Tables) to the Storage Account, and get their SAS URL to be used in the skill definition. After both URLs are provided, run the request.  

This will create a Skillstet in the Search Service that identifies all the information to be extracted from the CVs.

### Step 4: Create the Index
In Postman, navigate to Create Index and run the request. 

This will create an Index in the Search Service for the information to be extracted from the CVs as mentioned earlier.

### Step 5: Create the Indexer
In Postman, navigate to Create Indexer and run the request. 

This will create an Indexer in the Search Service that will exctract the defined information from the CVs.

### Step 6: Create the Web App Interface
In [Assets/Website Template](https://github.com/AhmedAlmu/cv-knowledge-engine-accelerator/tree/main/Assets/Website%20Template), open the solution file "CognitiveSearch.Template.sln" in Visual Studio. 

Navigate to the "appsettings.json" file, and change the values according to the following table:

| Placeholder Value | Value to replace |
| ------ | ------ |
| <SEARCH_SERVICE_NAME> | Name of Cognitive Search Service |
| <SEARCH_SERVICE_KEY> | Admin Key of Cognitive Search Service |
| <INDEX_NAME> | Index Name in Search Service |
| <INDEXER_NAME> | Indexer Name in Search Service |
| <STORAGE_ACCOUNT_NAME> | Storage Account Name that stores the documents |
| <STORAGE_ACCOUNT_KEY> | Storage Account Key |
| <CONTAINER_NAME> | Container Name in Storage Account that stores the documents |

You can test the website locally by running the solution in Visual Studio, or publish the website to Azure by following the instructions found here: [Quickstart: Publish an ASP.NET web app](https://docs.microsoft.com/en-US/visualstudio/deployment/quickstart-deploy-aspnet-web-app?view=vs-2019&tabs=azure).

### Step 7: Create the PowerBI Dashboard
COMING SOON

## References 
This accelerator was inspired by the [Knowledge Mining Solution Accelerator](https://github.com/Azure-Samples/azure-search-knowledge-mining).

## License
For all licensing information refer to [LICENSE](https://github.com/AhmedAlmu/cv-knowledge-engine-accelerator/blob/main/LICENSE).
