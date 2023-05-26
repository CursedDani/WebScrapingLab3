from CryptoTable import *
from Crypto import Crypto

class DB():
    def __init__(self) -> None:
        self.data = []
        a = getData()
        for i in a:
            self.data.append(Crypto(i))


    def showCrypto(self,l):
        for i in l:
            i.showCrypto()

    def showDatabase(self):
        self.showCrypto(self.data)

    def updateCrypto(self):
        a = getData()
        l = []
        for i in a:
            l.append(Crypto(i))
        self.data=l

    def bestCrypto(self,N):
        a = self.data
        l = []
        a.sort()

        for i in range(N):
            l.append(a[i])
        self.showCrypto(l)

    def searchCrypto(self,symbol):
        def findCrypto():
            for i in self.data:
                if i.symbol == symbol or symbol == i.name:
                    return i
                
        c = findCrypto()
        if c:
            c.showCrypto()
        else:
            print("Crypto not found")

    def mostExpensive(self,N):
        a = self.data
        l = []
        a.sort(key= lambda x:int(x.price),reverse=True)
        b = list(filter(lambda x:x.changerate > 0,a))
        for i in range(N):
            l.append(b[i])
        self.showCrypto(l)

    def addCrypto(self,burl):
        def extractCrypto():

            def get_body():
                bheaders = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"}
                r = requests.get(url=burl,headers=bheaders,timeout=5)
                bs = BeautifulSoup(r.content,features="lxml")
                return bs

            def getString():

                div = body.find('div' , {"class":"Mt(15px) D(f) Pos(r)"})
                alres = div.find('div',{"class":"D(ib)"})
                symb = alres.find('h1',{"class":"D(ib) Fz(18px)"}).get_text()
                return symb
            

            def getChangeRate():
                div = body.find('div' , {"class":"My(6px) Pos(r) smartphone_Mt(6px) W(100%) D(ib) smartphone_Mb(10px) W(100%)--mobp"})
                alres = div.find('div',{"class":"D(ib) Mend(20px)"})
                symb = alres.find('fin-streamer',{"class":"Fw(500) Pstart(8px) Fz(24px)"})
                res = symb.find("span").get_text()
                return res

            def getPrice():
                div = body.find('div' , {"class":"My(6px)"})
                alres = div.find('div',{"class":"D(ib) Mend(20px)"})
                symb = alres.find('fin-streamer',{"Fw(b) Fz(36px) Mb(-4px) D(ib)"}).get_text()
                return symb


            def getChangePerc():
                div = body.find('div' , {"class":"My(6px) Pos(r) smartphone_Mt(6px) W(100%) D(ib) smartphone_Mb(10px) W(100%)--mobp"})
                alres = div.find('div',{"class":"D(ib) Mend(20px)"})
                symb = alres.find('fin-streamer',{"data-field":"regularMarketChangePercent"}).get_text()
                return symb[1:symb.find(")")]

            def getMarketCap():
                div = body.find("table",{"class":"W(100%) M(0) Bdcl(c)"})
                alres = div.find("tr")
                symb = alres.find("td",{"class":"Ta(end)"}).get_text()
                return symb
            
            
            body = get_body()
            nameB = getString()
            name = nameB[:nameB.find("(")-1]
            symbol = nameB[nameB.find("(")+1:nameB.find("-")]
            change = getChangeRate()
            price = getPrice()
            changeperc = getChangePerc()
            marketcap = getMarketCap()
            price = price.replace(",","")
            changeperc = changeperc.replace("+","")
            changeperc = changeperc.replace("%","")
            return Crypto((symbol,name,price,change,changeperc,marketcap))
    
        def checkOnList(cr):
            check = False
            for i in self.data:
                if cr.symbol == i.symbol:
                    check = True
                    break
            return check
        #if not checkOnList(symbol):
        #    pass
        cr = extractCrypto()
        if not checkOnList(cr):
            self.data.append(cr)
            print(f'\nCrypto {cr.symbol} added correctly to database\n')
        else:
            print(f'\nCrypto {cr.symbol} is already on database\n')



            



    
