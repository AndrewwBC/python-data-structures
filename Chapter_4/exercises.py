# R-4.1

# list comprehension
elements = [number for number in range(200)]
# tuples = tuple(number for number in range(1000))
# dictio = {str(number): number for number in range(1000)}

# for i in range(100):
#     print(elements[i])
#     print(tuples[i])
#     print(dictio.get(str(i)))


start = 0
end = len(elements) - 1
aux = 0

# def findMaxElement(elements, start, end):
#     global aux
#     if elements[start] > aux:
#         aux = elements[start]
    
#     if start == end:
#         return aux

#     return findMaxElement(elements, start + 1, end)

# print(findMaxElement(elements, 0, end))


def productOfTwoPositiveIntegers(a, b):
    global aux
    if b != 0:
        aux = aux + a
    else:
        return aux
    
    return productOfTwoPositiveIntegers(a, b - 1)

print(productOfTwoPositiveIntegers(10,9))

string = "And"

def reverseString(textAsList: list, start, stop):

    if start > stop:
        result = ''
        for i in range(len(textAsList)):
            result = result + textAsList[i]
        return result    
    
    if len(text) == 0:
        return text 
    
    if len(text) > 0:
        originalElementAtStopIndex = textAsList[stop]
        textAsList[stop] = textAsList[start]
        textAsList[start] = originalElementAtStopIndex
    
    return reverseString(textAsList, start + 1, stop - 1)

text = "pots&pans"
textAsList: list = list(text)

print(reverseString(textAsList, 0, len(text) - 1))
