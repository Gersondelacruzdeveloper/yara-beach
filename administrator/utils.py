from checkout.models import ExcursionOrder
from excursions.models import Excursions
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from django.conf import settings
import time
import datetime
import random


def filter_category(category):
    all_excursion_orders = ExcursionOrder.objects.all()
    # fileter tomorow excursio
    tomorow_excursion_bookings = all_excursion_orders.filter(excursion_date=datetime.date.today() + timedelta(days=1))
    category_bookings = []
    Santo_domingo = Excursions.objects.filter(category__category=category)
    # print('Santo_domingo', Santo_domingo[0].id)
    for i in Santo_domingo:
        category_bookings += tomorow_excursion_bookings.filter(excursion_id=i.id)
    return category_bookings

def simulate_human_behavior(contact_names, messages):
    driver = None  # Initialize the driver variable outside the try block

    try:
        driver_path = './chromedriver_mac_arm64/chromedriver'
        driver = webdriver.Chrome(executable_path=driver_path)

        driver.get('https://web.whatsapp.com/')
        time.sleep(int(settings.TIME_WATING_FOR_BARCODE))
      

        for contact_name in contact_names:
            for message in messages:
                try:
                    search_box_xpath = '//div[@title="Search input textbox" and @role="textbox"]'
                    search_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, search_box_xpath))
                    )
                    search_box.clear()  # Clear the search box
                    
                    search_box.send_keys(contact_name)
                except TimeoutException:
                    print("Timeout: Search box not found.")
                    continue

                time.sleep(2)

                search_box.send_keys(Keys.RETURN)
                time.sleep(2)

                try:
                    message_box_xpath = '//div[@title="Type a message" and @role="textbox"]'
                    message_box = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, message_box_xpath))
                    )

                    simulate_typing_speed(message, message_box)

                    send_button_xpath = '//span[@data-icon="send"]'
                    send_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, send_button_xpath))
                    )
                    send_button.click()

                except TimeoutException:
                    print("Timeout: Message box or Send button not found.")
                    continue

                time.sleep(random.uniform(5, 10))

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
    finally:
        if driver:
            driver.quit()


def simulate_typing_speed(message, message_box):
    for char in message:
        message_box.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))


# get all the excursions related to that id
def get_excursions_from_id(id):
    arrays = []
    for order in id:
        excursions = Excursions.objects.get(id=order.excursion_id)
        arrays.append(excursions)
    return arrays

    
def update_image(excursion_bookings):
     for order in excursion_bookings:
        excursions = Excursions.objects.get(id=order.excursion_id)
        if order.image != excursions.main_image.url:
            order.image = excursions.main_image.url
            order.save()