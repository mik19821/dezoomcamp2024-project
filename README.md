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

## Local

*Files:*
1. Dockerfile
2. docker-compose.yml 
3. mage-pipelines
   - project_spff_loader.py
   - project_spff_transform.py
   - project_spff_exporter2pg.py


## GCS and Big Query
1. Data set was convert to .parquet files. After that I've  sent them to GCS and export to Biq Query. 
2. For optimization purposes, I used partitioning by year.



To process data in Mage:
1. Create loader to load data from csv from github
2. Create transform to change format date and upper case
3. Create exporter to parquet file
4. Create exporter to GCS

#### Files:
- project_spff_loader.py
- project_spff_transform.py
- project_spff_partition_parquet_exporter.py
- project_spff_exporter2gcs.py

**!NOTE:** To add gcs credential. [Matt Palmer - How to](https://www.youtube.com/watch?v=w0XmcASRUnc&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=25)
``` 
  GOOGLE_SERVICE_ACC_KEY_FILEPATH: "/home/src/key.json"
  GOOGLE_LOCATION: US # Optional
```


### Next step ... visualization and analysis.

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
