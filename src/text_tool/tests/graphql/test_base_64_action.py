def test_run_text_to_base64_action_as_unlogged(client_query):
    base_text = "Lorem Ipsum"

    query = """
        mutation runTextToBase64Action($baseText: String!){
            runTextToBase64Action(baseText: $baseText){
                result
            }
        }
    """
    variables = {"baseText": base_text}
    expected = {"runTextToBase64Action": {"result": "TG9yZW0gSXBzdW0="}}

    response = client_query(query, variables=variables)

    assert response.get("errors") is None
    assert response["data"] == expected


def test_run_text_from_base64_action_as_unlogged(client_query):
    base_text = "TG9yZW0gSXBzdW0="

    query = """
        mutation runTextFromBase64Action($baseText: String!){
            runTextFromBase64Action(baseText: $baseText){
                result
            }
        }
    """
    variables = {"baseText": base_text}
    expected = {"runTextFromBase64Action": {"result": "Lorem Ipsum"}}

    response = client_query(query, variables=variables)

    assert response.get("errors") is None
    assert response["data"] == expected
