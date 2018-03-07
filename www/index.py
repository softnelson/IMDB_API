# Infrastructure test page.
import os
from flask import Flask, request, render_template
from flask import Markup
from flask import render_template
import urllib.request, urllib.parse, urllib.error
import json

app = Flask(__name__)

serviceurl = 'http://www.omdbapi.com/?'
apikey = '&apikey='+'d96a8ed3'

def print_json(json_data):
    list_keys=['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer',
               'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Ratings',
               'Metascore', 'imdbRating', 'imdbVotes', 'imdbID']
    print("-"*50)
    for k in list_keys:
        if k in list(json_data.keys()):
            print(f"{k}: {json_data[k]}")
    print("-"*50)


def search_movie(title):
    if len(title) < 1 or title == 'quit':
        print("Goodbye now...")
        return None

    try:
        url = serviceurl + urllib.parse.urlencode({'t': title}) + apikey
        print(f'Retrieving the data of "{title}" now... ')
        uh = urllib.request.urlopen(url)
        data = uh.read()
        json_data = json.loads(data)

        if json_data['Response'] == 'True':
            print_json(json_data)
            return json_data
        else:
            print("Error encountered: ", json_data['Error'])

    except urllib.error.URLError as e:
        print(f"ERROR: {e.reason}")


@app.route("/")
def hello():
    return render_template('index.html')
 
@app.route("/echo", methods=['POST'])
def echo():
    title =request.form['text']
    result=search_movie(title)
    print(result)
    return render_template('index.html', result=result)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
