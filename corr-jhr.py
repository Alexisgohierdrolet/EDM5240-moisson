### BONJOUR, ICI Jean-Hugues ###
### Comme toujours, mes notes et corrections sont précédées de trois dièses #### coding : utf-8

import csv
import requests
from bs4 import BeautifulSoup

entetes = {
	"User-Agent":"Alexis Gohier-Drolet, requête envoyée pour un cours de data",
	"From":"alexis_gohier@hotmail.com"
}

fichier = "newScientist.csv"

#NewScientist est un média scientifique anglophone. Je voulais voir si 
#je pouvais facilement voir les nouvelles avec la date, l'auteur, les
#références, et possiblement le premier paragraphe. Je n'ai pas réussi
#cette dernière étape.

for n in range(1,493):
	url = "https://www.newscientist.com/section/news/page/{}/".format(n)
	#print(url)

	contenu = requests.get(url, headers=entetes)
	page = BeautifulSoup(contenu.text, "html.parser")
	#print(page)

	urlArticles = page.find_all("h2", class_="entry-title")
	#print(urlArticles)

	for urlArticle in urlArticles:
		scientist = []
		try:
			url2 = urlArticle.a["href"]
			# print(url2)
			scientist.append(url2)

			contenu2 = requests.get(url2)
			page2 = BeautifulSoup(contenu2.text, "html.parser")

			titre = page2.find("h1", class_="article-title").text
			# print(titre)
			scientist.append(titre)

			auteur = page2.find("span", class_="author").text
			# print(auteur)
			scientist.append(auteur)

### Tu souhaitais recueillir le premier paragraphe
### Est-ce le chapeau?
			chapo = page2.find("p", class_="strap").text.strip()
			scientist.append(chapo)

			theme = page2.find("section", class_="article-section").text
			# print(theme)

### Ici, il aurait été bien de séparer le «thème», ou la «section», de la date
			themeDate = theme.split("\n")
			# print(themeDate)
			section = themeDate[1].strip()
			date = themeDate[2].strip()
			scientist.append(section)
			scientist.append(date)

### Tu souhaitais recueillir le premier paragraphe
### Voici comment je m'y prendrais

			parag1 = page2.find("span", class_="author").find_next("p").text.strip()
			scientist.append(parag1)

			print(scientist)

			bob = open(fichier, "a")
			eponge = csv.writer(bob)
			eponge.writerow(scientist)

		except:
			print("Rien")

#J'ai trouvé moins d'informations que j'aurais voulu. Je n'ai pas réussi à
#extraire les références en fin d'article, avec le code DOI des recherches 
#mentionnées

### Pour cela, je crains qu'il faille être abonné...
