from elasticsearch import Elasticsearch

client = Elasticsearch(
    cloud_id="document_analisis:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyRiNDBiYTc4OWIwMjU0ZWUyYjE5NWQ4MjEzYzYyNzI1ZiQ4ODQ0ZWFjZWNlYzU0MDM1YjQ4NDVlMzFmNTViZTRmYg==",
    basic_auth=("elastic", "Gu1JSSWaqIBkMKEdwmmIOalX")
)

body = {
    "name": "my-cross-cluster-api-key",
    "expiration": "1d",
    "access": {
        "search": [{"names": ["logs*"]}],
        "replication": [{"names": ["archive*"]}]
    },
    "metadata": {
        "description": "phase one",
        "environment": {
            "level": 1,
            "trusted": True,
            "tags": ["dev", "staging"]
        }
    }
}

resp = client.security.create_cross_cluster_api_key(
    name="my-cross-cluster-api-key",
    expiration="1d",
    access={
        "search": [{"names": ["logs*"]}],
        "replication": [{"names": ["archive*"]}]
    },
    metadata={
        "description": "phase one",
        "environment": {
            "level": 1,
            "trusted": True,
            "tags": ["dev", "staging"]
        }
    }
)


print("✅ Cross-cluster API key creada:")
print(resp)
