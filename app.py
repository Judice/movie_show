# _*_ coding: utf-8 _*_
from movie import create_app

app = create_app()

if __name__ == '__main__':
    host = app.config.get('HOST', '127.0.0.1')
    port = app.config.get('PORT', '5010')
    debug = app.config.get('DEBUG', True)
    app.run(host, port, debug)
