from django.db import models

# Create your models here.

class Stage(models.Model):
    stage_name = models.CharField(max_length=100)
    stage_place = models.CharField(max_length=20)
    
    def __str__(self):
        return self.stage_name

class Event(models.Model):
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, null=True)
    event_name = models.CharField(max_length=30)
    MUZICKI = "Muzicki"
    FILMSKI =  "Filmski"
    LIKOVNI = "Likovni"
    PLESNI = "Plesni"
    KULINARSKI = "Kulinarski"
    CATEGORY_CHOICES = [
        (MUZICKI, "Muzicki"),
        (FILMSKI, "Filmski"),
        (LIKOVNI, "Likovni"),
        (PLESNI, "Plesni"),
        (KULINARSKI, "Kulinarski"),
    ]
    category = models.CharField(max_length=10,
    choices = CATEGORY_CHOICES,
    default = MUZICKI,
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.CharField(max_length=500)
    event_img = models.URLField(default="#")

    def __str__(self):
        return self.event_name


