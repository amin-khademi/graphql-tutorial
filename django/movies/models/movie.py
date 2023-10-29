from django.db import models
from movies.models.category import Category
from movies.models.helper.image_size_validatore import validate_image_size

class Movie(models.Model):

  name = models.CharField(max_length=50)

  image = models.ImageField(
    upload_to="images/%Y/%m/%d/",
    validators=[
      validate_image_size,
    ],
    null=True,
    blank=True
  )

  year = models.IntegerField()

  rating = models.IntegerField()

  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  created_at = models.DateTimeField(
    auto_now_add=True,
  )

  def __str__(self):
    return self.name +" - "+str(self.year)