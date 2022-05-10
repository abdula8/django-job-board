from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import FileField
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import datetime



# Create your models here.
'''
django model field:
    - html widget
    - validation
    - db size


'''
JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    n = datetime.now()
    str_date = str(n.year)+str(n.month)+str(n.day)
    str_time = str(n.month)+str(n.minute)+str(n.second)
    name = str(instance.id) + '__' + str_date + str_time
    return "jobs/%s/%s.%s"%(instance.id, name, extension)

class Job(models.Model): #class=table, here we enherite from models
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) # equivelant to column in SQL
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    describtion = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) # we put 'category' between '' because it is defined after this line يعني لو عرفتها قبل السطر دا متحطهاش بين السنجل كوتس 
    #on_delete means incase of deleteing item or specific category,  CASCADE to delete all things related to the deleted item (category)
    # hte following line requires Pillow module to be installed
    #pythpn -m pip install Pillow
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null=True)

#override the save method
#using super() to implement its function and my funciton
    def save(self, *args, **kwargs):
        ## logic
        self.slug = slugify(self.title) #slugify is used to replcae space by dashes -
        super(Job, self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

# str method is used to see what is inside list when you display it.
    def __str__(self):
        return self.name



class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
