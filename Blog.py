from bs4 import BeautifulSoup

import os
import functions

import requests


"""

main function
make http request  --> reuqests
use bs4            --> beautifulsoup
store cleaned data -- > funtions
read -data
remove data

"""
 



def main_scrapper(url,directory):
    
    functions.create_dir(directory)
    source_code=requests.get(url)
    source_text= source_code.text
    soup=BeautifulSoup(source_text,"html.parser")
    articles=(soup.find_all('article',{'class':'blog-post'}))
    
    

   
    for article in articles:
        print("url:" + article.a.get('href'))
        #print("title:" + article.a.text)
        print("title:" + article.a.get('title'))
        print()
        article_foramtted= "url:" + article.a.get('href') + "\n\n" + "title:" +  article.a.get('title') + "\n"
        if functions.does_file_exists(directory+"/articles.txt") is False:
            functions.create_new_file(directory+"/articles.txt")
     
        functions.write_to_file(directory+"/articles.txt", article_foramtted)
        get_details(article.a.get('href'))
        
        
    







def get_details(url):
    
    source_code=requests.get(url)
    source_text= source_code.text
    soup=BeautifulSoup(source_text,"html.parser")
    div_entry =soup.find('div',{'class':'entry'})
    soup=BeautifulSoup(str(div_entry),"html.parser")
    paragraphs=soup.find_all('p')
    print()
    print("Paragraphs")
    functions.write_to_file("DailyCoffeNews/articles.txt","Paragraphs :\n\n")
    
    for p in paragraphs:
        if p.string is not None:
            print(p.string)
            functions.write_to_file("DailyCoffeNews/articles.txt", p.string)
    
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    functions.write_to_file("DailyCoffeNews/articles.txt","---------------\n\n")
    
    

main_scrapper("https://dailycoffeenews.com/","DailyCoffeNews")

#functions.read_lines("DailyCoffeNews/articles.txt",14)