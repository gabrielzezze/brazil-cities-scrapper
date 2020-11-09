from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import requests
import urllib.request
import io
import os
from PIL import Image
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from .index import Scrapper


class GoogleImagesScrapper(Scrapper):
    def __init__(self, driver_path: str, raw_images_folder_path: str):
        super().__init__()
        self.DRIVE_PATH = driver_path
        self.RAW_IMAGES_FOLDER_PATH = raw_images_folder_path

        if not os.path.exists(raw_images_folder_path):
            os.mkdir(raw_images_folder_path)
    
    def _get_google_thumbnail_element(self, webdriver, index):
        image_thumbnail = WebDriverWait(webdriver,8).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.wXeWr'))
        )[index]

        if image_thumbnail is None:
            return None

        image_thumbnail.click()
        return image_thumbnail
    
    def _get_image_bytes_by_image_element_xpath(self, wd, xpath):
        img_element = wd.find_element_by_xpath(xpath)
        url = img_element.get_attribute('src')
        start = time.time()
        actual = start
        
        while (actual - start <= 8) and ('http' not in url):
            img_element = wd.find_element_by_xpath(xpath)
            url = img_element.get_attribute('src')

        if (url is not None) and ('http' in url):
            try:
                img_bytes = requests.get(url).content
                return img_bytes
            except Exception as e:
                return None

        return None
    
    def _save_image_bytes_to_file(self, image_bytes, file_name):
        image_file = io.BytesIO(image_bytes)
        try:
            image = Image.open(image_file).convert('RGB')
            with open(os.path.join(self.RAW_IMAGES_FOLDER_PATH, file_name), 'wb') as file:
                image.save(file, "JPEG", quality=100)
                return file_name
        except:
            return None
    
    def __call__(self, query, file_name, index=0, extra_queries=''):
        wd = webdriver.Chrome(executable_path=self.DRIVE_PATH)
        chrome_options = Options()
        chrome_options.add_argument("--incognito")

        wd.get(
            f'https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&{extra_queries}'
        )
        
        try:
            image = None
            image_bytes = None
            start = time.time()
            actual = start

            while (image_bytes is None) and (actual - start <= 16):
                self._get_google_thumbnail_element(wd, index)
                image_bytes = self._get_image_bytes_by_image_element_xpath(wd, '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img')
                actual = time.time()
                index += 1
            
            if image_bytes is None:
                raise TimeoutException
            
            saved_file_name = self._save_image_bytes_to_file(image_bytes, file_name)
            
            saved_file_path = f'{self.RAW_IMAGES_FOLDER_PATH}/{saved_file_name}'
            file_exists = self.does_file_exist(saved_file_path)
            if file_exists:
                print(f'[SUCCESS] Image available @ {saved_file_path}')
            else:
                print('[Error] File was not saved')
        except TimeoutException or Exception as e:
            print('[ Error ] Timeout')
        
        wd.quit()

            