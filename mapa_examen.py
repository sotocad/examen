import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "QfoGH3S4NYqFgOw88VkeSAGWBx1JoQiK"
idioma = "es"
kilom = "k"
while True: 
    orig = input("Ingrese Localizacion: ") 
    if orig == "salida" or orig == "s": 
        break
    dest = input("Destino: ")
    if dest == "quit" or dest == "q": 
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest, "locale":idioma, "unit":kilom})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================") 
        print("Direccion desde " + (orig) + " hasta " + (dest)) 
        print("Tiempo Duracion: " + (json_data["route"]["formattedTime"])) 
        print("Kilometros: " + str("{:.1f}".format((json_data["route"]["distance"]))))
        print("=============================================")
    for each in json_data["route"]["legs"][0]["maneuvers"]: 
        print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])) + " km)")) 
        print("=============================================\n")

