from flask import Flask
from main import index

app = Flask(__name__, template_folder='view', static_url_path='',static_folder='./static')
# 세션 사용
app.secret_key = '13kldnfkl24ndfdsf'

app.register_blueprint(index.main_blue)

app.run(host='0.0.0.0', port=80,debug=True)