from weather.ob_havo import Obhavo

data = Obhavo(city='samarqand').main()
print(data)