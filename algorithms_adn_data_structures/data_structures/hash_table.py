class HashTable:
    
    def __init__(self, max=10):
        self.__max = max
        self.__array = [[] for _ in range(max)]

    def __get_hash_value(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.__max

    def __setitem__(self, key, value):
        hash_value = self.__get_hash_value(key)
        found = False
        for index, element in enumerate(self.__array[hash_value]):
            if len(element) == 2 and element[0] == key:
                self.__array[hash_value][index] = (key, value)
                found = True
                break
        if not found:
            self.__array[hash_value].append((key, value))

    def __getitem__(self, key):
        hash_value = self.__get_hash_value(key)
        for element in self.__array[hash_value]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        hash_value = self.__get_hash_value(key)
        for index, element in enumerate(self.__array[hash_value]):
            if element[0] == key:
                del self.__array[hash_value][index]

    def show_table_content(self):
        print(self.__array)


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table["9384j324ofdh23o4fdh23fdowofbnr3493fdj55"] = "some item"
    hash_table["9384j324ofdh23o4fdh23fdowofbnr3493fdj534"] = "some item 0000"
    hash_table["002"] = "some item 2"
    hash_table.show_table_content()
    hash_table["004"] = "some item 4"
    hash_table["047"] = 740
    hash_table.show_table_content()
    print(hash_table["047"])
    print(hash_table["004"])
    print(hash_table["9384j324ofdh23o4fdh23fdowofbnr3493fdj55"])
    print(hash_table["9384j324ofdh23o4fdh23fdowofbnr3493fdj534"])
    del hash_table["9384j324ofdh23o4fdh23fdowofbnr3493fdj55"]
    del hash_table["001"]
    hash_table.show_table_content()
