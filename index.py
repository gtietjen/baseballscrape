import urllib
import csv
from bs4 import BeautifulSoup

url = 'http://www.baseball-reference.com/players/c/cespeyo01.shtml'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

tables = soup.findAll("table", { "class" : "stats_table" })
print len(tables) #4

with open("stats.csv", "a") as f:
	writeFile = csv.writer(f)
	for table in tables:
		for row in table.findAll("tr"):
			for col in row.findAll("td"):
				print col.getText()
        		writeFile.writerow([tables])