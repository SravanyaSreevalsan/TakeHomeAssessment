import TradeRecorder
class StockMetrics:
  def __init__(self, stockSymbol, type, lastDividend, fixedDividend, parValue, price):
    self.stockSymbol = stockSymbol
    self.type = type
    self.lastDividend = lastDividend
    self.fixedDividend = fixedDividend
    self.parValue = parValue
    self.price = price

  # Method to calculate dividend yield
  def calculateDividendYield(self):
    if self.type == "Common":
      dividendYield = self.lastDividend/self.price
      print("Dividend Yield for this stock is "+ dividendYield)
    elif self.type == "Preferred":
      dividendYield = self.fixedDividend / self.price
      print("Dividend Yield for this stock is " + dividendYield)

   # Method to calculate P/E ratio
  def calculatePbyERatio(self):
    pbyeRatio = self.price/self.lastDividend
    print("P by E ratio for this stock is "+ pbyeRatio)

  # Method to calculate Volume Weighted Stock Price
  def calculateVolumeWeightedStockPrice(self):
    pass

    # Method to calculate GBCE All Share Index
  def calculateGBCEAllShareIndex(self):
    pass






