# import markdownify 
import requests
import html2text
import re
from colorama import Fore, Back, Style,init
init(autoreset=True)

def remove_js_css_from_html(html_content):
    # Remove <script> tags (JS)
    html_content = re.sub(r'<script.*?>.*?</script>', '', html_content, flags=re.DOTALL)

    # Remove <style> tags (CSS)
    html_content = re.sub(r'<style.*?>.*?</style>', '', html_content, flags=re.DOTALL)

    return html_content
def convert_html_to_markdown(html_content):
    # Initialize html2text with desired options
    h = html2text.HTML2Text()
    h.ignore_links = True  # Ignore links in the HTML

    # Convert HTML to Markdown
    markdown_content = h.handle(html_content)

    return markdown_content

def WebsiteInfo(url:str):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            # Access the HTML content of the website
            print(Fore.GREEN +f"Website GET {response.status_code}")
            cleaned_html = remove_js_css_from_html(response.text)
            markdown_output = convert_html_to_markdown(cleaned_html)
            return markdown_output
        else:
            print(Fore.RED +f"Website Failed {response.status_code}")
            return f"Failed to fetch the website. Status code: {response.status_code}"
    except:
        print(Fore.RED +"Website Failed")
    
if __name__ == "__main__":
    print(WebsiteInfo("https://www.smh.com.au/business/companies/why-a-billionaire-s-son-could-change-the-fortunes-of-network-ten-20240410-p5fiss.html"))