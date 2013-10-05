# FeedMyTrip

## Attempted integration of Yelp API and Google Maps API
I wanted to make an app which would, when the user entered the start and end locations of their road trip along with a distance, output a map of highly-rated restaurants (distance) away from their road trip path.  I used Yelp's Search API v2 and Google Maps Api V3 (map, DirectionService, Geocoding, Places).

## Challenges
The API's are more limited than I thought.  For example:
- Yelp API doesn't return lat/long locations so geocoding is necessary to place restaurants onto a Google map (I think)
- Google's Geocoding, when done client-side, has a query-limit of 20. When done server-side, I believe it has a limit of 2500.  However, even for short road trips, I would have had to make 20 (number of restaurants returned by Yelp) * hundreds (number of points on overview_path in Maps API) of queries to geocode all the restaurants.
- Even with limited server-side computation for geocoding, the latency is still too high to be usable.
