from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, SelectField, DateField
from wtforms.validators import DataRequired
from ..models import STATUS_CHOICES


# TODO: Think about max_length validation
class TaskForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    # TODO: Think about more difficult logic
    status = SelectField('Status', choices=STATUS_CHOICES, coerce=int, validators=[DataRequired()])

    # TODO: Make it datetimefield
    #start_date = DateField('Start date', validators=[DataRequired()])
    #end_date = DateField('End date')
    # project select?
    # perfomers select?

    submit = SubmitField('Submit')

class ProjectForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    short_name = StringField('Short name', validators=[DataRequired()])
    description = StringField('Description')
    status = SelectField('Status', choices=STATUS_CHOICES, coerce=int, validators=[DataRequired()])
    # tasks
    submit = SubmitField('Submit')
