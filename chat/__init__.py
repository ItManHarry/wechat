from flask import Flask
# 动态创建App实例
def create_app():
    app = Flask('chat')
    register_app_global_url(app)
    return app
def register_app_global_url(app):
    @app.route('/chat/index')
    def index():
        return '<h1>Chat Index</h1>'