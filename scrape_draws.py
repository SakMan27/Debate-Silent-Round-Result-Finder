from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



def get_draws(url):
    global driver
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    table = driver.find_element(By.TAG_NAME, 'table')
    rooms = table.find_elements(By.XPATH, 'tbody/tr')

    ret = {
        'rooms': []
    }

    for room in rooms:
        tmp = []
        for team in room.find_elements(By.XPATH, 'td[contains(@class, "team-name")]'):
            tmp.append(team.find_element(By.XPATH, './/span[@class="tooltip-trigger"]').text)
        ret['rooms'].append(tmp)
        
    return ret


print(get_draws('https://counterfactualhst.calicotab.com/_/draw/'))