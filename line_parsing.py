import json
import re

def split_sentence(sentence):
    # Split the sentence using a regex that matches single spaces or multiple spaces
    words = re.split(r'(\s+)', sentence)
    # Filter out empty strings that result from consecutive spaces
    words = [word for word in words if word]
    return words

def remove_single_space_elements(arr):
    # Use a list comprehension to filter out single space elements
    return [element for element in arr if element != ' ']

def parse_table_to_json(table_str):
    # Split the input string into lines
    lines = table_str.strip().split('\n')
    
    # The first line contains the column names
    columns = lines[0].split()
    
    # Initialize a list to store the rows as dictionaries
    data = []
    
    # Iterate over the remaining lines to process each row
    for line in lines[1:]:
        # Split the row into values
        values = remove_single_space_elements(split_sentence(line))
        # Create a dictionary for the row, mapping columns to values
        row_dict = dict(zip(columns, values))
        # Add the row dictionary to the list
        data.append(row_dict)
    
    # Convert the list of dictionaries to a JSON string
    json_result = json.dumps(data, indent=4)
    
    return json_result

# Example table string
table_str = """
Column1 Column2 Column3
value1 value2 value3
value4  value6
"""

# Convert the table to JSON
json_result = parse_table_to_json(table_str)

# Print the JSON result
print(json_result)

