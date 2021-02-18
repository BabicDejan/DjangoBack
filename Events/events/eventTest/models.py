from django.db import models

# Create your models here.
class Event(models.Model):
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
