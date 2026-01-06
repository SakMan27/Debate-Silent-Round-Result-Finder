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
        cells = team.find_elements(By.XPATH, "td")
        tmp = {}
        team_name = None   # we'll detect it while iterating

        for key, td in zip(keys, cells):
            try:
                value = td.find_element(
                    By.XPATH, './/span[@class="tooltip-trigger"]'
                ).text
            except Exception:
                value = td.text.strip()

            tmp[key] = value

            # <-- put your normalization logic here
            normalized = key.lower().strip()
            if normalized in ("team", "teams", "team name"):
                team_name = value

        # fallback: if no header matched, use first column
        if not team_name:
            team_name = cells[0].text.strip()

        ret["teams"][team_name] = tmp
    
        
    return ret


print(get_standings(input("Enter the link of the tabs (calicotab): "))) # Eg. https://counterfactualhst.calicotab.com/_/tab/current-standings/
