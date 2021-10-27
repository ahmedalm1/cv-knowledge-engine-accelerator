# CV Knowledge Engine Solution Accelerator

## About this accelerator
The CV Knowledge Engine solution accelerator aims to provides a quick way of creating an intelligent search engine, that enables searching and filtering through CV and resume documents. It leverages Knowledge Mining and Cognitive Services technologies, to extract all the valuable information and insights from the CV documents, like names, contact information, years of experience, skills and qualifications, ..etc. It also creates an intuitive, easy-to-navigate user interface, that allows for a full search experience with capabilities like searching with search terms, customized filters, and informative result cards. Moreover, the extracted information can also be exported to Power BI and used to create informative dashboards, to give a high level overview of the information extracted. 

### Business Use Case 
The process of screening and searching through CV documents submitted by job seekers is a long and costly process, where the recruiters teams usually have to go through each submitted CV manually, to find the best candidates suited for the job opening. This accelerator will help extract all the essential information from CVs and resumes and simplify the process of searching and filtering through applicants, which will significantly reduce costs and time to isights. 

### Resources and Architecture 
- Storage Account 
- Cognitive Search 
- Cognitive Services
- Azure Function 
- App Service
![Architecture](https://user-images.githubusercontent.com/88718044/139073235-eb6b8b2c-3577-405e-b974-82bc951676dc.png)

### Sample Documents 
The sample documents used in this accelerator to create the demo were 223 dummy CV documents, acquired from [Resume Krafts Website](https://resumekraft.com/resume-examples/).

### Extracted Information 
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
- Past organization 
- Skills 
#### Other Insights
- Key phrases

### Web App Interface
#### Home Page
![Home Page](https://user-images.githubusercontent.com/88718044/139071306-6595000e-a33c-4dca-85eb-ed6c475d66cf.jpeg)

#### Search Results
![Search Results](https://user-images.githubusercontent.com/88718044/139071348-131db6aa-f11b-4857-88b4-cbe61bae5fb6.jpeg)

### PowerBI Dashboard
COMING SOON

## Deployemnt Process

### Prerequisites
- Azure Subscription 
- Visual Studio 2019 or later
- Postman
- Sample CV documents

### Step 1: Deploy the resources

### Step 2: Create the Datasource

### Step 3: Create the Index

### Step 4: Create the Skillset 
#### Step 4a: Custom Skill

#### Step 4b: Built-in Skills

### Step 5: Create the Indexer

### Step 6: Create the Web App Interface 

### Step 7: Create the PowerBI Dashboard
COMING SOON

## References 
This accelerator leverages the [Knowledge Mining Solution Accelerator](https://github.com/Azure-Samples/azure-search-knowledge-mining).

## License
Please refer to [LICENSE](https://github.com/AhmedAlmu/cv-knowledge-engine-accelerator/blob/main/LICENSE) for all licensing information.
