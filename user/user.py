from flask import Blueprint, render_template, request, session, redirect, url_for
from user import user_dao
import requests
import json

user_blue = Blueprint('user_blue', __name__)


@user_blue.route('/log_in')
def log_in():
    html = render_template('user/log_in.html')
    return html



@user_blue.route('/oauth')
def oauth():
    code = str(request.args.get('code'))

    url = "https://kauth.kakao.com/oauth/token"
    payload = "grant_type=authorization_code&client_id=0177e561c48a6f1f456e6568b22d0ba1&redirect_uri=http%3A%2F%2Flocalhost%2Foauth&code=" + str(code)
    headers = {
        'Content-Type' : "application/x-www-form-urlencoded",
        'Cache-Control' : "no-cache",
    }

    # access_token 받아오기
    response = requests.request("POST", url, data=payload, headers=headers)
    access_token = json.loads(((response.text).encode('utf-8')))['access_token']

    # 토큰 업데이트
    headers.update({'Authorization': "Bearer " + str(access_token)})

    # 카카오세션 id = DB id 확인
    if user_dao.user_kakao_login(headers)==True:
        # 로그인 완료
        session['login']='YES'
        session['user_name']=user_dao.user_kakao_user_id(headers)
        return f'''
            <script>
            alert('카카오 아이디 로그인 완료')
            location.href = "/"
            </script>
            '''

    else:
        kakao_dict = user_dao.user_kakao_insert(headers)
        user_kakao_idx = kakao_dict['user_kakao_idx']
        user_kakao_email = kakao_dict['user_kakao_email']
        return f'''
            <script>
                location.href = "/kakao_user_join?user_kakao_idx={user_kakao_idx}&user_kakao_email={user_kakao_email}"
            </script>
            '''

@user_blue.route('/kakao_user_join/')
def kakao_user_join():
    user_kakao_idx = request.values.get("user_kakao_idx")
    user_kakao_email = request.values.get("user_kakao_email")

    html =render_template('user/kakao_user_join.html', user_kakao_idx=user_kakao_idx, user_kakao_email=user_kakao_email)
    return html

@user_blue.route('/kakao_user_join_pro', methods=['post'])
def kakao_user_join_pro():
    user_name = request.form.get('user_name')
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')
    user_email = request.form.get('user_kakao_email')
    user_kakao_idx = request.form.get('user_kakao_idx')
    
    user_dao.add_user_kakao(user_name,user_id,user_pw,user_email, user_kakao_idx)
    print("회원가입완료")
    html = render_template('main/index.html')
    return html
    


'''
def kakao_logout(headers):
    url = "https://kapi.kakao.com/v1/user/unlink"
    payload = "target_id_type=user_id&target_id=1284321732"
    response = requests.request("POST", url, data=payload, headers=headers)
'''

@user_blue.route('/mypage')
def mypage():
    user_name=session['user_name']
    html = render_template('user/mypage.html',user_name=user_name)
    return html

@user_blue.route('/user_join')
def join():
    html = render_template('user/user_join.html')
    return html

@user_blue.route('/user_join_pro', methods=['post'])
def join_pro():
    user_name = request.form.get('user_name')
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')
    user_email = request.form.get('email')

    # print(user_name,user_id,user_pw,user_email)
    user_dao.add_user(user_name,user_id,user_pw,user_email)
    html = render_template('main/index.html')
    return html



@user_blue.route('/user_login_pro', methods=['post'])
def user_login_pro():
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')

    # print(user_name,user_id,user_pw,user_email)
    result=user_dao.login_check(user_id,user_pw)

    if result[0] == 'No' :
        return 'NO'
    else :
        session['login']='YES'
        session['user_idx'] = result[0]
        session['user_type'] = result[2]
        session['user_name'] = result[3]
        return 'YES'


    # html = render_template('main/index.html')
    # return html

@user_blue.route('/user_logout')
def user_logout():
    session['login']=False
    html = render_template('main/index.html')
    return html