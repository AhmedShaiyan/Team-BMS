# JobTrail
To test, you can download our repository at our GitHub. In a Python virtual environment, you can then download the packages required as listed in requirements.txt.
>>  pip install -r requirements.txt

The secret keys for the OpenAI API, the Django app, and the database details are not given. If you would like, you may sub in your own values for testing, or reach out to us to get access. Once done, set your working directory to Team-BMS\TestTrail and run:
>> python manage.py makemigrations
>> python manage.py migrate
>> python manage.py runserver

The web app will then be hosted on http://127.0.0.1:8000. You will be taken to the sign-up page for the app upon start up. You will be able to create an account, login/logout, upload a resume in PDF format, and receive the list of skills that were identified in the resume.
