from selenium import webdriver
from selenium.webdriver.common.by import By #Для поиска элементов
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
#import os #for path

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	browser = webdriver.Chrome()	
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)	
	
	# говорим Selenium проверять в течение ... секунд, пока кнопка не станет кликабельной
	button_element = WebDriverWait(browser, 30).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	button = browser.find_element(By.CSS_SELECTOR, "button.btn")	
	button.click()		
	
	x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
	x = x_element.text
	
	y = calc(x)
	
	input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
	input_answer.send_keys(y)
	
	# Отправляем заполненную форму
	button = browser.find_element(By.CSS_SELECTOR, "#solve")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()	
			
	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	#time.sleep(3)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()