import os
import requests
from bs4 import BeautifulSoup
import csv

BASE = "https://treeseeds.ca"
URL = "https://treeseeds.ca/collections/tree-seeds"
PAGE = "?page="

def collect_pages():
	pages = []

	for page_num in range(1, 7):
		request = requests.get(URL + PAGE + str(page_num))

		soup = BeautifulSoup(request.text, features="html.parser")

		for a in soup.find_all('a', href=True):
			link = a['href']
			if link.startswith("/collections/tree-seeds/products/tree-seed-"):
				pages.append(BASE + link)

	return pages


def collect_germination_info(page_url):
	request = requests.get(page_url)
	soup = BeautifulSoup(request.text, features="html.parser")

	name = page_url.split(BASE + "/collections/tree-seeds/products/tree-seed-")[1].replace('-', ' ').capitalize()
	price = float(soup.find("span", itemprop="price").contents[0].strip().replace("$", ''))
	desc = soup.find("div", itemprop="description").contents
	latin_name = str(desc[1]).split('(')[1].split(')')[0]
	description = str(desc[3]) \
		.replace("<p>", '') \
		.replace("</p>", '') \
		.replace("<em>", '') \
		.replace("</em>", '') \
		.replace("</br>", '')

	germination = "could not find info"
	germination_days = -1
	for group in desc:
		if "germination:" in str(group).lower():
			germination = str(group).replace("<p>", '').replace("</p>", '')
			split_germ = germination.lower().replace('.', '').replace(',', '').split()
			try:
				if 'days' in split_germ:
					germination_days = int(split_germ[split_germ.index('days') - 1].split('-')[0])
				if 'weeks' in split_germ:
					germination_days = int(split_germ[split_germ.index('weeks') - 1].split('-')[0]) * 7
			except:
				germination_days = -1

			break

	blob = {
		"name": name,
		"url": page_url,
		"price": price,
		"latin_name": latin_name,
		"description": description,
		"germination_info": germination,
		"germination_days": germination_days
	}

	return blob


def write_data():
	with open('tree-data.csv', 'w') as csvfile:
		fieldnames = ['name', 'url', 'price', 'latin_name', 'description', 'germination_info', 'germination_days']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for page_url in collect_pages():
			info = collect_germination_info(page_url)
			writer.writerow(info)
		

write_data()
