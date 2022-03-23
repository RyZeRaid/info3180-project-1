"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory
from .forms import Property
from .models import Properties
from werkzeug.utils import secure_filename
from operator import length_hint


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['GET', 'POST'])
def create():
    propertyform = Property()

    if request.method == 'POST' and propertyform.validate_on_submit():
        title = propertyform.prop_title.data
        description = propertyform.description.data
        rooms = propertyform.num_rooms.data
        bathrooms = propertyform.num_bathrooms.data
        price = propertyform.price.data
        prop_type = propertyform.prop_type.data
        location = propertyform.location.data
        photo = propertyform.photo.data
        photo_name = secure_filename(photo.filename)
        
        photo.save((os.path.join(app.config['UPLOAD_FOLDER'], photo_name)))

        property1 = Properties(title, description, rooms, bathrooms, price, prop_type, location, photo_name)
        db.session.add(property1)
        db.session.commit()

        flash('A new property has been successfully added', 'success')

        return redirect(url_for('properties'))

    return render_template('propertycreate.html', form = propertyform)

@app.route('/properties')
def properties():

    if get_info != []:
        return render_template('properties.html', prop = get_info()) 

@app.route('/properties/<int:id>')
def propetyid(id):
    properties = Properties.query.get_or_404(id)
    return render_template('property.html', properties = properties)

@app.route("/properties/create/<filename>")
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), path=filename)

def get_info():
    info = Properties.query.all()
    return info

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)




@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
