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

fout = open(sys.argv[3], "w")
fout.write('Latitude, Longitude, Stop Name, Stop Status')
fout.write("\n")


list_vehicle_details = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

for vehicle in range(len(list_vehicle_details)):
    latitude = str(list_vehicle_details[vehicle]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    longitude = str(list_vehicle_details[vehicle]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    
    list_onward_call = list_vehicle_details[vehicle]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall']
    for call in range(len(list_onward_call)):
        stop_name = str(list_onward_call[call]['StopPointName'])
        if stop_name == '': stop_name='N/A'
        stop_status = str(list_onward_call[call]['Extensions']['Distances']['PresentableDistance'])
        if stop_status == '': stop_status='N/A'
        fout.write("\n")
        fout.write(latitude + ", "+longitude + ", " + stop_name + ", " + stop_status)
    
