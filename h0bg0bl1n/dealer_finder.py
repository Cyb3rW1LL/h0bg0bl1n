import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

def find_dealers():
    location = os.getenv("SEARCH_LOCATION", "City, ST") #City, US State two letter abreviation
    print(f"Searching for Chevy dealers in {location}...")
    
    # Simple search, returns the first page of results
    query = f"Chevrolet dealerships {location}"
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    with open("dealers.txt", "w") as f:
        for a in soup.select('a[href^="http"]'):
            link = a['href']
            if "chevrolet" in link and "google" not in link:
                dealer_name = link.split('/')[2].replace('www.', '').split('.')[0]
                # Default search string for DealerOn/Inspire sites
                search_url = f"{link.split('/')[0]}//{link.split('/')[2]}/searchnew.aspx?Model=Colorado&ModelAndTrim=Colorado:ZR2"
                f.write(f"{dealer_name},{search_url}\n")
    
    print("Found potential dealers! Check dealers.txt to verify links.")

if __name__ == "__main__":
    find_dealers()