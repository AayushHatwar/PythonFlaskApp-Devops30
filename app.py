from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'GeeksForGeeks-Devops30-aayush ? HOW ARE YOU now bro'
    def a():
        print('test)
        a()
    def a():
        print('test')
        a()
    a()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
