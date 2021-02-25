from django import forms


class LoginForm(forms.Form):
    """
    Form of authorization
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)  # in file.html will be generation as
                                                            # element <input> where type = "password"
