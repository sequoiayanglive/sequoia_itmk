from flask import Flask
#from flask_cors import CORS
def create_api_app():
    app = Flask(__name__, static_folder='./vue_client/', static_url_path='')
    app.config.from_object('app.settings.DevAPIConfig')
    # CORS(app, supports_credentials=True)
    # app.config['JSON_AS_ASCII'] = False
    from app.api import api_bp
    app.register_blueprint(api_bp)
   # app.register_blueprint
    return app