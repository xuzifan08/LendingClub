import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def univariate(df, col, vartype, hue=None):
    """
    Univariate function will plot the graphs based on the parameters.
    df      : dataframe name
    col     : Column name
    vartype : variable type : continuos or categorical
                Continuos(0)   : Distribution, Violin & Boxplot will be plotted.
                Categorical(1) : Countplot will be plotted.
    hue     : It's only applicable for categorical analysis.

    """
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
                ax.annotate('{:1.1f}%'.format((p.get_height() * 100) / float(len(df))),
                            (p.get_x() + 0.05, p.get_height() + 20))
        else:
            for p in ax.patches:
                ax.annotate(p.get_height(), (p.get_x() + 0.32, p.get_height() + 20))
        del temp
    else:
        exit

    plt.show()


def crosstab(df, col):
    """
    df : Dataframe
    col: Column Name
    """
    crosstab = pd.crosstab(df[col], df['loan_status'],margins=True)
    crosstab['Probability_Charged Off'] = round((crosstab['Charged Off']/crosstab['All']),3)
    crosstab = crosstab[0:-1]
    return crosstab


# Probability of charge off
def bivariate_prob(df, col, stacked=True):
    """
    df      : Dataframe
    col     : Column Name
    stacked : True(default) for Stacked Bar
    """
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


def main():
    df_chunk = pd.read_csv('/Users/xuzifan/Desktop/LendingClub/loan_clean.csv', chunksize=1000000)
    chunk_list = []
    for chunk in df_chunk:
        chunk_list.append(chunk)
    loan = pd.concat(chunk_list)
    print(loan.shape)


    # compare the distribution of loan_amnt, installment
    univariate(df=loan, col='loan_amnt', vartype=0)
    univariate(df=loan, col='installment', vartype=0)

    # Multivariate Analysis for states
    filter_states = loan.addr_state.value_counts()
    filter_states = filter_states[(filter_states < 10)]

    loan_filter_states = loan.drop(labels=loan[loan.addr_state.isin(filter_states.index)].index)
    states = crosstab(loan_filter_states, 'addr_state')
    bivariate_prob(df=loan_filter_states, col='addr_state')

    # Multivariate Analysis for sub_grade of loan
    filter_grade = loan.sub_grade.value_counts()
    filter_grade = filter_grade[(filter_grade < 10)]

    loan_filter_grade = loan.drop(labels=loan[loan.sub_grade.isin(filter_grade.index)].index)
    sub_grade = crosstab(loan_filter_grade, 'sub_grade')
    bivariate_prob(df=loan_filter_grade, col='sub_grade')


if __name__ == "__main__":
    main()
