from bs4 import BeautifulSoup
import requests
import csv
import os

response = requests.get("https://humanist.kdl.kcl.ac.uk/")

# print(response.status_code)
# print(response.headers)

soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify())


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

# def get_text_from_link_page(volume_url, link):
#     volume_url = volume_url + link.get('href')
#     volume_response = requests.get(volume_url)
#     if volume_response.status_code == 200:
#         if "htm" or "txt" not in volume_url:
#             volume_soup = BeautifulSoup(volume_response.text, "html.parser")
#             writer.writerow([link.get_text(), volume_soup.get_text()])
#         else:
#             txt_or_htm(volume_url, link)
#     return

# def txt_or_htm(volume_url, link):
#     sub_response = requests.get(volume_url)
#     sub_soup = BeautifulSoup(sub_response.text, "html.parser")
#     sub_links = sub_soup.find_all('a')
#     for sub_link in sub_links:
#         if "txt" or "htm" in sub_link.get('href'):
#             sub_url = volume_url + sub_link.get('href')
#             sub_response = requests.get(sub_url)
#             sub_soup = BeautifulSoup(sub_response.text, "html.parser")
#             writer.writerow([link.get_text(), sub_soup.get_text()])

# with open('humanist_volumes.csv', 'w') as file:
#     writer = csv.writer(file)
#     volume_url = "https://humanist.kdl.kcl.ac.uk"
#     for link in links:
#         if "Archives" in link.get('href'):
#             get_text_from_link_page(volume_url, link)
        

def get_text_from_link_page(volume_url, link):
    volume_url = volume_url + link.get('href')
    sub_response = requests.get(volume_url)
    sub_soup = BeautifulSoup(sub_response.text, "html.parser")
    sub_links = sub_soup.find_all('a')
    if sub_response.status_code == 200:
        for sub_link in sub_links:
            if 'txt' in sub_link.get('href', '') or 'htm' in sub_link.get('href', ''):
                sub_volume_url = volume_url + sub_link.get('href')
                sub_volume_response = requests.get(sub_volume_url)
                sub_volume_soup = BeautifulSoup(sub_volume_response.text, "html.parser")
                writer.writerow([sub_link.get_text(), sub_volume_soup.get_text()])
    volume_soup = BeautifulSoup(sub_response.text, "html.parser")
    writer.writerow([link.get_text(), volume_soup.get_text()])
    return

with open('humanist_volumes.csv', 'w') as file:
    writer = csv.writer(file)
    # Write the headers
    writer.writerow(['Link', 'Volume Text'])
    volume_url = "https://humanist.kdl.kcl.ac.uk"
    for link in links:
        if "Archives" in link.get('href'):
            get_text_from_link_page(volume_url, link)