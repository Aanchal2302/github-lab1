import json


def search_json(json_data, search_string):
    results = []
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    # Search the data
    results = []

    # Iterate through each dictionary in the json_data list
    for data in json_data:
        result_dict = {}

        # Iterate through each key-value pair in the current dictionary
        for key, value in data.items():
            # Check if the search string (case-insensitive) is found in the value
            if search_string.lower() in str(value).lower():
                # If found, add the key-value pair to the result dictionary
                result_dict[key] = value

        # If the result dictionary is not empty (i.e., at least one match was found)
        if result_dict:
            # Append the result dictionary to the results list
            results.append(result_dict)

    return results
