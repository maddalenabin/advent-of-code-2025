# Day 1: Secret Entrance

[Problem Link](https://adventofcode.com/2025/day/1)

## Problem Summary

We need to decode a safe combination by simulating a dial that:
- Has numbers 0-99 arranged in a circle
- Starts at position 50
- Rotates left (L) or right (R) by specified amounts
- Wraps around (0-1 = 99, 99+1 = 0)

The password is the count of how many times the dial lands on 0 after any rotation.

## Approach

### Part 1

**Key Insights:**
- Use modulo arithmetic (`% 100`) to handle wrapping automatically
- Track position after each rotation
- Count occurrences of position 0

**Algorithm:**
1. Start at position 50
2. For each rotation instruction:
   - Parse direction (L/R) and distance
   - Update position: `(position ± distance) % 100`
   - Increment counter if position == 0
3. Return the count

**Complexity:**
- Time: O(n) where n is the number of rotations
- Space: O(1)

### Part 2

Count also the times you pass through 0.


## Example usage
```bash
python solution.py --file input.txt
```
