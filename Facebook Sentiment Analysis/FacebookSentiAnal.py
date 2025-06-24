import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# nltk.downloader.download('vader_lexicon') # run only one time

f = "sample_facebook_data.xlsx" # just giving variable a path to the file
xl = pd.ExcelFile(f)    #reading the file using pandas
dfs = xl.parse(xl.sheet_names[0]) # convertin the xl sheet into 'parse' dataframes, a 2-D data structure of pandas, and only the attritube [0] 
                                 # sheet_name[0] means onyl the first column or the relevant column is being converted.

dfs = list(dfs['Post']) # stored the relevant column/attribute in 'dfs' in form of list

# READING THE DATA IS DONE, NOW ANALYZING STARTS

sid = SentimentIntensityAnalyzer() #   pi initializing the object

for data in dfs: #  fetching each statement
    ss = sid.polarity_scores(data) #    scoring it 
    print(data)
    for i in ss:
        print(i,ss[i]) #    printing results
    print()
