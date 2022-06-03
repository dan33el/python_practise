def my_substr(string, num):
    i = 0
    substr = ''
    while i < num:
        current_char = string[i]
        substr = substr + current_char
        i += 1
    print(substr)

my_substr('testing string', 5)