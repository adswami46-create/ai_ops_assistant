PLAN_SCHEMA = {
    "type": "object",
    "properties": {
        "steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "step_number": {"type": "number"},
                    "action": {"type": "string"},
                    "tool": {"type": "string"}
                },
                "required": ["step_number", "action", "tool"]
            }
        }
    },
    "required": ["steps"]
}
