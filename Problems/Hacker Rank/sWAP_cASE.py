def swap_case(s):
    length= len(s)
    s1=""
    for i in range (length):
        if s[i].isupper():
            s1+=s[i].lower()
        else:
            s1+=s[i].upper()
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)