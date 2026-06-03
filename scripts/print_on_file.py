import sys

nome_file = sys.argv[1]

with open(nome_file, "w", encoding="utf-8") as file_output:
    print("ciao", file=file_output)