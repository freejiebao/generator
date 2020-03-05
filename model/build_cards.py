import os

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

    f_before = open ('restrict_before.txt', 'r')
    contents_before = f_before.read ()
    f_before.close ()
    f_after  = open ('restrict_after.txt', 'r') 
    contents_after = f_after.read ()
    f_after.close ()

    extramodels_content=""
    extramodels_content+="# customized model for EWdim6 EFT in 5f\n"
    extramodels_content+="SMEFTsim_A_U35_MwScheme_UFO_v3.tar.gz"
    proc_card_0=""
    proc_card_0+="set group_subprocesses Auto\n"
    proc_card_0+="set ignore_six_quark_processes False\n"
    proc_card_0+="set loop_optimized_output True\n"
    proc_card_0+="set complex_mass_scheme False\n"

    proc_card_1=""
    proc_card_1+="define p = g u c d s b u~ c~ d~ s~ \n"
    proc_card_1+="define j = p\n"
    proc_card_1+="define l+ = e+ mu+ ta+\n"
    proc_card_1+="define l- = e- mu- ta-\n"
    proc_card_1+="define vl = ve vm vt\n"
    proc_card_1+="define vl~ = ve~ vm~ vt~\n"
    proc_card_1+="\n"
    with open('../../../../../run_card.dat','r') as runfile:
        run_content=runfile.read()
    # loop over parameters to be restricted
    for ipar,param in enumerate(params):
        # 1D cards
        # int
        process='VBS_SSWW_'+ params[ipar][1]+'_int'
        os.makedirs(process)
        with open(process+'/'+process+'_extramodels.dat','w') as outfile:
            outfile.write(extramodels_content)
        with open(process+'/'+process+'_proc_card.dat','w') as outfile:
            outfile.write(proc_card_0)
            outfile.write('import model SMEFTsim_A_U35_MwScheme_UFO_v3_1-'+params[ipar][1]+ '_massless\n')
            outfile.write(proc_card_1)
            outfile.write("generate p p > l+ l+ vl vl j j QCD=0 SMHLOOP=0 NP=1 NP^2==1\n")
            outfile.write("add process p p > l- l- vl~ vl~ j j QCD=0 SMHLOOP=0 NP=1 NP^2==1\n")
            outfile.write("output "+process)
        with open(process+'/'+process+'_run_card.dat','w') as outfile:
            outfile.write(run_content)

        # bsm
        process='VBS_SSWW_'+ params[ipar][1]+'_bsm'
        os.makedirs(process)
        with open(process+'/'+process+'_extramodels.dat','w') as outfile:
            outfile.write(extramodels_content)
        with open(process+'/'+process+'_proc_card.dat','w') as outfile:
            outfile.write(proc_card_0)
            outfile.write('import model SMEFTsim_A_U35_MwScheme_UFO_v3-'+params[ipar][1]+ '_massless\n')
            outfile.write(proc_card_1)
            outfile.write("generate p p > l+ l+ vl vl j j QCD=0 SMHLOOP=0 NP=1 NP^2==2\n")
            outfile.write("add process p p > l- l- vl~ vl~ j j QCD=0 SMHLOOP=0 NP=1 NP^2==2\n")
            outfile.write("output "+process)
        with open(process+'/'+process+'_run_card.dat','w') as outfile:
            outfile.write(run_content)

        for jpar in range(ipar+1,len(params)):
            # 2D cards
            process='VBS_SSWW_'+ params[ipar][1] + '_' + params[jpar][1]
            os.makedirs(process)
            with open(process+'/'+process+'_extramodels.dat','w') as outfile:
                outfile.write(extramodels_content)
            with open(process+'/'+process+'_proc_card.dat','w') as outfile:
                outfile.write(proc_card_0)
                outfile.write('import model SMEFTsim_A_U35_MwScheme_UFO_v3-'+params[ipar][1] + '_' + params[jpar][1]+ '_massless\n')
                outfile.write(proc_card_1)
                outfile.write("generate p p > l+ l+ vl vl j j QCD=0 SMHLOOP=0 NP=1 NP"+params[ipar][1]+"^2==1 NP"+params[jpar][1]+"^2==1\n")
                outfile.write("add process p p > l- l- vl~ vl~ j j QCD=0 SMHLOOP=0 NP=1 NP"+params[ipar][1]+"^2==1 NP"+params[jpar][1]+"^2==1\n")
                outfile.write("output "+process)
            with open(process+'/'+process+'_run_card.dat','w') as outfile:
                outfile.write(run_content)