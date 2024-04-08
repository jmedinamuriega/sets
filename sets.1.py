# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline
# with a competitor. You have two sets of flight destinations, one for each airline. 
# Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
# Example Code:


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
my_list={"UYU", "CDG", "LHR", "AR"}
unique_routes=[]
unique_flies=[]
shared_flies=[]

for route in my_list:
    if route not in our_routes and route not in competitor_routes:
        unique_routes.append(route)

for route in our_routes:
    if route in competitor_routes:
        shared_flies.append(route)    
    else:
        unique_flies.append(route)


print(f"There is {unique_flies} unique flies and {shared_flies} shared flies")
print(f"Here is a list of routes that the airlines don't aboard {unique_routes}")
