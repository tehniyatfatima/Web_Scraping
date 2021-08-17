import requests
from bs4 import BeautifulSoup


url=input("paste or write website url here: ")
print("_____________________________")
filename=input("enter file name for html code:")
r=requests.get(url)
htmlcon=BeautifulSoup(r.text,"html.parser")
formated=htmlcon.prettify()



f=open(filename+".html","w",encoding="utf-8")
f.write(formated)
f.close()


h_list=htmlcon.find_all("p")
l1=("No of headinds are :",(len(h_list)))
print(type(l1))

para_list=htmlcon.find_all("p")
print("No of paragraphs are :",len(para_list))

div_list=htmlcon.find_all("div")
print("No of divs are :",len(div_list))

imglist=htmlcon.find_all("img")
print("No of images are :",len(imglist))

an_list=htmlcon.find_all("href")
print("No of links are :",len(an_list))





