from django.utils.translation import ugettext as _
from django.core.validators import MaxLengthValidator

def update_field_length(field, length):
    if hasattr(field, "max_length"):
        field.max_length = length

    if hasattr(field, "widget"):
        field.widget.attrs['maxlength'] = length

    if hasattr(field, "help_text"):
        field.help_text = _("Required, %s characters or fewer. Only letters, "
                            "numbers, and characters such as @.+_- are "
                            "allowed." % length)

    if hasattr(field, "validators"):
        # we need to find the MaxLengthValidator and change its
        # limit_value otherwise the auth forms will fail validation
        for v in field.validators:
            if isinstance(v, MaxLengthValidator):
                v.limit_value = length
