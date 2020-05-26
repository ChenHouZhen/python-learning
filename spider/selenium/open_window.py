from selenium import webdriver


URL_BAIDU = "https://www.baidu.com"

if __name__ == '__main__':
    # # 初始化浏览器
    driver = webdriver.Chrome()
    driver.get(URL_BAIDU)
