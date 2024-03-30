{
    "$schema" : "http://json-schema.org/draft-07/schema#",
    "type" : "object",
    "properties": {
        "projectId": {
            "type": "integer"
        },
        "projectName": {
            "type": "string"
        },
        "startDate": {
            "type": "string",
            "format": "date"
        },
        "endDate": {
            "type": "string",
            "format": "date"
        },
        "status": {
            "type": "string",
            "enum": ["active", "completed", "on hold"]
        },
        "tasks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "taskId": {
                        "type": "integer"
                    },
                    "title": {
                        "type": "string"
                    },
                    "description": {
                        "type": "string"
                    },
                    "assignee": {
                        "type": "string"
                    },
                    "priority": {
                        "type": "string"
                    },
                    "dueDate": {
                        "type": "string",
                        "format": "date"
                    }
                },
                "required": ["taskId", "title", "description", "assignee", "priority", "dueDate"]
            }
        },
        "teamMembers": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "memberId": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "role": {
                        "type": "string"
                    }
                },
                "required": ["memberId", "name", "role"]
            }
        }
    },
    "required": ["projectId", "projectName", "startDate", "endDate", "status", "tasks", "teamMembers"]
}