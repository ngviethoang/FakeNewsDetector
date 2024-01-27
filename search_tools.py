from googleapiclient.discovery import build
import os


def google_search(search_term, **kwargs):
  service = build("customsearch",
                  "v1",
                  developerKey=os.environ.get("GOOGLE_API_KEY"))
  res = (service.cse().list(q=search_term,
                            cx=os.environ.get("GOOGLE_CSE_ID"),
                            **kwargs).execute())
  return res["items"]


def search_internet(query, num=10):
  """Useful to search the internet
  about a a given topic and return relevant results"""
  results = google_search(query, num=num)
  string = []
  for result in results:
    try:
      string.append("\n".join([
          f"Title: {result['title']}",
          f"Link: {result['link']}",
          f"Snippet: {result['snippet']}",
          "\n-----------------",
      ]))
    except KeyError:
      next

  return "\n".join(string)
