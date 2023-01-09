import cloudscraper
from bs4 import BeautifulSoup

url = "https://clutch.co/agencies/digital-marketing?page=0"

HEADERS = {
    'User-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
}

# options = Options()
# options.headless = True
# driver = uc.Chrome(options=options)
# driver.get(url)
# data = driver.page_source

scraper = cloudscraper.create_scraper()
data = scraper.get(url, headers=HEADERS).text
soup = BeautifulSoup(data, "html.parser")
link = soup.select(".company_info")
for i in link:
    l = f"https://clutch.co{i.find('a')['href']}"
    data1 = scraper.get(l).text
    soup = BeautifulSoup(data1, "html.parser")
    tel = soup.select(".tel")
    for i in tel:
        print(i.text.strip())
