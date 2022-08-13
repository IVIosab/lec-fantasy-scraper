import time
import os
from dotenv import load_dotenv

load_dotenv()

from selenium import webdriver
from selenium.webdriver.common.by import By

# Global lists

players = {} #Follows the following structure 
# players = {
#   player_name: {
#       days: [],
#       scores: [],
#       items: [{}]
#   } 
# }
#
# days: the days the player played in (1-18 or more)
# scores: the base score of the player on day[index]
# items_score: the scores for all tiems on day[index] 

LEC_LINK = str(os.getenv('LEC_LINK')) #default link to lec superfantasy
EMAIL = str(os.getenv('EMAIL')) #email used to login 
PASSWORD = str(os.getenv('PASSWORD')) #password used to login
CHROME_DRIVER_PATH = str(os.getenv('CHROME_DRIVER_PATH')) #chromedriver path
urls = [
    LEC_LINK+"match/099a602a-d5cb-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/3599f818-d5cb-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/f309382c-d5ca-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/fc3f3782-d5ca-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/46c2254c-d5cb-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/4fd6c0d6-d5cb-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/5c2cff76-d5cc-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/62a9c173-d5cc-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/96cde42e-d5cc-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/0dcabb33-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/21953ef0-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/273e1d3b-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/40a3ec28-ed5e-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/38852cc9-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/4d899817-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/2fe638b2-ec97-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/5de03136-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/65a27aae-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/6cafcd4a-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/3d99b3da-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/42f7f445-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/9887ffb0-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/9f32a376-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/a698fd7d-d5cd-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/55dda676-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/5b48bdf3-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/6130026d-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/6614213a-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/6c0d60f6-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/86bdedcb-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/8cb695b2-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/92c32606-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/98a9bc0a-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/9e424544-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/c1396c43-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/b87f00cd-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/d42ff408-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/ce69dfca-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/c74ed1c2-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/c2516183-ec98-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/dfc9d5a2-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/e4fddc27-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/f6c9f6df-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/f0dcf1f8-d5d0-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/052194e6-d5d1-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/0d182948-d5d1-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/12c5d3ae-d5d1-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/18accb3e-d5d1-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/1ff7f1bc-d5d1-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/08181936-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/142f2733-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/1bb1594c-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/2124b14e-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/27143b20-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/3162b7a2-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/47a61b93-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/3a95aaf2-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/4e42f2a5-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/547320aa-d5d6-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/c934898e-d5d7-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/19bf6b62-ec9a-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/d08ef7c2-d5d7-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/2c61c133-ec9a-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/3fc0011f-ec9a-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/503010bf-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/58b9c175-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/5e353cbf-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/6db2163b-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/650bfabe-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/d4e308b0-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/dbd2c24b-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/e3d4139d-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/eef21fca-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/f934fbff-d5d9-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/be8ae974-d5db-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/d24b097a-d5db-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/cde8b957-d5db-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/c61b1233-d5db-11ec-9e84-06f414ba766d",
    LEC_LINK+"match/d738e2bc-d5db-11ec-9e84-06f414ba766d",
]


def main():
    # Setup
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(LEC_LINK+"login")
    driver.implicitly_wait(5)

    # Login Page
    cookies = driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
    cookies.click() #Accept Cookies 

    login_with_email = driver.find_element(by=By.XPATH,
                                value="/html/body/app-root/app-headerless-layout/div/div/div/app-login/div[2]/div[3]")
    login_with_email.click() #Click Login via Email

    email_input = driver.find_element(by=By.XPATH, value=
    "/html/body/app-root/app-headerless-layout/div/div/div/app-login/div[2]/div[3]/form/div[1]/div/input")
    email_input.send_keys(EMAIL) #Fill Email Field

    password_input = driver.find_element(by=By.XPATH, value=
    "/html/body/app-root/app-headerless-layout/div/div/div/app-login/div[2]/div[3]/form/div[2]/div/input")
    password_input.send_keys(PASSWORD) #Fill Password Field

    login_button = driver.find_element(by=By.XPATH, value=
    "/html/body/app-root/app-headerless-layout/div/div/div/app-login/div[2]/div[3]/form/button")
    login_button.click() #Click Login Button

    time.sleep(2) #Sleep for 2 seconds to allow page to load

    for idx in range(len(urls)):
        day = int((idx+1)/5) + 1 #Each day has 5 matches except the first day which has 4

        #if idx==1 : #TESTING
        #    break
        
        driver.get(urls[idx]) #Get the current match
        driver.implicitly_wait(5) #Wait for at most 5 seconds

        for j in [1, 3]:
            # 1: home team 
            # 3: away team
            for i in range(6):
                # {top, jung, mid, adc, supp, coach}
                x = driver.find_element(by=By.XPATH, value=
                "/html/body/app-root/app-header-laout/div/div/div/app-match/div[1]/div/div[3]/div/div[" + str(
                    j) + "]/div[" + str(i + 1) + "]/div[1]/div/span").get_attribute('innerHTML') 
                y = driver.find_element(by=By.XPATH, value=
                "/html/body/app-root/app-header-laout/div/div/div/app-match/div[1]/div/div[3]/div/div[" + str(
                    j) + "]/div[" + str(i + 1) + "]/div[2]/div/span").get_attribute('innerHTML')
                
                #home team
                player = x #player's name
                score = y #player's score
                
                if j == 3: #away team
                    player = y
                    score = x
    
                
                item_scores = {}

                for k in range(86):#get item scores for current player
                    item = driver.find_element(by=By.XPATH,
                                               value="/html/body/app-root/app-header-laout/div/div/div/app-match/div[2]/div[3]/div[2]/div[2]/div/div[" + str(
                                                   k+1) + "]/span").get_attribute('innerHTML')
                    player_item_score = driver.find_element(by=By.XPATH,
                                                            value="/html/body/app-root/app-header-laout/div/div/div/app-match/div[2]/div[3]/div[" + str(
                                                                j) + "]/div[1]/div[2]/div[" + str(
                                                                k+1) + "]/span").get_attribute('innerHTML')
                    if player_item_score=='-':
                        player_item_score = 0
                    item_scores[item] = player_item_score

                if player in players:
                    players[player]["days"].append(day)
                    players[player]["scores"].append(score)
                    players[player]["items"].append(item_scores)
                else:
                    players[player] = {}
                    players[player]["days"] = [day]
                    players[player]["scores"] = [score]
                    players[player]["items"] = [item_scores]
    
    f = open('test.json', 'a')
    f.write('{\n')
    for player in players:
        f.write('{')
        f.write('\n')

        f.write('\t')
        f.write('"name": ')
        f.write('"'+player+'",')
        f.write('\n')
        
        f.write('\t')
        f.write('"days": [')
        f.write('\n')
        
        for day in range(len(players[player]["days"])):
            f.write('\t\t')
            f.write('"')
            f.write(str(players[player]["days"][day]))
            f.write('"')
            if day == len(players[player]["days"])-1:
                f.write('\n')
                f.write('\t')
                f.write('],')
                f.write('\n')
            else :
                f.write(',')
                f.write('\n')

        f.write('\t')
        f.write('"scores": [')
        f.write('\n')
        
        for day in range(len(players[player]["scores"])):
            f.write('\t\t')
            f.write('"')
            f.write(str(players[player]["scores"][day]))
            f.write('"')
            if day == len(players[player]["scores"])-1:
                f.write('\n')
                f.write('\t')
                f.write('],')
                f.write('\n')
            else :
                f.write(',')
                f.write('\n')

        f.write('\t')
        f.write('"items": [')
        f.write('\n')

        for day in range(len(players[player]["items"])):
            f.write('\t\t')
            f.write('{')
            f.write('\n')
            for key in players[player]["items"][day]:
                f.write('\t\t\t')
                f.write('"')
                f.write(str(key))
                f.write('": "')
                f.write(str(players[player]["items"][day][key]))
                if str(key) == "Wild Spirit":
                    f.write('"')
                else: 
                    f.write('",')
                f.write('\n')
            f.write('\t\t')
            f.write('}')
            if day == len(players[player]["items"])-1:
                f.write('\n')
                f.write('\t')
                f.write(']')
                f.write('\n')
            else :
                f.write(',')
                f.write('\n')
        f.write('},')
        f.write('\n')
    f.write('}')
    f.close()

if __name__ == '__main__':
    main()
