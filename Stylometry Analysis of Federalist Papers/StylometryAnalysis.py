import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt


papers = { #    main record
    'Madison' : [10,14,37,38,39,40,41,42,43,44,45,46,47,48],
    'Hamilton' : [1, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17, 21, 22, 23, 24,
                    25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 59, 60,
                    61, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                    78, 79, 80, 81, 82, 83, 84, 85],
    'Jay' : [2, 3, 4, 5],
    'Shared' :  [18, 19, 20],
    'Disputed' : [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63]
}

def read_file(files):
    string = [] # making an empty string to hold the read data, each element of this list will hold the full paper
    for file_no in files: # taking a single file at once
        with open(f'C:/Users/ASUS/Desktop/swayam_python/stylometry-federalist/data/federalist_{file_no}.txt') as f: # openign the file
            string.append(f.read()) # reading its whole data and appending into the string
            
    return ('\n'.join(string)) #after reading all the data of the 'author' returning it to be stored in federalist_by_author dict in a single string

federalist_by_author = {} # record for holding all the papers of the author by concatenating the papers' text

for author,files in papers.items(): # with author as keys, and files as the values, or the list of file numbers written by the author
    federalist_by_author[author] = read_file(files) #passing the list of file number to function to retrieve its data under the 'author'
    
# for author in papers:
#     print(federalist_by_author[author][:100]) 

#REAL STYLOMETRY STARTS HERE: 

authors = ('Madison','Hamilton','Jay','Shared','Disputed') # holding author name for better tokenization

len_distribution = {} 
author_token = {} # words used by the authors

for author in authors:
    tokens = nltk.word_tokenize(federalist_by_author[author]) # tokenizing author's paper
    
    author_token[author] = [token for token in tokens if token.isalpha()] #   if the token in the list of tokens is only alpha, then select that token

    token_len = [ len(token) for token in author_token[author] ] # storing the len of each token to plot it in graph
    
    len_distribution[author] = nltk.FreqDist(token_len) # creates a graph of frequency distributed over the lenghts of tokens
    
    plt.figure(figsize=(5, 5))  # setting figure size
    plt.title(f'Word Length Distribution for {author}') #giving the figure a title
    plt.xlabel('Word Length') # word length on x axis: 1,2,3,4,5...
    plt.ylabel('Frequency') # frequency of these token have come up
    
    len_distribution[author].plot(15,title=author) # actual plotting of the graphs
    
    
plt.show() # displaying the graphs

print("done")