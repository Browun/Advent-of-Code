# Advent of Code - 2021

## Table of Contents

- [Day 1 - Sonar Sweep](day-1-sonar-sweep)

## Day 1 - Sonar Sweep

- [Problem](https://adventofcode.com/2021/day/1)
- [Solution](day2/day2.py)

### Part 1

### Part 2

## Day 2 - Dive!

### Part 1

- Forward adds numbers to horizontal
- Backward is not posible
- Down adds 5 to depth
- Up minuses from depth

- Find horizontal and vertical position, multiply together

### Part 2

- Find horizontal, vertical, and aim, multiplying horizontal and vertical together
- vertical is now set by aim * input value

## Day 3 - Binary Diagnostic

- Power consumption
- Use input to generate Gamma and Epsilon, power consumption = gamma * epsilon
- Gamma is the most common bit in the corresponding position, for each of the columns
- Epsilon is the oppsotte of the Gamma, with the least common bit

### Part 2

- Life support = Oxygen generator * CO2 scrubber
- Oxygen generator = most common in columns keep those preferring 1
- CO2 = lest common in columns keep those preferring 0
