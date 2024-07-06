import requests
from bs4 import BeautifulSoup
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_cars_droom():
    url = 'https://droom.in/cars'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        logging.info('Sending request to the website...')
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        logging.info('Parsing the page content...')
        soup = BeautifulSoup(response.content, 'html.parser')

        cars_grid = soup.find_all('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-4')
        cars_list = []

        logging.info('Extracting car details...')
        for car_grid in cars_grid:
            car_info = car_grid.find('div', class_='jss236')
            if car_info:
                car_title_elem = car_info.find('h3', class_='MuiTypography-root jss237 MuiTypography-body1')
                car_details_elems = car_info.find_all('div', class_='jss242')
                car_price_elem = car_info.find('div', class_='MuiGrid-root MuiGrid-container')
                car_link_elem = car_info.find('a', href=True)

                car_title = car_title_elem.text.strip() if car_title_elem else 'No title available'
                car_details = ' '.join([elem.text.strip() for elem in car_details_elems]) if car_details_elems else 'No details available'
                car_price = car_price_elem.text.strip() if car_price_elem else 'No price available'
                car_link = car_link_elem['href'] if car_link_elem else 'No details available'
                car_link = 'https://droom.in' + car_link if not car_link.startswith('http') else car_link

                car_dict = {
                    'title': car_title,
                    'details': car_details,
                    'price': car_price,
                    'link': car_link,
                    'image_url': 'No image available'
                }
                cars_list.append(car_dict)

        # Extract images separately
        car_pictures = soup.find_all('div', class_='RPKrE')
        for car_picture in car_pictures:
            parent_anchor = car_picture.find_parent('a', class_='MuiTypography-root MuiLink-root MuiLink-underlineHover MuiTypography-colorPrimary')
            if parent_anchor:
                car_image_tag = car_picture.find('img')
                car_image_url = car_image_tag['src'] if car_image_tag else 'No image available'
                for car in cars_list:
                    if car['link'] == parent_anchor['href']:
                        car['image_url'] = car_image_url
                        break
        
        logging.info('Updating data.json with new data...')
        update_json_file(cars_list)

    except requests.RequestException as e:
        logging.error(f'An error occurred: {e}')

def update_json_file(new_data):
    try:
        with open('data.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data['Sheet1'].extend(new_data)
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump({'Sheet1': new_data}, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    find_cars_droom()