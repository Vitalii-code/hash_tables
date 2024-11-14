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

    out = []
    for i, char in enumerate(s):
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

        # If something is already in the table then return False
        if self.retrieve(hash):
            # retrieve the current value that was in the cell originally, and add the new value to it 
            
            # what is currently in the cell
            current_element = self.__dictionary[hash]
            if type(current_element) is list: 
                # this will replace current element and make it a list
                current_element.append(value)
                self.__dictionary[hash] = current_element

            elif type(current_element) is str:
                self.__dictionary[hash] = [current_element, value]

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

    def search(self, value: str) -> [str, int]:
        # returns the hash index and what position is in the list it is [hash, index]
        hash = string_to_hash(value, self.hash_table_size)

        if type(self.__dictionary[hash]) is list:
                for i, element in enumerate(self.__dictionary[hash]):
                    if element == value:
                        return [hash, i]
                return False
        elif type(self.__dictionary[hash]) is str:
            return [hash, 0]
        
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
print(
    f"The percentage of collisions is: {collisions / my_hashtable1.hash_table_size * 100}%"
)


my_hashtable1.display()


print(my_hashtable1.search("abamps"))

