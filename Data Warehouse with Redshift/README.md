# Data Warehouse with AWS Redshift

## Introduction
As the music streaming startup, Sparkify rapidly grows their user base and song database, they want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on their songs app. 


## Project Goals:
    1. Build an ETL pipeline that extracts their data from S3
    2. Stage the data in Redshift
    3. Transform the data into a set of dimensional tables
    4. Review and analyze the data


## Data Structure
Cloud Data Warehouse
|____create_tables.py    # database/table creation script 
|____etl.py              # ELT builder
|____sql_queries.py      # SQL query collections
|____dwh.cfg             # AWS configuration file
|____test.ipynb          # testing


## ETL Pipeline Procedure
    1. Configure the **dwh.cfg** file to add the redshift database and IAM role information
    2. Create table schemas using SQL CREATE statements in the **sql_queries.py** file 
    3. Run **create_tables.py** file to connect to the data base and create these tables
    4. Implement the logic in **etl.py** to load data from S3 to the staging tables on Redshift, then from staging tables to the analytics tables

