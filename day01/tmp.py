def main(position, distance):
    through_zero = (position - distance)
    print(f"{position = } | {distance = }") 
    return through_zero


if __name__ == "__main__":
    sol = main(position=50, distance=68)
    print("="*50)
    print(f"Solution: {sol}")
    print("="*50)