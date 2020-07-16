from django import forms

class CostForm(forms.Form):

    date = forms.DateField()

    cost = forms.FloatField()



class RegistrationForm(forms.Form):
   teamname = forms.CharField(max_length = 50)
   player1 = forms.CharField(max_length = 50)
   player2 = forms.CharField(max_length = 50)
   player3 = forms.CharField(max_length = 50)
   player4 = forms.CharField(max_length = 50)
   player5 = forms.CharField(max_length = 50)
   player6 = forms.CharField(max_length = 50)
   player7 = forms.CharField(max_length = 50)
   player8 = forms.CharField(max_length = 50)
   player9 = forms.CharField(max_length = 50)
   player10 = forms.CharField(max_length = 50)
   player11 = forms.CharField(max_length = 50)
   coach = forms.CharField(max_length = 50)
   manager = forms.CharField(max_length = 50)