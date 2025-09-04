import requests

def plant_tree_api(user_id, trees):
    url = "https://vendor-api.com/plant"
    response = requests.post(url, json={"user": user_id, "trees": trees})
    return response.json()
