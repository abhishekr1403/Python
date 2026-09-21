# stock_prices= {}
# with open('E://Python//DSA/stock_prices.csv','r') as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_prices[day] = price
# print(stock_prices)
#
# print(stock_prices['march 9'])

# ----------------------------------------------------------------

class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100

    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    t = HashTable()
    # print(t.get_hash('march 18'))
    t['march 6'] = 130
    t['march 1'] = 200
    t['march 14'] = 100
    print(t.arr)
    del t['march 1']
    print(t.arr)

