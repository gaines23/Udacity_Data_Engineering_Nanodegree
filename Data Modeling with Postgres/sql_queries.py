# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY
        , start_time TIMESTAMP NOT NULL 
        , user_id INT NOT NULL
        , level VARCHAR 
        , song_id VARCHAR 
        , artist_id VARCHAR
        , session_id VARCHAR
        , location VARCHAR 
        , user_agent VARCHAR 
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        userId INT PRIMARY KEY
        , firstName VARCHAR(50)
        , lastName VARCHAR(50)
        , gender VARCHAR(1)
        , level VARCHAR(10)
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY
        , title VARCHAR(50)
        , artist_id VARCHAR
        , year INT
        , duration DECIMAL
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR PRIMARY KEY
        , name VARCHAR(150)
        , location VARCHAR(100)
        , latitude FLOAT(5)
        , longitude FLOAT(5)
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY
        , hour INT
        , day INT
        , week INT
        , month INT
        , year INT
        , weekday INT
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users(userId, firstName, lastName, gender, level)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (userId)
    DO UPDATE
    SET level = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT(song_id)
    DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT(artist_id)
    DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time(start_time, hour, day, week, month, year, weekday)
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT(start_time)
    DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT
        s.song_id
        , a.artist_id
    FROM
        songs AS s JOIN artists AS a ON a.artist_id = s.artist_id
    WHERE
        s.title = %s AND
        a.name = %s AND
        s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]