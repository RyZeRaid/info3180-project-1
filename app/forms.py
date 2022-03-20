from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, DataRequired , Length

class Property(FlaskForm):
    prop_title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators = [InputRequired()])
    num_rooms = IntegerField('No. of Rooms', validators = [InputRequired()])
    num_bathrooms = IntegerField('No. of Bathrooms', validators = [InputRequired()])
    price = IntegerField('Price', validators = [InputRequired()])
    prop_type = SelectField('Type', choices=[('House','House'), ('Apartment', 'Apartment')])
    location = StringField('Location', validators = [InputRequired()])
    photo = FileField('Photo', validators = [FileRequired(),FileAllowed(['jpg', 'png'])])