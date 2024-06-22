import requests
from bs4 import BeautifulSoup
from rich import print

# Specify the URL
url = 'https://www.smh.com.au/'

# Send a request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
def GetLinks():
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Create a set to store unique links
    links = set()
    
    # Find all anchor tags and extract their href attribute
    for a_tag in soup.find_all('a'):
        href = a_tag.get('href')
        # If href is not None, add it to the set
        if href:
            links.add(href)
    
    links = ["https://www.smh.com.au"+i for i in links if i.endswith(".html")]
    return links
    

if __name__ == "__main__":
    print(GetLinks())