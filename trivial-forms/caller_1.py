#!python

# caller_1.py
# caller file for forms
# Mikhail Kolodin, 2020
# ver. 2020-02-27 1.0

from forms_1 import *

global_values = {'max': 5000, 'min': 100, 'name': 'Vasya'}

def main(args):
    local_values = {'max': 3000, 'name': 'Kirill'}
    my_values = {**global_values, **local_values}
	
    temp = templates['main_template']
    print ("template: ", temp)
    print ("values: ", my_values)
    print (temp.format(names = my_values))

    temp = templates['aux_template']
    print ("template: ", temp)
    print ("values: ", my_values)
    print (temp.format(names = my_values))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
