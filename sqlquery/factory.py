import factory
from factory.faker import faker
from .models import Product

FAKE = faker.Faker()


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("sentence", nb_words=12)
    description = factory.Faker("text", max_nb_chars=1000)
    slug = factory.Faker("slug")
    price = factory.Faker("random_digit")
    quantity = factory.Faker("random_digit")
    created_at = factory.Faker("date_time_this_year")
    updated_at = factory.Faker("date_time_this_year")
