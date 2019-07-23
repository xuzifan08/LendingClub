import pandas as pd


df_chunk = pd.read_csv('/Users/xuzifan/Desktop/LendingClub/loan_clean.csv', chunksize=1000000)
chunk_list = []
for chunk in df_chunk:
    # chunk_filter = chunk_preprocessing(chunk) I can process it with
    chunk_list.append(chunk)
loan = pd.concat(chunk_list)
print(loan.shape)


def dimension_table(df, col, col_id):
    df[col_id] = df.groupby([col]).ngroup()
    d_table = df[[col_id, col]].drop_duplicates()
    return d_table


# generate dimension table for grade and sub_grade
col_grade = 'grade'
grade_id = 'grade_id'
grade = dimension_table(loan, col_grade, grade_id)
print(grade)


# generate dimension table for term
col_term = 'term'
term_id = 'term_id'
term = dimension_table(loan, col_term, term_id)
print(term)

# generate dimension table for emp_title
col_emp_title = 'emp_title'
emp_title_id = 'emp_title_id'
emp_title = dimension_table(loan, col_emp_title, emp_title_id)
print(emp_title)

# generate dimension table for home_ownership
col_home_ownership = 'home_ownership'
home_ownership_id = 'home_ownership_id'
home_ownership = dimension_table(loan, col_home_ownership, home_ownership_id)
print(home_ownership)

# generate dimension table for verification_status
col_verification_status = 'verification_status'
verification_status_id = 'verification_status_id'
verification_status = dimension_table(loan, col_verification_status, verification_status_id)
print(verification_status)

# generate dimension table for loan_status
col_loan_status = 'loan_status'
loan_status_id = 'loan_status_id'
loan_status = dimension_table(loan, col_loan_status, loan_status_id)
print(loan_status)

# generate dimension table for title
col_title = 'title'
title_id = 'title_id'
title = dimension_table(loan, col_title, title_id)
print(title)

# generate dimension table for addr_state
col_addr_state = 'addr_state'
addr_state_id = 'addr_state_id'
addr_state = dimension_table(loan, col_addr_state, addr_state_id)
print(addr_state)

# generate dimension table for initial_list_status
col_initial_list_status = 'initial_list_status'
initial_list_status_id = 'initial_list_status_id'
initial_list_status = dimension_table(loan, col_initial_list_status, initial_list_status_id)
print(initial_list_status)

# delete columns in fact table
col_drop = [col_grade, col_term, col_emp_title, col_home_ownership, col_verification_status, col_loan_status,
            col_title, col_addr_state,col_initial_list_status]
loan = loan.drop(col_drop, axis=1)
print(loan.shape)

