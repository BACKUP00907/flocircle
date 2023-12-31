print("hello world")
import webbrowser
import time

url = ["https://strmltpym1.streamlit.app/"]
k = 0

while k < len(url): 
  webbrowser.open(url[k])
  time.sleep(120)
  k+=1
