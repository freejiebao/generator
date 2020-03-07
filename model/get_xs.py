import os
import glob
from __future__ import print_function

if __name__ == "__main__":
    params = [('21', 'cW'),
        ('24', 'cHbox'),
        ('25', 'cHDD'),
        ('28', 'cHW'),
        ('30', 'cHB'),
        ('32', 'cHWB'),
        ('45', 'cHl1'),
        ('46', 'cHl3'),
        ('47', 'cHe'),
        ('48', 'cHq1'),
        ('49', 'cHq3'),
        ('50', 'cHu'),
        ('51', 'cHd'),
        #('53', 'cll'),
        ('54', 'cll1'),
        ('55', 'cqq1'),
        ('56', 'cqq11'),
        ('57', 'cqq3'),
        ('58', 'cqq31'),
    ]

    process_list=[]
    for ipar,param in enumerate(params):
        # 1D cards
        single_opt=params[ipar][1]

        int_process=single_opt+"_int"
        bsm_process=single_opt+"_bsm"

        process_list.append(int_process)
        process_list.append(bsm_process)
        # 2D
        for jpar in range(ipar+1,len(params)):
            d2_process=params[ipar][1] + '_' + params[jpar][1]
            process_list.append(d2_process)

    process_log_pair={}
    process_list_idle=process_list
    process_list_failed=[]
    log_list=glob.glob("log/*out*")
    for ilog in log_list:
        for iprocess in process_list:
            if iprocess+'.out' in ilog:
                process_log_pair[iprocess]=ilog
                process_list_idle.remove(iprocess)
                break
            else:
                pass

    for ipair in process_log_pair:
        xs=''
        with open(process_log_pair[ipair],'r') as outfile:
            for line in outfile:
                if '     Cross-section' in line:
                    xs=line.replace('     Cross-section :','')
                    xs.strip()
                    print(ipair+'\t'+xs)
                    break
            if xs=='':
                process_list_failed.append(ipair)

    print('have error, please check')
    for i in process_list_failed:
        print(i,end=' ')
    print('not out, might be idle')
    for i in process_list_idle:
        print(i,end=' ')