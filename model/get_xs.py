import os
import glob

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

    params_copy = [('21', 'cW'),
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
    not_out=[]
    have_error=[]
    outlog=glob.glob("log/*out*")
    for ipar,param in enumerate(params):
        # 1D cards
        single_opt=params[ipar][1]
        # int
        int_process=single_opt+"_int"
        for ilog in outlog:
            xs=''
            if int_process+'.out' in ilog:
                with open(ilog,'r') as outfile:
                    for line in outfile:
                        if '     Cross-section' in line:
                            xs=line.replace('     Cross-section :','')
                            print('int_process\t'+xs)
                            break
                        else:
                            have_error.append(int_process)
            else:
                not_out.append(int_process)

            # bsm
            bsm_process=single_opt+"_bsm"
            for ilog in outlog:
                xs=''
                if bsm_process+'.out' in ilog:
                    with open(ilog,'r') as outfile:
                        for line in outfile:
                            if '     Cross-section' in line:
                                xs=line.replace('     Cross-section :','')
                                print('int_process\t'+xs)
                                break
                            else:
                                have_error.append(bsm_process)
                else:
                    not_out.append(bsm_process)
        # 2D
        for jpar in range(ipar+1,len(params)):
            d2_process=params[ipar][1] + '_' + params[jpar][1]
            for ilog in outlog:
                xs=''
                if d2_process+'.out' in ilog:
                    with open(ilog,'r') as outfile:
                        for line in outfile:
                            if '     Cross-section' in line:
                                xs=line.replace('     Cross-section :','')
                                print('int_process\t'+xs)
                                break
                            else:
                                have_error.append(d2_process)
                else:
                    not_out.append(d2_process)
    print('have error, please check')
    for i in have_error:
        print(i)
    print('not out, maight be idle')
    for i in not_out:
        print(i)