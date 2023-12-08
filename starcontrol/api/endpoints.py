import json
from .. import app
from ..game_assets import solar_list, template_list



# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.json")

# @app.route('/solarsystem/<id>')
# def get_solarsystem(id):
#     system = assets.get(id)
#     return app.make_response(json.dumps(system, cls=CustomJSONEncoder))

@app.route('/solarsystems')
def get_solarsystem_list():
    return app.make_response(json.dumps(solar_list(), cls=CustomJSONEncoder))

@app.route('/planettemplates')
def get_all_templates():
    return app.make_response(json.dumps(template_list(), cls=CustomJSONEncoder))

@app.route('/planettemplates/<template>')
def get_single_template(template):
    template = template_list()[template]
    return app.make_response(json.dumps(template, cls=CustomJSONEncoder))

#TODO: remove duplicated in init
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__

