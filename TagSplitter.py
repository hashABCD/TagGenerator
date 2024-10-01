import argparse

def process_words(input_string):
    # Split the string by commas and strip leading/trailing spaces
    words = [word.strip() for word in input_string.split(',')]
    
    # Remove duplicates by converting the list to a set
    unique_words = list(set(words))
    
    # Sort the list alphabetically
    unique_words.sort()
    
    return unique_words

def read_from_file(file_path):
    # Open and read the content of the file
    with open(file_path, 'r') as file:
        input_string = file.read()
    return input_string

def save_to_file(output_string, file_path):
    # Write the comma-separated string into the output file
    with open(file_path, 'w') as file:
        file.write(output_string)

def main():
    # Set up argument parser to accept input and output file paths
    parser = argparse.ArgumentParser(description="Process words from input file and save unique, sorted words to output file.")
    
    # Input file path argument
    parser.add_argument('input_file', type=str, help='Path to the input file containing words separated by commas')
    
    # Output file path argument
    parser.add_argument('output_file', type=str, help='Path to save the processed, comma-separated words')
    
    # Parse the arguments
    args = parser.parse_args()

    # Read input file
    input_string = read_from_file(args.input_file)

    # Process words to get a sorted list of unique words
    unique_words = process_words(input_string)

    # Convert the list back to a comma-separated string
    comma_separated_string = ', '.join(unique_words)

    # Save the resulting string to the output file
    save_to_file(comma_separated_string, args.output_file)

    # Print a confirmation message
    print(f"Processed tags saved to {args.output_file}.")

# Main block to run the script
if __name__ == '__main__':
    main()
