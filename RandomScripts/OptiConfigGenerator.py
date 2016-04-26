'''
generates the scipts for running optimization on scinet
'''
from AutoGrouper import stepList

def getBase():
    '''
    the base config script without variables
    '''
    
    return "\
[Settings]\n\
base_directory= {0}\n\
output_directory= {1}\n\
organism= yeast\n\
input_type= nucmer\n\
file_name= Toxo20.txt\n\
reference= S288C\n\
optimize= True\n\
optimize_level= 3\n\
section_length= 8000\n\
S1_iVal= {2}\n\
S1_piVal= {3}\n\
S2_iVal= 5\n\
S2_piVal= 1.5\n\
[Optimization]\n\
section_length_min= 2000\n\
section_length_max= 10000\n\
section_length_step= 2000\n\
S1_iVal_min= {2}\n\
S1_iVal_max= {2}\n\
S1_iVal_step= 0\n\
S1_piVal_min= {3}\n\
S1_piVal_max= {3}\n\
S1_piVal_step= 0\n\
S2_iVal_min= 1\n\
S2_iVal_max= 10\n\
S2_iVal_step= 0.5\n\
S2_piVal_min= 1\n\
S2_piVal_max= 10\n\
S2_piVal_step= 0.5"

def makeConfigs():
    base_directory = '/scratch/j/jparkins/xescape/yeast/input_files'
    output_directory = '/scratch/j/jparkins/xescape/yeast/opti'
    working_directory = '/data/new/javi/configs_temp'
    S1_iMin = 1
    S1_iMax = 10
    S1_iStep = 0.5
    S1_piMin = 1
    S1_piMax = 10
    S1_piStep = 0.5
    
    i_list = stepList(S1_iMin, S1_iMax, S1_iStep)
    pi_list = stepList(S1_piMin, S1_piMax, S1_piStep)
    
    name_pattern = 'Config_I{}PI{}.txt'
    
    for i in i_list:
        for pi in pi_list:
            with open('/'.join([working_directory, name_pattern.format(int(i * 10), int(pi * 10))]), 'w') as output:
                output.write(getBase().format(base_directory, '/'.join([output_directory, 'I{}PI{}'.format(int(i * 10), int(pi * 10))]), i, pi))
    
if __name__ == '__main__':
    
    makeConfigs()    