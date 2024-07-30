
import datetime
class TradeRecorder:
    def __init__(self, quantity, price, buyorsellIndicator, timestamp, listoftrades):
        self.quantity = quantity
        self.price = price
        self.buyorsellIndicator = buyorsellIndicator
        self.timestamp = datetime.time(timestamp)
        self.listoftrades = listoftrades

        #method to record all trades
        def recordTrades(self):
            listoftrades = []
            listoftrades.extend([[self.timestamp, self.price,self.quantity, self.buyorsellindicator]])
            print(listoftrades[0])

        #method to get trades in last 5 minutes
        def tradesinlastfiveminutes(self):
            listoftradesinlast5minutes =[]
            timenow = datetime.datetime.now()
            for trade in listoftrades:
                if trade[0]-timenow==5:
                    listoftradesinlast5minutes.append(trade)





