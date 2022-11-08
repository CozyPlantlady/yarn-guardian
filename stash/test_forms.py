from django.test import TestCase
from .forms import AddYarnForm
from .models import Yarn


class TestAddYarnForm(TestCase):

    def test_yarn_producer_is_required(self):
        form = AddYarnForm({'producer': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('producer', form.errors.keys())
        self.assertEqual(form.errors['producer'][0], 'This field is required.')

    def test_yarn_name_is_required(self):
        form = AddYarnForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = AddYarnForm()
        self.assertEqual(
            form.Meta.fields, ['producer', 'name', 'body',
                               'color_group', 'color_name', 'color_code',
                               'amount', 'weight', 'material', 'favorite',
                               'frogged', ])
