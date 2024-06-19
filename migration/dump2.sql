CREATE TABLE levels (
    id SERIAL PRIMARY KEY,
    level_name VARCHAR NOT NULL,
    description VARCHAR,
    max_speed FLOAT
);

INSERT INTO levels (level_name, description, max_speed) VALUES ('Beginner', 'Beginner level', 30.0);
INSERT INTO levels (level_name, description, max_speed) VALUES ('Intermediate', 'Intermediate level', 60.0);
INSERT INTO levels (level_name, description, max_speed) VALUES ('Advanced', 'Advanced level', 90.0);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    lastname VARCHAR NOT NULL,
    firstname VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    password VARCHAR NOT NULL,
    level_id BIGINT,
    FOREIGN KEY (level_id) REFERENCES levels (id)
);

CREATE TABLE race (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    user_id BIGINT,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE lap (
    id SERIAL PRIMARY KEY,
    race_id BIGINT,
    time TIME,
    FOREIGN KEY (race_id) REFERENCES race (id)
);

CREATE TABLE metrics (
    id SERIAL PRIMARY KEY,
    race_id BIGINT,
    FOREIGN KEY (race_id) REFERENCES race (id)
);

CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    distance FLOAT NOT NULL,
    light FLOAT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

