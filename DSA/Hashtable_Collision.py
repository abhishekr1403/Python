# ------------------Chaining-----------------
from operator import index


# class HashTable:
#     def __init__(self):
#         self.max = 10
#         self.arr = [[] for i in range(self.max)]
#
#     def get_hash(self, key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.max
#
#     def __setitem__(self, key, value):
#         h = self.get_hash(key)
#         found = False
#         for index, element in enumerate(self.arr[h]):
#             if element[0] == key:
#                 self.arr[h][index] = (key, value)
#                 found = True
#         if not found:
#             self.arr[h].append((key, value))
#
#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         for element in self.arr[h]:
#             if element[0] == key:
#                 return element[1]
#
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         for index, element in enumerate(self.arr[h]):
#             if element[0] == key:
#                 del self.arr[h][index]
#
#
# if __name__ == '__main__':
#     t = HashTable()
#     t['march 1'] = 100
#     t['march 6'] = 240
#     t['march 17'] = 320
#     t['december 24'] = 480
#     print(t.arr)
#     print(t['march 6'])
#     print(t['march 17'])
#     del t['march 17']
#     print(t.arr)
#
# ---------------------------Problem 1--------------------------------------------------

# weather_data = []
# with open('E://Python//DSA/nyc_weather.csv','r') as f:
#     # next(f)
#     for line in f:
#         try:
#             tokens = line.split(',')
#             temparture = float(tokens[1])
#             weather_data.append(temparture)
#         except:
#             print("Ignore the first row.")
#     print(weather_data)
#
#     avg_1st_week = sum(weather_data[0:7])/len(weather_data[0:7])
#     print(round(avg_1st_week,2))
#
#     print(max(weather_data))
#
#     ---------------------Problem 2----------------------------------------

# weather_data = {}
# with open('E://Python//DSA/nyc_weather.csv','r') as f:
#     # next(f)
#     for line in f:
#         try:
#             tokens = line.split(',')
#             day = tokens[0]
#             temparture = float(tokens[1])
#             weather_data[day] = temparture
#         except:
#             print("Ignore the first row containing header.")
#     print(weather_data)
#     print(weather_data['Jan 9'])
#     print(weather_data['Jan 4'])

# ------------------Problem 3---------------------------

# word_count = {}
# with open('E://Python//DSA/poem.txt','r') as f:
#     for line in f:
#         tokens = line.split(' ')
#         for word in tokens:
#             word = word.translate(str.maketrans('', '', '!,?.:;\n'))
#             if word in word_count:
#                 word_count[word] += 1
#             else:
#                 word_count[word] = 1
# print(word_count)
# counts = []
# for key in word_count:
#     counts.append(word_count[key])
#
# max_count = max(counts)
# for key,value in word_count.items():
#     if word_count[key] == max_count:
#         print(f'{key} : {value}')

# -----------------------Linear Probabing-------------------------

class HashTable:
    def __init__(self):
        self.MAX = 10  # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return  # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)

if __name__ == '__main__':
    t = HashTable()
    t["march 6"] = 20
    t["march 17"] = 88
    t["march 17"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
