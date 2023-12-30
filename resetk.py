print("hello world")
import requests

url = ["https://strmltpym1.streamlit.app/"]
for k in url:
  response = requests.get(url[k])
print(response.content)
