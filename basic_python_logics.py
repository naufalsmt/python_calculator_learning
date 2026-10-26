from os import name

listing = [
    1, 2, "apple"
]

a= listing[0]
b= listing[1]
c= listing[2]
print(a, b, c)

listing.append("banana")
print(listing)

listing.remove(2)
print(listing)

listing[2] = 'strawberry'
print(listing)

dic1 = {
    'name' : 'Naufal',
    'age' : 20,
    'role' : "QA"
}
var1 = dic1['name']
print(var1)

dic1['exp'] = 5
print(dic1)

var2 = dic1.get('country')
print(var2)

set1 = {1,2,3,3,4}
print(set1) # print unique value in set 1, remove duplicates
set2 = {1,2,9,0}
print(set1 - set2) # value in set 1 and not in set 2
print(set2 - set1) # value in set 2 and not in set 1