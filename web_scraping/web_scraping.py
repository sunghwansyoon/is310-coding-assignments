from bs4 import BeautifulSoup
import requests
import csv

response = requests.get("https://humanist.kdl.kcl.ac.uk/")

print(response.status_code)
print(response.headers)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify())


# soup = BeautifulSoup(open("humanist_homepage.html"), features="html.parser")

# print(soup.prettify())
# # 'bs4' is the package, 'BeautifulSoup' is a class defined inside the package definition

links = soup.find_all('a')

# for link in links:
#     print(link)
#     if 'Volume' in link.get_text():
#         print(link.get('href'))

# for link in links:
#     if "Archives" in link.get('href'):
#         print(link.get_text())
#         volume_url = "https://humanist.kdl.kcl.ac.uk" + link.get('href')
#         volume_response = requests.get(volume_url)
#         volume_soup = BeautifulSoup(volume_response.text, "html.parser")
#         print(volume_soup.get_text())

def get_text_from_link_page(link, volume_url):
    sub_volume_link = volume_url + link
    sub_volume_response = requests.get(sub_volume_link)
    if sub_volume_response.status_code == 200:
        sub_volume_soup = BeautifulSoup(sub_volume_response.text, "html.parser")
        sub_volume_text = sub_volume_soup.get_text()
        return sub_volume_text


with open('humanist_volumes.csv', 'w') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['Link', 'Volume Text'])
    for link in links:
        if "Archives" in link.get('href'):
            volume_url = "https://humanist.kdl.kcl.ac.uk" + link.get('href')
            get_text_from_link_page(link, volume_url)
            volume_response = requests.get(volume_url)
            volume_soup = BeautifulSoup(volume_response.text, "html.parser")
            writer.writerow([link.get_text(), volume_soup.get_text()])