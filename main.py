import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Global lists
urls = [
    "https://l...content-available-to-author-only...l.com/match/099a602a-d5cb-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/3599f818-d5cb-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/f309382c-d5ca-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/fc3f3782-d5ca-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/46c2254c-d5cb-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/4fd6c0d6-d5cb-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/5c2cff76-d5cc-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/62a9c173-d5cc-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/96cde42e-d5cc-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/0dcabb33-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/21953ef0-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/273e1d3b-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/40a3ec28-ed5e-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/38852cc9-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/4d899817-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/2fe638b2-ec97-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/5de03136-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/65a27aae-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/6cafcd4a-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/3d99b3da-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/42f7f445-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/9887ffb0-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/9f32a376-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/a698fd7d-d5cd-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/55dda676-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/5b48bdf3-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/6130026d-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/6614213a-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/6c0d60f6-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/86bdedcb-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/8cb695b2-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/92c32606-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/98a9bc0a-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/9e424544-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/c1396c43-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/b87f00cd-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/d42ff408-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/ce69dfca-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/c74ed1c2-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/c2516183-ec98-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/dfc9d5a2-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/e4fddc27-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/f6c9f6df-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/f0dcf1f8-d5d0-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/052194e6-d5d1-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/0d182948-d5d1-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/12c5d3ae-d5d1-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/18accb3e-d5d1-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/1ff7f1bc-d5d1-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/08181936-d5d6-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/142f2733-d5d6-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/1bb1594c-d5d6-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/2124b14e-d5d6-11ec-9e84-06f414ba766d",
    "https://l...content-available-to-author-only...l.com/match/27143b20-d5d6-11ec-9e84-06f414ba766d"
]
players_scores = {}
players_matches = {}
players_matches_items_scores = {}

email = "mosab.f.r@gmail.com"
pwrd = "mosab8264436"


def main():
    # Setup
    os.environ['PATH'] += r"C:/Users/Mosab Mohamed/Downloads/SeleniumDrivers"
    driver = webdriver.Chrome()
    driver.get("https://l...content-available-to-author-only...l.com/login")
    driver.implicitly_wait(5)

    # Login Page
    cookies = driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
    cookies.click()
    login = driver.find_element(by=By.XPATH,
                                value="/html/body/app-root/app-headerless-layout/div/div/div/app-login/div[2]/div[3]")
    login.click()
    inmail = driver.find_element(by=By.XPATH, value=
    "/html/body/app-root/app-headerless-layout/div/div/div/app-login/div[2]/div[3]/form/div[1]/div/input")
    inmail.send_keys(email)
    inpwrd = driver.find_element(by=By.XPATH, value=
    "/html/body/app-root/app-headerless-layout/div/div/div/app-login/div[2]/div[3]/form/div[2]/div/input")
    inpwrd.send_keys(pwrd)
    submit = driver.find_element(by=By.XPATH, value=
    "/html/body/app-root/app-headerless-layout/div/div/div/app-login/div[2]/div[3]/form/button")
    submit.click()

    time.sleep(2)

    for idx in range(len(urls)):
        driver.get(urls[idx])
        driver.implicitly_wait(5)
        for j in [1, 3]:
            for i in range(6):
                x = driver.find_element(by=By.XPATH, value=
                "/html/body/app-root/app-header-laout/div/div/div/app-match/div[1]/div/div[3]/div/div[" + str(
                    j) + "]/div[" + str(i + 1) + "]/div[1]/div/span").get_attribute('innerHTML')
                y = driver.find_element(by=By.XPATH, value=
                "/html/body/app-root/app-header-laout/div/div/div/app-match/div[1]/div/div[3]/div/div[" + str(
                    j) + "]/div[" + str(i + 1) + "]/div[2]/div/span").get_attribute('innerHTML')
                player = x
                score = y
                if j == 3:
                    player = y
                    score = x
                if player in players_scores:
                    players_scores[player] = int(players_scores[player]) + int(score)
                    players_matches[player] = int(players_matches[player]) + 1
                else:
                    players_scores[player] = int(score)
                    players_matches[player] = 1
                if not (player in players_matches_items_scores):
                    players_matches_items_scores[player]={}
                players_matches_items_scores[player][players_matches[player]] = {}
                for k in range(86):
                    item = driver.find_element(by=By.XPATH,
                                               value="/html/body/app-root/app-header-laout/div/div/div/app-match/div[2]/div[3]/div[2]/div[2]/div/div[" + str(
                                                   k+1) + "]/span").get_attribute('innerHTML')
                    player_item_score = driver.find_element(by=By.XPATH,
                                                            value="/html/body/app-root/app-header-laout/div/div/div/app-match/div[2]/div[3]/div[" + str(
                                                                j) + "]/div[1]/div[2]/div[" + str(
                                                                k+1) + "]/span").get_attribute('innerHTML')
                    if player_item_score=='-':
                        player_item_score = 0
                    players_matches_items_scores[player][players_matches[player]][item] = int(player_item_score)

    sorted_values = sorted(players_scores.values(), reverse=True)
    sorted_dict = {}
    visited = {}
    for i in sorted_values:
        for k in players_scores.keys():
            if k in visited:
                continue
            if players_scores[k] == i:
                visited[k] = 1
                sorted_dict[k] = players_scores[k]
                break
    for key, value in sorted_dict.items():
        print(key, ": ", value)
    for key, value in players_matches_items_scores.items():
        print(key)
        for day, scores in value.items():
            print(day,": ",scores)

if __name__ == '__main__':
    main()
