import sys
dict_fileName = sys.argv[1]
db_fileName = sys.argv[2]

dict_file = open(dict_fileName, "r")
cur_keyword = dict_file.readline()
keyword_arr = []
total_len = 0
while cur_keyword != "":
    keyword_arr.append(cur_keyword)
    total_len = total_len + len(cur_keyword)
    cur_keyword = dict_file.readline()

print 'Number of keywords is: '
print len(keyword_arr)

arr = [[0 for y in range(5)] for x in range(total_len)]
print 'Arr[3][2] is initialized to: '
print arr[3][2]

cur_node = 0
next_open = 1
#   cur_node is set to root
for keyword in keyword_arr:
    for cur_symbol in keyword:
        if(cur_symbol == 'A'):
            key = 0
        elif(cur_symbol == 'T'):
            key = 1
        elif(cur_symbol == 'G'):
            key = 2
        elif(cur_symbol== 'C'):
            key = 3
        if(arr[cur_node][key] == 0 ):       #if there is not a node there
            arr[cur_node][key] = next_open
            cur_node = next_open
            next_open += 1
        else:       # cur_node already has a pointer for cur_symbol
            cur_node = arr[cur_node][key]
    arr[cur_node][4] = 9999
    cur_node = 0


print 'Trie successfully built'

