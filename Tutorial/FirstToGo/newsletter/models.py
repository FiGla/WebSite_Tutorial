from django.db import models

class SignUp(models.Model):
        email = models.EmailField()
        full_name = models.CharField(max_length = 120,blank=True,null = True)
        #you will need one time
        timestamp = models.DateTimeField(auto_now_add=True , auto_now = False)
        #updated you can update many time
        updated = models.DateTimeField(auto_now_add=False , auto_now = True,null=True)
        choics = models.IntegerField(default=1,null=True)

        def __unicode__(self):
            return self.email
