

import os

from bs4 import BeautifulSoup

import functions

import requests

result= requests.get('http://www.google.com')

print(result)
#print(result.text)

functions.create_dir('Wiki2')

html = """
<div>This is a div1</div>
<p id="tag">This ia a p tag1</p>
<div>This is a div2</div>
<div class="div">This is a div3</div>
<p>This ia a p tag2</p>
<p id="tag">This ia a p tag3</p>

<div id="test">
<h2>This is a div1</h2>
<p id="tag">This ia a p tag1</p>
<a href="http://www.example.com">Login</a>
<img src="image.jpg" alt="image">

</div>
"""

soup = BeautifulSoup(html,"html.parser")

#print(soup.p.text)

#print(soup.find_all("div")[-1])
#print(soup.find_all("div", {"class": "div"}))
#print(soup.find_all("div", {"id": "test"}))
#print(soup.find_all("div", {"id": "test"})[0].a)
#print(soup.find_all("div", {"id": "test"})[0].img)
#print(soup.find("div", {"id": "test"}).img)

