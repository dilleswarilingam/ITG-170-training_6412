string = "abbcccdddd"

max_char = ''
min_char = ''
max_count = 0
min_count = len(string)

# Finding frequency manually
for i in string:

    count = 0

    for j in string:
        if i == j:
            count = count + 1

    # Maximum occurring character
    if count > max_count:
        max_count = count
        max_char = i

    # Minimum occurring character
    if count < min_count:
        min_count = count
        min_char = i

# Displaying result
print("Maximum occurring character:", max_char)
print("Minimum occurring character:", min_char)