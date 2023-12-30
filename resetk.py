print("hello world")
import requests
from bs4 import BeautifulSoup

url = ["https://strmltpym1.streamlit.app/"]
for k in url:
  response = requests.get(url[k])
print(response.content)
