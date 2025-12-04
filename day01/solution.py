import argparse


def solve_safe_password(rotation_text):
    """
    Function to solve the safe password problem.    
    Args:
        rotattion_text (str): The text representing the rotation instructions.

    """
    position = 50
    zero_counts = 0
    through_zero_counts = 0

    lines = rotation_text.strip().split("\n")
    print(f"Lines read: {len(lines) = }")

    for i,line in enumerate(lines):
        # print(i, line)
        line = line.strip()
        if not line:
            continue

        direction = line[0] # should be L or R
        distance = int(line[1:]) # int number
        passes = 0 
        # print("\t", i, direction, distance)

        if direction == "L": # subtraction
            position = (position - distance) % 100

            if distance >= 100:
                passes = distance // 100
            
            if position < distance % 100:
                passes += 1

        elif direction == "R": # addition
            position = (position + distance) % 100
            
            if distance >= 100:
                passes = distance // 100
            
            if position + (distance % 100) >= 100:
                passes += 1
        
        through_zero_counts += passes

        # print(f"\t\t{position = }")

        if position == 0:
            zero_counts += 1

    return zero_counts, through_zero_counts

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, 
                        default="input.txt",
                        help="Input file with moves")
    
    args = parser.parse_args()

    try:
        # read input
        with open(args.file, "r") as f:
            puzzle_input = f.read()

        zero_counts, passes = solve_safe_password(puzzle_input)
        print(f"\n{'='*50}")
        print(f"Zero counts: {zero_counts}")
        print(f"Passes through zero: {passes}")
        print(f"{'='*50}")
        
    except FileNotFoundError:
        print("File not found")



if __name__ == "__main__":
    main()