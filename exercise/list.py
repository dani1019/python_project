#methods of list
city_list = ['osaka','tokyo']

#method of extend
city_list.extend(['fukuoka','sappro','tokyo'])

print(f"city_list_expend {city_list}")

#method pf append
city_list.append('nagoya')

print(f"city_list_append {city_list}")

#method of insert
city_list.insert(2,'miyazaki')

print(f"city_list_insert {city_list}")

#count of city_list's word
print(city_list.count('tokyo'))

city_list.sort()

print(f"sort of city_list {city_list}")

city_list.reverse()

print(f"reverse of city_list {city_list}")

print(city_list.pop())

print(city_list)

print(city_list.index('tokyo'))

stack = [3,4,5]
stack.append(6)

print(stack)

stack.pop()
print(stack)
