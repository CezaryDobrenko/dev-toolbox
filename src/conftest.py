import json

import pytest
from graphene_django.utils.testing import graphql_query


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        response = graphql_query(
            *args, **kwargs, client=client, headers={}, graphql_url="/graphql/"
        )
        return json.loads(response.content)

    return func
