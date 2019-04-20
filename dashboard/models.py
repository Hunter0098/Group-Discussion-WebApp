from django.db import models

class chatDatabase(models.Model):
    serialNo = models.IntegerField()
    username = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return "Serial no: " + str(self.serialNo) + ", Username " + self.username + ", Message: " + self.message
