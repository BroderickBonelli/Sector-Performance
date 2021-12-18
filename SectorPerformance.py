import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sectors = ['XLK', 'XLC', 'XLY', 'XLP', 'XLE', 'XLF', 'XLV', 'XLI', 'XLB', 'XLRE', 'XLU', 'SPY']

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

df_columns = ['Sector', '1w % Change', '1mo % Change', '3mo % Change', '6mo', '1y']
df = pd.DataFrame(df_list, columns=df_columns)
#print(df)

sns.set_palette('pastel')

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(4.5, 9))
#fig.suptitle("Sector Performance")

sns.barplot(ax=ax1, x=df['Sector'], y=df['1w % Change'], color='#3f616f')
ax1.set_title('1w')
ax1.axhline(df.loc[11, '1w % Change'], color='#000000')


sns.barplot(ax=ax2, x=df['Sector'], y=df['1mo % Change'], color='#3f616f')
ax2.set_title('1mo')
ax2.axhline(df.loc[11, '1mo % Change'], color='#000000')

sns.barplot(ax=ax3, x=df['Sector'], y=df['3mo % Change'], color='#3f616f')
ax3.set_title('3mo')
ax3.axhline(df.loc[11, '3mo % Change'], color='#000000')

plt.tight_layout()
plt.show()

#sns.barplot(x=df['Sector'], y=df['6mo'], color='#3f616f')
#plt.show()

#sns.barplot(x=df['Sector'], y=df['1y'], color='#3f616f')
#plt.show()


