import requests

def graphql_request(session, query_hash, user_id, edge):
    users = set()
    has_next = True
    cursor = None

    while has_next:
        variables = {
            "id": user_id,
            "first": 50
        }

        if cursor:
            variables["after"] = cursor

        params = {
            "query_hash": query_hash,
            "variables": str(variables).replace("'", '"')
        }

        r = session.get(
            "https://www.instagram.com/graphql/query/",
            params=params
        )

        data = r.json()
        edge_data = data["data"]["user"][edge]

        for e in edge_data["edges"]:
            users.add(e["node"]["username"])

        has_next = edge_data["page_info"]["has_next_page"]
        cursor = edge_data["page_info"]["end_cursor"]

    return users
