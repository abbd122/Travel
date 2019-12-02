from api import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host=app.config['IP'], port=app.config['PORT'], debug=app.config['DEBUG'])
