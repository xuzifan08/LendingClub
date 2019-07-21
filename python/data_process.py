import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from multiprocessing import Process

path = '/Users/xuzifan/Desktop/LendingClub/loan.csv'
chunksize = 10 ** 8
for loan in pd.read_csv(path, chunksize=chunksize):
    process(loan)


# data cleaning
# 1. function version
def removenull(dataframe, axis=1, percent=0.5):
    '''
    * removeNull function will remove the rows and columns based on parameters provided.
    * dataframe : Name of the dataframe
    * axis      : axis = 0 defines drop rows, axis =1(default) defines drop columns
    * percent   : percent of data where column/rows values are null,default is 0.5(50%)

    '''
    df = dataframe.copy()
    ishape = df.shape
    if axis == 0:
        rownames = df.transpose().isnull().sum()
        rownames = list(rownames[rownames.values > percent * len(df)].index)
        df.drop(df.index[rownames], inplace=True)
        print("\nNumber of Rows dropped\t: ", len(rownames))

    else:
        colnames = (df.isnull().sum() / len(df))
        colnames = list(colnames[colnames.values >= percent].index)
        df.drop(labels=colnames, axis=1, inplace=True)
        print("Number of Columns dropped\t: ", len(colnames))

    print("\nOld dataset rows,columns", ishape, "\nNew dataset rows,columns", df.shape)
    return df


loan = removenull(loan, axis=1, percent=0.5)


# 2. drop columns which has more than 95% same values (how to code it automatically???????)
same_vals = ['tax_liens', 'chargeoff_within_12_mths', 'delinq_amnt', 'num_tl_120dpd_2m', 'num_tl_30dpd', 'num_tl_90g_dpd_24m','out_prncp','out_prncp_inv', 'policy_code', 'acc_now_delinq', 'pub_rec_bankruptcies', 'application_type', 'hardship_flag']
loan = loan.drop(same_vals, axis=1)


# 3. remove duplicate columns (based on observation)
duplicate = ['purpose', 'funded_amnt', 'total_pymnt_inv']
loan = loan.drop(duplicate, axis=1)


# 4. select columns which makes sense for data warehouse and machine learning (based on observation)
cols_drop = ['pymnt_plan', 'zip_code', 'dti', 'pub_rec', 'total_rec_late_fee', 'recoveries','collection_recovery_fee', 'collections_12_mths_ex_med', 'disbursement_method', 'disbursement_method']
loan = loan.drop(cols_drop, axis=1)


# 5. filter out correlation
corr = loan.corr()
# drop the columns who have high correlations
corr_drop = ['int_rate', 'tot_hi_cred_lim', 'total_il_high_credit_limit', 'total_rev_hi_lim', 'revol_util', 'bc_util', 'tot_cur_bal','open_acc', 'num_actv_bc_tl', 'num_actv_rev_tl', 'num_bc_sats', 'num_bc_tl', 'num_op_rev_tl', 'num_rev_accts','num_rev_tl_bal_gt_0']
loan = loan.drop(corr_drop, axis=1)


# 6. Derive some new columns based on our business understanding that will be helpful in our analysis
# Loan amount to Annual Income ratio
loan['loan_income_ratio'] = loan['loan_amnt']/loan['annual_inc']
# Extract Year & Month from Issue date
loan['issue_month'], loan['issue_year'] = loan['issue_d'].str.split('-', 1).str


# generate ID for each row
loan["id"] = loan.index + 1


# write it to clean data
loan.to_csv("/Users/xuzifan/Desktop/LendingClub/clean_loan.csv", index=False)



