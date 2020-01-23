from flask import Flask, render_template, request
from member.MemberBluePrint import member_blue

app=Flask(__name__)
app.register_blueprint(member_blue)

@app.route('/')
def index():
    html = render_template('/index.html')
    return html

app.run(host='0.0.0.0', port=80, debug=True)