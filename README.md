_# Felyx data access for UvA students

## Introduction

Felyx uses Snowflake as data warehouse.
This repository shows how to query data available to
with Python, Pandas, and SQL.

Of course, you can also install a SQL client (e.g. [DBeaver](https://dbeaver.io/)) 
and connect to Snowflake directly.

## Installation

We provided two methods to install the required packages, 
[Poetry](https://python-poetry.org) (recommended) and a simple `requirements.txt`.

Based on your preference, either run:

```bash
poetry install
```

or 

```bash
pip install -r requirements.txt
```


## Run example

To run the exapmle, you need to create  a `.env` file 
in the root of this repository, e.g. by copying `.env.example`:

```bash
cp .env.example .env
```

Then, fill in the required credentials in `.env`:

```
SNOWFLAKE_USER=<your_username>
SNOWFLAKE_PASSWORD=<your_password>
``` 

Now, you can run the Python example.

```bash
# Assuming you have your virtual env activated
python example.py
```
