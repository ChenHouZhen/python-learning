from selenium import webdriver


url = "https://www.baidu.com"

if __name__ == '__main__':
    # # 初始化浏览器
    chrome_options = webdriver.Chrome()
    driver = webdriver.Chrome()
    driver.get(url)