
if __name__ == "__main__":
    params = [(' 1', 'ceWPh'),      
        (' 2', 'ceBPh'),     
        (' 3', 'cuGPh'),     
        (' 4', 'cuWPh'),     
        (' 5', 'cuBPh'),     
        (' 6', 'cdGPh'),     
        (' 7', 'cdWPh'),     
        (' 8', 'cdBPh'),     
        (' 9', 'cHudPh'),        
        ('10', 'ceHPh'),      
        ('11', 'cuHPh'),      
        ('12', 'cdHPh'),      
        ('13', 'cledqPh'),          
        ('14', 'cquqd1Ph'),            
        ('15', 'cquqd8Ph'),            
        ('16', 'clequ1Ph'),            
        ('17', 'clequ3Ph'),            
        ('19', 'cG'),
        ('20', 'cGtil'),  
        ('21', 'cW'),  
        ('22', 'cWtil'),  
        ('23', 'cH'),
        ('24', 'cHbox'),  
        ('25', 'cHDD'),
        ('26', 'cHG'),
        ('27', 'cHGtil'),  
        ('28', 'cHW'),  
        ('29', 'cHWtil'),    
        ('30', 'cHB'),
        ('31', 'cHBtil'),    
        ('32', 'cHWB'),
        ('33', 'cHWBtil'),      
        ('34', 'ceHAbs'),               
        ('35', 'cuHAbs'),    
        ('36', 'cdHAbs'),    
        ('37', 'ceWAbs'),    
        ('38', 'ceBAbs'),    
        ('39', 'cuGAbs'),    
        ('40', 'cuWAbs'),    
        ('41', 'cuBAbs'),    
        ('42', 'cdGAbs'),    
        ('43', 'cdWAbs'),    
        ('44', 'cdBAbs'),    
        ('45', 'cHl1'),
        ('46', 'cHl3'),
        ('47', 'cHe'),
        ('48', 'cHq1'),
        ('49', 'cHq3'),
        ('50', 'cHu'),
        ('51', 'cHd'),
        ('52', 'cHudAbs'),      
        ('53', 'cll'),  
        ('54', 'cll1'),    
        ('55', 'cqq1'),    
        ('56', 'cqq11'),      
        ('57', 'cqq3'),    
        ('58', 'cqq31'),      
        ('59', 'clq1'),    
        ('60', 'clq3'),    
        ('61', 'cee'),  
        ('62', 'cuu'),  
        ('63', 'cuu1'),    
        ('64', 'cdd'),  
        ('65', 'cdd1'),    
        ('66', 'ceu'),  
        ('67', 'ced'),  
        ('68', 'cud1'),    
        ('69', 'cud8'),    
        ('70', 'cle'),  
        ('71', 'clu'),  
        ('72', 'cld'),  
        ('73', 'cqe'),  
        ('74', 'cqu1'),    
        ('75', 'cqu8'),    
        ('76', 'cqd1'),    
        ('77', 'cqd8'),    
        ('78', 'cledqAbs'),            
        ('79', 'cquqd1Abs'),        
        ('80', 'cquqd8Abs'),             
        ('81', 'clequ1Abs'),         
        ('82', 'clequ3Abs')
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
