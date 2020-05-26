from selenium import webdriver
import os


URL_BAIDU = "https://www.baidu.com"

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    # 无界面模式
    chrome_options.add_argument('--headless')
    # 设置浏览器大小，这个可以截图全一点
    chrome_options.add_argument("window-size=1280,1024")
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(URL_BAIDU)
    driver.get_screenshot_as_file(os.getcwd()+"/baidu.png")
    driver.close()