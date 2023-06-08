# define your bluprint
from flask import Flask, Blueprint
blueprint = Blueprint('blueprint', __name__)

# put this sippet ahead of all your bluprints
# blueprint can also be app~~
@blueprint.after_request 
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    # Other headers can be added here if needed
    return response

# write your own blueprints with business logics
@blueprint.route('/test', methods=['GET'])
def test():
    return "test success"

@blueprint.route('/test/<int:id>/', methods=['GET'])
def test_id(id):
    return f"test success {id}"

app = Flask(__name__)
app.register_blueprint(blueprint=blueprint)