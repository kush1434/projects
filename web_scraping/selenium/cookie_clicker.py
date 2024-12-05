from selenium import webdriver#allows u to interact with the browser through a thirdparty
from selenium.webdriver.chrome.service import Service#starts and manges the webdriver executation
from selenium.webdriver.common.by import By#allows u to locate elements in the webpage
from selenium.webdriver.support.ui import WebDriverWait#used to wait for the the page to load and make sure desired element is present
from selenium.webdriver.support import expected_conditions as EC#allows u to use conditions for the module above
from selenium.webdriver.common.action_chains import ActionChains#allows u to simulate the hover
from selenium.common.exceptions import TimeoutException#handles error

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")


product_price = 'productPrice'
product_name = 'productName'
cookie = 'bigCookie'
num_of_cookies = 'cookies'
buildings = {
    "Cursor": 0,
    "Grandma": 1,
    "Farm": 2,
    "Mine": 3,
    "Factory": 4,
    "Bank": 5,
    "Temple": 6,
    "Wizard Tower": 7,
    "Shipment": 8,
    "Alchemy Lab": 9,
    "Portal": 10,
    "Time Machine": 11,
    "Antimatter Condenser": 12,
    "Prism": 13,
    "Chancemaker": 14,
    "Fractal Engine": 15,
    "Javascript Console": 16,
    "Idleverse": 17,
    "Cortex Baker": 18,
    "You": 19
}
small_purchase_count = 0
small_purchase_limit = 2


def text_to_number(text):
    quantities = [
    "million", "billion", "trillion", "quadrillion", "quintillion",
    "sextillion", "septillion", "octillion", "nonillion", "decillion",
    "undecillion", "duodecillion", "tredecillion", "quattuordecillion",
    "quindecillion", "sexdecillion", "septendecillion", "octodecillion",
    "novemdecillion", "vigintillion"]

    quants_dict = {quantity: 10 ** (6 + 3 * i) for i, quantity in enumerate(quantities)}

    if not text:
        return 0

    parts = text.split()
    if (len(parts)==2) and (parts[1] in quants_dict):
        return int((float(parts[0])*quants_dict[parts[1]]))
    return int(parts[0].replace(',',''))


def get_CPS(product_num):
    try:

        hover_element = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.XPATH, f"//div[@class='product unlocked enabled'][@id='product{str(product_num)}']"))
        )

        actions = ActionChains(driver)
        actions.move_to_element(hover_element).perform()
 
        hover_content = WebDriverWait(driver, 8).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id='tooltipBuilding']//div[@class='descriptionBlock'][1]/b"))
        )

    except TimeoutException:
        return None 

    parts = hover_content.text.split()
    return float(parts[0])

def ROI(CPS, price):
    if (CPS == 0) or (price == 0):
        return 0
    return CPS/price


def best_to_buy(current_cookies):

    global small_purchase_count

    conversions = {driver.find_element(By.XPATH, f"//div[@id='productName{str(i)}']").text: text_to_number(driver.find_element(By.ID, 'productPrice' + str(i)).text) for i in range(20)}
    del conversions['']
    current_cookies = text_to_number(current_cookies)

    rois = []
    for building, price in conversions.items():
        building_index = buildings[building]
        cps = get_CPS(building_index)
        if not cps:
            cps = 10**18
        rois.append([ROI(cps, price), building, price])

    sorted_rios = sorted(rois, key=lambda x: x[0], reverse=True)#sorts based on roi

    for roi, building, price in sorted_rios:
        if price <= current_cookies * 2 and price > current_cookies * 0.3:
            small_purchase_count = 0  
            return building, price
        
        elif price <= current_cookies * 0.3 and small_purchase_count < small_purchase_limit:
            small_purchase_count += 1
            return building, price

    return sorted_rios[0][1], sorted_rios[0][2]



WebDriverWait(driver, 7).until(
    EC.presence_of_all_elements_located((By.XPATH,"//div[@id='langSelect-EN']"))
)

lang = driver.find_element(By.XPATH,"//div[@id='langSelect-EN']")
lang.click()

WebDriverWait(driver, 7).until(
    EC.presence_of_all_elements_located((By.ID,cookie))
)

cookie = driver.find_element(By.ID,cookie)


while True:
    for _ in range(100):
        cookie.click()

    cookies = driver.find_element(By.ID, num_of_cookies).text
    target_building, target_price = best_to_buy(cookies)

    if text_to_number(cookies) >= target_price:
        product_to_purchase = driver.find_element(By.ID, 'product' + str(list(buildings.keys()).index(target_building)))
        product_to_purchase.click()