# ecommerce-vikas
E-commerce 
This is a simple e-commerce that demonstrates an E-commerce website using the Python Djnago. The application loads products a postgresql database and displays them. Users can select to display products in a single category. Users can click on any product to get more information including pricing.  Users can select items and add them to their shopping cart

Live Demonstration
Here are screenshots.

HOME PAGE
![home](https://user-images.githubusercontent.com/64350435/200903115-740b0668-4077-44b4-b457-99b985bb9ff2.png)

CONTACT PAGE
![contact](https://user-images.githubusercontent.com/64350435/200902214-9658a9e7-32c7-4f13-a03e-977c6389dbeb.png)



REGISTRATION PAGE
![registration](https://user-images.githubusercontent.com/64350435/200902129-9706049f-99d4-4df8-ac68-4283a848d945.png)


LOGIN PAGE
![login page](https://user-images.githubusercontent.com/64350435/200902107-ebfdedc1-5347-41e3-9454-8310dffba71d.png)



ADMIN PANEL PAGE

![admin panel](https://user-images.githubusercontent.com/64350435/200902239-26805105-d645-42c9-b877-c78ec2d2144d.png)




Getting Started

1.Install  VS Code
2.Install PostgreSql

then 
install 
1. pillow 
pip install pillow

2.psycopg2
pip install psycopg2

3. then Change in the setting.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "ecommerce",       #write your database name here
        'USER':"postgres",
        
        'PASSWORD':" ", #write your postgresql database password here 
        'HOST':'localhost',
    } }

4. then do migrate
python manage.py migrate

5. then makemigrations
python manage.py makemigrations

6. then collectstatic
python manage.py collectstatic

7. if you want add product then first create super user to ass django admin panel
python manage.py createsuperuser 

8. then run the project
python manage.py runserver
