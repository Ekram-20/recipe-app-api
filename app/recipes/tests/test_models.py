"""Tests for models."""

from django.test import TestCase
from django.contrib.auth import get_user_model
from recipes import models
from unittest.mock import patch


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

    # we mock the behavior because it is random
    @patch('recipes.utils.uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test generating image path."""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'example.jpg')

        self.assertEqual(file_path, f'uploads/recipe/{uuid}.jpg')


class TagModelTests(TestCase):
    """Test Tag model."""

    def test_create_tag(self):
        """Test creating a tag is successful."""
        user = get_user_model().objects.create_user(
            email='user@example.com',
            password='test123',
        )
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag), tag.name)


class IngredientModelTests(TestCase):
    """Test Tag model."""

    def test_create_ingredient(self):
        """Test creating an ingredient is successful."""
        user = get_user_model().objects.create_user(
            email='user@example.com',
            password='test123',
        )
        ingredient = models.Ingredient.objects.create(
            user=user,
            name='Ingredient1'
        )

        self.assertEqual(str(ingredient), ingredient.name)
