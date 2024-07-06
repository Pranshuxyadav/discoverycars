import requests
from bs4 import BeautifulSoup

# Define the URL
url = 'https://www.cars24.com/buy-used-car/?f=bodyType%3Ain%3Asuv&f=year%3Abw%3A2021%2C2021&sort=bestmatch&serveWarrantyCount=true&gaId=1057448734.1719685701&listingSource=TabFilter&storeCityId=2'

# Make a request to the URL
response = requests.get(url)
html_text = response.text

# Parse the HTML content
soup = BeautifulSoup(html_text, 'lxml')

# Find the container holding the car listings
car_listings = soup.find_all('a', class_='IIJDn')

# Debugging: Print the number of car listings found
print(f"Number of car listings found: {len(car_listings)}")

# Loop through each car listing to extract image URLs
image_urls = []
for listing in car_listings:
    main_div = listing.find('div', class_='RPKrE')
    if main_div:
        # Debugging: Print to confirm we found the main_div
        print("Found main_div")

        img_span = main_div.find('span', class_='lazy-load-image-background')
        if img_span:
            # Debugging: Print to confirm we found the img_span
            print("Found img_span")

            img_tag = img_span.find('img')
            if img_tag:
                # Debugging: Print the entire img_tag
                print(f"Found img_tag: {img_tag}")

                # Debugging: Print the attributes of img_tag
                print(f"Attributes: {img_tag.attrs}")

                # Check for src or data-src attribute and add to image_urls
                if 'src' in img_tag.attrs:
                    image_urls.append(img_tag['src'])
                elif 'data-src' in img_tag.attrs:
                    image_urls.append(img_tag['data-src'])

# Print the extracted image URLs
for img_url in image_urls:
    print(img_url)

# Debugging: Print to confirm the completion of extraction process
print("Image URL extraction complete")
