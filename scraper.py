import json
import logging
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_cars_cars24mumbai():
    url = 'https://www.cars24.com/buy-used-cars-mumbai/'
    
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    service = Service("C:\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    try:
        logging.info('Waiting for the page to load...')
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'RPKrE')))
        time.sleep(15)

        logging.info('Scrolling the page...')
        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(3):
            body.send_keys(Keys.END)
            time.sleep(10)

        logging.info('Parsing the page source...')
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        cars_info = soup.find_all('a', class_='IIJDn')
        cars_list = []

        logging.info('Extracting car details...')
        for car_info in cars_info:
            car_title = car_info.find('h3', class_='_11dVb').text.strip() if car_info.find('h3', class_='_11dVb') else 'No title available'
            car_details = ' '.join([li.text.strip() for li in car_info.find('ul', class_='_3J2G-').find_all('li')]) if car_info.find('ul', class_='_3J2G-') else 'No details available'
            car_price = car_info.find('div', class_='_2KyOK').text.strip() if car_info.find('div', class_='_2KyOK') else 'No price available'
            more_info = car_info['href'] if 'href' in car_info.attrs else 'No details available'
            
            car_dict = {
                'title': car_title,
                'details': car_details,
                'price': car_price,
                'link': more_info,
                'image_url': 'No image available'
            }
            cars_list.append(car_dict)

        logging.info('Extracting images...')
        car_pictures = soup.find_all('div', class_='RPKrE')
        for car_picture in car_pictures:
            parent_anchor = car_picture.find_parent('a', class_='IIJDn')
            if parent_anchor:
                car_image_tag = car_picture.find('img')
                car_image_url = car_image_tag['src'] if car_image_tag else 'No image available'
                for car in cars_list:
                    if car['link'] == parent_anchor['href']:
                        car['image_url'] = car_image_url
                        break

        logging.info('Updating data.json with new data...')
        update_json_file(cars_list)

    except Exception as e:
        logging.error(f'An error occurred: {e}')
    
    finally:
        driver.quit()


def find_cars_cars24delhi():
    url = 'https://www.cars24.com/buy-used-car/?sort=bestmatch&serveWarrantyCount=true&gaId=1476729337.1720017156&storeCityId=2'
    
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    options.add_argument('--headless')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    service = Service("C:\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    try:
        logging.info('Waiting for the page to load...')
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'RPKrE')))
        time.sleep(15)

        logging.info('Scrolling the page...')
        body = driver.find_element(By.TAG_NAME, 'body')
        for _ in range(3):
            body.send_keys(Keys.END)
            time.sleep(10)

        logging.info('Parsing the page source...')
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        cars_info = soup.find_all('a', class_='IIJDn')
        cars_list = []

        logging.info('Extracting car details...')
        for car_info in cars_info:
            car_title = car_info.find('h3', class_='_11dVb').text.strip() if car_info.find('h3', class_='_11dVb') else 'No title available'
            car_details = ' '.join([li.text.strip() for li in car_info.find('ul', class_='_3J2G-').find_all('li')]) if car_info.find('ul', class_='_3J2G-') else 'No details available'
            car_price = car_info.find('div', class_='_2KyOK').text.strip() if car_info.find('div', class_='_2KyOK') else 'No price available'
            more_info = car_info['href'] if 'href' in car_info.attrs else 'No details available'
            
            car_dict = {
                'title': car_title,
                'details': car_details,
                'price': car_price,
                'link': more_info,
                'image_url': 'No image available'
            }
            cars_list.append(car_dict)

        logging.info('Extracting images...')
        car_pictures = soup.find_all('div', class_='RPKrE')
        for car_picture in car_pictures:
            parent_anchor = car_picture.find_parent('a', class_='IIJDn')
            if parent_anchor:
                car_image_tag = car_picture.find('img')
                car_image_url = car_image_tag['src'] if car_image_tag else 'No image available'
                for car in cars_list:
                    if car['link'] == parent_anchor['href']:
                        car['image_url'] = car_image_url
                        break

        logging.info('Updating data.json with new data...')
        update_json_file(cars_list)

    except Exception as e:
        logging.error(f'An error occurred: {e}')
    
    finally:
        driver.quit() 





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
        car_pictures = soup.find_all('div', class_='MuiBox-root jss214')
        for car_picture in car_pictures:
            parent_anchor = car_picture.find_parent('a', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-4')
            if parent_anchor:
                car_image_tag = car_picture.find_all('img')
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
    find_cars_cars24mumbai()
    find_cars_cars24delhi()
    find_cars_droom()
