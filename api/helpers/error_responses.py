ValidationErrorList = [
    # Path Parameter Errors
    {"location": ["path", "book_id"],"msg": "Book ID must be a positive integer.","type": "value_error.integer"},
    # Body Validation Errors
    {"location": ["body", "title"],"msg": "The title must have at least 3 characters.","type": "value_error.any_str.min_length"},
    {"location": ["body", "genre"],"msg": "Genre must be one of ['Fiction', 'Fantasy', 'Mystery', 'Historical Fiction', 'Science Fiction', 'Romance'].","type": "value_error.enum"},
    {"location": ["body", "summary"],"msg": "The summary must not exceed 500 characters.","type": "value_error.any_str.max_length"},
    {"location": ["query", "author_firstname"],"msg": "Author's first name must have at least 1 character.","type": "value_error.any_str.min_length"},
    {"location": ["query", "author_lastname"],"msg": "Author's last name must have at least 1 character.","type": "value_error.any_str.min_length"}
]

def get_validation_errors(*fields):
    """
    Filters the ValidationErrorList to return errors for the specified fields.

    Parameters:
        fields (str): Field names to filter by (e.g., "title", "genre").

    Returns:
        list: A list of dictionaries containing validation errors for the specified fields.
    """
    return [error for error in ValidationErrorList if error["location"][1] in fields]

def generate_422_response(*fields):
    """
    Generates a 422 error response for the specified fields.

    Args:
        fields (str): Field names to filter by (e.g., "title", "genre").

    Returns:
        dict: A 422 error response structure for use in FastAPI routes.
    """
    return {
        422: {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "example": {
                        "error_message": "Validation Error",
                        "detail": get_validation_errors(*fields)
                    }
                }
            }
        }
    }




       