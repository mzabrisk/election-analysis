#print("Hello World")
# How many votes did you get?
#my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe", "Denver", "Jefferson"]
#if counties[1] == "Denver":
#    print(counties[1])

#if counties[3] != "Jefferson":
#    print(counties[2])

#if-else
if "El Paso" in counties:
    print("El Paso is in the list of counties")

else:
    print ("El Paso is not in the list of counties")

#if-and
if "Arapahoe" in counties and "El PAso" in counties:
    print("Arapahoe and El Paso are in the list of counties")

else:
    print("Arapahoe or El Paso is not in the lis of counties.")

#if-or
if "Arapahoe" in counties or "El PAso" in counties:
    print("Arapahoe or El Paso is in the list of counties")

else:
    print("Arapahoe or El Paso is not in the lis of counties.")


for county in counties:
    print(county)