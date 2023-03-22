from flask import Flask, render_template, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "whatasecretkey"
    app.debug = True

    @app.route('/index')
    def index():
        return render_template("index.html"), {'Content-Type': 'text/html'}

    @app.route('/about')
    def about():
        return render_template("about.html"), {'Content-Type': 'text/html'}

    @app.route('/blog')
    def blog():
        return render_template("blog.html"), {'Content-Type': 'text/html'}

    @app.route('/contact')
    def contact():
        return render_template("contact.html"), {'Content-Type': 'text/html'}

    @app.route('/services')
    def services():
        return render_template("services.html"), {'Content-Type': 'text/html'}

    return app

if __name__ == '__main__':
    app.run()