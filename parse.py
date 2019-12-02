import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import lxml
import json

URL = "https://www.data.go.kr/search/index.do?index=OPENAPI&query=&currentPage=1&countPerPage=4000&sortType=VIEW_COUNT"

req = requests.get(URL)

soup = BeautifulSoup(req.content, 'html.parser')

title_list = soup.find_all('div',class_='data-title')

api_list = []

for i in title_list:

    api_list.append(i.find('a')['href'])


driver = webdriver.Chrome('./chromedriver')

api_process_data = dict()
api_process_data = list()


count = 0
try:
    for api in api_list:
        res = driver.get("https://www.data.go.kr" + api)

        driver.implicitly_wait(2)
        try:
            result = driver.find_element(By.XPATH, '//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[3]/div[1]/table/tbody/tr[1]/td')
            title = driver.find_element(By.XPATH, '//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[3]/div[1]/table/thead/tr/th')
        except:
            try:
                result = driver.find_element(By.XPATH, '//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[4]/div[1]/table/tbody/tr[1]/td')
                title = driver.find_element(By.XPATH, '//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[4]/div[1]/table/thead/tr/th')
                raise ZeroDivisionError
                try:
                    result = driver.find_element(By.XPATH, '//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[5]/div[1]/table/tbody/tr[1]/td')
                    title = driver.find_element(By.XPATH, '//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[5]/div[1]/table/thead/tr/th')
                    raise ZeroDivisionError
                    try:
                        result = driver.find_element(By.XPATH, '//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td')
                        title = driver.find_element(By.XPATH, '//*[@id="sub-main"]/div[4]/div/div[2]/div[2]/div[2]/div[2]/div[1]/table/thead/tr/th')
                        raise ZeroDivisionError
                    
                    except ZeroDivisionError:
                        pass
                    except Exception as e:
                        raise e

                except ZeroDivisionError:
                    pass
                except Exception as e:
                    raise e
            except ZeroDivisionError:
                pass
            except Exception as e:
                api_list.append(api)
                print("No API EndPoint")
                continue

        value = dict(title=title.text, endpoint=result.text.split('\n')[0])
        api_process_data.append(value)
        count+=1
        print(count)
        print(value)
        
    
except Exception as e:
    print(e)

finally:
    #driver.close()
    json_data = json.dumps(api_process_data)
    with open('data.json', 'w') as f:
        f.write(json_data)

# 저장되지않은 api_endpoint 
    no_data = json.dumps(api_list)
    with open('no_api.json', 'w') as f:
        f.write(no_data)
