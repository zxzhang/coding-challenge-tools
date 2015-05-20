---------------------------------------------------------------
Existing code: There is no existing code in the project. I wrote all the code.
---------------------------------------------------------------

* How to set up the project

  I used the remote database server. So, you do not need to do "python manage.py migrate".

  You just need to make sure your laptop can use Django to connect to remote Postgre database server.
  Then, run "python manage.py runserver". That is it.

  If you want to set the database, you can use "python manage.py migrate" first. Then run "python load.py" to load the data into database.

  You can use admin to view the data. One user is "admin" and password is "password".

* Description of the problem and solution.

  --SF Movies--

  Create a service that shows on a map where movies have been filmed in San
  Francisco. The user should be able to filter the view using autocompletion
  search.

  The data is available on [DataSF](http://www.datasf.org/): [Film
  Locations](https://data.sfgov.org/Arts-Culture-and-Recreation-/Film-Locations-in-San-Francisco/yitu-d5am).

  I chose the PostgreSQL database in Carnegie Mellon University as the database server. The database configurtion is that:
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2', 
          'NAME': 'contrib_zhengxiz',
          'USER': 'zhengxiz',
          'PASSWORD': 'zhengxiong',
          'HOST': 'contrib-postgres.club.cc.cmu.edu',   # Or an IP Address that your DB is hosted on
          'PORT': '5432',
      }
  }

  I used Django and Google Map API to implement a web application to show all the movies in the given data set on the map. I finished 
  the autocomplete and search feature using Ajax. The web server will provide json or xml data for given movie, position or company. Then,
  browser can use javascript to send POST request to server to sychronize the Marker and Infowindow on the map.

* Whether the solution focuses on back-end, front-end or if it's full stack.

  My solution focuses on back-end, e.g. how the server provide the data and browser use ajax to synchronize it on the map.

* Reasoning behind your technical choices, including architectural. Trade-offs
  you might have made, anything you left out, or what you might do differently
  if you were to spend additional time on the project.

  If I have more time, I will do something like ngrams to make the autocomplete better. Also, I can build users registration and login system, so that
  users can add "like" movie into his favourite list. Also, I can add route in the map. 

* Link to other code you're particularly proud of.

  https://github.com/zxzhang/MapReduceFacility
  https://github.com/zxzhang/Introduction-To-Computer-System

* Link to your resume or public profile.

  https://www.linkedin.com/in/zhengxiongz


