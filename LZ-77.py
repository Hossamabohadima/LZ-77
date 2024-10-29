def Compression(message):
    searchWindow = ""
    temp = ""
    v = []

    for i in range(len(message)):
        temp += message[i]

        # Check if the current temp substring is not in the search window
        if temp not in searchWindow:
            if len(temp) == 1:
                v.append((0, 0, temp))
                searchWindow += temp
                temp = ""
            else:
                # Get the previous occurrence of the substring
                temp = temp[:-1]
                index = searchWindow.rfind(temp)
                v.append((len(searchWindow) - index, len(temp), message[i]))
                searchWindow += temp + message[i]
                temp = ""

            # Keep search window to a max size of 12
            if len(searchWindow) > 12:
                searchWindow = searchWindow[len(searchWindow) - 12:]

    # Ensure any remaining characters in temp are processed
    if temp:
        if len(temp) == 1:
            v.append((0, 0, temp))
        else:
            index = searchWindow.rfind(temp)
            v.append((len(searchWindow) - index, len(temp), ''))

    return v


def Decompression(v):
    message = ""
    for i in range(len(v)):
        index = int(v[i][0])
        length = int(v[i][1])
        newChar = v[i][2]

        if index == 0 and length == 0:
            message += newChar
        else:
            temp = message[len(message) - index:len(message) - index + length]
            message += temp + newChar

    return message


# Example usage
compressed = Compression("aaabbaa")
decompressed = Decompression(compressed)

print("Compressed:", compressed)
print("Decompressed:", decompressed)
