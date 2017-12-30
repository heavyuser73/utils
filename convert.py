
input = open("한국속담.csv", 'r')
output = open("한국속담.out", 'w')
output.write("[")
output.write("\n")
while True:
    line = input.readline()
    if not line: break

    line = line.strip()
    line = line.strip("\"")
    if len(line) > 2 :
        strTemp = "\"" + line + "\"" + "," + "\n"
        output.write(strTemp)
    
output.write("]")
output.write("\n")

input.close()
output.close()

