from selenium import webdriver

driver = webdriver.Chrome()  # 用于启动浏览器
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()

driver.quit()

# 验证浏览器
# driver = webdriver.Chrome()  # 用于启动浏览器
# driver = webdriver.Firefox()  # 用于启动浏览器
# driver = webdriver.Opera()  # 用于启动浏览器
