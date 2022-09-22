import datetime

from rest_framework import fields, serializers, ISO_8601
from rest_framework.settings import api_settings
from month import Month, models


class MonthField(fields.DateField):

    def to_internal_value(self, value):
        month: Month = None
        if isinstance(value, Month):
            month = value
        elif isinstance(value, datetime.datetime):
            month = Month.from_date(value)
            if len(str(month.year)) < 4:
                raise serializers.ValidationError(
                    self.error_messages['invalid_year'],
                    code='invalid_year',
                    # params={'value': value},
                )
        else:
            month = None
        return month

    def to_representation(self, value):
        if not value:
            return None
        # base-code from DRF
        # output_format = getattr(self, 'format', api_settings.DATE_FORMAT)
        output_format = getattr(self, 'format', '%Y-%m')
        if output_format is None or isinstance(value, str):
            return value

        # Applying a `DateField` to a datetime value is almost always
        # not a sensible thing to do, as it means naively dropping
        # any explicit or implicit timezone info.
        # assert not isinstance(value, datetime.datetime), (
        assert not isinstance(value, Month) or not isinstance(value, datetime.datetime), (
            'Expected a `Month` or `date`, but got a `datetime`. Refusing to coerce, '
            'as this may mean losing timezone information. Use a custom '
            'read-only field and deal with timezone issues explicitly.'
        )

        if output_format.lower() == ISO_8601:
            return value.isoformat()

        return value.strftime(output_format)


