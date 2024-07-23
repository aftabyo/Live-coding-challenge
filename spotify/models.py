from django.db import models

#we can create the user profiles in the models.py file 
#here as we create the models , it will register in the database as a field

class user_profiles(models.Model):
    name=models.CharField(max_length=50,blank=False)
    age=models.IntegerField()
    profile_picture=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None) #We can modify this as per our convinience and use S3 bucket or other plaforms to store that image
    bio=models.CharField(max_length=150,blank=True)


#for registering these fields we have to use the command python manage.py makemigrations , to initiate the migration
#followed by python manage.py migrate , to finally push the changes into  the database