import os
import sys

if __name__ == "__main__":
    for i in range(1,len(sys.argv)):
        print('remove:')
        print('log/*{0}.*'.format(sys.argv[i]))
        os.system('rm log/*{0}.*'.format(sys.argv[i]))
        os.system('condor_submit submit_{0}.jdl'.format(sys.argv[i]))