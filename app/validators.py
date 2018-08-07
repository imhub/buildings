import datetime
from django.core.exceptions import ValidationError

def validate_year_built(value):
    if value not in range(datetime.datetime.now().year):
        raise ValidationError(
            ('%(value)s is not a valid year'),
            params={'value': value},
        )

def validate_birth_date(value):
    if value > datetime.date.today():
        raise ValidationError(
            ('%(value)s is not a valid birth date'),
            params={'value': value},
        )