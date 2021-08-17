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

h1_list=htmlcon.find_all("h1")
print("No of h1 headinds are :",(len(h1_list)))

h2_list=htmlcon.find_all("h2")
print("No of h2 headinds are :",(len(h2_list)))

h3_list=htmlcon.find_all("h3")
print("No of h3 headinds are :",(len(h3_list)))

h4_list=htmlcon.find_all("h4")
print("No of h4 headinds are :",(len(h4_list)))

h5_list=htmlcon.find_all("h5")
print("No of h5 headinds are :",(len(h5_list)))

h6_list=htmlcon.find_all("h6")
print("No of h6 headinds are :",(len(h6_list)))


para_list=htmlcon.find_all("p")
print("No of paragraphs are :",len(para_list))

div_list=htmlcon.find_all("div")
print("No of divs are :",len(div_list))

imglist=htmlcon.find_all("img")
print("No of images are :",len(imglist))

an_list=htmlcon.find_all("a")
print("No of links are :",len(an_list))





