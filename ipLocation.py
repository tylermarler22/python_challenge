import geoip2.database
def locateIp(ipAddress):
    noLocation = "This IP has not been assigned"
    noCity, noState = "No associated city for this IP", "No associated state for this IP"
    column,row = 4, len(ipAddress)
    ipLocation = [[0 for c in range(column)]for r in range(row)]
    reader = geoip2.database.Reader("GeoLite2-City/GeoLite2-City.mmdb")
    for i in range(len(ipAddress)):
            ip = ipAddress[i]
            ipLocation[i][0] = ip
            try:
                response = reader.city(ip)
                cityName = response.city.name
                countryName = response.country.name
                stateName = response.subdivisions.most_specific.name
                if stateName is None:
                    ipLocation[i][1]= noCity
                    ipLocation[i][2] = noState
                    ipLocation[i][3] = countryName
                elif cityName is None:
                    ipLocation[i][1]= noCity
                    ipLocation[i][2] = stateName
                    ipLocation[i][3] = countryName
                else:
                    ipLocation[i][1] = cityName
                    ipLocation[i][2] = stateName
                    ipLocation[i][3] = countryName
            except geoip2.errors.AddressNotFoundError:
                ipLocation[i][1] = noLocation
                ipLocation[i][2] = noLocation
                ipLocation[i][3] = noLocation
    reader.close()
    return ipLocation
