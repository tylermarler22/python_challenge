
def filterIP(ipLocations, country = None, state = None, city = None):
    results = []
    if city and state and country is not None:
        for ip in ipLocations:
            if ip[1] == city and ip[2] == state and ip[3] == country:
                newResult = [ip[0], city, state, country]
                results.append(newResult)
    elif (city and state) or (state and country) or (city and country) is not None:
        for ip in ipLocations:
            if ip[2] == state and ip[1] == city:
                newResult = [ip[0],city,state,ip[3]]
                results.append(newResult)
            elif ip[2] == state and ip[3] == country:
                newResult = [ip[0],ip[1],state,country]
                results.append(newResult)
            elif ip[3] == country and ip[1] == city:
                newResult = [ip[0], city, ip[2], country]
                results.append(newResult)
    elif city  is not None:
        for ip in ipLocations:
            if city == ip[1]:
                newResult = [ip[0], city, ip[2], ip[3]]
                results.append(newResult)
    elif state is not None:
        for ip in ipLocations:
            if state == ip[2]:
                newResult = [ip[0], ip[1], state, ip[3]]
                results.append(newResult)
    elif country is not None:
        for ip in ipLocations:
            if country == ip[3] and country:
                newResult = [ip[0], ip[1], ip[2], country]
                results.append(newResult)
    if not results:
        return "Ip not found"
    else:
        return results
def filterLocation(ipLocations, ipAddress):
    results = []
    for ip in ipLocations:
        if ipAddress == ip[0]:
            newResult = [ipAddress, ip[1], ip[2] , ip[3]]
            results.append(newResult)
    if not results:
        return "Ip not found"
    else:
        return results