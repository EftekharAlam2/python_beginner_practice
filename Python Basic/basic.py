# # Beginner Hello World 😁
# print("Hello, World!")

# # Numbers
# x = 1
# print(type(x))

# # Casting
# y = 2.8
# print(int(y))

# # String
# z = 'Ami basic sikhci'
# print(z[4])
# print(z[4:10])
# print(z[:4])
# for i in z:
#     print(i)
# if 'basic' in z:
#     print('ami asolei basic sikhci')
# if 'advance' not in z:
#     print('ami asolei advance sikhci na')

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# # List
# amarList = ['ami', 'amar', 'amader', 'akn', 'amar', 'duplicate', 34, True, 
#             'Different Data Types Allow']
# print(amarList)
# print(amarList[5], amarList[8], amarList[:3], len(amarList))
# if 'ami' in amarList:
#     print('ami list e achi')
# amarList[3] = 'akn change kore fellam'
# print(amarList)
# amarList.insert(4, 'change er pore add korlam')
# print(amarList)
# notunList = ['notun', 'list', 'aita']
# amarList.append('new vabe seseh add hoilam')
# amarList.extend(notunList)
# print(amarList)
# # amarList.sort() # Need to have same type
# copyKorci = amarList.copy()
# print(copyKorci)
# joinList = ['join']
# twoList = amarList + joinList
# print(twoList)

# # Tuple
# amarTuple =('ordered', 'unchangeable', 'deletable by making it list', 'allow duplicates')
# print(amarTuple)
# print(len(amarTuple))
# thisisTuple=('one item',)
# print(type(thisisTuple))
# thisisnotTuple = ('one item')
# print(type(thisisnotTuple))
# notunadd = ('notun tuple',)
# amarTuple += notunadd
# print(amarTuple)
# for x in amarTuple:
#     print(x)

# # Set
# myset = {'unordered', 'unchangeable', 'no duplicates', 'unindexed'}
# print('unordered' in myset)
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)

# # Dictionaries
# thisDict = {
#     "have": "ordered or unordered",
#     "changeable": "changeable",
#     "no duplicates": "no duplicates",
# }
# print(thisDict["changeable"])
# print(thisDict.keys())
# thisDict.update({"add": "ai vabe add kore"})
# print(thisDict)

# # Function
# def my_function():
#   print("Hello from a function")
# my_function()