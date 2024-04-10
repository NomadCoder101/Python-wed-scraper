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
   # results=(soup.find_all('div',{'class':'course-listing'})[0].a)
    results=(soup.find_all('h4',{'class':'ql-align-center'}))
    
    
   #print(results)
   
    for result in results:
        #print(result)
        #print()
        #print( result.text)
        title_foramtted= result.text + "\n"
        if functions.does_file_exists(directory+"/articles.txt") is False:
            functions.create_new_file(directory+"/articles.txt")
     
        functions.write_to_file(directory+"/articles.txt",title_foramtted)
        
        
    
   

   
    #print(results.get('href'))
  
    #
  
    #print(results.text)
    
    
    #print(source_text)
                  
#block__text-wrapper
#b-126170120-top

#main_scrapper("https://calmandcode.teachable.com/p/create-a-laravel-social-network","calmandcode")

#functions.read_file("calmandcode/articles.txt")

functions.read_lines("calmandcode/articles.txt",4)