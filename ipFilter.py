def filterIP(ipLocations, country = None, state = None, city = None):
    results = []
    topResult = []
    for ip in ipLocations:
        if ip[1] == city and ip[2] == state and ip[3] == country:
            results = []
            topResult.append(ip)
        elif ip[1] == city or ip[2] == state or ip[3] == country:
            newResult = [ip[0], ip[1], ip[2], ip[3]]
            if topResult is True:
                results = []
                for ip in topResult:
                    if ip[1] == newResult[1] and ip[2] == newResult[2] and ip[3] == newResult[3]:
                        topResult.append(newResult)
                    else:
                        results = []
            else:
                results.append(newResult)
    if not results:
        return "Ip not found"
    elif topResult is True:
        return topResult
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
