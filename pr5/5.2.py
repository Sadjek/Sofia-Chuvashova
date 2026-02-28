line = ""
stop = 0
while stop == 0:
    word = input()
    line += word + " "
    if word == "stop":
        stop = 1
print(line)