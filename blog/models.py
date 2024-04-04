from django.db import models

class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=10)
    Username = models.CharField(max_length=12)
    Password = models.CharField(max_length=16)
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.Firstname, self.Lastname, self.Email, self.Phone, self.Username, self.Password)

class Publisher(models.Model):
    Authorname = models.CharField(max_length=50)
    Titlename = models.CharField(max_length=50)
    Content = models.CharField(max_length=5000)
    Published_date = models.DateField()
    Published_time = models.CharField(max_length=50)
    Blog_name = models.CharField(max_length=50)
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.Authorname, self.Titlename, self.Content, self.Published_date, self.Published_time, self.Blog_name)