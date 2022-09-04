# Programming questions 4
def calculateString(string):
    output = ''
    for s in string:
        if s not in output:
            output += s + str(string.count(s))
    return output

inputString = 'occurrences'
# print(calculateString(inputString))

# Programming questions 6
def camelToSnake(string):
    camel = ''
    for char in string:
        if char.isupper():
            camel += '_' + char.lower()
        else:
            camel += char
    
    if string[0].isupper():
        return camel[1:]
    return camel 

camel1 = 'HackerEarth'
camel2 = 'macOS'

# print(camelToSnake(camel1))
# print(camelToSnake(camel2))

# Programming questions 7
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

def time_notification(time):
    time_input = time.split(':')
    time_now = current_time.split(':')

    hour = int(time_input[0]) - int(time_now[0])
    minutes = int(time_input[1]) - int(time_now[1])
    second = int(time_input[2]) - int(time_now[2])

    if time_input == time_now:
        return 'now'
    elif hour > 0:
        return str(hour) + ' hours ago'
    elif hour == 0 and minutes > 0:
        return str(minutes) + ' minute ago'
    elif hour == 0 and minutes == 0 and second > 0:
        return str(second) + ' seconds ago'

# print(time_notification('23:08:05'))

# Programming questions 9 
def rearranging(n, array):
    m = n //2
    tmp = array
    for i in range(1, len(tmp)):
        tmp[i], tmp[m+1] = tmp[m+1], tmp[i]
    
    if tmp[:m] == tmp[m:0]:
        return 'YES'
    else:
        return 'NO'

N = 4
test1 = [5, 5, 7, 7]
xx = ['5', ' ', '7', '5', '7', ' ']
xx.remove(' ')
print(xx)