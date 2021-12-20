# Data Modeling with Postgres

## Introduction

Through the use of Postgres, we were able to better analyze the complex user and song data provided by Sparkify. Postgres allowed us to build a database and query information that better explains Sparkify's user base.

## Project Goals:
    1. Define fact and dimension tables for a start schema
    2. Setup a database with Postgres SQL using Python and SQL
    3. Build an ETL pipeline in Python
    4. Review and analyze the data

## Dataset Provided

The song dataset is a subset of real time data from the [Million Song Dataset](http://millionsongdataset.com/). Each file is provided in JSON format and contains metadata about each song and artist. 

The log dataset is provided in JSON format from that describes user activity on the app. 

## Data Models

## Fact Table: **songplays**
| COLUMN | TYPE | CONSTAINT |
| ------ | ---- | --------- |
| songplay_id | SERIAL | PRIMARY KEY |
| start_time | TIMESTAMP | NOT NULL |
| user_id | VARCHAR | NOT NULL |
| level | VARCHAR	|
| song_id |	VARCHAR	|
| artist_id | VARCHAR	|
| session_id | VARCHAR	|
| location | VARCHAR	|
| user_agent | VARCHAR	|


songplay_id is an auto-increment Primary Key. 
Query to insert data:
```
INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
```

## Dimension Table: **users**
| COLUMN | TYPE | CONSTAINT |
| ------ | ---- | --------- |
| user_id | VARCHAR | PRIMARY KEY|
| firstname | VARCHAR(50) |
| lastname | VARCHAR(50) |
| gender | VARCHAR(1) |
| level | VARCHAR(10) |

Query to insert data:
```
INSERT INTO users(userId, firstName, lastName, gender, level)
VALUES(%s, %s, %s, %s, %s)
```

## Dimension Table: **songs**
| COLUMN | TYPE | CONSTAINT |
| ------ | ---- | --------- |
| song_id | VARCHAR | PRIMARY KEY |
| title | VARCHAR(50) |
| artist | VARCHAR |
| year | INT |
| duration | DECIMAL |	

Query to insert data:
```
INSERT INTO songs(song_id, title, artist_id, year, duration)
VALUES(%s, %s, %s, %s, %s)
```

## Dimension Table: **artists**
| COLUMN | TYPE | CONSTAINT |
| ------ | ---- | --------- |
| artist_id | VARCHAR | PRIMARY KEY |
| name | VARCHAR(150) |
| location | VARCHAR(100) |
| latitude | FLOAT(5) |
| longitude | FLOAT(5) |

Query to insert data:
```
INSERT INTO artists(artist_id, name, location, latitude, longitude)
VALUES(%s, %s, %s, %s, %s)
```

## Dimension Table: **time**
| COLUMN | TYPE | CONSTAINT |
| ------ | ---- | --------- |
| start_time | TIMESTAMP | PRIMARY KEY |
| hour| INT	|
| day | INT	|
| week | INT |
| year | INT |
| weekday | INT |	

Query to insert data:
```
INSERT INTO time(start_time, hour, day, week, month, year, weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s)
```

## ETL Pipeline
The ETL pipeline is generate through the **etl.py** file. This file reads the song and log data files in JSON and inserts each row of data into its specified column based on the SQL INSERT queries provided above. The **etl.py** file reads the SQL information from the **sql_queries.py** file. 
