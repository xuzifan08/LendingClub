import pandas as pd
from sqlalchemy import create_engine


## This file is used to read cleaned loan data, extract and create dimentional tables, create loan fact table, and write dataframe into PostgreSQL


def dimension_table(df, col, col_id):
    """
    Dimention_table function will create a dimensional table for a specific category column in Dataframe
    :param df: Dataframe name
    :param col: The category column for creating dimensional table
    :param col_id: Unique ID for rows in dimensional table
    :return: Finalized dimensional table
    """
    df[col_id] = df.groupby([col]).ngroup()
    d_table = df[[col_id, col]].drop_duplicates()
    return d_table


def main():
    """
    Main function will get the cleaned dataframe, generate fact table and dimensional tables from Dataframe, write
    data into relational database
    """
    ## read cleaned loan data into Dataframe
    df_chunk = pd.read_csv('/Users/xuzifan/Desktop/LendingClub/loan_clean.csv', chunksize=1000000)
    chunk_list = []
    for chunk in df_chunk:
        chunk_list.append(chunk)
    loan = pd.concat(chunk_list)

    ## generate dimension tables
    # grade table
    grade = dimension_table(loan, 'grade', 'grade_id')

    # term table
    term = dimension_table(loan, 'term', 'term_id)

    # emp_title table
    emp_title = dimension_table(loan, 'emp_title', 'emp_title_id')

    # home_ownership table
    home_ownership = dimension_table(loan, 'home_ownership', 'home_ownership_id')

    # verification_status table
    verification_status = dimension_table(loan, 'verification_status', 'verification_status_id')

    # loan_status table
    loan_status = dimension_table(loan, 'loan_status', 'loan_status_id')

    # title table
    title = dimension_table(loan, 'title', 'title_id')

    # addr_state table
    addr_state = dimension_table(loan, 'addr_state', 'addr_state_id')

    # initial_list_status table
    initial_list_status = dimension_table(loan, 'initial_list_status', 'initial_list_status_id')

    # delete columns in fact tables which already exist in dimensional tables
    col_drop = ['grade', 'term', 'emp_title', 'home_ownership', 'verification_status', 'loan_status',
                'title', 'addr_state', 'initial_list_status']
    loan = loan.drop(col_drop, axis=1)

    ## save data into tables in database
    engine = create_engine('postgresql://xuzifan@localhost:5432/lendingclub')
    loan.to_sql('loan_fact', engine)
    grade.to_sql('grade', engine)
    term.to_sql('term', engine)
    emp_title.to_sql('emp_title', engine)
    home_ownership.to_sql('home_ownership', engine)
    verification_status.to_sql('verification_status', engine)
    loan_status.to_sql('loan_status', engine)
    title.to_sql('title', engine)
    addr_state.to_sql('addr_state', engine)
    initial_list_status.to_sql('initial_list_status', engine)


if __name__ == "__main__":
    
    main()

