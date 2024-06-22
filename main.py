from links.ABC import GetLinks as ABCLinks
from links.SMH import GetLinks as SMHLinks
from tools.WebScrape import WebsiteInfo
from llms.Groq import Groq
from rich import print

def main():
    links = ABCLinks() + SMHLinks()
    for link in links:
        info = WebsiteInfo(link)
        yield eval(Groq(info,Print=False))

for i in main():
    input("\nnext ... ")
    print(i)
