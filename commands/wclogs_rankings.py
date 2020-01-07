from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Player:
    def __init__(self, name, dps, rank, bracket):
        self.name = name
        self.dps = dps
        self.rank = rank
        self.bracket = bracket

    def __str__(self):
        return "{0} | DPS: {1} | Rank: {2} | Bracket Rank: {3}"\
            .format(self.name, self.dps, self.rank, self.bracket)

    def __repr__(self):
        return "{0} | DPS: {1} | Rank: {2} | Bracket Rank: {3}"\
            .format(self.name, self.dps, self.rank, self.bracket)


async def wclogs_rankings(client, message):
    players = []

    print("Loading: %s" % message.content)
    driver = webdriver.PhantomJS()
    driver.get(message.content)
    timeout = 5

    try:
        element_present = EC.presence_of_element_located((By.ID, 'DataTables_Table_0'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        await client.send(message.channel, "Error Loading Log (Timeout)")
        return

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.save_screenshot("yay.png")
    driver.close()
    print(soup.prettify())
    rows = soup.find("table", {"id": "DataTables_Table_0"}).find("tbody").findChildren("tr")

    for row in rows:
        name = row.find("td", {"class": "main-table-name"}).findChild('a').string
        dps = row.find("td", {"class": "rank-per-second primary"}).string
        rank = row.find("td", {"class": "rank-percent"}).string
        bracket = row.findAll("td", {"class": "rank-percent"})[1].string
        players.append(Player(name, float(dps.replace(',', '')), int(rank), int(bracket)))

    players.sort(key = lambda x: -x.dps)

    top_dps_string = "Top DPS\n----------\n"
    for player in players[:3]:
        top_dps_string += str(player) + "\n"

    players.sort(key=lambda x: -x.bracket)
    top_rankings_string = "Top Rankings (by iLvL)\n-----------\n"
    for player in players[:3]:
        top_rankings_string += str(player) + "\n"

    player_string = top_dps_string + "\n" + top_rankings_string

    await client.send(message.channel, player_string)
    return

