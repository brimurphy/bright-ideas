from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class PrettyFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Currently')
    input_text = _('')
    template_name = 'products/custom_widget_templates/pretty_file_input.html'
