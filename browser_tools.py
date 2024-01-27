from selenium import webdriver
from unstructured.partition.html import partition_html

# Set up the driver, this will open a browser window.
options = webdriver.ChromeOptions()
options.add_argument("headless")  # to run chrome in headless mode


def get_html_content(url: str):
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    html = driver.page_source

    driver.quit()

    elements = partition_html(text=html)
    content = "\n\n".join([str(el) for el in elements])
    content = [content[i : i + 8000] for i in range(0, len(content), 8000)]

    return content
