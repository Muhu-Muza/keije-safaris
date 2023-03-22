from flask import Flask, render_template, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "whatasecretkey"
    app.debug = True

    @app.route('/index')
    def index():
        return render_template("index.html")

    @app.route('/about')
    def about():
        return render_template("about.html")

    @app.route('/blog')
    def blog():
        return render_template("blog.html")

    @app.route('/contact')
    def contact():
        return render_template("contact.html")

    @app.route('/services')
    def services():
        return render_template("services.html")

    return app

if __name__ == '__main__':
    app.run()