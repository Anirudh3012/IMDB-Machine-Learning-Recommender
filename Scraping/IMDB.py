pip install selenium
pip install pandas
pip install parsel
pip install openpyxl
pip install xlrd

import openpyxl
import pandas as pd
from pandas import DataFrame
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Basic details of the movies and tvshows in a very raw format
TitleDetails = pd.read_csv('/Users/Anirudh/Downloads/Title.tsv', sep='\t',low_memory = False)
TitleDetails

#Movie ratings and the number of votes
ratings_table = pd.read_csv('/Users/Anirudh/Downloads/title.ratings.tsv', sep='\t')
ratings_table

#Movie title and type is mentioned in this dataset
basic = pd.read_csv('/Users/Anirudh/Downloads/basic.tsv', sep='\t',low_memory = False)
basic

#Merging title details with the ratings respectively
motherdata = pd.merge(basic, ratings_table, on='tconst')
motherdata 

#Removing unwanted columns from our DataFrame
motherdata = motherdata.drop(columns=["isAdult","endYear","runtimeMinutes"])
motherdata

#Making a new dataframe with a decreasing order of number of votes and taking a sample of 200000 to work with
MasterData = motherdata.sort_values(by=['numVotes'], ascending=False)
MasterData = MasterData[0:200000]
MasterData

#Details of crew that worked on a project 
NameDetails = pd.read_csv('/Users/Anirudh/Downloads/namedetails.tsv', sep='\t',low_memory = False)
NameDetails

#Connection between the crew member to a movie title
df = pd.read_csv('/Users/Anirudh/Downloads/title.principals.tsv', sep='\t',low_memory = False)
df
df = df[(df['category']=='actor') | (df['category']=='director')]

#Create a table with crew members and tconst to later join it to the final table
CrewDetails = pd.merge(df,NameDetails,on = 'nconst')
CrewDetails = CrewDetails[ (CrewDetails['category']=='actor') | (CrewDetails['category']=='director')]
CrewDetails

#Merge it to make the final table
Table = pd.merge(MasterData,CrewDetails,on= 'tconst')
Table = Table.drop(columns = ['knownForTitles','primaryProfession','deathYear','characters','job','ordering'])
Table

#Making a seperate column with the directors to use as a factor
DirectorList = Table[Table['category']=='director']
DirectorList = DirectorList[['tconst','primaryName']]
DirectorList
Table = Table[Table['category']=='actor']
Table

#Merging the director details with the actors
Table = pd.merge(Table,DirectorList,on ='tconst')
Table = Table.drop(columns = ['originalTitle'])
Table

#Removing unwanted columns 
Table = Table.rename(columns={'tconst':'ID','titleType':'Type','primaryTitle':'Title','startYear':'Year','genres':'Genres','averageRating':'Rating','numVotes':'Votes','birthYear':'Birth Year'})
Table
Table.to_excel('Data.xlsx')

x = Table[Table['Type']=='movie']

x = x.groupby('ID').agg(lambda x: x.tolist())

x.to_excel('prof.xlsx')

FinalTable = pd.read_excel('/Users/Anirudh/Desktop/prof.xlsx')
FinalTable =FinalTable[['ID','Type','Director','Title','Year','Year','Genres','Rating','Votes','Actors']]
Actors = []
Actors = FinalTable['Actors'].tolist()
Actors
Actors = list(dict.fromkeys(Actors))
FinalTable['new_col'] = Actors

Actors(set(x))
Final = pd.read_excel('/Users/Anirudh/Downloads/Actors.xlsx')
Act = []
up =[]
Act = Final['Actor'].tolist()

Act
FinalTable['new_col'] = Act