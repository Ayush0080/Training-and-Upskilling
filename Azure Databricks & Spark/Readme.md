## Databricks
- Databricks
  - Databricks is a cloud-based data and AI platform built on Apache Spark that provides tools for data processing, analytics, and machine learning.
  - Databricks = platform that makes Spark easy to use
---

- Apache Spark
  - Apache Spark is an open-source distributed data processing engine used to process large-scale data quickly across multiple machines.
  - Spark = engine that processes big data in parallel

---
- Databricks handles data processing, while Azure ML handles model training, deployment, and monitoring in the MLOps lifecycle.

    | Stage               | Databricks | Azure ML |
    | ------------------- | ---------- | -------- |
    | Data ingestion      | ✅          | ❌        |
    | Data processing     | ✅          | ⚠️       |
    | Feature engineering | ✅          | ⚠️       |
    | Training            | ⚠️         | ✅        |
    | Experiment tracking | ✅          | ✅        |
    | Model registry      | ❌          | ✅        |
    | Deployment          | ❌          | ✅        |
    | Monitoring          | ❌          | ✅        |

---



### Databricks Cluster Configuration

Databricks clusters are used to run Apache Spark jobs. Proper configuration helps in performance, cost optimization, and security.

#### 1. Single Node / Multi Node
- Single Node: One machine, used for small workloads or testing  
- Multi Node: Multiple machines, used for large-scale data processing  

#### 2. Access Mode
- Single User: One user, more secure  
- Shared: Multiple users  
- No Isolation: Less secure  

#### 3. Databricks Runtime
- Pre-configured environment with Apache Spark, libraries, and ML tools  
- Example: Databricks Runtime 13.x (Spark 3.x)  
- Think of it as: Environment + Spark + Libraries  

#### 4. Auto Termination
- Automatically stops the cluster after inactivity  
- Example: Auto terminate after 30 minutes  
- Helps in cost saving  

#### 5. Auto Scaling
- Automatically adjusts number of nodes  
- Example: Min nodes: 2, Max nodes: 10  
- Scales up for high load and down for low load  

#### 6. Cluster VM Type / Size
- Defines compute power (CPU, Memory, GPU)  
- Example: Standard_DS3_v2  

#### 7. Cluster Policy
- Defines rules for cluster creation  
- Used for cost control, security, and governance  
- Example:
  {
    "autotermination_minutes": {"type": "fixed", "value": 60},
    "num_workers": {"type": "range", "minValue": 2, "maxValue": 10}
  }

#### 8. Cluster Pool
- A cluster pool is a set of pre-provisioned compute resources that reduce cluster startup time and optimize cost in Databricks.

##### Without Pool
- Create cluster → wait 3–5 minutes  
  - Reason:
    - VMs are created from scratch  

###### With Pool
- Cluster uses pre-created VMs → starts in seconds  



------


- file system command  (%fs)
![alt text](image.png)

- shell command (%sh)
![alt text](image-1.png)

- install python libraries (%pip)
  ![alt text](image-2.png)

- import another notebook into the cureerrnt notebook (%run)
  ![alt text](image-3.png)



--- 

####  Creating Azure Data Lake Storage Gen2
![alt text](image-4.png)

- also created 4 containers (raw, processed, presentation, demo)
![alt text](image-5.png)

- upload demo csv(circuits.csv) file in demo container 
  ![alt text](image-6.png)


---
#### access azure datalake using service principal
(- ref (section/6/setup3.access_adls_using_service_principal))

- Register Azure AD Application / Service Principal
  ![alt text](image-7.png)
- Generate a secret/ password for the Application
  ![alt text](image-8.png)
  ![alt text](image-9.png)
- Set Spark Config with App/ Client Id, Directory/ Tenant Id & Secret (add storage account name)
  ![alt text](image-10.png)
- Assign Role 'Storage Blob Data Contributor' to the Data Lake. 
![alt text](image-12.png)
![alt text](image-11.png)
![alt text](image-13.png)
![alt text](image-15.png)



#### Access Azure Data Lake using ADD  Credential Passthrough 

- Set the spark config fs.azure.account.key in the cluster
- assign  Access Control (IAM) of blob storage to the user
- List files from demo container
- Read data from circuits.csv file
- Credential passthrough is deprecated starting with Databricks Runtime 15.0 and will be removed for future Databricks Runtime versions. 

---
#### Securing Access to Azure Data Lake using Azure key-vault backed Secret Scope


- Creating Azure Key Vault
  ![alt text](image-16.png)
  ![alt text](image-17.png)

- add Storage account Access keys as Secrets in key vault  
  ![alt text](image-18.png)
  ![alt text](image-19.png)


- Creating Secret Scope add (#secrets/createScope) after ws link  
  ![alt text](image-20.png)
  ![alt text](image-21.png)
  ![alt text](image-22.png)
  ![alt text](image-23.png)


----

### Unity Catalog in Databricks

Unity Catalog is a centralized data governance solution in Databricks used to manage data access, security, and metadata across all data assets.

---

 Unity Catalog provides a unified way to control and manage access to data stored in external storage like ADLS, S3, or Blob.

---


### 1. Catalog
Top-level container for organizing data.

Example:
catalog_name

---

### 2. Schema (Database)
Logical grouping of tables inside a catalog.

Example:
catalog.schema

---

### 3. Table
Actual data stored in structured format.

Example:
catalog.schema.table

---

###  Works

Data is stored in external storage (ADLS / S3), and Unity Catalog controls access to it.

Flow:

Notebook → Unity Catalog → Data Lake (ADLS)

---

You can access data using:

```python
df = spark.read.table("catalog.schema.table")
```
---

## Data ingestion

![alt text](image-25.png)
![alt text](image-26.png)


### Circuits File - Dataframe Reader  [ref](Formula1-Project-Solutions/Section-11-12-13))

- Step 1 - Read the CSV file using the spark dataframe reader
![alt text](image-27.png)

- Step 2 - Select only the required columns
  ![alt text](image-28.png)

-  Step 3 - Rename the columns as required  and Add ingestion date to the dataframe
  ![alt text](image-29.png)

- Step 5 - Write data to datalake as parquet
   ![alt text](image-30.png)  


#### for Ingest races.csv file

- Step 1 - Read the CSV file using the spark dataframe reader API
![alt text](image-31.png)

- Step 2 - Add ingestion date and race_timestamp to the dataframe
 ![alt text](image-34.png)

- Step 3 - Select only the columns required & rename as required
 ![alt text](image-35.png)

-  Step 4 - Write the output to processed container in parquet format
![alt text](image-36.png)
![alt text](image-37.png)
 

#### for Ingest constructors.json file
![alt text](image-38.png)
![alt text](image-39.png)

#### for Ingest drivers.json file
![alt text](image-40.png)
![alt text](image-41.png)
![alt text](image-42.png)

#### for Ingest results.json file
![alt text](image-43.png)
![alt text](image-44.png)
![alt text](image-45.png)

#### for Ingest pit_stops.json file
![alt text](image-46.png)
![alt text](image-47.png)


## Data ingestion - Multiple files 

#### Ingest lap_times folder
![alt text](image-48.png)
![alt text](image-49.png)

#### Ingest qualifying folder 

![alt text](image-50.png)
![alt text](image-51.png)



- `lit` : for text variable order to add a column to a dataframe, you need to convert that to a column type
and then you add that.So lit basically gives you the ability to convert a text into a column type, and then you can add that to a dataframe.



### Join Race Results  and put into the presentation container [REF](Formula1-Project-Solutions/Section-16)
![alt text](image-52.png)

- first we created  not book that hold path of the data (../includes/configuration) using that we call data into the another notebook

![alt text](image-53.png)
![alt text](image-54.png)
![alt text](image-55.png)
![alt text](image-56.png)




### using Aggregate functions [REF](Formula1-Project-Solutions/Section-16)

| Function  | Meaning        |
| --------- | -------------- |
| `sum()`   | Total          |
| `avg()`   | Average        |
| `count()` | Number of rows |
| `max()`   | Highest value  |
| `min()`   | Lowest value   |

```bash
groupBy() + agg()
```
- Driver Standings
![alt text](image-57.png)
![alt text](image-58.png)
![alt text](image-59.png)

-  Constructor Standings
![alt text](image-60.png)
![alt text](image-61.png)


### Temporary Views in Spark (Local vs Global)

- Temporary Views in Spark allow you to run SQL queries on DataFrames.

- There are two types:
   - Local Temporary View
   - Global Temporary View

---

##### Local Temporary View
- A Local Temp View is a temporary table accessible only within the current Spark session (notebook).
```bash
##Create

df.createOrReplaceTempView("drivers")

###  Query

spark.sql("SELECT * FROM drivers")


* Scope → Current session only
* Visibility → Single notebook
* Lifetime → Ends when session stops
* Prefix → Not required
```
---

#####  Global Temporary View
- A Global Temp View is a temporary table accessible across multiple notebooks within the same Spark application.
```bash
### Create

df.createOrReplaceGlobalTempView("drivers")

###  Query

spark.sql("SELECT * FROM global_temp.drivers")


* Scope → Across notebooks (same cluster)
* Visibility → Multiple notebooks
* Lifetime → Until application/cluster stops
* Prefix → Must use `global_temp`
```
---

### Key Differences

| Feature    | Local Temp View | Global Temp View         |
| ---------- | --------------- | ------------------------ |
| Scope      | Current session | Across sessions          |
| Visibility | One notebook    | Multiple notebooks       |
| Prefix     | Not required    | Required (`global_temp`) |
| Lifetime   | Session ends    | Cluster/application ends |

---

### Hive Metastore

- Hive Metastore is a **central metadata repository** that stores information about tables in Spark or Hive.

- It does NOT store actual data  
- It stores **data about data (metadata)**

---
```bash
## What it Stores

- Database names  
- Table names  
- Column names & data types  
- Table location (ADLS / S3 path)  
- Partition details  

---

## What it DOES NOT Store

- Actual data files   
(Data is stored in ADLS / S3 / HDFS)

---
```



| Feature       | Managed Table        | External Table         |
| ------------- | -------------------- | ---------------------- |
| Data location | Default location     | Custom path (ADLS/S3)  |
| Data control  | Spark manages        | User manages           |
| Drop table    | Deletes data         | Keeps data             |
| Use case      | Temporary / internal | Production / data lake |

---

## Data Loading Design Patterns

| Type        | Data Processed | Frequency | Complexity | Use Case     |
| ----------- | -------------- | --------- | ---------- | ------------ |
| Full Load   | All data       | Scheduled | Low        | Small data   |
| Incremental | New data only  | Scheduled | Medium     | Large data   |
| Streaming   | Continuous     | Real-time | High       | Live systems |
| Batch       | Chunk-based    | Scheduled | Low        | General ETL  |







## Delta Lake

- `ACID` transactions are a set of database properties—Atomicity, Consistency, Isolation, and Durability—that guarantee reliable processing of data operations. 

  - Atomicity: Transactions are "all-or-nothing." If one part of a transaction fails, the entire transaction fails, and the database remains unchanged.

   - Consistency: A transaction brings the database from one valid state to another, maintaining all predefined rules, constraints, and triggers.

   - Isolation: Concurrent transactions do not interfere with each other. The result of running multiple transactions simultaneously is the same as if they were run sequentially.

    - Durability: Once a transaction is committed, it remains committed, even in the case of a system failure or power loss



### Data Lake

- A Data Lake stores **raw data in its original format** (CSV, JSON, Parquet, etc.).

---

- No structure required  
- Stores everything (structured + unstructured)  
- Cheap storage  

---
Examples
- ADLS (Azure Data Lake Storage)  
- S3  

---
Characteristics
- Raw data  
- Schema-on-read  
- Used by data engineers  

---

###  Data Warehouse

- A Data Warehouse stores **processed, structured data** for analytics and reporting.

---

- Clean, organized data  
- Optimized for SQL queries  
- Used by analysts  

---

Examples
- Snowflake  
- Azure Synapse  
- BigQuery  

---
Characteristics
- Structured data only  
- Schema-on-write  
- Fast query performance  

---

### Lakehouse (Modern Approach)

- Lakehouse combines **Data Lake + Data Warehouse** features.

---
- Stores data in data lake  
- Provides warehouse capabilities  
- Uses Delta Lake  

---
Example
- Databricks Lakehouse  

---
Characteristics
- ACID transactions  
- Schema enforcement  
- Supports SQL + DataFrame  
- Works on data lake storage  

---

| Format  | Type     | Speed     | Use Case   |
| ------- | -------- | --------- | ---------- |
| CSV     | Row      | Slow      | Raw data   |
| JSON    | Semi     | Medium    | APIs       |
| Parquet | Column   | Fast      | Analytics  |
| ORC     | Column   | Fast      | Hive       |
| Delta   | Advanced | Very Fast | Production |

| Layer              | Format          |
| ------------------ | --------------- |
| Raw (Bronze)       | CSV / JSON      |
| Processed (Silver) | Parquet / Delta |
| Final (Gold)       | Delta           |


###  Architecture Comparison

```text
Data Lake:
Raw Data → Storage

Data Warehouse:
Raw → ETL → Structured Tables → BI

Lakehouse:
Raw → Delta (Bronze/Silver/Gold) → BI    
```
![alt text](image-63.png)
![alt text](image-64.png)
![alt text](image-65.png)


- `Delta Lake` is a storage layer built on top of Parquet that not only formats the data but also adds features like ACID transactions, schema enforcement, and time travel.

  ```bash
  Parquet is a **columnar file format** used to store data efficiently.
    Stores data column-wise (not row-wise)  
    Optimized for fast reads  
    Used for analytics

  ```

- Delta Lake is a storage layer built on top of Parquet that adds advanced features.
  ```bash
    

  Internally stores data as Parquet
  Adds a transaction log (_delta_log)
  Makes data reliable and manageable
  ```
```bash
Write data to delta lake (managed table)
Write data to delta lake (external table)
Read data from delta lake (Table)
Read data from delta lake (File)

```

![alt text](image-66.png)
![alt text](image-67.png)
![alt text](image-68.png)

---
- History & Versioning

![alt text](image-70.png)
![alt text](image-71.png)

- Time Travel
![alt text](image-72.png)

- Vaccum
  -  VACUUM in Delta Lake is used to remove old and unused data files that are no longer needed for time travel, helping to optimize storage. By default, it retains data for 7 days to ensure safe recovery.

  ![alt text](image-73.png) 

- if deleted record than we can able to go to the previous version 
![alt text](image-74.png)



## Azure Data Factory
- Azure Data Factory is a cloud-based data integration and orchestration service used to create, schedule, and manage data pipelines for moving and transforming data across different systems.

![alt text](image-69.png)



##### Ingest circuits csv file usign ADF and trigger databricks notebook

- creted pipeline 

![alt text](image-75.png)

- add databricks notebook
![alt text](image-76.png)

- created Databricks linked service and atteched 

![alt text](image-78.png)
![alt text](image-79.png)
- automatically created Managed identity noq give role addignment to the this Managed identity into the databricks to aalow ADF to run notebook into the databricks
![alt text](image-77.png)
![alt text](image-80.png)
![alt text](image-81.png)


- added notebook path 

  ![alt text](image-82.png)


- addigned variables values first created variable and parameters outside
![alt text](image-83.png)
![alt text](image-84.png)
![alt text](image-85.png)
![alt text](image-86.png)
![alt text](image-87.png)



- added conditon to check data exist in conatiner than notbook is running

    ![alt text](image-88.png)
![alt text](image-90.png)
![alt text](image-89.png)
![alt text](image-91.png)
![alt text](image-92.png)
![alt text](image-93.png)



## Unity Catalog

![alt text](image-94.png)

- Created Azure Databricks Workspace
  ![alt text](image-95.png)

- Create Azure Data Lake Gen2 
  ![alt text](image-96.png)

- Create Access Connector
  ![alt text](image-97.png)

- Add role Storage Blob Data Contributor
  ![alt text](image-100.png)
  ![alt text](image-98.png)
  ![alt text](image-99.png)


- Create Unit Catalog Metastore [link](accounts.azuredatabricks.net)
![alt text](image-101.png)  
![alt text](image-104.png)
![alt text](image-105.png)
![alt text](image-106.png)



### Accessing External Data Lake 
![alt text](image-107.png)

- Create Azure Data Lake Gen2 
  ![alt text](image-96.png)

- Create Access Connector
  ![alt text](image-97.png)

- Add role Storage Blob Data Contributor
  ![alt text](image-100.png)
  ![alt text](image-98.png)
  ![alt text](image-99.png)


- Create Storage Credential
![alt text](image-109.png)
- Create External Location
  ![alt text](image-110.png)


![alt text](image-108.png)