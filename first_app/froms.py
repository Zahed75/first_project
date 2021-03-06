from django import forms


class user_form(forms.Form):
    # <label for="user_name">Full-Name</label>
    # <input type="text" name="user_name" value="Name.." required>
    user_name = forms.CharField(required=True,label="Full_Name",widget=forms.TextInput(
    attrs={'placeholder':'Enter Your full name'} ))
      # <label for="user_name">Your Mail</label>
      # <input type="email" name="user_email" value="someone@gmail.com" required>
    user_dob=forms.DateField(label="Date of Birth",widget=forms.TextInput(
    attrs={'type':'date'}
    ))
    user_email = forms.EmailField(label="Email",widget=forms.TextInput(
    attrs={'placeholder':'Enter Your Mail'} ))
