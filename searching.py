from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()

    file_path = cwd_path / file_name

    if field not in ("dna_sequence", "ordered_numbers", "unordered_numbers"):
        return None
    else:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data[field]

def linear_search(sequence, number):
    count = 0
    position = 0
    vyskyty = []
    for prvek in sequence:
        if prvek == number:
            count +=1
            vyskyty.append(position)
        position +=1
    result = {
        "positions" : vyskyty,
        "count" : count
    }
    return result


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)


    search_results = linear_search(sequential_data, 0)
    print(search_results)

if __name__ == "__main__":
    main()
