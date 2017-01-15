from django.forms.widgets import TextInput, PasswordInput, EmailInput
from django.utils.html import format_html

# ref https://github.com/django/django/blob/stable/1.8.x/django/forms/widgets.py
class PhoneTextInput(TextInput):

    def render(self, name, value, attrs=None):
        # Unlike inputs using paper-input-container directly,
        # paper-input does not work out of the box with the native form
        # element.
        if value is None:
            html = u"""<gold-phone-input label='Номер телефона' name="{0}" maxlength="13" country-code="7" phone-number-pattern="XXX-XXX-XX-XX">
            <label>Номер телефона</label>
            </gold-phone-input>"""
            return format_html(html, name)
        else:
            html = u"""<gold-phone-input label='Номер телефона' name="{0}" maxlength="13" country-code="7" phone-number-pattern="XXX-XXX-XX-XX" attr-for-value="value">
            <label>Номер телефона</label>
            </gold-phone-input>"""
            return format_html(html, name, value)

class PaperTextInput(TextInput):

    def render(self, name, value, attrs=None):
        # Unlike inputs using paper-input-container directly,
        # paper-input does not work out of the box with the native form
        # element.
        if value is None:
            html = u"""<paper-input-container label='{0}'>
            <label>{0}</label>
            <input is="iron-input" name="{0}" placeholder=" " class="paper-input-input">
            </paper-input-container>"""
            return format_html(html, name,)
        else:
            html = u"""<paper-input-container label='{0}' attr-for-value="value">
            <label>{0}</label>
            <input is="iron-input" name="{0}" placeholder=" "  value="{1}">
            </paper-input-container>"""
            return format_html(html, name, value)

class PaperTextInputName(TextInput):

    def render(self, name, value, attrs=None):
        # Unlike inputs using paper-input-container directly,
        # paper-input does not work out of the box with the native form
        # element.
        if value is None:
            html = u"""<paper-input-container label='{0}'>
            <input is="iron-input" name="{0}" placeholder="Введите Ваше имя" class="paper-input-input">
            </paper-input-container>"""
            return format_html(html, name,)
        else:
            html = u"""<paper-input-container label='{0}' attr-for-value="value">
            <label>{0}</label>
            <input is="iron-input" name="{0}" placeholder=" "  value="{1}">
            </paper-input-container>"""
            return format_html(html, name, value)

class PaperPasswordInput(PasswordInput):

    def render(self, name, value, attrs=None):
        if value is None:
            html = u"""<paper-input-container label='{0}'>
            <label>{0}</label>
            <input is="iron-input" name="{0}" type="password"/>
            </paper-input-container>"""
            return format_html(html, name)
        else:
            html = u"""<paper-input-container label='{0}'  type="password" attr-for-value="value">
            <label>{0}</label>
            <input is="iron-input" name="{0}" type="password" value="{1}"/>
            </paper-input-container>"""
            return format_html(html, name, value)

class PaperEmailInput(EmailInput):
    def __init__(self, attrs=None):
        if attrs is not None:
            self.attrs = attrs.copy()
        else:
            self.attrs = {}
    def render(self, name, value, attrs=None):
        if value is None:
            html = u"""<paper-input-container label='{0}' autoValidate>
            <label>{0}</label>
            <input is="iron-input" name="{1}" type="email">
            </paper-input-container>"""
            if 'label' in self.attrs:
                return html.format(self.attrs['label'], name)
            else:
                return format_html(html, name, name)
        else:
            html = u"""<paper-input-container label='{0}' autoValidate attr-for-value="value">
            <label>{0}</label>
            <input is="iron-input" name="{0}" value="{1}" type="email">
            </paper-input-container>"""
            return format_html(html, name, value)