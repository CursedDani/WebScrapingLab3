class Crypto():
    def __init__(self,data) -> None:
        self.symbol = data[0]
        self.name = data[1]
        self.price = float(data[2])
        self.changerate = float(data[3])
        self.changeperc = float(data[4])
        self.marketcap = data[5]
    
    def __lt__(self, other):
        return self.price < other.price and self.changeperc > other.changeperc

    def showCrypto(self):
        print(f'\n*******Crypto {self.symbol}*******')
        print(f'Name:{self.name}')
        print(f'Price:{self.price}')
        print(f'Change Rate:{self.changerate}')
        print(f'Change Percentage:{self.changeperc}%')
        print(f'Market Cap:{self.marketcap}\n')