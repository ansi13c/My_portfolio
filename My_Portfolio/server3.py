from flask import Flask , render_template
from PIL import Image

# image_to_convert = Image.open("D:/webserver/static/assets/images/space.jfif")
# image_to_convert.save('./static/assets/images/space.jpg',"jpeg")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def portfolio_activator(page_name):
    return render_template(page_name)

# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")
#
# @app.route('/work.html')
# def work():
#     return render_template("work.html")
#
# @app.route('/works.html')
# def works():
#     return render_template("works.html")