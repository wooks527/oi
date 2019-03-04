Pandas
=======

**read_csv and to_csv**

::

    # read_csv
    pd.read_csv('sample1.csv')
    pd.read_csv('sample2.csv', names=['c1', 'c2', 'c3'])
    pd.read_csv('sample1.csv', index_col='c1')
    # This defines separator as being one single white space or more
    pd.read_table('sample3.txt', sep='\s+')

    # to_csv
    df.to_csv('sample6.csv')
    df.to_csv('sample7.txt', sep='|')
    df.to_csv('sample8.csv', na_rep='누락')


**Handle the dataframe**

::

    # Drop rows of Pandas DataFrame whose value in certain columns is NaN
    df[pd.notnull(df['IC50 (nM)'])]

    # Reset the index
    df.reset_index(drop=True)

    # Get header list
    list(df.columns.values)
    list(df)

    # Select rows from a Pandas DataFrame based on values in a column
    df.loc[df['favorite_color'] == 'yellow']
    df[df['A'].str.contains("hello")]
    df[df['A'].str.contains("Hello|Britain")==True]
    array = ['yellow', 'green']
    df.loc[df['favorite_color'].isin(array)]

    # Change column names
    df.rename(index=str, columns={"A": "a", "C": "c"})



**Reference**
    * https://datascienceschool.net/view-notebook/c5ccddd6716042ee8be3e5436081778b/
    * https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html