import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_chunk = pd.read_csv('/Users/xuzifan/Desktop/LendingClub/loan.csv', chunksize=1000000)
chunk_list = []
for chunk in df_chunk:
    # chunk_filter = chunk_preprocessing(chunk) I can process it with
    chunk_list.append(chunk)
loan = pd.concat(chunk_list)
print(loan.shape)


# data cleaning
# 1. drop columns which has more than 50% missing values
# function version
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
"""same_vals=['tax_liens', 'chargeoff_within_12_mths', 'delinq_amnt', 'num_tl_120dpd_2m', 'num_tl_30dpd', 'num_tl_90g_dpd_24m','out_prncp',
           'out_prncp_inv', 'policy_code', 'acc_now_delinq', 'pub_rec_bankruptcies', 'application_type', 'hardship_flag']"""
same_vals = ['tax_liens', 'chargeoff_within_12_mths', 'delinq_amnt', 'num_tl_120dpd_2m', 'num_tl_30dpd', 'num_tl_90g_dpd_24m','out_prncp',
           'out_prncp_inv', 'policy_code', 'acc_now_delinq', 'pub_rec_bankruptcies', 'application_type', 'hardship_flag']
loan = loan.drop(same_vals, axis=1)


# 3. remove duplicate columns (based on observation)
"""duplicate=['purpose', 'funded_amnt', 'out_prncp_inv', 'total_pymnt_inv']"""
duplicate = ['purpose', 'funded_amnt', 'total_pymnt_inv']
loan = loan.drop(duplicate, axis=1)


# 4. select columns which makes sense for data warehouse and machine learning (based on observation)
cols_drop = ['pymnt_plan', 'zip_code', 'dti', 'pub_rec', 'total_rec_late_fee', 'recoveries',
             'collection_recovery_fee', 'collections_12_mths_ex_med', 'disbursement_method', 'disbursement_method']
loan = loan.drop(cols_drop, axis=1)


# 5. filter out correlation
corr = loan.corr()
# drop the columns who have high correlations
corr_drop = ['int_rate', 'tot_hi_cred_lim', 'total_il_high_credit_limit', 'total_rev_hi_lim', 'revol_util', 'bc_util', 'tot_cur_bal',
             'open_acc', 'num_actv_bc_tl', 'num_actv_rev_tl', 'num_bc_sats', 'num_bc_tl', 'num_op_rev_tl', 'num_rev_accts',
             'num_rev_tl_bal_gt_0']
loan = loan.drop(corr_drop, axis=1)


# 6. Derive some new columns based on our business understanding that will be helpful in our analysis
# Loan amount to Annual Income ratio
loan['loan_income_ratio'] = loan['loan_amnt']/loan['annual_inc']
# Extract Year & Month from Issue date
loan['issue_month'], loan['issue_year'] = loan['issue_d'].str.split('-', 1).str


# generate ID for each row
loan["id"] = loan.index + 1


# EDA
# One variable: Data visualization
def univariate(df, col, vartype, hue=None):
    '''
    Univariate function will plot the graphs based on the parameters.
    df      : dataframe name
    col     : Column name
    vartype : variable type : continuos or categorical
                Continuos(0)   : Distribution, Violin & Boxplot will be plotted.
                Categorical(1) : Countplot will be plotted.
    hue     : It's only applicable for categorical analysis.

    '''
    sns.set(style="darkgrid")

    if vartype == 0:
        fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 8))
        ax[0].set_title("Distribution Plot")
        sns.distplot(df[col], ax=ax[0])
        ax[1].set_title("Violin Plot")
        sns.violinplot(data=df, x=col, ax=ax[1], inner="quartile")
        ax[2].set_title("Box Plot")
        sns.boxplot(data=df, x=col, ax=ax[2], orient='v')

    elif vartype == 1:
        temp = pd.Series(data=hue)
        fig, ax = plt.subplots()
        width = len(df[col].unique()) + 6 + 4 * len(temp.unique())
        fig.set_size_inches(width, 7)
        ax = sns.countplot(data=df, x=col, order=df[col].value_counts().index, hue=hue)
        if len(temp.unique()) > 0:
            for p in ax.patches:
                ax.annotate('{:1.1f}%'.format((p.get_height() * 100) / float(len(loan))),
                            (p.get_x() + 0.05, p.get_height() + 20))
        else:
            for p in ax.patches:
                ax.annotate(p.get_height(), (p.get_x() + 0.32, p.get_height() + 20))
        del temp
    else:
        exit

    plt.show()


univariate(df=loan, col='loan_amnt', vartype=0)


# Bivariate/Multivariate Analysis
def crosstab(df, col):
    '''
    df : Dataframe
    col: Column Name
    '''
    crosstab = pd.crosstab(df[col], df['loan_status'],margins=True)
    crosstab['Probability_Charged Off'] = round((crosstab['Charged Off']/crosstab['All']),3)
    crosstab = crosstab[0:-1]
    return crosstab


# Probability of charge off
def bivariate_prob(df, col, stacked=True):
    '''
    df      : Dataframe
    col     : Column Name
    stacked : True(default) for Stacked Bar
    '''
    # get dataframe from crosstab function
    plotCrosstab = crosstab(df, col)

    linePlot = plotCrosstab[['Probability_Charged Off']]
    barPlot = plotCrosstab.iloc[:, 0:2]
    ax = linePlot.plot(figsize=(20, 8), marker='o', color='b')
    ax2 = barPlot.plot(kind='bar', ax=ax, rot=1, secondary_y=True, stacked=stacked)
    ax.set_title(df[col].name.title() + ' vs Probability Charge Off', fontsize=20, weight="bold")
    ax.set_xlabel(df[col].name.title(), fontsize=14)
    ax.set_ylabel('Probability of Charged off', color='b', fontsize=14)
    ax2.set_ylabel('Number of Applicants', color='g', fontsize=14)
    plt.show()


filter_states = loan.addr_state.value_counts()
filter_states = filter_states[(filter_states < 10)]

loan_filter_states = loan.drop(labels=loan[loan.addr_state.isin(filter_states.index)].index)
states = crosstab(loan_filter_states, 'addr_state')
bivariate_prob(df=loan_filter_states, col='addr_state')


# save dataframe as cleandata


# create sub_dataframe according to schema
