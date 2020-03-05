
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

    # loop over parameters to be restricted
    for ipar,param in enumerate(params):
        # get 1st operator for cross term
        for jpar in range(ipar+1,len(params)):
            # get 2nd operator for cross term
            f_restrict = open ('restrict_'+ params[ipar][1] + '_' + params[jpar][1] + '_massless.dat', 'w')
            f_restrict.write (contents_before)

            # loop over parameters to be written
            for kpar,param3 in enumerate(params):
                if kpar == ipar or kpar==jpar:
                    f_restrict.write ('   ' + param3[0] + ' 9.999999e-01 # ' + param3[1] + '\n')
                else:
                    f_restrict.write ('   ' + param3[0] + ' 0 # ' + param3[1] + '\n')
            f_restrict.write (contents_after)
            f_restrict.close ()
