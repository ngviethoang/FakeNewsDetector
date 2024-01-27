from ai import get_chat_response
from search_tools import search_internet
from browser_tools import get_html_content
from dotenv import load_dotenv

load_dotenv()

print("Enter the news or an URL you want to confirm:")

news = input()
news = news.strip()

# check if it's an url
if news.startswith("http"):
  news = get_html_content(news)
  news = ' '.join(news)

print("Analyzing...")

news_summary = get_chat_response([{
    "role":
    "system",
    "content":
    "You are a fake new detector expert. You analyze the news's title, content to summarize, then use it to search on the internet to confirm if it's true. You will be given the news from user, then response the short summarized content so user can search on the internet and confirm. Remember to response only the content, nothing else.",
}, {
    "role": "user",
    "content": f"Here is the news: {news}",
}])

print("News Summary:", news_summary)

search_result = search_internet(news_summary, num=15)

print("Sources: ", search_result)

fake_detect_result = get_chat_response([{
    "role":
    "system",
    "content":
    """You are a fake new detector expert. You will be provided the news that need to be detected, and the results searched from in the internet. Your job is to analyze carefully the provided content and decide if it's the fake news or not.
    Your answer must provide these terms:
    - Trustworthiness Score: Assigned a score indicating its likely credibility.
    - Reasoning Summary: Provides a summary of why a piece of content was flagged as misinformation, including inconsistencies found, questionable sources, or lack of verification from trusted sources.
    - Sources Comparison: Offers a comparison or references from trusted sources to counter-check the facts in the input content.
    """,
}, {
    "role":
    "user",
    "content":
    f"Here is the news: {news}\nHere is the search result from internet: {search_result}"
}])

print("Result:", fake_detect_result)
