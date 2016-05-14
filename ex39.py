#create a mapping of state to abrreviation

states ={
    "Oregon"        : "OR",
    "Florida"       : "FL",
    "California"    : "CA",
    "New York"      : "NY",
    "Michigan"      : "MI"
}

#create a basic set of states and some cities in them
cities = {
    "CA" : "San Franscisco",
    "MI" : "Detroit",
    "FL" : "Jacksonville"
    }

#add some more cities
cities["NY"] = "New York"
cities ["OR"] = "PortLand"

#print out some cities
print ("_" *10)
print("NY state has :", cities ["NY"])
print("OR state has :", cities ["OR"])

#print some states
print("_"*10)
print("Michigan's abreviation is ", states["Michigan"])
print("Florida's abreviation is ", states["Florida"])

#do it by using the state then cities dict
print("_"*10)
for state,abbrev in states.items():
    print("%s is abbreviated %s" %(state,abbrev))

#print every city in states
print ("_"*10)
for abbrev,city in cities.items():
    print("%s has the city %s " %(abbrev,city))

#now do both at the same time

print("_"*10)
for state,abbrev in states.items():
     print("%s state is abbreviated %s and has city %s" %
         (state,abbrev,cities[abbrev]))
print ("_"*10)
#safely get an abbreviation by state that might not be there
state = states.get("Texas", None)

if not state:
    print ("Sorry, no Texas")
#get the city with a default value

city = cities.get("TX", "Does Not Exist")
print("The city for the state TX is : %s"%city) 
