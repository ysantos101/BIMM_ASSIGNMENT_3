import sys
dict_fileName = sys.argv[1]
db_fileName = sys.argv[2]

dict_file = open(dict_fileName, "r")
db_file = open(db_fileName, "r")
cur_keyword = dict_file.readline()
keyword_arr = []
total_len = 0
while cur_keyword != "":
    keyword_arr.append(cur_keyword)
    total_len = total_len + len(cur_keyword)
    cur_keyword = dict_file.readline()

print 'Number of keywords is: '
print len(keyword_arr)

arr = [[0 for y in range(5)] for x in range(total_len + len(keyword_arr))]
print 'Arr[3][2] is initialized to: '
print arr[3][2]

cur_node = 0
next_open = 1
i = 0
#   cur_node is set to root
for keyword in keyword_arr:
    for cur_symbol in keyword:
        if(cur_symbol == '\n'):
            break
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
    arr[cur_node][4] = i + 1
    print 'terminal node added for keyword number: '
    print i
    print 'that terminal node is node number: '
    print cur_node
    next_open += 1
    cur_node = 0
    i += 1


print 'Trie successfully built'

print 'value of arr[0][4], corresponding to root terminal status is: '
print arr[0][4]

cur_node = 0
start = 0
cur_line = db_file.readline()
db_string = ""
while cur_line != "":
    db_string = db_string + cur_line
    cur_line = db_file.readline()
#   db_string now contains entire database

num_matches = [0 for q in range(len(keyword_arr))]
while start < len(db_string):
    cur_index = start
    while(True):

        if(cur_index >= len(db_string)):
            break
        cur_symbol = db_string[cur_index]
        if(cur_symbol == '\n' and cur_index + 1 < len(db_string)):
            cur_index += 1
            cur_symbol = db_string[cur_index]
        elif(cur_symbol == '\n'):
            break
        if(cur_symbol == 'A'):
            key = 0
        elif(cur_symbol == 'T'):
            key = 1 
        elif(cur_symbol == 'G'):
            key = 2
        elif(cur_symbol == 'C'):
            key = 3
        if(arr[cur_node][4] > 0 ):    #current node is a terminal one!
            match_index = arr[cur_node][4] - 1
            num_matches[match_index] += 1
            print 'match found'
            
        if(arr[cur_node][key] == 0):    #Current symbol is not in Trie!
            break
        else:
            cur_node = arr[cur_node][key]
            #   move to next node
        cur_index += 1

    start += 1
    cur_node = 0
    if(start%1000000 == 0):
        num_done = str(start)
        print 'Index for start is: ' + num_done
        print '\n'


print 'Number of Matches for each keyword:'
m = 0
while(m < len(keyword_arr)):
    num = str(num_matches[m])
    index = str(m)
    print 'Number of matches for keyword number ' + index + ' is: ' + num
    print 'that keyword is: '
    print '       ' + keyword_arr[m]
    print '\n'
    m += 1














