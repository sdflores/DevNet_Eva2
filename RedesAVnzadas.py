import urllib.parse 
import requests

while True:
    main_api = "https://www.mapquestapi.com/directions/v2/route?" 
    orig = input("Origen (Ciudad, Pais): ")
    if orig == "S" or orig == "salida": 
        break  
    dest = input("Destino (Ciudad, Pais): ")
    if dest == "S" or dest == "salida": 
        break  
    key = "FZt607NjrKFLOktpcn6QHhd9UUh1sxIx"  
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "unit": "k"}) 
    json_data = requests.get(url).json() 

    print("URL: " + url) 
    json_status = json_data["info"]["statuscode"] 

    if json_status == 0:     
        print("API Status: " + str(json_status) + " = Llamada a ruta correcta.\n")
        print("=============================================")         
        print("Dirección de origen: " + orig + " Hacia: " + dest)         
        print("Duración del viaje: " + json_data["route"]["formattedTime"])         
        print("Kilómetros: " + str("{:.1f}".format(json_data["route"]["distance"]))) 
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " (" + str("{:.1f}".format(each["distance"])) + " km)")	 
    print("=====================================================\n")

