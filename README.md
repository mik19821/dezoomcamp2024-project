<!--multilang v0 en:README.md pl:READMEPL.md -->
<!--multilang buttons-->

language: [English](README.md) also available in:
[Polish](READMEPL.md)

<!--lang:en-->

# DEZoomcamp2024-project

### Description
Spcff.pl is the website of the Polish WWFF diploma program. This is a register of all activities of Polish flora&fauna. Oporeators, I mean Hunters or HAM Amateur send QSO's log from SPFF objects to the register. On the website you can check who, when and how many connections were made. Due to the fact that these are only dry data and Guest should to that manually. I decided to download them automatically and visualize them so that the summaries were concentrated in one place and in a more readable form. The initial data download and export to PostgreSQL was performed on a local environment using Docker and Mage AI. Simple transformation data was made by Mage. The scripts have been included in the repository.


#### Data set structure:
```
- ID of object (SPFF-DDDD)
- date of activation (YYYYMMDD)
- HAM callsign (SQ7M)
- number of QSO - connection to other HAM operators (integer)
```

## To run on local docker:

0. [Manuall for install docker engine on your OS.](https://docs.docker.com/engine/install/)


### 1. Run Mage AI in the container.  

**Step 1.** The following files must be placed in the same directory:
      - [Dockerfile](https://github.com/mik19821/dezoomcamp2024-project/blob/main/Dockerfile) 
      - [docker-compose.yml](https://github.com/mik19821/dezoomcamp2024-project/blob/main/docker-compose.yml)
   
   **Step 2.** After that run command ``` docker compose up -d ```
   
   **Links:** [Awesome tutorial by Matt Palmer is here](https://youtu.be/2SV-av3L3-k?feature=shared).  

### 2. Pipeline
   **Step 3.** Create new pipeline with:
   - [Loader - to load data from csv from github](https://github.com/mik19821/dezoomcamp2024-project/blob/main/mage-local/data_loaders/project_spff_loader.py)
   - [Transform - to change format date, rok (year) and upper case for znak (callsign operator) ](https://github.com/mik19821/dezoomcamp2024-project/blob/main/mage-local/transformers/project_spff_transform.py)
   - [Export - export data to parquet file](https://github.com/mik19821/dezoomcamp2024-project/blob/main/mage-local/data_exporters/project_spff_exporter2pg.py)
   
   **Links:** [Create pipeline by Matt Palmer]([Pipelines](https://youtu.be/stI-gg4QBnI?feature=shared))

   **Step 4.** If the connection to the database is ensured, the launch of the pipeline components should be successful and the data will be found in the database.


## GCS and Big Query

**Step 1.** In the previous instance of Mage create new pipeline.
- use the same code for [loader](https://github.com/mik19821/dezoomcamp2024-project/blob/main/mage-cloud/data_loaders/project_spff_loader.py) because this file is responsible for load data from the csv file
- as above transformer file can be reused without any changes. [Transformer](https://github.com/mik19821/dezoomcamp2024-project/blob/main/mage-local/transformers/project_spff_transform.py) change format date, rok (year) and upper case for znak (callsign operator)
- there is to option to use exporter:
  - [project_spff_wrtie2bq.sql](https://github.com/mik19821/dezoomcamp2024-project/blob/main/mage-cloud/data_exporters/project_spff_wrtie2bq.sql) - export DataFrame to Big Query directly
  Data set is patition by column rok because this is the most optimize ![Partitioning](https://github.com/mik19821/dezoomcamp2024-project/blob/main/img/partitioning.png) 
  - [parquet4gcsandgq.py](https://github.com/mik19821/dezoomcamp2024-project/blob/main/mage-cloud/data_exporters/parquet4gcsandgq.py) - export parquet file to GCS and after that we can create external and static table using transformer  
  [project_spff_stat_from_ext_table.sql](https://github.com/mik19821/dezoomcamp2024-project/blob/main/mage-cloud/transformers/project_spff_stat_from_ext_table.sql). 


[//]: # (#### Files:)

[//]: # (1. mage-cloud/data_loaders/project_spff_loader.py)

[//]: # (2. mage-cloud/transformers/project_spff_transform.py)

[//]: # (3. mage-cloud/data_exporters/parquet4gcsandgq.py)

[//]: # (4. mage-cloud/transformers/project_spff_stat_from_ext_table.sql)

[//]: # (5. mage-cloud/data_exporters/project_spff_wrtie2bq.sql)

**!!! There is possible to create external table from created parquet file. If you want just use a parquet4gcsandgq.py and after that project_spff_stat_from_ext_table.sql.** 

**!IMPORTANT:** To add credentials for [GCS](https://youtu.be/w0XmcASRUnc?feature=shared) and [Big Query](https://youtu.be/JKp_uzM-XsM?feature=shared) - all tutorials from Big Matt Palmer :-) 
``` 
  GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/key.json"
  GOOGLE_LOCATION: US # Optional
```




## First charts made by Data/Look Studio -> [link](https://lookerstudio.google.com/s/iMUVwbUlJrk).
![Charts01](https://github.com/mik19821/dezoomcamp2024-project/blob/main/img/multichart01.png)



[//]: # (#### TODO:)

[//]: # (1. Get dataset)

[//]: # (- [x] script getting data statistics &#40;one csv file for each object&#41;)

[//]: # (- [ ] create parquet file from csv)

[//]: # (2. Import and transformation)

[//]: # (- [X] import file to container with postgresql &#40;v15&#41;)

[//]: # (  - transformation:)

[//]: # (    - [X] activation's date to date format)

[//]: # (    - [X] change callsign to uppercase)

[//]: # (- [ ] copy file to gcs)

[//]: # (- [ ] import file to BigQuery)

[//]: # (  - transformation:)

[//]: # (    - [ ] activation's date to date format)

[//]: # (    - [ ] change callsign to uppercase)

[//]: # (3. create dashboards)
