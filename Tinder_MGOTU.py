import urllib
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.action_chains import ActionChains 


def log_n_pass():
    
    # Open the website
    driver.get('https://ies.unitech-mo.ru/user?userid=30072')

    # Select the input button
    input_button = driver.find_element(By.CLASS_NAME, 'log_in_link').click()

    # Find and select the login box
    login_box = driver.find_element(By.NAME, 'login').send_keys('Frolcovbe.21')

    # Find and select the password box
    pass_box = driver.find_element(By.NAME, 'pass').send_keys('Zalupka')

    # Find and select the enter button
    enter_button = driver.find_element(By.ID, 'main_login_link').click()

    #Ждем пока вся страница прогрузится 
    time.sleep(.2)

def parsing(id, i):
    user_id = id
    for i in range(i):
        # Открываю первого пользователя
        user_link = 'https://ies.unitech-mo.ru/user?userid='
        user_link = user_link + str(user_id)
        
        #Открываем профиль на портале
        profile = driver.get(user_link)

        #Ждем пока вся страница прогрузится 
        time.sleep(.2)

        # Открываем фото профиля на весь экран
        circle_photo = driver.find_element(By.CLASS_NAME, 'user_rating').click()


        # Находим img на странице и вытаскиваем его
        user_photo_finder = driver.find_element(By.XPATH, '//*[@id="img_modal"]/img')
        user_photo_link = user_photo_finder.get_attribute('src')

        # Находим ФИО пользователя 
        user_name = driver.find_element(By.XPATH, '//*[@id="user_info_block_wrapper"]/div[1]/div[1]/div[3]').text
        user_sec_name = driver.find_element(By.XPATH, '//*[@id="user_info_block_wrapper"]/div[1]/div[1]/div[2]').text
        user_otch = driver.find_element(By.XPATH, '//*[@id="user_info_block_wrapper"]/div[1]/div[1]/div[4]').text

        # Находим номер группы
        try:
            user_group = driver.find_element(By.XPATH, '//*[@id="user_info_block_wrapper"]/div[1]/div[2]/div[5]').text
        except:
            user_group = 'Неизвестно'

        # Проверка наличие фото в профиле и женского пола, занесение данных в файлы (user_name[-1] == 'а' or 'я')
        if (user_photo_link[25:] != '/files/upload/pages/image/stock_people.png') and (user_otch[-2:] == 'на' or user_otch[-3:-1] == 'зы'):
            with open('bio.txt', 'a', encoding="utf-8") as bio:
                ph = user_photo_link[25:]
                nm = user_name[5:]
                snm = user_sec_name[9:]
                bio_list = 'https://ies.unitech-mo.ru' + ph + ', ' + snm + ', ' + nm + ', ' + 'Группа - ' + user_group[8:] + ', ' + 'id - ' + str(user_id)
                bio.write(str(bio_list) + '\n')
            
            user_id += 1
        else:
            user_id += 1

#Дрочка с настройкой webfriver'а
options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
binary_yandex_driver_file = 'yandexdriver.exe' # path to YandexDriver
driver = webdriver.Chrome(binary_yandex_driver_file, options=options)


log_n_pass()
parsing(30072, 3000)

