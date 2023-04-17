

# how i can know the list  in python is Three Pairs

`from collections import Counter

my_list = [1, 1, 2, 2, 3, 3]

counts = Counter(my_list)

if all(count == 2 for count in counts.values()) and len(counts) == 3:
    print("The list represents Three Pairs!")
else:
    print("The list does not represent Three Pairs.")

`

