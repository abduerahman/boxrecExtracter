import re,csv

def checker(text):
    if(text.find('<span') == -1  and text.find('<i') == -1):
        return text
    start = 0;
    end = 0;

    if(text.find('<span') != -1):
       end = re.search('>naps/<', text[::-1]).span()[0]
       start= re.search('<span|<span>', text).span()[0]
    elif (text.find('<i') != -1):
        end = re.search('>i/<', text[::-1]).span()[0]
        start = re.search('<i|<i>', text).span()[0]

    return text[:start]+text[len(text)-end:]

def gettintagInfo(text):
    result = {'start':0,'end':0}
    result['end'] = re.search('</\w+>',text).span()[0]
    result['start'] = re.search('(\"| +)>|<\w+>', text).span()[1]
    return result

def extract_data(text):
    text= checker(text)
    values = gettintagInfo(text)
    return text[values['start']:values['end']].strip()

def finder(value,data):
    for i in range(0,len(data)):
        if data[i] == value:
            return i
    return -1

def adding_data(data):
    with open('fighterdata.csv', 'a', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(data)

def initlization(data,title):
    neededData = ['name', 'wins', 'loss', 'draws', 'sex',
                  'height', 'reach', 'stance', 'nationality', 'KOs']
    realData = [];
    for i in neededData:
        index = finder(i,title)
        if(index != -1):
            if(i == "height" or i == "reach"):
                cleand = data[index].split(" ")
                realData.append(cleand[len(cleand) - 1])
            else:
                realData.append(data[index])
        else:
            realData.append("None")
    adding_data(realData)