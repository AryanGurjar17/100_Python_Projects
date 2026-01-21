capitals = {
    "France" : "paris",
    "Germany" : "berlin",
}

#nested list in dictionary

travel_log = {
    "France": ["Paris", "Lille", "dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][0])

nested_list = ["A", "B", ["C","D"]]

print(nested_list[2][1])
#dict inside dict
travel_logs = {
    "France": {
        "cities_visited": ["Paris", "Lille", "dijon"],
        "total_visits" : 12
    },
    "Germany" : {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
print(travel_logs["France"]["cities_visited"][2])