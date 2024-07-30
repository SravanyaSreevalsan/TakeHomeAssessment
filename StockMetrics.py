class StockMetrics:
  def __init__(self, stockSymbol, type, lastDividend, fixedDividend, parValue, price):
    self.stockSymbol = stockSymbol
    self.type = type
    self.lastDividend = lastDividend
    self.fixedDividend = fixedDividend
    self.parValue = parValue
    self.price = price

  def calculateDividendYield(self):
    dividendYield = self.lastDividend/self.price
    print("Dividend Yield for this stock is "+ dividendYield)
  def calculatePbyERatio(self):
    pbyeRatio = self.price/self.lastDividend
    print("P by E ratio for this stock is "+ pbyeRatio)



