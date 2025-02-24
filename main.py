"""
Name: Bin Ni
Email: bin.ni81@myhunter.cuny.edu
Resources: None
"""

def calculate_average_grades(input_filename, output_filename):
    """
    Open the file, read the lines, and calculate the average grade
    """
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, \
            open(output_filename, 'w', encoding='utf-8') as outfile:
            for line in infile:
                parts = line.split()
                name = parts[0]
                grades = list(map(int, parts[1:]))
                average = sum(grades) / len(grades) if grades else 0
                outfile.write(f"{name} {average:.1f}\n")
    except FileNotFoundError:
        print("Error: Input file not found.")

def main():
    """
    Inputs and calls function
    """
    input_file = input("Enter your input file name: ")
    output_file = input("Enter your output file name: ")
    calculate_average_grades(input_file, output_file)

if __name__ == "__main__":
    main()
