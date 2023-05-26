from bs4 import BeautifulSoup
import requests

burl = "https://finance.yahoo.com/crypto?count=100&offset=0"
bheaders = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}

def getData()->list:


    def getBody():
        r = requests.get(url=burl,headers=bheaders,timeout=5)
        bs = BeautifulSoup(r.content,features="lxml")
        tab = bs.find('table' , {"class":"W(100%)"})
        body= tab.find('tbody')
        return body
    
    body = getBody()

    def getCryptoNames():
        list = []
        for i in body.find_all('tr'):
            list.append(i.find("td",{"aria-label":"Name"}).get_text())
        return list
    
    def getCryptoPrices()->list:
        list  = []
        def getParent(td = [])->list:
            for i in body.find_all('tr'):
                td.append(i.find("td", {"aria-label":"Price (Intraday)"}))
            return td
        for j in getParent():
                a = j.find("fin-streamer").get_text()
                if a.find(",") != 0:
                     a = a.replace(",","")
                list.append(a) 
        return list



    def getCryptoSymbols()->list:
        
        list = []
        def symbolList(ls = []):
            for i in body.find_all('tr'):
                ls.append(i.find("a").get_text())
            return ls
        for i in symbolList():
            list.append(i.split("-")[0]) 
        return list
    

    def getChangeRate()->list:        
        list = []
        def getParent(td = [])->list:
            for i in body.find_all('tr'):
                td.append(i.find("td", {"aria-label":"Change"}))
            return td
        for j in getParent():
                list.append(j.find("fin-streamer").get_text())  
        return list        

        


    def getPercentChange()->list:
        
        list = []
        def getParent(td = [])->list:
            for i in body.find_all('tr'):
                td.append(i.find("td", {"aria-label":"% Change"}))
            return td
        for j in getParent():
                a = j.find("fin-streamer").get_text()
                a = a.replace("+","")
                a = a.replace("%","")
                list.append(a)  
        return list


    def getMarketCap()->list:
        list = []
        def getParent(td = [])->list:
            for i in body.find_all('tr'):
                td.append(i.find("td", {"aria-label":"Market Cap"}))
            return td
        for j in getParent():
                list.append(j.find("fin-streamer").get_text())  
        return list
    


    s = getCryptoSymbols() 
    n = getCryptoNames()
    p = getCryptoPrices()
    c = getChangeRate()
    per = getPercentChange()
    m = getMarketCap()

    ls = list(zip(s, n, p, c, per,m))
        

    return ls
