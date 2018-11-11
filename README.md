# Django_Utility

This Repository Contains Various Django related projects
  Project contains :
  Django Scheduler :
  packages required :
        
        > Django
        > djcelery
        Installations required
        django-celery==3.2.1


        Installation of Redis Server :

        sudo apt install redis-server
        verify it by cmd
        > ping 
        if response
        > pong 
        Means redis server is properly  installed and ready to use

        #########################################################

        To start server
        python manage.py runserver

        Start celery worker
        celery -A schedular worker -l info


        For scheduled jobs/cron jobs
        python manage.py celerybeat
