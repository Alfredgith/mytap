from django.db import models





term=(('1','1'), ('2','2'), ('first','iron'),('second','zinc'))


class cas(models.Model):
      times=models.CharField(max_length=20,choices=term)
      email=models.EmailField()
      






