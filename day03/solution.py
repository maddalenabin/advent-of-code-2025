import argparse

def part1(input_txt):
    # read bank of batteries joltages
    banks = input_txt.strip().split("\n")
    # print(f"{banks = }")
    joltages = []
    
    for bank in banks:
        voltage = 0
        # print(bank)
        i = 1

        for id1 in bank[:-1]:

            for id2 in bank[i:]:
                tmp_voltage = int(id1 + id2)
                # print(f"{id1} | {id2} | {tmp_voltage}")
                
                if tmp_voltage > voltage:
                    voltage = tmp_voltage
                    # print("\t", voltage)
            i += 1

        joltages.append(voltage)
        # print(joltages)

    return sum(joltages)


def part2(input_txt):
    # read bank of batteries joltages
    banks = input_txt.strip().split("\n")
    # print(f"{banks = }")
    joltages = []
    target_length = 12

    for bank in banks:
        # print("\n", bank)
        to_remove = len(bank) - target_length

        if to_remove < 0:
            continue

        stack = []
        for digit in bank:
            while to_remove > 0 and stack and stack[-1] < digit:
                stack.pop()
                to_remove -= 1
            stack.append(digit)
        
        best_digits = "".join(stack[:target_length])
        # print("\t", best_digits)
        joltages.append(int(best_digits))
    
    return sum(joltages)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str,
                        default="input.txt",
                        help="input file"
    )

    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            input = f.read()
    
        result1 = part1(input)
        result2 = part2(input)

        print(f"\n{'='*50}")
        print(f"Part 1: {result1}")
        print(f"Part 2: {result2}")
        print(f"{'='*50}")

    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
