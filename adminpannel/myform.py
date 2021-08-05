from django import forms

class addForm(forms.Form):
    addname=forms.CharField()
    addbrand=forms.CharField(required=False)
    adddesc=forms.CharField(required=False)
    addprice=forms.IntegerField(widget=forms.TextInput)
    addavail=forms.DecimalField(widget=forms.TextInput)


    list_of_choices=[
    ('Stationary','Stationary'),
    ('art_supplies','Art Supplies'),
    ('craft_supplies','Craft Supplies'),
    ('customercr','Crafts by Customer')

    ]
    addcat=forms.ChoiceField(choices=list_of_choices)

    addpic=forms.FileField()
class UpdateForm(forms.Form):
    pid=forms.IntegerField(widget=forms.TextInput)
    upname=forms.CharField()
    upbrand=forms.CharField(required=False)
    updesc=forms.CharField(required=False)
    upprice=forms.IntegerField(widget=forms.TextInput)
    upavail=forms.DecimalField(widget=forms.TextInput)


    list_of_choices=[
    ('Stationary','Stationary'),
    ('art_supplies','Art Supplies'),
    ('craft_supplies','Craft Supplies'),
    ('customercr','Crafts by Customer')

    ]
    upcat=forms.ChoiceField(choices=list_of_choices)

    #uppic=forms.FileField()
