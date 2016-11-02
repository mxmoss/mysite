from django import forms
from .models import myRecord

class PersonForm(forms.ModelForm):
    active_ind = forms.BooleanField(
                                 required=False,
                                 label='Active',
#                                 widget = forms.BooleanField(attrs={'style': 'text-align: left;', 'title': 'Active',}),
                                 )
                                 
    prefix_txt = forms.CharField(
                                 label='Prefix',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'small-name-edit', 'title': 'Prefix',}))
    
    middle_nm_txt = forms.CharField(
                                 label='MI',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'medium-name-edit', 'title': 'MI',}))
    
    suffix_txt = forms.CharField(
                                 label='Suffix',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'small-name-edit', 'title': 'Suffix',}))

    first_nm_txt = forms.CharField( #label='First Name', help_text='foo bar',
                                 label='First',
                                 required=True,
                                 widget = forms.TextInput(attrs={'class': 'big-name-edit',}))

    last_nm_txt = forms.CharField(
                                 label='Last',
                                 required=True,
                                 widget = forms.TextInput(attrs={'class': 'big-name-edit', 'title': 'Last Name',}))
                                 
    nickname_txt = forms.CharField(
                                 label='Nickname',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'big-name-edit', 'title': 'Nickname',}))

    pronounced_txt = forms.CharField(
                                 label='Pronounced',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'big-name-edit', 'title': 'Pronounced',}))
                                 
    other_id = forms.CharField(
                                 label='Other ID',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'medium-name-edit', 'title': 'Other ID',}))

#Address info formatting
    address_street1 = forms.CharField(
                                 label='Address 1',
                                 required=True,
                                 widget = forms.TextInput(attrs={'class': 'big-name-edit', 'title': 'Address 1',}))
    address_street2 = forms.CharField(
                                 label='Address 2',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'big-name-edit', 'title': 'Address 2',}))
    city_cd = forms.CharField(
                                 label='City',
                                 required=True,
                                 widget = forms.TextInput(attrs={'class': 'medium-name-edit', 'title': 'City',}))
    zip_cd = forms.CharField(
                                 label='Zip Code',
                                 required=True,
                                 widget = forms.TextInput(attrs={'class': 'small-name-edit', 'title': 'Zip Code',}))
    zip_cd_ext = forms.CharField(
                                 label='Zip Code+4',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'small-name-edit', 'title': 'Zip Code Extension',}))
    county_nm_txt = forms.CharField(
                                 label='County',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'big-name-edit', 'title': 'County',}))
#Birthdate formatting
    birth_dt = forms.DateField(
                                 label='Birthdate',
                                 required=False,
                                 widget = forms.SelectDateWidget(attrs={'class': 'date', 'title': 'Birth Date',}, years=range(2016,1910,-1) ))
#Email formatting
    email_txt = forms.CharField(
                                 label='E-Mail',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'big-name-edit', 'title': 'Email',}))
                                 
#Phone info formatting
    phone1_number = forms.CharField(
                                 label='Phone 1',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'phone-number', 'title': 'Phone 1',}))
    phone2_number = forms.CharField(
                                 label='Phone 2',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'phone-number', 'title': 'Phone 2',}))
    phone3_number = forms.CharField(
                                 label='Phone 3',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'phone-number', 'title': 'Phone 3',}))
                                 
    phone1_extension = forms.CharField(
                                 label='Ext 1',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'phone-ext', 'title': 'Phone 1 Ext',}))
    phone2_extension = forms.CharField(
                                 label='Ext 2',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'phone-ext', 'title': 'Phone 2 Ext',}))
    phone3_extension = forms.CharField(
                                 label='Ext 3',
                                 required=False,
                                 widget = forms.TextInput(attrs={'class': 'phone-ext', 'title': 'Phone 3 Ext',}))
    comments_txt = forms.CharField(
                                 label='Comments',
                                 required=False,
                                 widget = forms.Textarea(attrs={'title': 'Comments',}))
                                 
    class Meta:
        model = myRecord
        fields = (
                  'active_ind',
                  'last_nm_txt',
                  'first_nm_txt',
                  'middle_nm_txt',
                  'prefix_txt',
                  'suffix_txt',
                  'nickname_txt',
                  'pronounced_txt',
                  'gender_cd',
                  'birth_dt',
                  'other_id',
                  'address_street1',
                  'address_street2',
                  'city_cd',
                  'state_cd',
                  'zip_cd',
                  'zip_cd_ext',
                  'county_nm_txt',
                  'email_txt',
                  'phone1_number',
                  'phone1_extension',
                  'phone1_type_cd',
                  'phone2_number',
                  'phone2_extension',
                  'phone2_type_cd',
                  'phone3_number',
                  'phone3_extension',
                  'phone3_type_cd',
									'comments_txt',
        ) 
                  #'person_image' )
