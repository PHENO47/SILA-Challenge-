from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from .utils import random_user_agent, random_delay

def start_driver():

    options = Options()

    options.add_argument(f"user-agent={random_user_agent()}")
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    return driver


def get_page(url):

    driver = start_driver()

    driver.get(url)

    random_delay()

    html = driver.page_source

    driver.quit()

    return html