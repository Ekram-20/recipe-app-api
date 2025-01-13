from django.conf import settings
from django.db import models

from recipes.utils import recipe_image_file_path


class Recipe(models.Model):
    """Recipe object."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        blank=True
    )
    time_minutes = models.IntegerField()
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    link = models.CharField(
        max_length=255,
        blank=True,
    )
    tags = models.ManyToManyField('Tag')
    ingredients = models.ManyToManyField('Ingredient')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)

    def __str__(self):
        """Return string representation of recipe."""
        return self.title


class Tag(models.Model):
    """Tag for filtering recipes."""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient for recipes."""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
