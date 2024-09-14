def test_run_text_revert_action_as_unlogged(client_query):
    base_text = "Lorem Ipsum"

    query = """
        mutation runTextRevertAction($baseText: String!){
            runTextRevertAction(baseText: $baseText){
                result
            }
        }
    """
    variables = {"baseText": base_text}
    expected = {"runTextRevertAction": {"result": "muspI meroL"}}

    response = client_query(query, variables=variables)

    assert response.get("errors") is None
    assert response["data"] == expected
