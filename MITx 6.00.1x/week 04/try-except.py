"""
It is wrong as we cannot close file that 
we did not open it before
"""

try:
    fh = open('test.txt')
except:
    print('Can not open a File')
else :
    print('good openning')
finally:
    fh.close()
