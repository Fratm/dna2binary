#!/usr/bin/python
import sys

def main(file_path):
    try:
        with open(file_path, 'r') as file:
            while True:
                char = file.read(1)
                if not char:
                    break
                if char == "A":
                    dnaDec = 0
                elif char == "C":
                    dnaDec = 1
                elif char == "G":
                    dnaDec = 2
                elif char == "T":
                    dnaDec = 3
                else:
                    return(0)
                print(decimal_to_binary(dnaDec), end='')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An IOError occurred while trying to read '{file_path}'.")

def decimal_to_binary(decimal_number, bit_length=2):
    if decimal_number == 0:
        return "0".zfill(bit_length)
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number.zfill(bit_length)

# Check if the script is run with a file path argument
if len(sys.argv) != 2:
    print("Usage: python script_name.py <file_path>")
else:
    file_path = sys.argv[1]
    main(file_path)
    print ("\n")