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
    with open(file_name, "r") as file:
        data = json.load(file)
    keys = ["unordered_numbers", "ordered_numbers", "dna_sequence"]

    if field not in keys:
        return None
    else:
        hodnoty = data.get(field)
        return hodnoty

    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

def linear_search(sequence, number):
    slovnik = {}
    count = 0
    pozice_seznam = []
    for i in range(len(sequence)):
        if sequence[i] == number:
            pozice_seznam.append(i)
            count += 1
    slovnik["positions"] = pozice_seznam
    slovnik["count"] = count
    return slovnik

def binary_search(numbers_list, cislo):
    left = 0
    right = len(numbers_list) - 1
    if cislo not in numbers_list:
        return None

    while left <= right:
        middle = (left + right) // 2
        if numbers_list[middle] == cislo:
            return middle
        elif numbers_list[middle] < cislo:
            left = middle + 1
        else:
            right = middle - 1
    return None



    #for i in range(len(numbers_list)):
        #if numbers_list[i] == cislo:
            #return i

    return None


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data, 5))
    seznam = read_data("sequential.json", "ordered_numbers")
    print(seznam)
    print(binary_search(seznam, 21))



if __name__ == "__main__":
    main()
