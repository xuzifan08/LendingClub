# Lending Club


## Table of contents
1. [Introduction](#Introduction)
2. [Motivation](#Motivation)
3. [Data Source](#Data-Source)
4. [Process](#Process)
    1. [Data Cleaning](#Data-Cleaning-see-code-here)
    2. [Exploratory Data Analysis](#Exploratory-Data-Analysis-see-code-here)
    3. [Prototype of Data pipline](#Prototype-of-Data-pipline-see-code-here) 
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
 1. EDA: Lending club loan data cleaning and exploratory data analysis
 2. Data pipeline: Build a prototype of production data pipeline to support software engineers, data scientists and data analysts.


## Data Source
Lending club loan data (2007-2015) is stored in Kaggle as a csv file: https://www.kaggle.com/wendykan/lending-club-loan-data


## Process
### Data Cleaning (see code [here](src/python/data_cleaning.py))
The data source contains 145 features. It was messy with a lot of missing values for some features and unstructured string data that needed to be cleaned and transformed.
This is the steps of cleaning the dataset:
 1. Drop feature if it has missing 50% values of that record
 2. Drop feature if 95% values of it are the same
 3. Drop feature if it is the same as other feature (I might only choose to use one of them)
 4. Drop feature if the features are highly correlated (|r| >0.8) (I might only choose to use one of them)
 5. Derive some new columns based on domain knowledge that will be helpful for machine learning models and data analysis

### Exploratory Data Analysis (see code [here](src/python/exploratory_data_analysis.py))
#### Univariate Analysis
![Image description](docs/uni_analysis.png)

#### Bivariate/Multivariate Analysis
![Image description](docs/binary_analysis.png)

### Prototype of Data pipline (see code [here](src/python/build_database.py))
#### Design Schema for Database
I choose the star schema for the relational database which stored the processed structure data.
This is the finalized star schema:
![Image description](docs/LendingClubStarSchema.png)
Reasons I choose relational database and star schema:
 1. Avoid redundency as data grows
 2. A good fit for interactive query and data analysis especially if a use case focuses on data analysis in terms of a category feature, such as loan grade or employment title
 3. Easy to maintain and understand the relaionship between features
 
#### ETL process


## Project Structure


## How to run


## Future Improvements
1. Computing tool consideration:
   
   The loan data from 2007 to 2015 is about 1GB, it is comparatively efficient to use pandas do computation. If the data is growing in the future, I would consider use spark running the ETL process on cloud services like AWS.
   
2. Relational database consideration:

   Use postgreSQL for storage
    
  
