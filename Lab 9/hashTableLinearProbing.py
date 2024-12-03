hashTable = [(None, None) for i in range(10)]

def hashFuncKey(data, key):
    return key % len(data)

def insert(data, key, value):
    searchInfo = __searchHelper(data, key, insert = True)

    # if key is None, we insert
    # if key is deleted, we insert
    # if key is found, we update value == update (key, value) pair == insert/replace
    # so in all cases, we simply insert
    data[searchInfo[0]] = (key, value)
    

def search(data, key):
    searchInfo = __searchHelper(data, key)

    print(searchInfo[1][1])

def delete(data, key):
    searchInfo = __searchHelper(data, key)

    # if key found, we delete
    if(searchInfo[1][0] == key):
        data[searchInfo[0]] = ('deleted', 'deleted')
    # otherwise print error message
    else:
        print("Key was not found in the table.")


def __searchHelper(data, key, insert = False):
    # compute hash value for key
    hashValue = hashFuncKey(data, key)

    counter = 0
    # iterate up to one full cycle ...
    while counter != len(data):
        pos = (hashValue + counter) % len(data)
        # ... as long as key is not None ...
        if (data[pos][0] is None):
            break
        # ... or key found
        elif (data[pos][0] == key):
            break
        # in case we are searching for a slot to insert,
        # deleted slots are potential candidates too
        elif (insert and data[pos][0] == 'deleted'):
            break
    
        counter = counter + 1
    
    pos = (hashValue + counter) % len(data)
    
    # if data[pos] is None, the sequence of potential keys has ended
    # if entire data table is deleted, pos == hashValue, so we return pos
    # if key found, we return
    # in all cases we return the (pos,(key, value)) tuple
    return (pos,data[pos])




insert(hashTable, 10, 'Alex')
insert(hashTable, 14, 'Mary')
insert(hashTable, 18, 'Deni')
insert(hashTable, 20, 'Jane')
insert(hashTable, 21, 'Besmir')
insert(hashTable, 30, 'Kejd')
insert(hashTable, 24, 'Rei')
insert(hashTable, 18, 'Rei')

print(hashTable)
# expected: [(10, 'Alex'), (20, 'Jane'), (21, 'Besmir'), (30, 'Kejd'), (14, 'Mary'), (24, 'Rei'), (None, None), (None, None), (18, 'Rei'), (None, None)]
# result:   [(10, 'Alex'), (20, 'Jane'), (21, 'Besmir'), (30, 'Kejd'), (14, 'Mary'), (24, 'Rei'), (None, None), (None, None), (18, 'Rei'), (None, None)]

delete(hashTable, 10)
print(hashTable)
# result:   [('deleted', 'deleted'), (20, 'Jane'), (21, 'Besmir'), (30, 'Kejd'), (14, 'Mary'), (24, 'Rei'), (None, None), (None, None), (18, 'Rei'), (None, None)]

search(hashTable, 20)
# expected: Jane
# result:   Jane

insert(hashTable, 10, 'Martin')
print(hashTable)
# expected: [(10, 'Martin'), (20, 'Jane'), (21, 'Besmir'), (30, 'Kejd'), (14, 'Mary'), (24, 'Rei'), (None, None), (None, None), (18, 'Rei'), (None, None)]
# result:   [(10, 'Martin'), (20, 'Jane'), (21, 'Besmir'), (30, 'Kejd'), (14, 'Mary'), (24, 'Rei'), (None, None), (None, None), (18, 'Rei'), (None, None)]

search(hashTable, 20)
# expected: Jane
# result:   Jane