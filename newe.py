import requests
from bs4 import BeautifulSoup
import json
 
urls = [
    "https://www.investopedia.com/terms/m/mutualfund.asp",
    "https://www.amfiindia.com/investor-corner/knowledge-center/what-are-mutual-funds-new.html",
    "https://zerodha.com/varsity/chapter/introduction-to-mutual-funds/",
    "https://en.wikipedia.org/wiki/Mutual_fund"
]

 
def scrape_website(url):
    try:
 
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

 
        title = soup.title.string if soup.title else "No title available"
        meta_desc = soup.find("meta", attrs={"name": "description"})
        description = meta_desc["content"] if meta_desc else "No description available"

        keywords_tag = soup.find("meta", attrs={"name": "keywords"})
        keywords = keywords_tag["content"] if keywords_tag else "No keywords available"

 
        overview = description[:150] + "..." if len(description) > 150 else description
        summary = f"Overview of the page titled '{title}' from {url}"

        return {
            "Overview": overview,
            "Summary": summary,
            "Description": description,
            "Keywords": keywords,
            "Link": url
        }
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return {
            "Overview": "Error",
            "Summary": "Error",
            "Description": "Error",
            "Keywords": "Error",
            "Link": url
        }

 
data = [scrape_website(url) for url in urls]

 
json_data = json.dumps(data, indent=4)

 
with open("mutual_funds_data.json", "w") as file:
    file.write(json_data)

print("Data has been successfully scraped and saved to 'mutual_funds_data.json'.")
