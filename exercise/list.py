city_list = ['tokyo','osaka','yamagata']

print(city_list[2])

city_list[2] = 'miyazaki'
print(city_list[2])

city_list.extend(['nagoya','fukuoka'])

for i in range(len(city_list) -1):
    print(city_list)

city_list.append('sapporo')

for i in range(len(city_list) -1):
    print(city_list)