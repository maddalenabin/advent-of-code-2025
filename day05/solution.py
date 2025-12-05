import argparse

def solution_function(input_file):
    """
    Docstring for solution_function
    """
    part1, part2 = input_file.strip().split("\n\n")
    ranges = [(tuple(x.split("-"))) for x in part1.split("\n")]
    ingredients = [int(x) for x in part2.split("\n")]

    fresh = [None] * len(ingredients)

    # print(f"{ranges = }")
    # print(f"{ingredients = }")

    

    for i,ingr in enumerate(ingredients):

        for r in ranges:
            ingr_range = range(int(r[0]), int(r[1])+1)
            # print("\n", i,r, ingr_range)

            if ingr in ingr_range:
                # print("\t", i,r, ingr_range)
                # print("\tyes !!")
                fresh[i] = 1
            
    # print(ingredients)
    fresh = [0 if x is None else x for x in fresh]
    # fresh[fresh==None] = 0

    # print("\n", fresh)

    return fresh



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file", type=str,
                       default="input.txt",
                       help="input file")
    
    args = parser.parse_args()
    
    with open(args.file, "r") as f:
        file = f.read()

    fresh_ingredients = solution_function(file)
    
    print(f"\n{'='*50}")
    print(f"Solution - Fresh ingredients are {sum(fresh_ingredients)}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()