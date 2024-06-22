from duckduckgo_search import DDGS
from rich import print
import arrow


def Search(keywords, timelimit):
    news_list = []
    with DDGS() as webs_instance:
        WEBS_news_gen = webs_instance.news(
          keywords,
          region="wt-wt",
          safesearch="off",
          timelimit=timelimit,
          max_results=100
        )
        for r in WEBS_news_gen:
            r['date'] = arrow.get(r['date']).humanize()
            news_list.append(r)
    return news_list, keywords

if __name__ == '__main__':
    print(Search("python", 0.5))
