from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField, SubmitField, TextAreaField


class MessageForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('信息', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField('发布')
    pass
