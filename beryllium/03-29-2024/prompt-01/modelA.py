{
  "$schema" : "http://json-schema.org/draft-07/schema#",
  "type" : "object",
  "properties": {
    "products": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "productId": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "category": {
            "type": "object",
            "properties": {
              "mainCategory": {
                "type": "string"
              },
              "subCategories": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              }
            }
          },
          "price": {
            "type": "object",
            "properties": {
              "listPrice": {
                "type": "number"
              },
              "discount": {
                "type": "number"
              },
              "tax": {
                "type": "number"
              },
              "finalPrice": {
                "type": "number"
              }
            }
          },
          "stock": {
            "type": "integer"
          },
          "images": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "customerReviews": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "rating": {
                  "type": "integer"
                },
                "comment": {
                  "type": "string"
                }
              }
            }
          }
        },
        "required": ["productId", "name", "category", "price", "stock", "images"]
      }
    }
  },
  "required": ["products"]
}