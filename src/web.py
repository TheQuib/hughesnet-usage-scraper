from flask import Flask, render_template, request

class Webserver:
    def start_server():
        app = Flask(__name__, template_folder='web/templates', static_folder='web/static')


        @app.route('/')
        def home():
            return render_template('home.html')

        @app.route('/settings')
        def settings():
            return render_template('settings.html')

        if __name__ == '__main__':
            app.run(debug=True)
