import json
from typing import Dict, Any

def parse_openapi_file(content: bytes) -> Dict[str, Any]:
    try:
        data = json.loads(content.decode("utf-8"))

        paths = data.get("paths", {})
        parsed_endpoints = []

        for path, methods in paths.items():
            for method, details in methods.items():
                parsed_endpoints.append({
                    "path": path,
                    "method": method.upper(),
                    "summary": details.get("summary", ""),
                    "description": details.get("description", ""),
                    "parameters": details.get("parameters", [])
                })

        return {
            "success": True,
            "endpoint_count": len(parsed_endpoints),
            "endpoints": parsed_endpoints
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
