# # Get Data Flags
# query = f'SELECT last_known_ticker, data_flag from {table_name} WHERE data_flag = "Y"'
# df.to_csv(r"C:\Users\Anthony's Razer\Desktop\Repositories\python_sql\csv\data_flags.csv")

# # Create Retail Universe
# query = f'SELECT * from {table_name}'
# df.to_csv(r"C:\Users\Anthony's Razer\Desktop\Repositories\python_sql\csv\ec_universe_20190531_retail.csv")

# # Find Chars in Column Data
# query = f'SELECT * FROM {table_name} WHERE field_name LIKE "%Example%"'

# # Group By
# df['mvd_sector_rank'] = df.groupby('gics_sector')['mean_valuation_deviation'].rank(ascending=False)

# # Find the average price by Sector --GMAs
# column = 'Sector'
# avg_sector_px = df.groupby(column)['Price'].mean()
# print(avg_sector_px)