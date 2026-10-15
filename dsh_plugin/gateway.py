import json

def get_config():
    return {"models": ["DeepSeek-V4.1-Flash", "Kimi-K3"], "status": "active"}

def validate_request(req):
    return "model" in req and req["model"] in get_config()["models"]
