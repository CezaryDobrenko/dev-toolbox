def test_run_text_censor_action_as_unlogged(client_query):
    base_text = "Lorem Ipsum ipsum dolor sit amet, consectetur adipiscing elit."
    censored_phrases = ["Ipsum", "consectetur"]
    is_case_sensitive = False

    query = """
        mutation runTextCensorAction(
            $baseText: String!,
            $censoredPhrases: [String]!,
            $isCaseSensitive: Boolean!,
        ){
            runTextCensorAction(
                baseText: $baseText,
                censoredPhrases: $censoredPhrases,
                isCaseSensitive: $isCaseSensitive
            ){
                result
            }
        }
    """
    variables = {
        "baseText": base_text,
        "censoredPhrases": censored_phrases,
        "isCaseSensitive": is_case_sensitive,
    }
    expected = {
        "runTextCensorAction": {
            "result": (
                "Lorem [censored] [censored] dolor "
                "sit amet, [censored] adipiscing elit."
            )
        }
    }

    response = client_query(query, variables=variables)

    assert response.get("errors") is None
    assert response["data"] == expected
