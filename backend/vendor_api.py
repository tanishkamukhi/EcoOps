def plant_tree_api(user_id, trees, vendor="EcoOps Demo Vendor"):
    return {
        "user": user_id,
        "trees": trees,
        "vendor": vendor,
        "status": "success",
        "message": f"🌳 {trees} trees planted successfully with {vendor}!"
    }
