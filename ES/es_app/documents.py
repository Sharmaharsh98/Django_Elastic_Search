from django_elasticsearch_dsl import (
    Document,
    fields,
    Index,
)
from .models import Alphabets
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class AlphaDocs(Document):
    class Index:
        name = 'alphabets'

    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }

    class Django:
        model = Alphabets
        fields = ['alphabet', 'word']

# alphabets_index.create()