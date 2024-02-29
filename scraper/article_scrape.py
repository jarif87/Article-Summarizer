from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()
    title_url = "https://www.dailymail.co.uk/femail/index.html"
    article_data = []

    for idx in tqdm(range(150)):
        driver.get(title_url)
        time.sleep(2)  # Give the page some time to load

        rows = driver.find_elements(By.CSS_SELECTOR, '.link-bogr2')

        for row in rows:
            url_tag = row.find_element(By.TAG_NAME, 'a')
            title = row.find_element(By.CSS_SELECTOR, '.pufftext').text
            url = url_tag.get_attribute('href')
            article_data.append({
                "title": title,
                "url": url
            })

        time.sleep(1)

    driver.quit()  # Close the browser window

    df = pd.DataFrame(data=article_data, columns=["title", "url"])
    df.to_csv("article_data_9.csv", index=False)