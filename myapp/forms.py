from django import forms

from .models import myRecord

class PersonForm(forms.ModelForm):

    class Meta:
        model = myRecord
        fields = ('active_ind',  'prefix_txt',  'first_nm_txt',  'middle_nm_txt',  'last_nm_txt',  'suffix_txt',  'nickname_txt',  
                  'pronounced_txt',  'gender_cd',  'birth_dt',  'other_id',  
                  'address_street1',  'address_street2',  'city_cd',  'state_cd',  'zip_cd',  'zip_cd_ext',  
                  'county_nm_txt',  'email_txt',  
                  'phone1_number',  'phone1_extension',  'phone1_type_cd',  
                  'phone2_number',  'phone2_extension',  'phone2_type_cd',  
                  'phone3_number',  'phone3_extension',  'phone3_type_cd' ) #,  'person_image' )
