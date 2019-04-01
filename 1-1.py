from flask import Flask, url_for

app = Flask(__name__)


@app.route('/bootstrap_sample')
def index():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    <title>Hello</title>
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
                    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
                    <title>Hello</title>
                  </head>
                  <body>
                    <h1>Hello, world</h1>
                    <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                    <div id="list-example" class="list-group">
<nav id="navbar-example3" class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">Navbar</a>
  <nav class="nav nav-pills flex-column">
    <a class="nav-link" href="#item-1">Пункт 1</a>
    <nav class="nav nav-pills flex-column">
      <a class="nav-link ml-3 my-1" href="#item-1-1">Пункт 1-1</a>
      <a class="nav-link ml-3 my-1" href="#item-1-2">Пункт 1-2</a>
    </nav>
    <a class="nav-link" href="#item-2">Пункт 2</a>
    <a class="nav-link" href="#item-3">Пункт 3</a>
  </nav>
</nav>
<button type="button" class="btn btn-primary">Супер мега кнопка</button>
</div>
<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" width=250  height=250 src="{}" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" width=250  height=250 src="{}" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" width=250  height=250 src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/01-Russian_alphabet-%D0%90_%D0%B0.svg/220px-01-Russian_alphabet-%D0%90_%D0%B0.svg.png" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>                              
                  </body>
                </html>'''.format(url_for('static', filename='A.jpg'),
                                      url_for('static', filename='orange.jpg'),
                                      url_for('static', filename='A.jpg'),
                                      url_for('static', filename='A.jpg'))

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
