from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



def get_standings(url):
    global driver
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    table = driver.find_element(By.TAG_NAME, 'table')

    # get keys
    header = table.find_elements(By.XPATH, 'thead/tr/th')
    keys = []
    for h in header:
        spans = h.find_elements(By.XPATH, './/span')
        if len(spans) == 0:
            keys.append(h.get_attribute('data-original-title'))
        else:
            keys.append(spans[0].text)
    print(keys)

    ret = {
        'teams': {},
    }

    # get teams
    teams = table.find_elements(By.XPATH, 'tbody/tr')
    for team in teams:
        tmp = {}
        for key, td in zip(keys, team.find_elements(By.XPATH, 'td')):
            tmp[key] = td.find_element(By.XPATH, './/span[@class="tooltip-trigger"]').text
        ret["teams"][tmp["Team"]] = tmp
    
        
    return ret


print(get_standings('https://counterfactualhst.calicotab.com/_/tab/current-standings/'))

