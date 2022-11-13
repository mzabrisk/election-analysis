#We set the variable x = 0 before we enter the loop.
#We test if x is less than or equal to 5.
#If this condition is true, then we print the value of x.
#With x = x + 1, we increment x by 1.
#The condition is tested again
#We repeat this process until the condition is false. When x is greater than 5, the loop stops.

x=0

while x<=5:
    print(x)
    x=x+1


counties = ["Arapahoe", "Denver", "Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county in counties:
    print(county)

    #Arapahoe
    #Denver
    #Jefferson

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

    #0
    #1
    #2
    #3
    #4

for num in range(5):
    print(num)

    #0
    #1
    #2
    #3
    #4


#The variable i is used to indicate the index, or the values 0, 1, and 2, in the length of the counties list. The letter i is often used for simplicity, but any variable can be used.
#Inside the range() function, we get the length of the list of counties, which is the integer 3.
#Then, we iterate through the list, where the variable i is equal to 0 for the first index. The 0 is passed into the print(counties[i]) statement, where i = 0, and "Arapahoe" is printed.
#This process is continued until all three items, or counties, in the list are printed to the screen.

for i in range(len(counties)):
    print(counties[i])

    #Arapahoe
    #Denver
    #Jefferson


for county in counties_dict:
    print(county)

    #Arapahoe
    #Denver
    #Jefferson

for county in counties_dict.keys():
    print(county)

     #Arapahoe
    #Denver
    #Jefferson

for voters in counties_dict.values():
    print(voters)

    #422829
    #463353
    #432438

for county in counties_dict:
    print(counties_dict[county])

    #422829
    #463353
    #432438

for county in counties_dict:
    print(counties_dict.get(county))

    #422829
    #463353
    #432438

#for key,value in dictionary_name.items():
    #print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)

    #Arapahoe 422829
    #Denver 463353
    #Jefferson 432438

for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " regiestered voters.")

    #Arapahoe county has 422829 regiestered voters.
    #Denver county has 463353 regiestered voters.
    #Jefferson county has 432438 regiestered voters.

for county_dict in voting_data:
    print(county_dict)

    #{'county': 'Arapahoe', 'registered_voters': 422829}
    #{'county': 'Denver', 'registered_voters': 463353}
    #{'county': 'Jefferson', 'registered_voters': 432438}

for i in range(len(voting_data)):
    print(voting_data[i]["county"])

    #Arapahoe
    #Denver
    #Jefferson

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

        #Arapahoe
        #422829
        #Denver
        #463353
        #Jefferson
        #432438

for county_dict in voting_data:
    print(county_dict["registered_voters"])

    #422829
    #463353
    #432438

for county_dict in voting_data:
    print(county_dict["county"])

    #Arapahoe
    #Denver
    #Jefferson