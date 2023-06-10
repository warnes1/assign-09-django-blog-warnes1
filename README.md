Repository name: https://github.com/warnes1/assignment-09-django-blog-warnes1

Lesson
  Continuous Integration
  Continuous Deployment
  Setting up GitHub Actions
  Code style enforcement
  Automatic Heroku Deployment

Heroku
  runtime.txt - specify version of python to use
  procfile

Generate requirements.txt file:
  python -m pip freeze > requirements.txt
  We need a requirements.txt  for heroku to know
  which python modules need to be loaded

Push the requirements.txt to github origin
  git add requirements.txt
  git commit -m "Adding requirements.txt"
  git push origin
    5ad740e..2b92133  dev -> dev

Now we will use "github actions" for continuous integration.
  In the github repository select the 'Actions" tab, then select "Configure"
  button for "Dajango - By GitHub Action - Build and Test a Django Project"
  This will add a file to the repository called: .github/workflows/django.yml
    
Now set things for heroku deployment:
  python -m pip install psycopg2-binary whitenoise gunicorn dj-database-url