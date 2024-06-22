import requests
from bs4 import BeautifulSoup
from rich import print
# Define the URL for the ABC News site
url = 'https://abcnews.go.com/'

# Fetch the webpage content using requests
response = requests.get(url)


def GetLinks():
    # Parse the webpage content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Locate the specific element using the HTML class you provided
    element = soup.find('div', class_='block__single-column block HeadlineStackBlock__trioheadlines')
    
    # Initialize a list to hold the links
    links = []
    
    # Check if the element exists
    if element:
        # Find all 'a' tags within the element
        a_tags = element.find_all('a', class_='AnchorLink News__Item external flex flex-row')
        
        # Loop through each 'a' tag to extract the href attribute (URL)
        for a_tag in a_tags:
            link = a_tag.get('href')
            if link:
                links.append(link)
    return links

if __name__ == "__main__":
    print(GetLinks())

