print("hello world")
from requests_html import HTMLSession

url = ["https://strmltpym1.streamlit.app/"]
k = 0

while k < len(url): 
  
  

  session = HTMLSession()

  r = session.get(url[k])

  r.html.render() 
  #response = requests.get(url[k])
  k+=1
  print(response.content)
