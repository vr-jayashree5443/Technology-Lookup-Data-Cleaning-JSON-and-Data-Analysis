import pandas as pd
from bs4 import BeautifulSoup
import requests
from flask import Flask, request, render_template, jsonify
import re
df_tech=pd.read_csv("cleaned_data.csv")
df_tech.index=df_tech['Unnamed: 0']
def Technology(url):
  _url="https://"+re.sub(".*//[a-z]*.|.*//|www.|/.*","",str(url))
  req=requests.get(_url)
  soup =BeautifulSoup(req.content)
  a=str(soup)
  i1=0
  techs_used=[]
  for i in df_tech.columns:

    for j in range(0,len(df_tech)):
      try:
        if(df_tech.iloc[j][i1] in a):
          techs_used.append(df_tech.index[j])
      except:
        pass
    i1+=1

  print(techs_used)
  return techs_used

#########################################################################################################s
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    url = request.form['url']
    output_list = Technology(url)
    return jsonify(output_list)

if __name__ == '__main__':
    app.run(debug=True)
