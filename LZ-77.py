def Compression(message):
    searchWindow=""
    temp=""
    v=[]
    for i in range(0,len(message)):
        temp+=message[i]
        if temp not in searchWindow:
            if len(temp)==1:
                v.append("<"+"0"+","+"0"+","+temp+">")
                searchWindow+=temp
                temp=""
            else:
                temp = temp[:-1]
                index=searchWindow.rfind(temp)
                v.append("<"+str(len(searchWindow)-index)+","+str(len(temp))+","+message[i]+">")
                searchWindow+=temp+message[i]
                temp=""
            if len(searchWindow)>12:
                searchWindow = searchWindow[len(temp)-12:]
    print(v)
    return v





def Decompression(v):
    message=""
    for i in range(0,len(v)):
        components = v[i][1:-1].split(',')
        index = int(components[0])
        length = int(components[1])
        newChar= components[2]
        
        if index == 0 and length == 0:
            message+=newChar
        else:
            temp = message[len(message)-index:len(message)-index+length]
            message+=temp+newChar
    print(message)
    return message

Decompression(Compression("ABAABABAABBBBBBBBBBBBA"))