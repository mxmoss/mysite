from django.db import models
from django.utils import timezone

class myRecord(models.Model):
  STATE_CHOICES = (
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AS', 'American Samoa'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MP', 'Northern Mariana Islands'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NA', 'National'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VI', 'Virgin Islands'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming'),
  )

  PHONE_TYPE_CHOICES = (
    ('H', 'Home'),
    ('W', 'Work'),
    ('M', 'Mobile'),
    ('O', 'Other'),
  )
  GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown'),
  )
#  person_id = models.AutoField(primary_key=True)
  active_ind = models.BooleanField(default=True)
  prefix_txt = models.CharField(max_length=25, blank=True, default='')
  first_nm_txt = models.CharField(max_length=255, blank=False, default='')
  middle_nm_txt = models.CharField(max_length=255, blank=True, default='')
  last_nm_txt = models.CharField(max_length=255, blank=False, default='')
  suffix_txt = models.CharField(max_length=25, blank=True, default='')
  nickname_txt = models.CharField(max_length=255, blank=True, default='')
  pronounced_txt = models.CharField(max_length=255, blank=True, default='')
  gender_cd = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, default='')
  birth_dt = models.DateTimeField(blank=False, null=True,)
  other_id = models.CharField(max_length=50, blank=True, default='')
  address_street1 = models.CharField(max_length=50, blank=False, default='')
  address_street2 = models.CharField(max_length=50, blank=True, default='')
  city_cd = models.CharField(max_length=50, blank=False, default='')
  state_cd = models.CharField(max_length=2, choices=STATE_CHOICES, default='OR', blank=False)
  zip_cd = models.CharField(max_length=5, blank=False, default='')
  zip_cd_ext = models.CharField(max_length=4, blank=True, default='')
  county_nm_txt = models.CharField(max_length=50, blank=True, default='')
  email_txt = models.EmailField(max_length=254, blank=True, default='')
  phone1_number = models.CharField(max_length=14, blank=True, default='')
  phone1_extension = models.CharField(max_length=10, blank=True, default='')
  phone1_type_cd = models.CharField(max_length=15, choices=PHONE_TYPE_CHOICES, blank=True, default='')
  phone2_number = models.CharField(max_length=14, blank=True, default='')
  phone2_extension = models.CharField(max_length=10, blank=True, default='')
  phone2_type_cd = models.CharField(max_length=15, choices=PHONE_TYPE_CHOICES, blank=True, default='')
  phone3_number = models.CharField(max_length=14, blank=True, default='')
  phone3_extension = models.CharField(max_length=10, blank=True, default='')
  phone3_type_cd = models.CharField(max_length=15, choices=PHONE_TYPE_CHOICES, blank=True, default='')
  comments_txt = models.TextField(default='')
  add_dt = models.DateTimeField(auto_now=True) #, default=timezone.now)
  added_by = models.ForeignKey('auth.User')
  edit_dt = models.DateTimeField(blank=True, null=True)
  edited_by = models.CharField(max_length=50, blank=True, default='')
  delete_dt = models.DateTimeField(blank=True, null=True)
  deleted_by = models.CharField(max_length=50, blank=True, default='')
#  person_image = models.ImageField(height_field=100, width_field=100)
  
  def publish(self):
      self.published_date = timezone.now()
      self.save()
        
  def delete(self):
    self.active_ind = 'I'
    self.delete_dt = timezone.now()
    self.deleted_by = auth.User
    self.save()

  def __str__(self):
    return '{last}, {first}'.format(last='last_nm_txt', first='first_nm_txt')