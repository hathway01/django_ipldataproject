======
IPL DATA PROJECT
======

IPL DATA PROJECT is a simple django app that takes a csv file and plots the graph for following questions using high charts.




Quick start:
--------------

1. Add "project" to your INSTALLED_APPS setting like this::
	INSTALLED_APPS = [
		...
		'dataproject',
		...
		]

2. Include the project URLconf in your project urls.py like this::
	path('project/',include('project.urls')),

3. Run './manage.py migrate' to create the project models.

4. Start the development server and visit localhost:8000/admin to create project.
5. Visit localhost:8000/project/ to view the project.
