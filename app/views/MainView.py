import json as json
from flask import Blueprint, render_template, current_app, g, jsonify

from app.shared.request import api_response
from ..shared.Authentification import Auth
from app.models import UserModel, PostModel
from app.models.UserModel import UserSchema
from app.utl import with_config


main = Blueprint('main', __name__)

@main.route('/testmain', methods = ['GET'])

# @Auth.auth_required
@with_config(app=current_app, config_key="eva")
def testmain():
    return api_response({'status': 'App is working !'})


