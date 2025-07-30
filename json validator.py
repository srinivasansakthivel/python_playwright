import json

def validate_json_path(json_data, path):
    """
    Validates if the given path exists in the JSON data.

    Args:
        json_data (dict): The JSON data as a dictionary.
        path (str): The dot-separated path to validate.

    Returns:
        bool: True if the path exists, False otherwise.
    """
    keys = path.split('.')
    current_data = json_data

    try:
        for key in keys:
            # Handle list indices in the path
            if '[' in key and ']' in key:
                key_name, index = key[:-1].split('[')
                index = int(index)
                current_data = current_data[key_name][index]
            else:
                current_data = current_data[key]
        return True
    except (KeyError, IndexError, TypeError):
        return False

# Load JSON data from the file
with open("/Users/srinivasansakthivel/Desktop/Wealth json file.json", "r") as file:
    json_data = json.load(file)

# Path to validate
path_to_validate = "onboardingDetails.metadata.manualReviewAttempts.reviewAttemptMapping.ITEM_TYPE_AADHAAR_REDACTION.reviewAttempts[0].id"

# Validate the path
is_valid = validate_json_path(json_data, path_to_validate)
print(f"Is the path valid? {is_valid}")
