from django import forms
class LoginForm(forms.Form):
    username=forms.CharField(max_length=80,min_length=2,label="User Name")
    password=forms.CharField(min_length=5,label="Password",widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    first_name=forms.CharField(max_length=150,min_length=2,label="Name - Surname")
    username=forms.CharField(max_length=80,min_length=2,label="User Name")
    email=forms.EmailField(min_length=5,label="Email")
    password=forms.CharField(min_length=5,label="Password",widget=forms.PasswordInput)
    confirm=forms.CharField(min_length=5,label="Confirm Password",widget=forms.PasswordInput)
    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        email=self.cleaned_data.get("email")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Password does not match!")

        values = {
            "first_name": first_name,
            "username":username,
            "password" : password,
            "email":email,
        }
        return values  




