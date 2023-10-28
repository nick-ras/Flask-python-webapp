from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from src.accounts.models import User
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, DateTimeField, SubmitField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    email = EmailField(
        "Email", validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        "Repeat password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match."),
        ],
    )

    def validate(self):
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        if self.password.data != self.confirm.data:
            self.password.errors.append("Passwords must match")
            return False
        return True
  class Boxes(db.Model):
			id = db.Column(db.Integer, primary_key=True)
			location = db.Column(db.String(100))
			size = db.Column(db.Integer)
			in_use = db.Column(db.Boolean, default=False)
			booked_on = db.Column(db.DateTime)
		location = StringField('Location', validators=[DataRequired()])
		size = IntegerField('Size', validators=[DataRequired()])
		duration = IntegerField('Duration', validators=[DataRequired()])
		submit = SubmitField('Book Box')

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])