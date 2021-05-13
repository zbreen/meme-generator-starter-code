"""The process of enacting the meme generator and ingestors."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

# last project wanted me to remove todo's
from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    files = ['./_data/DogQuotes/DogQuotesTXT.txt',
             './_data/DogQuotes/DogQuotesDOCX.docx',
             './_data/DogQuotes/DogQuotesPDF.pdf',
             './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    images_path = "./_data/photos/dog/"

    for q in files:
        quotes.extend(Ingestor.parse(q))

    imgs = []

    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # randomly decide on one of the choices
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author', "No one")
    image_response = requests.get(path).content
    rand_num = random.randint(0, 10000)
    tmp = f'./tmp/{rand_num}.jpg'

    with open(tmp, "wb") as file_ref:
        file_ref.write(image_response)

    path = meme.make_meme(tmp, body, author)

    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
