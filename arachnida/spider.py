import os
import requests # to fetch the HTML content of a webpage
from bs4 import BeautifulSoup # to parse the HTML content and extract image URLs
import argparse # handle command-line arguments such as -r, -l, and -p.
from urllib.parse import urljoin, urlparse # to handle file paths and download the images into the specified directory

def download_image(image_url, save_path):
	"""Downloads an image from a URL and saves it to the specified path."""
	try:
		img_data = requests.get(image_url).content
		img_name = os.path.basename(urlparse(image_url).path)
		with open(os.path.join(save_path, img_name), 'wb') as f:
			f.write(img_data)
		print(f"Downloaded: {image_url}")
	except Exception as e:
		print(f"Failed to download {image_url}: {str(e)}")

def is_image_url(url):
	"""Checks if a URL ends with a supported image extension."""
	return url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))

def spider(url, visited_urls, save_path, recursive=False, max_depth=5, current_depth=0):
	"""Recursively downloads images from a URL."""
	if current_depth > max_depth:
		return

	headers = {
		# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
	}

	if url in visited_urls:
		return
	else:
		visited_urls.add(url)

	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()
	except requests.RequestException as e:
		print(f"Error fetching {url}: {str(e)}")
		return
	soup = BeautifulSoup(response.text, 'html.parser')

	# print(response.text[:1000])
	print(f"Downloading from: {url}")
	img_tags = soup.find_all('img')
	for img in img_tags:
		img_url = img.get('src')
		print(f"Found image: {img_url}")
		if img_url and is_image_url(img_url):
			img_url = urljoin(url, img_url)
			download_image(img_url, save_path)


	if recursive:
		a_tags = soup.find_all('a', href=True)
		for a in a_tags:
			next_url = urljoin(url, a['href'])
			if urlparse(next_url).netloc == urlparse(url).netloc:  # Stay on the same domain
				spider(next_url, visited_urls ,save_path, recursive=True, max_depth=max_depth, current_depth=current_depth + 1)

def main():
	parser = argparse.ArgumentParser(description="Spider program to download images from a website.")
	parser.add_argument('URL', help="The URL of the website to spider")
	parser.add_argument('-r', action='store_true', help="Recursively download images")
	parser.add_argument('-l', type=int, default=5, help="Maximum depth level for recursion (default: 5)")
	parser.add_argument('-p', default='./data/', help="Path to save the downloaded files (default: ./data/)")

	args = parser.parse_args()

	save_path = args.p
	if not os.path.exists(save_path):
		os.makedirs(save_path)

	visited_urls = set()

	spider(args.URL, visited_urls, save_path, recursive=args.r, max_depth=args.l)

if __name__ == "__main__":
	main()
