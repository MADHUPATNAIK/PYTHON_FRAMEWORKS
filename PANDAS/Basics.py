import pandas as pd

'''
Pandas DataFrame:
    A data frame is a way represent and work with tabular data.
    Tabular data has rows and columns.
'''
reviews = pd.read_csv("ign.csv")
'''
Head() and tail() are used to print the 1st 5 elements
and last 5 elements of the dataset. By default its 5.
'''
ld = reviews.head()
'''
shape - is used to given the no. of rows and columns of 
the matrix(its not a function)
'''
sh = reviews.shape
'''
iloc is similar to head function and , separates the 
rows and columns specifications.
'''
ld1 = reviews.iloc[0:10,:]
'''
loc() : allows to index using labels instead of positions
Trying loc with numbers lower than 10 or higher than 20
results in an error.
'''
ld2 = reviews.loc[0:5,:]
ld4 = reviews.loc[:5,"score"]
ld5 = reviews.loc[:5,["score","release_year"]]
'''
index property:
'''
ld3 = reviews.index



###########
#PANDAS SERIES OBJECTS
##########

'''Just specifying the name of the column would retrieve
the whole column. When we retrieve a single column,
we're actually retrieving a Pandas.
'''

ld6 = reviews["score"]
ld7 = reviews[["score","release_year"]]

'''Series Object: Usually DF stores tabular data, but series 
stores a single column or row of Data. Each column in a DataFrame
is a series object.
'''
ty1 = type(ld6)

'''
To create a series, we pass a list or NUmpy array into the
series object when we instantiate it
'''
ty2 = pd.Series([1,2,3,4])

#A series can have any kind of data, mixed types.
ty3 = pd.Series(["TirupatiRao","Swarna","Praneeth","Madhu"])

'''
Creating a DataFrame:
    A dataframe is created by passing multiple series 
    into DF class
'''
df1 = pd.DataFrame([ty2,ty3])
#or
df2 = pd.DataFrame([
            [1,2,3,4],
            ["U","T","O","N"]
        ])
    
df3 = pd.DataFrame([
            [1,2,3,4],
            ["U","T","O","N"]
        ],
    index = ["row1","row2"],
    columns = ["col1","col2","col3","col4"])

s = df3.loc["row2","col1":"col2"]

#######################
#CALCULATIONS IN PANDAS
######################

meanval = reviews["score"].mean()

#also,
#calculates mean of all numerical columns
meanOfAllCols = reviews.mean() 

'''Axis Keyword - computes mean of each row or
each column by default. By default, axis is 0
and computes the mean of each column, if axis
is 1, it then computes mean of each row. Also,
it only computes mean of numerical values
'''
meanOfEachRow = reviews.mean(axis = 1)

'''Corr: used to see if any columns have any
correlation'''
cr1 = reviews.corr()

'''Count - counts number of non-null values'''
count1 = reviews.count()

'''
MAX : highest value in each columns
'''
highest = reviews.max()
'''
MIN : lowest value in each column
'''
lowest = reviews.min()
'''
median: Median of each numerical column
'''
med = reviews.median()
'''
std = standard Deviation of each numerical column
'''
std = reviews.std()
'''
MATH OPERATIONS ON SERIES
'''
div = reviews["score"]/2 #+,-,*,/,^ = will apply to each element in DF or series

#################
#BOOLEAN INDEXING
#################
scores_filter = reviews["score"] > 7
'''
Using this filter to select only those rows that are true
'''
filtered_reviews = reviews[scores_filter]
fr1 = filtered_reviews.head()
'''Using multiple conditions for filtering
Say, if we want to find games for Xbox One that have score 
more than 7
'''
xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
fr2 = reviews[xbox_one_filter].head()
print(fr2)
