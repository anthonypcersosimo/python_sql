import pandas as pd

data = [['AAPL', "Consumer Discretionary", 0.0876], ['TSLA', "Consumer Discretionary", 0.0153], [
    'NVDA', "Information Technology", 0.0473], ['CSCO', "Information Technology", 0.0212]]

df = pd.DataFrame(data, columns=['ticker', 'abv_gics_sector', 'dividend_yield'])

sector_yield = df.groupby('abv_gics_sector')['dividend_yield'].mean()

print(sector_yield)