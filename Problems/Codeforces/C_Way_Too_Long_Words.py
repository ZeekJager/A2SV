num_input= int(input())

for i in range (num_input):
    word= input()
    length= len(word)

    if length<=10:
        print(word)
    else:
        abbr= word[0]+str(length-2)+word[-1]
        print(abbr)