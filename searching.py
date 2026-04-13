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
    count = 0 #1
    position = 0 #1
    vyskyty = [] #1
    for prvek in sequence:
        if prvek == number: #n
            count +=1
            vyskyty.append(position)
        position +=1 #n
    result = {
        "positions" : vyskyty,
        "count" : count
    } #1
    return result #1

    #nejhorší scénář: 2n +5 - O(n)
    #nejlepší scénář: n - O(n)

def binary_search(seznam, cislo):
    prvni = 0
    posledni = len(seznam) # je o 1 větší než actual index
    while len(seznam[prvni:posledni]) > 1:

        if len(seznam[prvni:posledni]) % 2 == 0:
            prostredek = prvni + int((len(seznam[prvni:posledni]) / 2)-1)
        else:
            prostredek = prvni + int((len(seznam[prvni:posledni]) - 1) / 2)

        if seznam[prostredek] > cislo:
            posledni = prostredek
        elif seznam[prostredek] == cislo:
            return prostredek
        else:
            prvni = prostredek
    return prostredek


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    ordered_numbers =  read_data("sequential.json", "ordered_numbers")
    print(sequential_data)


    search_results = linear_search(sequential_data, 0)
    search_bin = binary_search(ordered_numbers, -12)
    print(search_results)
    print(search_bin)

#nejlepší - veprostřed 1 operace O(1)
#nejhorší - n/2**k, k = log2(n) - Olog(n)

if __name__ == "__main__":
    main()
