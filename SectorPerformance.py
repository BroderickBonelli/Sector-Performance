import requests
from bs4 import BeautifulSoup
import pandas as pd

sectors = ['XLC', 'XLY', 'XLP', 'XLE', 'XLF', 'XLV', 'XLI', 'XLB', 'XLRE', 'XLU', 'SPY']

df_list = []

for each_sector in sectors:
	url = 'https://finviz.com/quote.ashx?t={}'.format(each_sector)
	r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	soup = BeautifulSoup(r.text, 'lxml')

	perf_week = soup.find('td', string='Perf Week').find_next('td').text
	perf_month = soup.find('td', string='Perf Month').find_next('td').text
	perf_quarter = soup.find('td', string='Perf Quarter').find_next('td').text
	perf_half_year = soup.find('td', string='Perf Half Y').find_next('td').text
	perf_year = soup.find('td', string='Perf Year').find_next('td').text

	df_list.append([each_sector, perf_week, perf_month, perf_quarter, perf_half_year, perf_year])

df_columns = ['Ticker', '1w', '1mo', '3mo', '6mo', '1y']
df = pd.DataFrame(df_list, columns=df_columns)
print(df)