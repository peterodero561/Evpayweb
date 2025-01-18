from flask import Blueprint, redirect, url_for, render_template, jsonify, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask import current_app
from app.extensions import db
from app.models.user import User
from app.models.bus import Bus
from app.models.driver import Driver
from app.models.garage import Garage
from app.models.garage_manager import GarageManager
import os
from sqlalchemy.exc import IntegrityError


profiles_bp = Blueprint('profiles', __name__, template_folder='templates')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# function to check allowed upload file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@profiles_bp.route('/user_profile', methods=['GET'], strict_slashes=False)
@login_required
def user_profile():
    '''method to serve user home page'''
    if current_user.user_role != 'user':
        return redirect(url_for('auth.login'))
    return render_template('passengers_home.html', user=current_user)

@profiles_bp.route('/driver_profile', strict_slashes=False, methods=['GET'])
@login_required
def driver_profile():
    '''method to serve driver home page'''
    if current_user.user_role != 'driver':
        redirect(url_for('auth.login'))
    return render_template('owners_home.html', driver=current_user)

@profiles_bp.route('/manager_profile', methods=['GET'], strict_slashes=False)
@login_required
def manager_profile():
    '''method to serve manager home page'''
    if current_user.user_role != 'garage manager':
        redirect(url_for('auth.login'))
    return render_template('manager_home.html', manager=current_user)

@profiles_bp.route('/garage_setup_page', methods=['GET'], strict_slashes=False)
@login_required
def garage_setup_page():
    '''Method to serrve the garage setup page'''
    if current_user.user_role != 'garage manager':
        redirect(url_for('auth.login'))
    return render_template('garage_setup.html', manager=current_user)

@profiles_bp.route('/account', methods=['GET'], strict_slashes=False)
@login_required
def account():
    '''Serves the profile page for users'''
    return render_template('profile.html', user=current_user)

@profiles_bp.route('/account_data', methods=['GET'], strict_slashes=False)
@login_required
def account_data():
    '''return current user information'''
    return jsonify(current_user.to_dict())

@profiles_bp.route('/account_update', strict_slashes=False, methods=['PUT'])
@login_required
def account_update():
    '''methos to update account information'''
    if request.method == 'PUT':
        name = request.form.get('name')
        email = request.form.get('email')
        newPasswd = request.form.get('password')

        # chack if a file is uploaded for the profile pic
        if 'pic' in request.files:
            pic_file = request.files['pic']
            if pic_file and allowed_file(pic_file.filename):
                # save file in the profile images directory
                pic_file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], secure_filename(pic_file.filename)))
                pic = pic_file.filename

        role = current_user.user_role
        # update with the given data
        user = User.query.get(current_user.user_id)
        #check if there is a user with the given email
        existing_email = User.query.filter_by(user_email=email).first()
        if existing_email and existing_email.user_email != current_user.user_email:
            return jsonify({'status': 'error', 'message': 'An account with this email already exists', 'code': 403})
        if user:
            user.user_name = name
            user.user_email = email
            user.user_password = generate_password_hash(newPasswd)
            user.user_role = role
            user.user_profile_pic = pic
            # commit
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Account Update Sucessfully', 'code': 200})
    return jsonify({'status': 'error', 'message': 'Incorect Request Method', 'code': 403})
        

@profiles_bp.route('/battery_charge', strict_slashes=False, methods=['GET'])
@login_required
def battery_charge():
    '''serves the charge page'''
    return render_template('battery_charging.html')

@profiles_bp.route('/battery_maintanance', strict_slashes=False, methods=['GET'])
@login_required
def battery_maintain():
    '''serve battery maintenace page'''
    return render_template('battery_maintanance.html')


@profiles_bp.route('/account_bus', strict_slashes=False, methods=['GET'])
@login_required
def account_bus():
    '''Returns information about a bus of a given driver'''
    user_id = current_user.user_id
    driver = Driver.query.filter_by(user_id=user_id).first()
    driver_id = driver.driver_id
    bus = Bus.query.filter_by(driver_id=driver_id).first()
    if bus:
        return jsonify(bus.to_dict())
    else:
        return jsonify({'busId': 'Null'})
    
@profiles_bp.route('/account_bus_update', strict_slashes=False, methods=['PUT'])
@login_required
def account_bus_update():
    '''Updates information about Bus'''
    if request.method == 'PUT':
        bus_model = request.form.get('busModel')
        plate = request.form.get('plate')
        battery_model = request.form.get('batteryModel')
        battery_company = request.form.get('batteryCompany')
        seats = request.form.get('busSeats')
        userId = current_user.user_id
        driver = Driver.query.filter_by(user_id=userId).first()
        driverId = driver.driver_id

        if bus_model and plate and battery_model and battery_company and seats:
            bus = Bus.query.filter_by(driver_id=driverId).first()
            if bus:
                try:
                    bus.busModel = bus_model
                    bus.busPlateNo = plate
                    bus.busBatteryModel = battery_model
                    bus.busBatteryCompany = battery_company
                    bus.busSeatsNo = seats
                    db.session.commit()
                    return jsonify({'status': 'success', 'code': 200, 'message': 'Successfully update bus information'})
                except IntegrityError:
                    db.session.rollback()
                    return jsonify({'status': 'error', 'code': 403, 'message': 'Integrity Error in updating bus information'})
        return jsonify({'status': 'error', 'code': 403, 'message': 'Fill out the form'})
    return jsonify({'status': 'error', 'code': 403, 'message': 'Bad request'})


@profiles_bp.route('/account_garage', methods=['GET'], strict_slashes=True)
@login_required
def account_garage():
    if request.method == 'GET':
        user_id = current_user.user_id
        garageManager = GarageManager.query.filter_by(user_id=user_id).first()
        garageManagerID = garageManager.managerId
        garage = Garage.query.filter_by(managerId=garageManagerID).first()

        if garage:
            return jsonify(garage.to_dict()), 200
        else:
            return jsonify({'garId': 'Null'}), 403
    return jsonify({'status': 'error', 'message': 'Bad request'}), 403