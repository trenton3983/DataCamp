CREATE TABLE diagrams.left_table (
  id                    INTEGER   PRIMARY KEY,
  val                   CHARACTER(2)
);

CREATE TABLE diagrams.right_table (
  id                    INTEGER   PRIMARY KEY,
  val                   CHARACTER(2)
);

CREATE TABLE diagrams.left_one (
  id                    INTEGER   PRIMARY KEY
);

CREATE TABLE diagrams.right_one (
  id                    INTEGER   PRIMARY KEY
);

CREATE TABLE diagrams.right2 (
  id                    INTEGER,
  val                   CHARACTER(2) PRIMARY KEY
);

CREATE TABLE diagrams.table1 (
  id                    INTEGER   PRIMARY KEY
);

CREATE TABLE diagrams.table2 (
  id                    CHARACTER(1)   PRIMARY KEY
);


-- Copy over data from CSVs
copy diagrams.left_table FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/diagrams/left_table.csv' DELIMITER ',' CSV HEADER;
copy diagrams.right_table FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/diagrams/right_table.csv' DELIMITER ',' CSV HEADER;
copy diagrams.left_one FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/diagrams/left_one.csv' DELIMITER ',' CSV HEADER;
copy diagrams.right_one FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/diagrams/right_one.csv' DELIMITER ',' CSV HEADER;
copy diagrams.right2 FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/diagrams/right2.csv' DELIMITER ',' CSV HEADER;
copy diagrams.table1 FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/diagrams/table1.csv' DELIMITER ',' CSV HEADER;
copy diagrams.table2 FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/diagrams/table2.csv' DELIMITER ',' CSV HEADER;

/*
createdb diagrams
psql diagrams < data/diagrams/diagrams.sql
*/