import os

if __name__ == "__main__":
    params = [('21', 'cW'),
        ('24', 'cHbox'),
        ('25', 'cHDD'),
        ('28', 'cHW'),
        #('30', 'cHB'),
        ('32', 'cHWB'),
        ('45', 'cHl1'),
        ('46', 'cHl3'),
        ('47', 'cHe'),
        ('48', 'cHq1'),
        ('49', 'cHq3'),
        #('50', 'cHu'),
        #('51', 'cHd'),
        #('53', 'cll'),
        ('54', 'cll1'),
        ('55', 'cqq1'),
        ('56', 'cqq11'),
        ('57', 'cqq3'),
        ('58', 'cqq31'),
    ]
    with open('hadd.log','w') as log:
        # loop over parameters to be restricted
        for ipar,param in enumerate(params):
            # 1D cards
            # int
            in_name=params[ipar][1]+'_int_*.root'
            out_name=params[ipar][1]+'_int.root'
            
            nfiles=0
            try:
                p=os.popen('ls -l ../{0} | grep "^-" | wc -l'.format(in_name))
                nfiles=int(p.read())
            except:
                log.write('>>>>>>>>>> {0} not done, please check\n'.format(out_name))
            
            if nfiles > 0:
                if os.path.exists(params[ipar][1]+ '_int'):
                    print('========== '+params[ipar][1]+'_int exist')
                else:
                    os.mkdir(params[ipar][1]+ '_int')
                    os.system('haddnano.py {0}_int/{1} ../{2}'.format(params[ipar][1],out_name,in_name))
                    events=nfiles*2500
                    log.write('---------> {0}:{1}\n'.format(out_name,events))
            else:
                log.write('>>>>>>>>>> {0} not done, please check\n'.format(out_name))
            # bsm
            in_name=params[ipar][1]+'_bsm_*.root'
            out_name=params[ipar][1]+'_bsm.root'
            nfiles=0
            try:
                p=os.popen('ls -l ../{0} | grep "^-" | wc -l'.format(in_name))
                nfiles=int(p.read())
            except:
                log.write('>>>>>>>>>> {0} not done, please check\n'.format(out_name))
            
            if nfiles > 0:
                if os.path.exists(params[ipar][1]+ '_bsm'):
                    print('========== '+params[ipar][1]+'_bsm exist')
                else:
                    os.mkdir(params[ipar][1]+ '_bsm')
                    os.system('haddnano.py {0}_bsm/{1} ../{2}'.format(params[ipar][1],out_name,in_name))
                    events=nfiles*2500
                    log.write('---------> {0}:{1}\n'.format(out_name,events))
            else:
                log.write('>>>>>>>>>> {0} not done, please check\n'.format(out_name))

            # 2D cards
            for jpar in range(ipar+1,len(params)):
                in_name=params[ipar][1] + '_' + params[jpar][1]+'_*.root'
                out_name=params[ipar][1] + '_' + params[jpar][1]+'.root'
                nfiles=0
                try:
                    p=os.popen('ls -l ../{0} | grep "^-" | wc -l'.format(in_name))
                    nfiles=int(p.read())
                except:
                    log.write('>>>>>>>>>> {0} not done, please check\n'.format(out_name))
                if nfiles > 0:
                    if os.path.exists(params[ipar][1]+ '_'+params[jpar][1]):
                        print('========== '+params[ipar][1]+ '_'+params[jpar][1]+' exist')
                    else:
                        os.mkdir(params[ipar][1]+ '_'+params[jpar][1])
                        os.system('haddnano.py {0}/{1} ../{2}'.format(params[ipar][1]+ '_'+params[jpar][1],out_name,in_name))
                        events=nfiles*2500
                        log.write('---------> {0}:{1}\n'.format(out_name,events))
                else:
                    log.write('>>>>>>>>>> {0} not done, please check\n'.format(out_name))
