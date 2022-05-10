
frontend template icontians some information

on macOS:
	virtualenv -p python3.10 NAME

windows:
	python -m venv
	activate:
		source ./script/activate
	pip install ***
	deactivate

pip:
	pip freeze
	python manage.py runserver

github:
	git add .
	git commit -m "Commint"
	git push

edit in model using classes to edit in database this is ORM

python manage.py createsuperuser
abdallah
01099110790aA@
atef.66.ae@gmail.com

django:
	each time you make edit in database you must write a command:
		**python manage.py makemigrations 
		this command may ask you to add default values you can write: '' ==> to add blank input
		==> to check if edits are
		available to be done or not
		**python manage.py makemigrate    ==> to add the edits to database

add your work in admin script to appear in admin page
django model fields


there was a problem appearing on adding category field ===>>> video 7 in minute 8


** is used in older versions of django 
** # from django.conf.urls import url, include


django url path

django model queryset
render means that handling data between "html and database"

templates forlder in job folder, it must be named "templates" to be known by django

class based veiws playlist

django template language


# Static files : [frontend] (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
media files : [upload] images
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


"project/settings.py" in this file has list named "TEMPLATE" in it key named "DIRS" this key is for templates folder that contains the "base.html" that all html will inherite from it


to inhirit from html you create 'base.html', what ever name is, and delete from other html pages the content you want to inhirit from 'base.html' and in base.html i write the syntax you will use  e.g.
{% block body %}   
{% endblock body %}
as we used in the 'base.html' it is used before the html lines you want to inhirit them
then in the html file you want to inhirit to it write 
{% extends 'base.html' %}
in the first line of the html file to tell it to get content from 'base.html'
and the html code between ==>
       {% block body %} 
	   html CONTENT  
	   {% endblock body %}


django template date format


the main URL is named using keyword:namespace" and any other url is named using "name" keyword


django template filter count

django pagination

django slug

#slugify is used to replcae space by dashes -

using slug is better in CSEO

Adding slug steps:
	1- add slug field in models.py: 
		slug = models.SlugField(blank=True, null=True)
	2- override save() builtin function
		def save(self, *args, **kwargs):
			self.slug = slugify(self.title)
			super(Job, self).save(*args, **kwargs)
	3- in 'views.py' add slug as an argument in job_detail()
		def job_detail(request, slug):
		    job_detail = Job.objects.get(slug=slug)
	4- in secondary 'urls.py' job => adding slug as string as:
		path('<str:slug>', views.job_detail, name='job_detail'),
	5- lastly, in html files use slug:
		line: {% url 'jobs:job_detail' job.slug %}
		place:
			<a href="{% url 'jobs:job_detail' job.slug %}"><h4>{{job}}</h4></a>

any new module added must be added in 'admin.py' file to see it there:
	admin.site.register(MODEL_NAME)
	e.g.: ===>>>admin.site.register(Apply)

django bootstrab

the error that appeared in the form is invalid and cannot POST, the solution is to add ==> enctype="multipart/form-data"<== to the html form

django user authentication:
	django documentation
	MDN ==> Mozilla Developer Network

django phone field
django city field
django country field
django signals ---->
simpleisbetterthancomplex.com

django filter:
	https://github.com/carltongibson/django-filter
	https://django-filter.readthedocs.io/en/main/guide/usage.html


django sending email

django rest framework: we use it to make API and convert data to json to be used in mobile and other frameworks

http methods:
	GET
	POST
	PUT
	DELETE

- function based views:
	- simplest way in understanding and coding
	- customize: you can customise ti to your need
	- complex: you can make complex logic using it
- class based views == Generic views:
	- fast development
	- not complex: you cannot make complex operations(logic) using it
https://www.django-rest-framework.org/api-guide/generic-views/
- Viewsets:
	- api --> [model + url] [CURD]
		you can do anything using api but it is not customised, you cannot customize it to your function

django LTS chart


