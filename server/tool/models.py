from django.db import models


# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now_add=True)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.created_time.empty_strings_allowed = True

    def __str__(self):
        return self.text[:20]
