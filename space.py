import os
in_file=input("Target > ")
start= int(input("Starting line > "))
end=int(input("Ending line > "))
final= sum(1 for line in open(in_file))
with open(in_file, "r") as file:
    data= file.readlines()
    os.remove(in_file)
    with open(in_file, "a") as file2:
        n=0
        while n<final:
            if (start-2)<n & n<end:
                data[n] = "    "+data[n]
                file2.write(data[n])
            else:
                file2.write(data[n])
            n +=1