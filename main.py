from flask import Flask
from board import board
from main import index
from user import user
from intro import intro
from nanum_info import nanum_info


app = Flask(__name__)


app = Flask(__name__, template_folder='view', static_url_path='', static_folder='./static')
# 세션 사용
app.secret_key = '13kldnfkl24ndfdsf'

app.register_blueprint(index.main_blue)
app.register_blueprint(board.board_blue)
app.register_blueprint(user.user_blue)
app.register_blueprint(intro.intro_blue)
app.register_blueprint(nanum_info.nanum_info_blue)

app.run(host='0.0.0.0', port=80,debug=True)