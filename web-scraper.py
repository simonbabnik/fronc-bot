from bs4 import BeautifulSoup
import requests

url = "https://www.ehrana.si/pri-froncu/tedenske-malice-10h-14h"

page = requests.get(url)
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

ponudbaHTML = soup.find(id="rest-hrana")

ponudbe_divs = ponudbaHTML.find_all(class_="rest-hrana")

sestavljen_message = ""

for div in ponudbe_divs:
    malica = div.find(class_="rest-hrana-ime").get_text().strip()

    if malica not in ["Ponedeljek", "Torek", "Sreda", "Četrtek", "Petek", "Sobota", "Nedelja", "MALICA 1."]:

        hrana = div.find(class_="rest-hrana-opis").get_text().strip()
        cena = div.find(class_="rest-hrana-cena").get_text().strip()

    else:
        hrana = ""
        cena = ""

    if malica.strip() in ["Ponedeljek", "Torek", "Sreda", "Četrtek", "Petek", "Sobota", "Nedelja"]:
        # print("\n")
        # print("----------------------------------------------------------------------")
        sestavljen_message += ("----------------------------------" + malica + "------------------------------------")
        sestavljen_message += "\n"

    else:
        # print(malica)
        sestavljen_message += malica
        sestavljen_message += "\n"

    if hrana != "" and hrana != " ":
        # print(hrana + " " + cena)
        sestavljen_message += (hrana + " " + cena)
        sestavljen_message += "\n"
        sestavljen_message += "\n"

# print(message)
# print(len(message))
