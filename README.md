# Lending Club 

# Table of contents
1. [Introduction](#Introduction)
2. [Motivation](#Motivation)
3. [Data Source](#Data-Source)
4. [Process](#Process)
    1. [Data Cleaning](#Data-Cleaning)
    2. [Exploratory Data Analysis](#Exploratory-Data-Analysis)
    3. [Prototype of Datapipline](#Prototype-of-Datapipline) 
5. [Project Structure](#Project-Structure)
6. [How to run](#How-to-run)
7. [Future Improvements](#Future-Improvements)


## Introduction
LendingClub.com was founded in 2005. Annual returns on peer-to-peer lending are higher and more attractive compare to the saving rates and bond yields, but riskier. The number of issued loans increased dramatically over the years in Lending Club from 21K in 2011 to 47 billion in 2019. Therefore, there has been increasing demands for intelligently automated programs to pick up the “Right Loan” to get risk-free or low-risk returns of the loan investments as typical fixed income investors expect. 

In this project, based on the lending club data which has more than 226k rows and 145 columns, my objective is to extract useful information for exploratory data analysis through data cleaning, and build a prototype of production data pipeline which allows data scientists and data analysts to interactively query and explore the data, and will also be used for machine learning model training and evaluation.

The baby data pipeline should reach several standards:
- Create a relational data model / schema in a database or storage engine
- Develop code that will persist the dataset into this storage system in a fully automated way
- Include any data validation routines if necessary

## Motivation
 1. Data cleaning and exploratory data analysis
 2. Build a prototype of production data pipeline to support software engineers, data scientists and data analysts.

## Data Source
Lending club data is stored in Kaggle as a csv file: https://www.kaggle.com/wendykan/lending-club-loan-data

## Process
### Data Cleaning (see code [here](sc/python/data_cleaning.py))
The data source contains 145 features. It was messy with a lot of missing values for some features and unstructured string data that needed to be cleaned and transformed.
This is the steps of cleaning the dataset:
1. Drop columns and rows which has more than 95% same values
2. Remove duplicate columns
3. Select columns which makes sense for data warehouse and machine learning (based on observation)
4. Filter out columns which have high correlations
5. Derive new columns based on domain knowledge that will be helpful in machine learning models

### Exploratory Data Analysis (see code [here](sc/python/exploratory_data_analysis.py))
link to run

### Prototype of Datapipline (see code [here](sc/python/build_database.py))
link to run

## Project Structure


## How to run


## Future Improvements
