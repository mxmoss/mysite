from django import forms

from .models import myRecord

class PersonForm(forms.ModelForm):
#    prefix_txt = forms.CharField(max_length=5, required=False, widget = forms.TextInput(attrs={'width': 100, 'title': 'Prefix',}))
    prefix_txt = forms.CharField(max_length=5, 
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 50px;', 'title': 'Prefix',}))
    
    middle_nm_txt = forms.CharField(max_length=5,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 50px;', 'title': 'MI',}))
    
    suffix_txt = forms.CharField(max_length=5,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 50px;', 'title': 'Suffix',}))

    first_nm_txt = forms.CharField(max_length=30,
                                 required=True,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'First Name',}))

    last_nm_txt = forms.CharField(max_length=30,
                                 required=True,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'Last Name',}))
                                 
    nickname_txt = forms.CharField(max_length=30,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'Nickname',}))

    pronounced_txt = forms.CharField(max_length=30,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'Pronounced',}))
                                 
    other_id = forms.CharField(max_length=30,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'Other ID',}))

#Address info formatting
    address_street1 = forms.CharField(max_length=50,
                                 required=True,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'Address 1',}))
    address_street2 = forms.CharField(max_length=50,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'Address 2',}))
    city_cd = forms.CharField(max_length=50,
                                 required=True,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'City',}))
    zip_cd = forms.CharField(max_length=5,
                                 required=True,
                                 widget = forms.TextInput(attrs={'style': 'width: 50px;', 'title': 'Zip Code',}))
    zip_cd_ext = forms.CharField(max_length=4,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 50px;', 'title': 'Zip Code Extension',}))
    county_nm_txt = forms.CharField(max_length=50,
                                 required=True,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'County',}))
#Email formatting
    email_txt = forms.CharField(max_length=50,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 250px;', 'title': 'Email',}))
                                 
#Phone info formatting
    phone1_number = forms.CharField(max_length=12,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 150px;', 'title': 'Phone 1',}))
    phone2_number = forms.CharField(max_length=12,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 150px;', 'title': 'Phone 2',}))
    phone3_number = forms.CharField(max_length=12,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 150px;', 'title': 'Phone 3',}))
                                 
    phone1_extension = forms.CharField(max_length=8,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 50px;', 'title': 'Phone 1 Ext',}))
    phone2_extension = forms.CharField(max_length=8,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 50px;', 'title': 'Phone 2 Ext',}))
    phone3_extension = forms.CharField(max_length=8,
                                 required=False,
                                 widget = forms.TextInput(attrs={'style': 'width: 50px;', 'title': 'Phone 3 Ext',}))
                                 
    birth_dt = forms.DateField(widget=forms.SelectDateWidget())
    class Meta:
        model = myRecord
        fields = ('active_ind',  'prefix_txt',  'first_nm_txt',  'middle_nm_txt',  'last_nm_txt',  'suffix_txt',  'nickname_txt',  
                  'pronounced_txt',  'gender_cd',  'birth_dt',  'other_id',  
                  'address_street1',  'address_street2',  'city_cd',  'state_cd',  'zip_cd',  'zip_cd_ext',  
                  'county_nm_txt',  'email_txt',  
                  'phone1_number',  'phone1_extension',  'phone1_type_cd',  
                  'phone2_number',  'phone2_extension',  'phone2_type_cd',  
                  'phone3_number',  'phone3_extension',  'phone3_type_cd' ) #,  'person_image' )
