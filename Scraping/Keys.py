import openpyxl
import pandas as pd
from pandas import DataFrame
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

IDT = pd.read_excel('/Users/Anirudh/Desktop/ID.xlsx')
IDT =IDT[['ID']]
IDT
ID = IDT['ID'].tolist()
ID


imdb = []
count = 0

driver = webdriver.Firefox(executable_path = '/Users/Anirudh/Desktop/crawling/geckodriver',log_path="/Users/Anirudh/Desktop/geckodriver.log")
driver.set_page_load_timeout(600)
for i in ID:
    a = i
    driver.get('https://www.imdb.com/title/' + a + '/')
    sel = Selector(text=driver.page_source)
    try:
        meta = driver.find_element_by_css_selector('.metacriticScore')
        meta = meta.text
        print(meta)
    except:
        meta = print("-") 
        print(meta)

    try:
        cumulative = driver.find_element_by_css_selector('div.txt-block:nth-child(15)')
        cumulative = cumulative.text
        print(cumulative)
    except:
        cumulative = print("-") 
        print(cumulative)
    try: 
        language = driver.find_element_by_css_selector('#titleDetails > div:nth-child(5) > a:nth-child(2)')
        language = language.text
        print(language)
    except:
        language = print("-")  
        print(language) 
    summary = driver.find_element_by_css_selector('div.inline:nth-child(3)')
    summary = summary.text
    print(summary)
    k = []
    temp = [a,meta,cumulative,language,summary]
    try:
        keywordsnav = driver.find_element_by_css_selector('div.see-more:nth-child(6) > nobr:nth-child(12) > a:nth-child(1)').click()
        keywords = driver.find_elements_by_class_name('sodatext')
        keywordslist = len(keywords)
        for i in range(keywordslist):
            k.append(keywords[i].text)
        temp.append(k)
        imdb.append(temp)
    except:
        print("-")
    count +=1
    print('\n')
    print(count)
    print('\n')
        
driver.quit()

Data = pd.DataFrame(imdb)
Data
Data.to_excel('/Users/Anirudh/Desktop/data.xlsx')
a

