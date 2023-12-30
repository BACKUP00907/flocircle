print("hello world")
import requests
import webbrowser

url = ["https://strmltpym1.streamlit.app/"]
k = 0

while k < len(url): 
  

  webbrowser.open('http://www.python.org')
  response = requests.get(url[k])
  k+=1
  print(response.content)
