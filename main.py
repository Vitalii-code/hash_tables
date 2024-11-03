from random_words import words


def swap_middle_letters(s: str) -> str:
    length = len(s)
    middle = length // 2

    # turn the string to list
    s_list = list(s)

    # try to swap the middle two values
    try:
        s_list[middle], s_list[middle + 1] = s_list[middle + 1], s_list[middle]

    except IndexError:
        return s

    s = "".join(s_list)

    return s


def string_to_hash(s, max_size) -> int:
    """returns a hash from a string"""
    # swap the middle letters

    s_swapped = s
    # s_swapped = swap_middle_letters(s)

    out = []
    for i, char in enumerate(s_swapped):
        out.append(ord(char) ** i ^ 7919)

    # all the numbers of the letters added together
    hash = (sum(out)) % max_size

    return hash


class HashTable:

    def __init__(self, size) -> None:
        """size is the maximum size of the hash table"""
        self.__dictionary = {}
        self.hash_table_size = size

    def append(self, value) -> bool:
        """appends a value to the hash table. Returns True on success or False on failure"""
        hash = string_to_hash(value, self.hash_table_size)

        # If hash already exists in the table then return False
        if self.retrieve(hash):
            return False
        # Assign the value to the hash if the slot is empty
        else:
            self.__dictionary[hash] = value
        return True

    def retrieve(self, hash):
        """Tries to retrieve the value, returns False if it couldn't find it"""
        try:
            return self.__dictionary[hash]
        except KeyError:
            return False

    def remove(self, hash):
        """Removes something from the table"""
        self.__dictionary.pop(hash)

    def display(self):
        print(self.__dictionary)

    def get_dict(self):
        """Returns the dictionary where the hash values are stored"""
        return self.__dictionary


my_hashtable1 = HashTable(100)
collisions = 0

for i in range(0, 100):
    if my_hashtable1.append(words[i]):
        pass
    else:
        collisions += 1

# print area
# print(
#     "The number of collisions is:",
#     collisions,
# )
# print("Hash table size:", my_hashtable1.hash_table_size)
# print("The length of the table after adding words is", len(my_hashtable1.get_dict()))
# print(
#     f"The percentage of collisions is: {collisions / my_hashtable1.hash_table_size * 100}%"
# )

# print(my_hashtable1.search("Another value"))

# my_hashtable1.display()

hash = string_to_hash("aardvarks", my_hashtable1.hash_table_size)
print(my_hashtable1.retrieve(hash))
