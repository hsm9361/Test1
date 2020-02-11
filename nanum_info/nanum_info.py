from flask import Blueprint, render_template

nanum_info_blue = Blueprint('nanum_info_blue', __name__)

@nanum_info_blue.route('/volunteer')
def volunteer():
    html = render_template('nanum_info/volunteer.html')
    return html

@nanum_info_blue.route('/support')
def support():
    html = render_template('nanum_info/support.html')
    return html

@nanum_info_blue.route('/facility_rental')
def facility_rental():
    html = render_template('nanum_info/facility_rental.html')
    return html