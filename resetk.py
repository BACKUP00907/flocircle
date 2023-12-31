print("hello world")
from requests_html import HTMLSession
import webbrowser
import time

url = ["https://strmltpym1.streamlit.app/"]
k = 0

while k < len(url): 
  
  
  webbrowser.open(url[k])
  time.sleep(66)
  
  #session = HTMLSession()

  #r = session.get(url[k])

  #r.html.render() 
  #response = requests.get(url[k])
  k+=1
  #print(response.content)
