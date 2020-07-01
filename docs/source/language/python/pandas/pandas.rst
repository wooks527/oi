=======
Pandas
=======

위키피디아에 따르면 Pandas를 다음과 같이 정의할 수 있다.

.. code-block:: text

    In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis.

Pandas는 행과 열을 가지는 2차원 데이터를 다루는데 유용한 파이선 Library이고, 이는 Data를 조작하거나 분석하는데 유용하다. Pandas의 Dataframe으로 이러한 작업을 진행하고, 하나의 열을 Series라고 한다.


Series
=======

* 데이터 생성하기
* 데이터 분석하기
* 데이터 선택하기
* 데이터 변경하기

Other functions
****************

* Series ￫ numpy array

    * to_numpy

        * 코드

        ::

            >>> ser = pd.Series(pd.Categorical(['a', 'b', 'a']))
            >>> ser.to_numpy()
            array(['a', 'b', 'a'], dtype=object)

        * 참조

            * `pandas documentation, pandas.Series.to_numpy <https://pandas.pydata.org/pandas-docs/version/0.24.0rc1/api/generated/pandas.Series.to_numpy.html>`_

* Series.max

    * 코드

    ::

        >>> idx = pd.MultiIndex.from_arrays([
        ...     ['warm', 'warm', 'cold', 'cold'],
        ...     ['dog', 'falcon', 'fish', 'spider']],
        ...     names=['blooded', 'animal'])
        >>> s = pd.Series([4, 2, 0, 8], name='legs', index=idx)
        >>> s
        blooded  animal
        warm     dog       4
                falcon    2
        cold     fish      0
                spider    8
        Name: legs, dtype: int64

    * 참조

        * `pandas, pandas.Series.max <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.max.html>`_


DataFrame
==========

* 데이터 생성하기
* 데이터 선택하기
* `데이터 변환하기 <dataframe.ipynb>`_
* 데이터 종류와 전처리
* group by, transform
* pivot/pivot_table, stack/unstack
* 데이터 병합하기

Other functions
****************

* Delete rows

    * 코드

    ::

        # Deleting columns

        # Delete the "Area" column from the dataframe
        data = data.drop("Area", axis=1)

        # alternatively, delete columns using the columns parameter of drop
        data = data.drop(columns="area")

        # Delete the Area column from the dataframe in place
        # Note that the original 'data' object is changed when inplace=True
        data.drop("Area", axis=1, inplace=True)

        # Delete multiple columns from the dataframe
        data = data.drop(["Y2001", "Y2002", "Y2003"], axis=1)

    * 참조

        * `Shane Lynn, The Pandas DataFrame – loading, editing, and viewing data in Python <https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/>`_

* Append rows

    * 코드

    ::

        # Importing pandas as pd 
        import pandas as pd 
        
        # Creating the first Dataframe using dictionary 
        df1 = df = pd.DataFrame({"a":[1, 2, 3, 4], 
                                "b":[5, 6, 7, 8]}) 
        
        # Creating the Second Dataframe using dictionary 
        df2 = pd.DataFrame({"a":[1, 2, 3], 
                            "b":[5, 6, 7]}) 

        # to append df2 at the end of df1 dataframe 
        df1 = df1.append(df2)

    * 참조

        * `GeeksforGeeks, Python| Pandas dataframe.append() <https://www.geeksforgeeks.org/python-pandas-dataframe-append/>`_

* numpy array ￫ DataFrame

    * 코드

    ::

        numpy_data = np.array([[1, 2], [3, 4]])
        df = pd.DataFrame(data=numpy_data, index=["row1", "row2"], columns=["column1", "column2"])

    * 참조

        * `kite, How to create Pandas DataFrame from a Numpy array in Python <https://kite.com/python/answers/how-to-create-pandas-dataframe-from-a-numpy-array-in-python>`_

* read_csv and to_csv

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

* Handle the dataframe

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

* Column 내용 수정

    * apply

        * 코드
        
        ::

            def add_one(x):
                return x + 1

            df[1] = df[1].apply(add_one)
            df[1] = df[1].apply(lambda x: x + 1)

        * 참조

            * `kite, How to modify all the values in a pandas DataFrame column in Python <https://kite.com/python/answers/how-to-modify-all-the-values-in-a-pandas-dataframe-column-in-python>`_

* Reset index

    * 코드

    ::

        >>> df = pd.DataFrame([('bird', 389.0),
        ...                 ('bird', 24.0),
        ...                 ('mammal', 80.5),
        ...                 ('mammal', np.nan)],
        ...                 index=['falcon', 'parrot', 'lion', 'monkey'],
        ...                 columns=('class', 'max_speed'))
        >>> df
                class  max_speed
        falcon    bird      389.0
        parrot    bird       24.0
        lion    mammal       80.5
        monkey  mammal        NaN

    * 참조

        * `pandas, pandas.DataFrame.reset_index <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html>`_

* Iterate rows

    * ilocs

        * 코드

        ::

            # import pandas package as pd 
            import pandas as pd 
            
            # Define a dictionary containing students data 
            data = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'], 
                            'Age': [21, 19, 20, 18], 
                            'Stream': ['Math', 'Commerce', 'Arts', 'Biology'], 
                            'Percentage': [88, 92, 95, 70]} 
            
            # Convert the dictionary into DataFrame 
            df = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage']) 
            
            print("Given Dataframe :\n", df) 
            
            print("\nIterating over rows using iloc function :\n") 
            
            # iterate through each row and select  
            # 0th and 2nd index column respectively. 
            for i in range(len(df)) : 
            print(df.iloc[i, 0], df.iloc[i, 2]) 

        * 출력

        ::

            Given Dataframe :
                    Name  Age    Stream  Percentage
            0      Ankit   21      Math          88
            1       Amit   19  Commerce          92
            2  Aishwarya   20      Arts          95
            3   Priyanka   18   Biology          70

            Iterating over rows using iloc function :

            Ankit Math
            Amit Commerce
            Aishwarya Arts
            Priyanka Biology


        * 참조

            * `GeeksforGeeks, Different ways to iterate over rows in Pandas Dataframe <https://www.geeksforgeeks.org/different-ways-to-iterate-over-rows-in-pandas-dataframe/>`_

* 정렬

    * 코드

    ::

    In [1]: import pandas as pd

    In [2]: personnel_df = pd.DataFrame({'sequence': [1, 3, 2],
    ...: 'name': ['park', 'lee', 'choi'],
    ...: 'age': [30, 20, 40]})

    In [3]: personnel_df

    Out[3]:
    age  name  sequence
    0   30  park         1
    1   20   lee         3
    2   40  choi         2

    * 참조
    
        * `R, Python 분석과 프로그래밍의 친구 (by R Friend) <https://rfriend.tistory.com/281>`_


:h2:`Reference`

* `Wikipedia, Pandas <https://en.wikipedia.org/wiki/Pandas_(software)>`_
* https://datascienceschool.net/view-notebook/c5ccddd6716042ee8be3e5436081778b/
* https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
