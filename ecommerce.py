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
    products=(soup.find_all('div',{'class':'product-single'}))
    
    

   
    for product in products:
        print("image:" + product.img['src'])
        print("title:" + product.h1.string)
        print("Price:" + product.find('span',{'id':'ProductPrice'}).string.strip())
        print()
        
        image =product.img['src']
        title = product.h1.string
        price = product.find('span',{'id':'ProductPrice'}).string.strip()
        product_foramtted= "Title:" + title + "\n" + "Image:" + image  + "\n" + "Price:" + price + "\n\n\n"
        
        if functions.does_file_exists(directory+"/products.txt") is False:
            functions.create_new_file(directory+"/products.txt")
     
        functions.write_to_file(directory+"/products.txt", product_foramtted)
        #get_details(article.a.get('href'))
        
        
    







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
            if "coffee" in p.string:
                print("Found it")
                print(p.string)
                functions.write_to_file("DailyCoffeNews/articles.txt", p.string)
    
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    functions.write_to_file("DailyCoffeNews/articles.txt","---------------\n\n")
    
    

main_scrapper("https://sprudge.myshopify.com/","Sprudge")

#functions.read_lines("DailyCoffeNews/articles.txt",14)