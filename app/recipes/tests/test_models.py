"""Tests for models."""

from django.test import TestCase
from django.contrib.auth import get_user_model
from recipes import models


class RecipeModelTests(TestCase):
    """Test models."""

    def test_create_recipe(self):
        """Test creating a recipe is successful."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=5.50,
            description='Sample recipe description.',
        )

        self.assertEqual(str(recipe), recipe.title)
