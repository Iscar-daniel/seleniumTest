from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox(executable_path='D:/Qa/geckodriver.exe')
driver.get('https://popcat.click/')
element=driver.find_element_by_class_name('cat-img')
actionChains=ActionChains(driver)
for i in range(100000):
    actionChains.double_click(element).perform()
driver.close()
