# NYC Taxi ELT Pipeline with BigQuery and dbt

## Overview

This project builds an end-to-end ELT pipeline using Python, Google BigQuery, and dbt.

The pipeline extracts NYC Taxi trip data from a CSV file, loads the raw data into BigQuery, and uses dbt to transform the data into analytics-ready tables.

## Architecture

CSV Dataset
↓
Python Extract & Load
↓
BigQuery Raw Layer
↓
dbt Transformations
↓
Analytics Tables


## Tech Stack

- Python
- Pandas
- Google BigQuery
- dbt Core
- SQL
- Git/GitHub


## Pipeline Steps

### 1. Extract

Python reads the NYC Taxi CSV dataset.

### 2. Load

The raw dataset is loaded into BigQuery:


### 3. Transform

dbt creates analytics models:


Staging layer:
- cleans column names
- prepares data types
- creates a reliable base table

## Project Structure


```text
etl-bigquery-dbt-project/
│
├── scripts/
│   ├── explore_data.py
│   └── load_bigquery.py
│
├── taxi_trip/
│   ├── models/
│   │   ├── staging/
│   │   │   ├── sources.yml
│   │   │   ├── schema.yml
│   │   │   └── stg_taxi_trips.sql
│   │   │
│   │   └── marts/
│   │       ├── trip_summary.sql
│   │       └── daily_revenue.sql
│   │
│   ├── tests/
│   ├── macros/
│   ├── seeds/
│   ├── snapshots/
│   ├── analyses/
│   └── dbt_project.yml
│
├── requirements.txt
└── README.md
```

## dbt Folder Explanation

- `models/`  
  Contains SQL transformations that build analytics tables.

- `models/staging/`  
  Contains cleaned representations of raw BigQuery tables.

- `models/marts/`  
  Contains business-facing tables used for analytics.

- `seeds/`  
  Stores small static CSV files that dbt can load into the warehouse.

- `snapshots/`  
  Used for tracking historical changes in source data (SCD Type 2).

- `tests/`  
  Contains custom data quality tests.

- `macros/`  
  Contains reusable SQL/Jinja functions.

- `analyses/`  
  Contains SQL queries for exploration that do not create database objects.