from chalice import Chalice
from chalicelib.endpoints.application.app import application

app = Chalice(app_name='putio')
app.register_blueprint(application, url_prefix="/application")


@app.route('/')
def index():
    return {'hello': 'world'}
