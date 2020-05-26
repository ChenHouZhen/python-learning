from selenium import webdriver

# 执行前需要进入 Chrome 的安装目录执行：chrome.exe --remote-debugging-port=9222

URL_BAIDU = "https://www.baidu.com"

if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(URL_BAIDU)