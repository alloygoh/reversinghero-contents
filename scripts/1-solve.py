a = "abcdefghijklmnopqrstuvwxyz012345"
b = "lfatoi1wrd4zmgbupj2xse50nhcvqk3y"
indexes = []
for i in a:
    indexes.append(b.find(i))
key = ""
const = "89349536319392163324855876422573"
for x in indexes:
    key += const[x]
print(key)
