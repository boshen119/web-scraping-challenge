from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(-__name__)

# Use flask pymongo to set up mongo connection
app.config("MONGO_URI") = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    return


@app.route("/scrape"):
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.all()
    mars.replace({}, mars_data, upsert=True)
    return "Scraping Successful"

if__name__ == "__main__":
app.run()

