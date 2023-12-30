print("hello world")
import requests

url = ["https://strmltpym1.streamlit.app/"]
k = 0

while k < len(url): 
  response = requests.get(url[K])
  k+=1
  print(response.content)
