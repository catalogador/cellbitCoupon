
from selenium import webdriver
import itertools
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Edge()
driver.get("https://www.lolja.com.br/checkout/v3/start/564060841/3c7ddc554290e40aa07cc12d644c4398efcdaa68?from_store=1")


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/div[2]/div[3]/div[2]/div/div/div[2]/div/div/div/div'))).click()
      
chances ={'1':['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], '2':['0','1','2','3','4','5','6','7','8','9']}
for combo in itertools.product(*[chances[k] for k in sorted(chances.keys())]):
    
    letra=combo[0]
    numero=combo[1]
    codigo=letra+"kajsdkl"+numero
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'coupon'))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'coupon'))).send_keys(codigo)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID,'coupon'))).send_keys(Keys.ENTER)