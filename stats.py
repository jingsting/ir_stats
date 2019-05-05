from config import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LOGIN_URL = 'https://members.iracing.com/membersite/login.jsp'
URL = 'https://members.iracing.com/membersite/member/myracers.jsp?drivername='

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(15)

# login
driver.get(LOGIN_URL)
driver.find_element_by_name('username').send_keys(USERNAME)
driver.find_element_by_name('password').send_keys(PASSWORD)
driver.find_element_by_id('submit').click()

# stats
stats = []
with open('list.txt', 'r') as fin:
    lines = fin.readlines()
for line in lines:
    name = line.strip()
    driver.get(URL+name)
    link = driver.find_element_by_link_text(name)
    custid = link.get_attribute('href').split('=',1)[1] 
    link.click()
    saftyno = driver.find_element_by_xpath("//div[@id='roadTabContent']/div[1]/div/div[2]/div[1]")
    irating = driver.find_element_by_xpath("//div[@id='roadTabContent']/div[1]/div/div[2]/div[3]")
    saftylt = saftyno.text.split()[1]
    saftyno = saftyno.text.split()[2]
    irating = irating.text.split()[1]
    print(name, custid, saftylt, saftyno, irating)
    stats.append(f'{name}, {custid}, {saftylt}, {saftyno}, {irating}')

driver.quit()
# driver.close()
with open('stats.txt', 'w+') as out:
    [out.write(f'{row}\n') for row in stats]