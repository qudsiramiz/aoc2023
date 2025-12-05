def parse_input(file_path):
    """Reads the input file and parses the comma-separated, hyphenated ranges."""
    with open(file_path, 'r') as f:
        content = f.read().strip()

    ranges = []
    for part in content.split(','):
        if not part:
            continue
        start, end = map(int, part.split('-'))
        ranges.append((start, end))
    return ranges


"""Main function to solve the puzzle."""
input_ranges = parse_input('data/input_v02.txt')
max_id = max(end for _, end in input_ranges)
total_sum = 0
found_ids = set()

# Generate invalid IDs and check them
# The base can be any number. We iterate up to a reasonable limit.
# A base pattern can't be longer than half the length of the max_id string.
limit = 10 ** (len(str(max_id)) // 2 + 1)

for base in range(1, limit):
    base_str = str(base)

    # Only consider two repetitions for Part One
    k = 2
    repeated_str = base_str * k
    candidate_id = int(repeated_str)

    if candidate_id > max_id:
        continue

    if candidate_id in found_ids:
        continue
    # Check if candidate_id is in any of the ranges
    for start, end in input_ranges:
        if start <= candidate_id <= end:
            # Found a valid ID, add it to our sum and set
            total_sum += candidate_id
            found_ids.add(candidate_id)
            # Once found, no need to check other ranges for this ID
            break

print(f"The sum of all invalid IDs is: {total_sum}")


