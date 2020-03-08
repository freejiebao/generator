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

    for ipar,param in enumerate(params):
        # 1D cards
        single_opt=params[ipar][1]
        # int
        int_process=single_opt+"_int"
        with open('submit_{0}.jdl'.format(int_process),'w') as outfile:
            outfile.write("Universe = vanilla\n")
            outfile.write("Executable = wrapper_{0}.sh\n".format(int_process))
            outfile.write("arguments = \"{0}\" $(Process)\n".format(int_process))
            outfile.write("RequestCpus = 4\n")
            outfile.write("should_transfer_files = YES\n")
            outfile.write("Error = log/{0}.err_$(Cluster)-$(Process)\n".format(int_process))
            outfile.write("Output = log/{0}.out_$(Cluster)-$(Process)\n".format(int_process))
            outfile.write("Log = log/{0}.log_$(Cluster)\n".format(int_process))
            outfile.write("transfer_output_remaps = \"cmsgrid_final.lhe = {}_$(Cluster)_$(Process).lhe\"\n".format(int_process))
            outfile.write("when_to_transfer_output = ON_EXIT\n")
            outfile.write("Queue 15\n")
        os.system("curl http://stash.osgconnect.net/+jiexiao/wrapper_events.sh -o wrapper_{0}.sh".format(int_process))

        # bsm    
        bsm_process=single_opt+"_bsm"
        with open('submit_{0}.jdl'.format(bsm_process),'w') as outfile:
            outfile.write("Universe = vanilla\n")
            outfile.write("Executable = wrapper_{0}.sh\n".format(bsm_process))
            outfile.write("arguments = \"{0}\" $(Process)\n".format(bsm_process))
            outfile.write("RequestCpus = 4\n")
            outfile.write("should_transfer_files = YES\n")
            outfile.write("Error = log/{0}.err_$(Cluster)-$(Process)\n".format(bsm_process))
            outfile.write("Output = log/{0}.out_$(Cluster)-$(Process)\n".format(bsm_process))
            outfile.write("Log = log/{0}.log_$(Cluster)\n".format(bsm_process))
            outfile.write("transfer_output_remaps = \"cmsgrid_final.lhe = {}_$(Cluster)_$(Process).lhe\"\n".format(bsm_process))
            outfile.write("when_to_transfer_output = ON_EXIT\n")
            outfile.write("Queue 15\n")
        os.system("curl http://stash.osgconnect.net/+jiexiao/wrapper_events.sh -o wrapper_{0}.sh".format(bsm_process))

        # 2D
        for jpar in range(ipar+1,len(params)):
            d2_process=params[ipar][1] + '_' + params[jpar][1]
            with open('submit_{0}.jdl'.format(d2_process),'w') as outfile:
                outfile.write("Universe = vanilla\n")
                outfile.write("Executable = wrapper_{0}.sh\n".format(d2_process))
                outfile.write("arguments = \"{0}\" $(Process)\n".format(d2_process))
                outfile.write("RequestCpus = 4\n")
                outfile.write("should_transfer_files = YES\n")
                outfile.write("Error = log/{0}.err_$(Cluster)-$(Process)\n".format(d2_process))
                outfile.write("Output = log/{0}.out_$(Cluster)-$(Process)\n".format(d2_process))
                outfile.write("Log = log/{0}.log_$(Cluster)\n".format(d2_process))
                outfile.write("transfer_output_remaps = \"cmsgrid_final.lhe = {}_$(Cluster)_$(Process).lhe\"\n".format(d2_process))
                outfile.write("when_to_transfer_output = ON_EXIT\n")
                outfile.write("Queue 15\n")
            os.system("curl http://stash.osgconnect.net/+jiexiao/wrapper_events.sh -o wrapper_{0}.sh".format(d2_process))
