def getSizeForUrl(size):
    baseUrlNumber = 590
    minSize = 7
    return (size - 7) * 20

def makeUrlForShoe(shoeId):
    return 'https://www.adidas.com/us/' + shoeId + '.html'

def makeUrlWithSize(shoeId, size):
    sizeNumber = getSizeForUrl(size)
    baseUrl = makeUrlForShoe(shoeId)
    return baseUrl + '?forceSelSize=' + shoeId + '_' + str(sizeNumber)