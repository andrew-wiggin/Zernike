def Sdf_input(path, diam):
    return path
def Cap_input(path, sensor_ch):
    import numpy as np
    tmp = []
    with open(path, 'r') as f:
        for line in f:
            ws = line.split(' ')
            tmp.append(ws[5].replace(',', '.'))
    marr = np.array(tmp, dtype='double')
    return marr;
    
path = 'cap_result_test.txt'
sensor_ch = 5
marr = Cap_input(path, sensor_ch)
print(marr)
    
    
