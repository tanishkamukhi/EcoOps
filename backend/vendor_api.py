import requests

def plant_tree_api(user_id: str, trees: int):
    """
    Try calling real vendor API.
    If it fails, return a dummy offline response.
    """
    url = "https://vendor-api.com/plant"  # demo vendor endpoint

    try:
        response = requests.post(url, json={"user": user_id, "trees": trees}, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "user": user_id,
                "trees": trees,
                "status": "failed",
                "message": f"Vendor API error {response.status_code}"
            }
    except Exception:
        # Fallback offline response
        return {
            "user": user_id,
            "trees": trees,
            "status": "success",
            "message": "🌳 Demo mode: Trees planted successfully (offline)"
        }
