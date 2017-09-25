import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

list_vehicle_details = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
#print name of the bus
print("Bus Line: " + list_vehicle_details[0]['MonitoredVehicleJourney']['PublishedLineName'])
#print number of active buses
print("Number of Active Buses: " + str(len(list_vehicle_details)))
#print location
for vehicle in range(len(list_vehicle_details)):
    latitude = str(list_vehicle_details[vehicle]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    longitude = str(list_vehicle_details[vehicle]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    print("Bus "+str(vehicle)+ " is at latitude "+latitude+" and longitude "+ longitude)