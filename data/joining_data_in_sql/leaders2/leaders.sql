CREATE TABLE leaders.presidents (
  country                 VARCHAR   PRIMARY KEY,
  continent               VARCHAR,
  president               VARCHAR
);

CREATE TABLE leaders.prime_ministers (
  country                 VARCHAR   PRIMARY KEY,
  continent               VARCHAR,
  prime_minister          VARCHAR
);

CREATE TABLE leaders.states (
  name                    VARCHAR   PRIMARY KEY,
  continent               VARCHAR,
  indep_year              INTEGER,
  fert_rate               REAL,
  women_parli_perc        REAL
  
);

CREATE TABLE leaders.monarchs (
  country                 VARCHAR   PRIMARY KEY,
  continent               VARCHAR,
  monarch                 VARCHAR
);

-- Copy over data from CSVs
copy leaders.presidents FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/leaders2/presidents.csv' DELIMITER ',' CSV HEADER;
copy leaders.prime_ministers FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/leaders2/prime_ministers.csv' DELIMITER ',' CSV HEADER;
copy leaders.states FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/leaders2/states.csv' DELIMITER ',' CSV HEADER;
copy leaders.monarchs FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/leaders2/monarchs.csv' DELIMITER ',' CSV HEADER;

/*
createdb leaders
psql leaders < data/leaders/leaders.sql
*/