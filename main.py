# using Flask to run Python code within an HTML page


from flask import Flask, render_template, request

import requests



# The following code defines a Flask application and defines two routes:
# The first route, @app.route("/", methods=["GET"]), handles the initial GET request when the user loads the page.
# The second route, @app.route("/", methods=["POST"]), handles the POST request that is triggered when the user submits the search form.

# The search() function gets the search term submitted by the user, then sends a request to the Wikipedia API to search for articles that match the query.
# It then processes the JSON response to extract the titles and URLs of the first 10 search results and store them in a separate HTML template.



app = Flask(__name__)
# creates a Flask application instance.


@app.route('/', methods=['GET', 'POST'])   # This decorator specifies when the function below is triggered. It's when the user makes a GET (user loads the page) or POST (user submits the form) request.
def search():   # This function retrieves the user's input from a form on the webpage and sends it to another API.
    if request.method == 'POST':
        url = "https://en.wikipedia.org/w/api.php"
        target = request.form.get('search')
        p = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": target,
            "prop": "info",
            "inprop": "url",
            "utf8": "",
        }
        r = requests.get(url, params=p)
        data = r.json()
        results = []
        for result in data["query"]["search"]:
            title = result["title"]
            url = "https://en.wikipedia.org/wiki/" + title.replace(" ", "_")
            results.append({'title': title, 'url': url})
        return render_template('index.html', results=results)
    else:
        return render_template('index.html')    # This line of code gets executed if the request.method is GET. (when the page is loaded)
      
      
if __name__ == '__main__':
    app.run(debug=True)      
