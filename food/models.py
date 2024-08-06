from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    user_name = models.ForeignKey(User, on_delete = models.CASCADE, default = 1 )
    item_name = models.CharField(max_length = 200)
    item_desc = models.CharField(max_length = 200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length = 500, default="https://imgs.search.brave.com/0IOQ36WzS8XUXevrHw22EYgKB9yC8U_fq8_lE0Et65s/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTM1/Nzg4MDQ4Ny92ZWN0/b3IvbG9hZGluZy5q/cGc_cz02MTJ4NjEy/Jnc9MCZrPTIwJmM9/WHhsNmpSeTB0b25E/M0NRLWRzSXdNb2R4/b3VhS0dJcjRvYkFG/MlphMURnST0")

    def get_absolute_url(self):
        return reverse("food:detail",kwargs = {"pk" : self.pk})

