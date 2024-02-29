from selenium.webdriver.common.by import By
from selenium import webdriver
from tqdm import tqdm
import pandas as pd
import time

if __name__ == "__main__":
    # Set up the webdriver
    driver = webdriver.Chrome()
    # Load the DataFrame containing article URLs
    df = pd.read_csv("article_data_9.csv")
    article_urls = df.url.to_list()

    article_data = []
    for article_url in tqdm(article_urls):
        try:
            # Load the URL in the webdriver
            driver.get(article_url)
            # Wait for page to load (You might need to increase or decrease this time)
            time.sleep(3)

            # Find the title element
            title_element = driver.find_element(By.CLASS_NAME, "mol-para-with-font")
            # Extract text from the title element
            title = title_element.text

            # Append the data to article_data list
            article_data.append({
                "url": article_url,
                "description": title
            })

            # Optionally, you can write this data to CSV after every iteration
            # This will prevent loss of data in case of any exception
            df = pd.DataFrame(data=article_data, columns=article_data[0].keys())
            df.to_csv("article_details_9.csv", index=False)
        
        except Exception as e:
            print(f"Error processing {article_url}: {str(e)}")
            # Continue to the next iteration if there's an exception
            continue

    # Close the webdriver after processing all URLs
    driver.quit()
