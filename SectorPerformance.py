import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sectors = ['XLC', 'XLY', 'XLP', 'XLE', 'XLF', 'XLV', 'XLI', 'XLB', 'XLRE', 'XLU', 'SPY']

df_list = []

for each_sector in sectors:
	url = 'https://finviz.com/quote.ashx?t={}'.format(each_sector)
	r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	soup = BeautifulSoup(r.text, 'lxml')

	perf_week = soup.find('td', string='Perf Week').find_next('td').text.strip('%')
	perf_month = soup.find('td', string='Perf Month').find_next('td').text.strip('%')
	perf_quarter = soup.find('td', string='Perf Quarter').find_next('td').text.strip('%')
	perf_half_year = soup.find('td', string='Perf Half Y').find_next('td').text.strip('%')
	perf_year = soup.find('td', string='Perf Year').find_next('td').text.strip('%')

	df_list.append([each_sector, float(perf_week), float(perf_month), float(perf_quarter), float(perf_half_year), float(perf_year)])

df_columns = ['Sector', '1w', '1mo', '3mo', '6mo', '1y']
df = pd.DataFrame(df_list, columns=df_columns)
#print(df)

sns.set_palette('pastel')

sns.barplot(x=df['Sector'], y=df['1w'], color='#3f616f')
plt.show()

sns.barplot(x=df['Sector'], y=df['1mo'], color='#3f616f')
plt.show()

sns.barplot(x=df['Sector'], y=df['3mo'], color='#3f616f')
plt.show()

sns.barplot(x=df['Sector'], y=df['6mo'], color='#3f616f')
plt.show()

sns.barplot(x=df['Sector'], y=df['1y'], color='#3f616f')
plt.show()
