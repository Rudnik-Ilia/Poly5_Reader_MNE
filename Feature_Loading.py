import time
import numpy

line = '='
line_2 = '='
span_2 = ' '
span = ' ' * 100


def convert(string):
    list1 = []
    list1[:0] = string
    list1.pop()
    span = ''.join(list1)
    return span


for i in range(101):
    x = span.replace(' ', '=', i)
    print(f'\r loadind: {i}%[{x}]', end='\r')
    # line+=line_2
    # convert(span)
    time.sleep(0.2)

if __name__ == '__main__':
    pass
