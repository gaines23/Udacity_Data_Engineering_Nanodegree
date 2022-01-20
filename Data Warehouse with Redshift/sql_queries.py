import configparser

# CONFIG
config = configparser.ConfigParser()
config.read_file(open('dwh.cfg'))

# GLOBAL VARIABLES
DWH_ROLE_ARN = config.get("IAM_ROLE", "ARN")
LOG_DATA = config.get("S3", "LOG_DATA")
LOG_JSONPATH = config.get("S3", "LOG_JSONPATH")
SONG_DATA = config.get("S3", "SONG_DATA")

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE IF NOT EXISTS staging_events (
    event_id BIGINT IDENTITY(0,1)
    , artist VARCHAR
    , auth VARCHAR
    , firstName VARCHAR
    , gender VARCHAR
    , itemInSession VARCHAR
    , lastName VARCHAR
    , length VARCHAR
    , level VARCHAR
    , location VARCHAR
    , method VARCHAR
    , page VARCHAR
    , registration VARCHAR
    , sessionId INT SORTKEY DISTKEY
    , song VARCHAR
    , status INt
    , ts BIGINT
    , userAgent VARCHAR
    , userId INT
)

""")

staging_songs_table_create = ("""
CREATE TABLE IF NOT EXISTS staging_songs (
    song_id VARCHAR
    , num_songs INTEGER
    , title VARCHAR
    , artist_name VARCHAR
    , artist_latitude FLOAT
    , year INTEGER
    , duration FLOAT
    , artist_id VARCHAR
    , artist_longitude FLOAT
    , artist_location VARCHAR
)

""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id INT IDENTITY(0,1) PRIMARY KEY
    , start_time TIMESTAMP SORTKEY DISTKEY
    , user_id INT
    , level VARCHAR(10)
    , song_id VARCHAR(50)
    , artist_id VARCHAR(40)
    , session_id VARCHAR(50)
    , location VARCHAR(100)
    , user_agent VARCHAR(255)
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY SORTKEY
    , first_name VARCHAR(50)
    , last_name VARCHAR(50)
    , gender VARCHAR(10)
    , level VARCHAR(10)
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR(50) PRIMARY KEY SORTKEY
    , title VARCHAR(200)
    , artist_id VARCHAR(50)
    , year INT NOT NULL
    , duration DECIMAL(9)
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR(50) PRIMARY KEY SORTKEY
    , name VARCHAR(200)
    , location VARCHAR(200)
    , latitude DECIMAL(9)
    , longitude DECIMAL(9)
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY
    , hour SMALLINT
    , day SMALLINT
    , week SMALLINT
    , month SMALLINT
    , year SMALLINT
    , weekday SMALLINT
) diststyle all;
""")





# STAGING TABLES

staging_events_copy = ("""
    COPY staging_events FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    TIMEFORMAT as 'epochmillisecs'
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL
    FORMAT AS JSON {};
""").format(LOG_DATA, DWH_ROLE_ARN, LOG_JSONPATH)

staging_songs_copy = ("""
    COPY staging_songs FROM {}
    CREDENTIALS 'aws_iam_role={}'
    COMPUPDATE OFF region 'us-west-2'
    FORMAT AS JSON 'auto' 
    TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL;
""").format(SONG_DATA, DWH_ROLE_ARN)





# FINAL TABLES

songplay_table_insert = ("""
    INSERT INTO songplays (
        start_time
        , user_id
        , level
        , song_id
        , artist_id
        , session_id
        , location
        , user_agent
    )
    SELECT DISTINCT 
        to_timestamp(to_char(se.ts, '9999-99-99 99:99:99'),'YYYY-MM-DD HH24:MI:SS') AS start_time
        , se.userId AS user_id
        , se.level
        , ss.song_id
        , ss.artist_id
        , se.sessionId AS session_id
        , se.location AS location
        , se.userAgent AS user_agent
    FROM staging_songs AS ss
    JOIN staging_events AS se ON se.song = ss.title AND se.artist = ss.artist_name
    WHERE se.page = 'NextSong'
""")

user_table_insert = ("""
    INSERT INTO users (
        user_id
        , first_name
        , last_name
        , gender
        , level
    )
    SELECT DISTINCT
        userId AS user_id
        , firstName AS first_name
        , lastname AS last_name
        , gender
        , level
    FROM staging_events
    WHERE userId IS NOT NULL
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id
        , title
        , artist_id
        , year
        , duration
    )
    SELECT DISTINCT 
        song_id
        , title
        , artist_id
        , year
        , duration
    FROM staging_songs
""")

artist_table_insert = ("""
    INSERT INTO artists (
        artist_id
        , name
        , location
        , latitude
        , longitude
    )
    SELECT DISTINCT
        artist_id
        , artist_name AS name
        , artist_location AS location
        , artist_latitude AS latitude
        , artist_longitude AS longitude
    FROM staging_songs
""")

time_table_insert = ("""
    INSERT INTO time (
        start_time
        , hour
        , day
        , week
        , month
        , year
        , weekday
    )
    SELECT DISTINCT
        start_time
        , EXTRACT(hour FROM start_time)
        , EXTRACT(day FROM start_time)
        , EXTRACT(week FROM start_time)
        , EXTRACT(month FROM start_time)
        , EXTRACT(year FROM start_time)
        , EXTRACT(weekday FROM start_time)
    FROM songplays
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
