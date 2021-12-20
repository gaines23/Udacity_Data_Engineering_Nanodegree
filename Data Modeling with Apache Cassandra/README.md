# Data Modeling with Apache Cassandra

## Introduction

Through the use of Apache Cassandra, we will create queries on song play data that can help answer the tough questions Sparkify has regarding their song and user activity. These queries help them understand what songs their users are listening to. 

## Dataset Provided

The dataset provided is a collection of CSV files that contain information of song and user activity throughout a certain period of time.

The CSV files list the following information:
artist, firstName, gender, itemInSession, lastName, length, level, sessionId, song, userId

## Data Tables
The tables below were created to to render specific queries for each question that was posed. 

## **music_library**
| COLUMN | TYPE |
| ------ | ---- |
| sessionId | int |
| itemInSession | int |
| artist | text |
| song_title | text  |
| song_length |	decimal	|

Question: Give me the artist, song title, and song's length in the music app that was heard
during sessionId = 338, and itemInSession = 4

## **users**
| COLUMN | TYPE |
| ------ | ---- |
| userid | int |
| sessionId | int |
| itemInSession | int |
| artist | text |
| song_title | text |
| user_fn | text |
| user_ln | text |

Question: Give me only the following: name of artist, song (sorted by itemSessionId)
and user first and last name for userid = 10, sessionId = 182

## Dimension Table: **user_song**
| COLUMN | TYPE |
| ------ | ---- |
| song_tittle | text |
| user_id | int |
| user_fn | text |
| user_ln | text |

Question: Give me every user name (first and last) in my music app history who 
listened to the song 'All Hands Against His Own'
