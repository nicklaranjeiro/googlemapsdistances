import urllib.request
import json

#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'PUT YOUR API KEY HERE'

#Give the original work address and lists of addresses.
#Format has to be (Number Street Name City Province)
#So for example 1280 Main Strret Hamilton ON

origin = ('PUT ORIGIN ADDRESS HERE').replace(' ','+')
destinations = ['Address1', 'Address2', 'Address3']
distances = []

#Goes through the array of addresses and calculated each of their distances
for i in range(len(destinations)):
 
    #Replaces the spaces with + so that it can properly work with the google maps api url
    currentDestination = destinations[i].replace(' ','+')

    #Building the URL for the request
    nav_request = 'origin={}&destination={}&key={}'.format(origin,currentDestination,api_key)

    #Builds the request to be sent
    request = endpoint + nav_request

    #Sends the request and reads the response.
    response = urllib.request.urlopen(request).read()

    #Loads response as JSON
    directions = json.loads(response)

    #Gets the distance from the address in the array to the origin address
    distance = directions["routes"][0]["legs"][0]["distance"]["text"]

    #Adds it to the list of distances found from each address
    distances.append(distance)

#Finds the closest distance using min
closestDistance = min(distances)

#Prints the closest distance to work
print("The closest distance to work is: " + closestDistance)
print("The address is: " + destinations[distances.index(closestDistance)])
