import argparse

def if_pattern_id(n):
    """
    Check if a number matches the invalid criteria:
        - The number consists of a sequence of digits repeated twice.
    Examples: 11, 6464, 123123. 

    Args:
        n (int): The number to check

    Returns:
        bool: True if the number matches the criteria, False otherwise
    """
    s = str(n)
    lenght = len(s)

    # if length is odd it can't be two equal halves
    if lenght % 2 != 0:
        return False
    
    mid = lenght // 2
    first_half = s[:mid]
    second_half = s[mid:]

    return first_half == second_half

def solution_function(input_text: str):
    """
    Solve the task: loops over the ranges provided and checks for invalid pattern
    """
    # get all ranges: it'ss like ["11-22", "143451-253452", ...]
    input_text = input_text.strip()
    all_ranges = input_text.split(",")

    total_sum = 0
    invalid_ids_found = []

    for r in all_ranges:
        start_str, end_str = r.split("-")
        start = int(start_str)
        end = int(end_str)
        # print(f"\nrange: {r}")

        # iterate throught the range
        for num in range(start, end+1):
            if str(num)[0] == 0:
                invalid_ids_found.append(num)
                total_sum += num
            elif if_pattern_id(num):
                invalid_ids_found.append(num)
                total_sum += num

    print(f"Found IDs: {invalid_ids_found}")

    return total_sum


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, 
                        default="input.txt",
                        help="input file")
    
    args = parser.parse_args()

    # Use the input string provided in your prompt if file reading fails
    # or for direct testing
    fallback_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    try:
        with open(args.file, "r") as f:
            input_text = f.read()

    except FileNotFoundError:
        print("File not found, using example input from prompt...")
        input_text = fallback_input

    restult = solution_function(input_text)
    print("="*50)
    print(f"Final sum: {restult}")
    print("="*50)

if __name__ == "__main__":
    main()