import pandas as pd

data = [['AAPL', "Consumer Discretionary", 12.88], ['TSLA', "Consumer Discretionary", 92.52], [
    'NVDA', "Information Technology", 221.37], ['CSCO', "Information Technology", 631.47]]

df = pd.DataFrame(data, columns=['ticker', 'sector', 'price'])

# Create a column called Price_Rank and rank the price descending by Sector
df['price_rank'] = df.groupby('sector')['price'].rank(ascending=False)

# Print your shiny new data frame sorted by Sector A-Z and then Price_Rank Hi-Lo
sortedDf = df.sort_values(['sector', 'price_rank'], ascending=[False, True])

print(sortedDf)