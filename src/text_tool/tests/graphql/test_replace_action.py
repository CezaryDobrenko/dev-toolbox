def test_run_text_replace_action_as_unlogged(client_query):
    base_text = "Lorem Ipsum ipsum"
    old_text = "Ipsum"
    new_text = "amet"

    query = """
        mutation runTextReplaceAction(
            $baseText: String!,
            $oldText: String!,
            $newText: String!,
        ){
            runTextReplaceAction(
                baseText: $baseText,
                oldText: $oldText,
                newText: $newText
            ){
                result
            }
        }
    """
    variables = {"baseText": base_text, "oldText": old_text, "newText": new_text}
    expected = {"runTextReplaceAction": {"result": "Lorem amet ipsum"}}

    response = client_query(query, variables=variables)

    assert response.get("errors") is None
    assert response["data"] == expected
