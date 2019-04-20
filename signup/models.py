from django.db import models

class SaveUserDetails(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return "Email " + self.email + " Username " + self.username + " Password " + self.password
