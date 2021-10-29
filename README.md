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
| TO-DO | TO-DO |

### Step 2: Create the Datasource
In Postman, navigate to Create Datasource and run the request. 

This will create a Datasource in the Search Service from the container that has the sample documents. 

### Step 3: Create the Skillset 
#### Step 3a: Custom Skill

#### Step 3b: Built-in Skills

### Step 4: Create the Index
In Postman, navigate to Create Index and run the request. 

This will create an Index in the Search Service for the information to be extracted from the CVs as mentioned earlier.

### Step 5: Create the Indexer
In Postman, navigate to Create Indexer and run the request. 

This will create a Datasource in your Search Service from the container that has the sample documents.

### Step 6: Create the Web App Interface 

### Step 7: Create the PowerBI Dashboard
COMING SOON

## References 
This accelerator leverages the [Knowledge Mining Solution Accelerator](https://github.com/Azure-Samples/azure-search-knowledge-mining).

## License
Please refer to [LICENSE](https://github.com/AhmedAlmu/cv-knowledge-engine-accelerator/blob/main/LICENSE) for all licensing information.
