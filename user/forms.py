from django import forms
class RegisterForm(forms.Form):
    username= forms.CharField(widget= forms.TextInput
                           (attrs={'class':'form-control px-5 '
				   }),label="Kullanıcı adı: ")
    password= forms.CharField(widget= forms.PasswordInput
                           (attrs={'class':'form-control px-5'
				   }),label="Parola: ")
    confirm= forms.CharField(widget= forms.PasswordInput
                           (attrs={'class':'form-control px-5'
				   }),label="Parola(Tekrar)")
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        if password and confirm and password!=confirm:
            raise forms.ValidationError("Parolalar uyuşmamaktadır...")
        values={
            "username":username,
            "password":password
        }
        return values


class LoginForm(forms.Form):
    #username= forms.CharField(widget= forms.TextInput
                           #(attrs={'class':'form-control px-5'
				   #}),label="username")

    username=forms.CharField(label="username") 
         
    password=forms.CharField(label="password" , widget=forms.PasswordInput)
    """
    password= forms.CharField(widget= forms.PasswordInput
                           (attrs={'class':'form-control px-5'
				   }),label="password")"""
