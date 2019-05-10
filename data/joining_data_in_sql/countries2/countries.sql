sCREATE TABLE countries.cities (
  name                    VARCHAR   PRIMARY KEY,
  country_code            VARCHAR,
  city_proper_pop         REAL,
  metroarea_pop           REAL,
  urbanarea_pop           REAL
);

CREATE TABLE countries.countries (
  code                  VARCHAR     PRIMARY KEY,
  name                  VARCHAR,
  continent             VARCHAR,
  region                VARCHAR,
  surface_area          REAL,
  indep_year            INTEGER,
  local_name            VARCHAR,
  gov_form              VARCHAR,
  capital               VARCHAR,
  cap_long              REAL,
  cap_lat               REAL
);

CREATE TABLE countries.languages (
  lang_id               INTEGER     PRIMARY KEY,
  code                  VARCHAR,
  name                  VARCHAR,
  percent               REAL,
  official              BOOLEAN
);

CREATE TABLE countries.economies (
  econ_id               INTEGER     PRIMARY KEY,
  code                  VARCHAR,
  year                  INTEGER,
  income_group          VARCHAR,
  gdp_percapita         REAL,
  gross_savings         REAL,
  inflation_rate        REAL,
  total_investment      REAL,
  unemployment_rate     REAL,
  exports               REAL,
  imports               REAL
);

CREATE TABLE countries.currencies (
  curr_id               INTEGER     PRIMARY KEY,
  code                  VARCHAR,
  basic_unit            VARCHAR,
  curr_code             VARCHAR,
  frac_unit             VARCHAR,
  frac_perbasic         REAL
);

CREATE TABLE countries.populations (
  pop_id                INTEGER     PRIMARY KEY,
  country_code          VARCHAR,
  year                  INTEGER,
  fertility_rate        REAL,
  life_expectancy       REAL,
  size                  REAL
);


CREATE TABLE countries.countries_plus (
  name                  VARCHAR,
  continent             VARCHAR,
  code                  VARCHAR     PRIMARY KEY,
  surface_area          REAL,
  geosize_group         VARCHAR
);

CREATE TABLE countries.economies2010 (
  code                  VARCHAR     PRIMARY KEY,
  year                  INTEGER,
  income_group          VARCHAR,
  gross_savings         REAL
);

CREATE TABLE countries.economies2015 (
  code                  VARCHAR     PRIMARY KEY,
  year                  INTEGER,
  income_group          VARCHAR,
  gross_savings         REAL
);

-- Copy over data from CSVs
copy countries.cities FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/countries2/cities.csv' DELIMITER ',' CSV HEADER;
copy countries.countries FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/countries2/countries.csv' DELIMITER ',' CSV HEADER;
copy countries.languages FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/countries2/languages.csv' DELIMITER ',' CSV HEADER;
copy countries.economies FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/countries2/economies.csv' DELIMITER ',' CSV HEADER;
copy countries.economies2010 FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/countries2/economies2010.csv' DELIMITER ',' CSV HEADER;
copy countries.economies2015 FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/countries2/economies2015.csv' DELIMITER ',' CSV HEADER;
copy countries.currencies FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/countries2/currencies.csv' DELIMITER ',' CSV HEADER;
copy countries.populations FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/countries2/populations.csv' DELIMITER ',' CSV HEADER;
copy countries.countries_plus FROM 'D:/PythonProjects/DataCamp/data/joining_data_in_sql/countries2/countries_plus.csv' DELIMITER ',' CSV HEADER;

/*
createdb countries
psql countries < data/countries/code/countries.sql
*/