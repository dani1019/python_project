travel_log = [
{
    "country" : "France",
    "visits" : 12,
    "cities" :["Paris","Lille","Dijon"]
},
{
    "country" : "Germany",
    "visits" : 5,
    "cities" : ["Berlin", "Hamburg", "Stuttgart"]
}
]

def add_new_country(country, visit_count,list):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visit_count
    new_country["cities"] = list

    travel_log.append(new_country)

    print(travel_log)

add_new_country("Russia",2,["Moscow", "Saint Peterburg"])

