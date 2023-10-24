import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

url = "https://www.commodityonline.com/mandiprices/tomato/karnataka"

try:
    driver.get(url)
    table_locator = (By.CSS_SELECTOR, '#main-table2')
    table = WebDriverWait(driver, 10).until(EC.presence_of_element_located(table_locator))
except Exception as e:
    print("INVALID: ", e)

print("Fetching column names...")
column_names = [cell.text for cell in table.find_elements(By.TAG_NAME, 'th')]

print("Fetching rows...")
table_data = []
for row in table.find_elements(By.TAG_NAME, 'tr'):
    row_data = [cell.text for cell in row.find_elements(By.TAG_NAME, 'td')]
    table_data.append(row_data)

df = pd.DataFrame(table_data, columns=column_names)
df = df.dropna()
df = df.drop('Mobile App', axis=1)
data = pd.DataFrame(df.iloc[0])
print(type(data))

csv_file_path = r"C:\Users\Hewlett Packard\major-project\Agro-demand-supply-analysis\datasets\historical_price_tomato.csv"

data.to_csv(csv_file_path, mode='a', header=False, index=False)

driver.quit()