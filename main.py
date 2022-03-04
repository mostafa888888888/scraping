import csv
from itertools import zip_longest

import requests
from bs4 import BeautifulSoup

#tit = []
#loc = []
#skil = []
#nam = []
#link = []
#salary= []

result=requests.get('https://www.jobzella.com/search/#?what=sales&type=jobs&sortby=relevance&filterSearch=any&keywordtype=any')
src=result.content
#print(src)
soup=BeautifulSoup(src,"lxml")
#print(soup)

titles=soup.find_all("span",{"class":"ng-binding ng-isolate-scope"})
print(titles)
#location=soup.find_all("span",{"class":"css-5wys0k"})
#skills=soup.find_all("div",{"class":"css-y4udm8"})
#name=soup.find_all("a",{"class":"css-17s97q8"})
#print(history)

#for i in range (len(titles)):
# tit.append(titles[i].text)
     ##link.append(titles[i].find("a").attrs['href'])
     #loc.append(location[i].text)
     # skil.append(skills[i].text)
# nam.append(name[i].text)


#for link in link:
     #  result = requests.get('https://wuzzuf.net/jobs/p/rP4CGFeghsV8-Senior-Software-Engineer---Python-Paymob-Solutions-Cairo-Egypt?o=1&l=sp&t=sj&a=python|search-v3|navbg|spbg')
    #src=result.content
     #   soup=BeautifulSoup(src,"lxml")
     # salaries=soup.find("span",{"class":"css-wn0avc"})
# salary.append(salaries.text.strip())

#file=[tit,loc,skil,nam,link,salary]
#export=zip_longest(*file)
#with open("D:\pythonProject\pythonProject1jobzella\jobs.csv","w") as myfil:

     # wr=csv.writer(myfil)
     # wr.writerow(["titles","location","name"])
    #wr.writerows(export)
