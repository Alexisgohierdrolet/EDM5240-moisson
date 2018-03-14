# coding : utf-8

import csv
import requests
from bs4 import BeautifulSoup

entetes = {
	"User-Agent":"Alexis Gohier-Drolet, requête envoyée pour un cours de data",
	"From":"alexis_gohier@hotmail.com"
}

fichier = "newScientist.csv"

for n in range(1,493):
	url = "https://www.newscientist.com/section/news/page/{}/".format(n)
	print(url)

	contenu = requests.get(url, headers=entetes)
	page = BeautifulSoup(contenu.text, "html.parser")
	# print(page)

	urlArticles = page.find_all("h2", class_="entry-title")
	# print(page.find("h2",class_="entry-title"))
	# print(urlArticles)

	for urlArticle in urlArticles:
		scientist = []
		try:
			url2 = urlArticle.a["href"]
			#print(url2)
			url2 = "https://www.newscientist.com" + url2
			print(url2)
			scientist.append(url2)

			contenu2 = requests.get(url2)
			page2 = BeautifulSoup(contenu2.text, "html.parser")

			titre = page2.title
			#print(titre)
			scientist.append(titre)
			# print(scientist)

			#bob = open(fichier, "a")
			#eponge = csv.writer(bob)
			#eponge.writerow(scientist)

		except:
			print("Rien")



