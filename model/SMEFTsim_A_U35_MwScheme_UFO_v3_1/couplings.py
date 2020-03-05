# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Tue 18 Feb 2020 12:04:44


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(-2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '(cth**2*dg1*ee*complex(0,1))/3.',
                order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = '(-2*cth**2*dg1*ee*complex(0,1))/3.',
                order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'cth**2*dg1*ee*complex(0,1)',
                order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = '(dg1*ee**2*complex(0,1))/cth**2',
                order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-2*cth**2*dg1*ee**2*complex(0,1)',
                 order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(complex(0,1)*G)',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'G',
                 order = {'QCD':1})

GC_13 = Coupling(name = 'GC_13',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '6*dGf*complex(0,1)*lam*cmath.sqrt(2)',
                 order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '(2*cdd*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcdd':1,'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '(2*cdd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcdd1':1,'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '(ced*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPced':1,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(2*cee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcee':1,'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(ceu*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPceu':1,'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(-6*cG)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcG':1,'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = 'cGtil/LambdaSMEFT**2',
                 order = {'NP':1,'NPcGtil':1,'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '(90*cH*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcH':1,'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(-3*cHbox*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHbox':1,'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '-((cHDD*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcHDD':1,'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(4*cHG*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHG':1,'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(-2*cHGtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHGtil':1,'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '(4*cHW*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHW':1,'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(4*cHWtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHWtil':1,'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(cld*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcld':1,'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(cle*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcle':1,'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(2*cll*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcll':1,'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(2*cll1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcll1':1,'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(clq1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq1':1,'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '-((clq3*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(2*CKM1x1*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(2*CKM1x2*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(2*CKM1x3*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(2*CKM2x1*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(2*CKM2x2*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(2*CKM2x3*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(2*CKM3x1*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(2*CKM3x2*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(2*CKM3x3*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclq3':1,'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(clu*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPclu':1,'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '(cqd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqd1':1,'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cqd8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqd8':1,'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cqe*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqe':1,'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(2*cqq1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqq1':1,'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '(2*cqq11*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqq11':1,'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '(-2*cqq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqq3':1,'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(2*cqq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqq3':1,'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(2*cqq31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqq31':1,'QED':2})

GC_55 = Coupling(name = 'GC_55',
                 value = '(4*cqq31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqq31':1,'QED':2})

GC_56 = Coupling(name = 'GC_56',
                 value = '(cqu1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqu1':1,'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(cqu8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcqu8':1,'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '(-2*cHBtil*cth**2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHBtil':1,'QED':2})

GC_59 = Coupling(name = 'GC_59',
                 value = '(-2*cHWtil*cth**2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHWtil':1,'QED':2})

GC_60 = Coupling(name = 'GC_60',
                 value = '(cud1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcud1':1,'QED':2})

GC_61 = Coupling(name = 'GC_61',
                 value = '(cud8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcud8':1,'QED':2})

GC_62 = Coupling(name = 'GC_62',
                 value = '(2*cuu*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcuu':1,'QED':2})

GC_63 = Coupling(name = 'GC_63',
                 value = '(2*cuu1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcuu1':1,'QED':2})

GC_64 = Coupling(name = 'GC_64',
                 value = '(6*cth*cW*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcW':1,'QED':2})

GC_65 = Coupling(name = 'GC_65',
                 value = '(2*cth*cWtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcWtil':1,'QED':2})

GC_66 = Coupling(name = 'GC_66',
                 value = '(4*cHW*ee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHW':1,'QED':3})

GC_67 = Coupling(name = 'GC_67',
                 value = '(2*cHWB*ee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHWB':1,'QED':3})

GC_68 = Coupling(name = 'GC_68',
                 value = '(-2*cHWBtil*ee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHWBtil':1,'QED':3})

GC_69 = Coupling(name = 'GC_69',
                 value = '(-4*cHWtil*ee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHWtil':1,'QED':3})

GC_70 = Coupling(name = 'GC_70',
                 value = '(6*cth*cW*ee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcW':1,'QED':3})

GC_71 = Coupling(name = 'GC_71',
                 value = '(-2*cth*cWtil*ee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcWtil':1,'QED':3})

GC_72 = Coupling(name = 'GC_72',
                 value = '(-4*cHW*ee**2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHW':1,'QED':4})

GC_73 = Coupling(name = 'GC_73',
                 value = '(-6*cth*cW*ee**2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcW':1,'QED':4})

GC_74 = Coupling(name = 'GC_74',
                 value = '(-4*cth*cWtil*ee**2*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'NPcWtil':1,'QED':4})

GC_75 = Coupling(name = 'GC_75',
                 value = '(-6*cG*complex(0,1)*G)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcG':1,'QCD':1,'QED':2})

GC_76 = Coupling(name = 'GC_76',
                 value = '(cGtil*complex(0,1)*G)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcGtil':1,'QCD':1,'QED':2})

GC_77 = Coupling(name = 'GC_77',
                 value = '(-4*cHG*G)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHG':1,'QCD':1,'QED':2})

GC_78 = Coupling(name = 'GC_78',
                 value = '(4*cHGtil*G)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHGtil':1,'QCD':1,'QED':2})

GC_79 = Coupling(name = 'GC_79',
                 value = '(-3*cG*G**2)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcG':1,'QCD':2,'QED':2})

GC_80 = Coupling(name = 'GC_80',
                 value = '(3*cG*G**2)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcG':1,'QCD':2,'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(-2*cGtil*G**2)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcGtil':1,'QCD':2,'QED':2})

GC_82 = Coupling(name = 'GC_82',
                 value = '(2*cGtil*G**2)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcGtil':1,'QCD':2,'QED':2})

GC_83 = Coupling(name = 'GC_83',
                 value = '(-4*cHG*complex(0,1)*G**2)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcHG':1,'QCD':2,'QED':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '-((cG*complex(0,1)*G**3)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcG':1,'QCD':3,'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cG*complex(0,1)*G**3)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcG':1,'QCD':3,'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '-((cGtil*complex(0,1)*G**3)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcGtil':1,'QCD':3,'QED':2})

GC_87 = Coupling(name = 'GC_87',
                 value = '(cGtil*complex(0,1)*G**3)/LambdaSMEFT**2',
                 order = {'NP':1,'NPcGtil':1,'QCD':3,'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '-((cquqd1*complex(0,1)*I1d11*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((cquqd8*complex(0,1)*I1d11*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_90 = Coupling(name = 'GC_90',
                 value = '-((cquqd1*complex(0,1)*I1d12*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((cquqd8*complex(0,1)*I1d12*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_92 = Coupling(name = 'GC_92',
                 value = '-((cquqd1*complex(0,1)*I1d13*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((cquqd8*complex(0,1)*I1d13*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_94 = Coupling(name = 'GC_94',
                 value = '-((cquqd1*complex(0,1)*I1d21*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_95 = Coupling(name = 'GC_95',
                 value = '-((cquqd8*complex(0,1)*I1d21*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_96 = Coupling(name = 'GC_96',
                 value = '-((cquqd1*complex(0,1)*I1d22*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((cquqd8*complex(0,1)*I1d22*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_98 = Coupling(name = 'GC_98',
                 value = '-((cquqd1*complex(0,1)*I1d23*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((cquqd8*complex(0,1)*I1d23*I6d11)/LambdaSMEFT**2)',
                 order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_100 = Coupling(name = 'GC_100',
                  value = '-((cquqd1*complex(0,1)*I1d31*I6d11)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((cquqd8*complex(0,1)*I1d31*I6d11)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((cquqd1*complex(0,1)*I1d32*I6d11)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((cquqd8*complex(0,1)*I1d32*I6d11)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_104 = Coupling(name = 'GC_104',
                  value = '-((cquqd1*complex(0,1)*I1d33*I6d11)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((cquqd8*complex(0,1)*I1d33*I6d11)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_106 = Coupling(name = 'GC_106',
                  value = '-((cquqd1*complex(0,1)*I1d11*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_107 = Coupling(name = 'GC_107',
                  value = '-((cquqd8*complex(0,1)*I1d11*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_108 = Coupling(name = 'GC_108',
                  value = '-((cquqd1*complex(0,1)*I1d12*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((cquqd8*complex(0,1)*I1d12*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((cquqd1*complex(0,1)*I1d13*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_111 = Coupling(name = 'GC_111',
                  value = '-((cquqd8*complex(0,1)*I1d13*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_112 = Coupling(name = 'GC_112',
                  value = '-((cquqd1*complex(0,1)*I1d21*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_113 = Coupling(name = 'GC_113',
                  value = '-((cquqd8*complex(0,1)*I1d21*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((cquqd1*complex(0,1)*I1d22*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((cquqd8*complex(0,1)*I1d22*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((cquqd1*complex(0,1)*I1d23*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_117 = Coupling(name = 'GC_117',
                  value = '-((cquqd8*complex(0,1)*I1d23*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((cquqd1*complex(0,1)*I1d31*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((cquqd8*complex(0,1)*I1d31*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_120 = Coupling(name = 'GC_120',
                  value = '-((cquqd1*complex(0,1)*I1d32*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((cquqd8*complex(0,1)*I1d32*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_122 = Coupling(name = 'GC_122',
                  value = '-((cquqd1*complex(0,1)*I1d33*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_123 = Coupling(name = 'GC_123',
                  value = '-((cquqd8*complex(0,1)*I1d33*I6d12)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((cquqd1*complex(0,1)*I1d11*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_125 = Coupling(name = 'GC_125',
                  value = '-((cquqd8*complex(0,1)*I1d11*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_126 = Coupling(name = 'GC_126',
                  value = '-((cquqd1*complex(0,1)*I1d12*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_127 = Coupling(name = 'GC_127',
                  value = '-((cquqd8*complex(0,1)*I1d12*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_128 = Coupling(name = 'GC_128',
                  value = '-((cquqd1*complex(0,1)*I1d13*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_129 = Coupling(name = 'GC_129',
                  value = '-((cquqd8*complex(0,1)*I1d13*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_130 = Coupling(name = 'GC_130',
                  value = '-((cquqd1*complex(0,1)*I1d21*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_131 = Coupling(name = 'GC_131',
                  value = '-((cquqd8*complex(0,1)*I1d21*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_132 = Coupling(name = 'GC_132',
                  value = '-((cquqd1*complex(0,1)*I1d22*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_133 = Coupling(name = 'GC_133',
                  value = '-((cquqd8*complex(0,1)*I1d22*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_134 = Coupling(name = 'GC_134',
                  value = '-((cquqd1*complex(0,1)*I1d23*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_135 = Coupling(name = 'GC_135',
                  value = '-((cquqd8*complex(0,1)*I1d23*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_136 = Coupling(name = 'GC_136',
                  value = '-((cquqd1*complex(0,1)*I1d31*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_137 = Coupling(name = 'GC_137',
                  value = '-((cquqd8*complex(0,1)*I1d31*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_138 = Coupling(name = 'GC_138',
                  value = '-((cquqd1*complex(0,1)*I1d32*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_139 = Coupling(name = 'GC_139',
                  value = '-((cquqd8*complex(0,1)*I1d32*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((cquqd1*complex(0,1)*I1d33*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((cquqd8*complex(0,1)*I1d33*I6d13)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_142 = Coupling(name = 'GC_142',
                  value = '-((cquqd1*complex(0,1)*I1d11*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((cquqd8*complex(0,1)*I1d11*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_144 = Coupling(name = 'GC_144',
                  value = '-((cquqd1*complex(0,1)*I1d12*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_145 = Coupling(name = 'GC_145',
                  value = '-((cquqd8*complex(0,1)*I1d12*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((cquqd1*complex(0,1)*I1d13*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((cquqd8*complex(0,1)*I1d13*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_148 = Coupling(name = 'GC_148',
                  value = '-((cquqd1*complex(0,1)*I1d21*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((cquqd8*complex(0,1)*I1d21*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_150 = Coupling(name = 'GC_150',
                  value = '-((cquqd1*complex(0,1)*I1d22*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((cquqd8*complex(0,1)*I1d22*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((cquqd1*complex(0,1)*I1d23*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((cquqd8*complex(0,1)*I1d23*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((cquqd1*complex(0,1)*I1d31*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_155 = Coupling(name = 'GC_155',
                  value = '-((cquqd8*complex(0,1)*I1d31*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_156 = Coupling(name = 'GC_156',
                  value = '-((cquqd1*complex(0,1)*I1d32*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((cquqd8*complex(0,1)*I1d32*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_158 = Coupling(name = 'GC_158',
                  value = '-((cquqd1*complex(0,1)*I1d33*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_159 = Coupling(name = 'GC_159',
                  value = '-((cquqd8*complex(0,1)*I1d33*I6d21)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_160 = Coupling(name = 'GC_160',
                  value = '-((cquqd1*complex(0,1)*I1d11*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((cquqd8*complex(0,1)*I1d11*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_162 = Coupling(name = 'GC_162',
                  value = '-((cquqd1*complex(0,1)*I1d12*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((cquqd8*complex(0,1)*I1d12*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_164 = Coupling(name = 'GC_164',
                  value = '-((cquqd1*complex(0,1)*I1d13*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((cquqd8*complex(0,1)*I1d13*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_166 = Coupling(name = 'GC_166',
                  value = '-((cquqd1*complex(0,1)*I1d21*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((cquqd8*complex(0,1)*I1d21*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_168 = Coupling(name = 'GC_168',
                  value = '-((cquqd1*complex(0,1)*I1d22*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((cquqd8*complex(0,1)*I1d22*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_170 = Coupling(name = 'GC_170',
                  value = '-((cquqd1*complex(0,1)*I1d23*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_171 = Coupling(name = 'GC_171',
                  value = '-((cquqd8*complex(0,1)*I1d23*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_172 = Coupling(name = 'GC_172',
                  value = '-((cquqd1*complex(0,1)*I1d31*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_173 = Coupling(name = 'GC_173',
                  value = '-((cquqd8*complex(0,1)*I1d31*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_174 = Coupling(name = 'GC_174',
                  value = '-((cquqd1*complex(0,1)*I1d32*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((cquqd8*complex(0,1)*I1d32*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((cquqd1*complex(0,1)*I1d33*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_177 = Coupling(name = 'GC_177',
                  value = '-((cquqd8*complex(0,1)*I1d33*I6d22)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_178 = Coupling(name = 'GC_178',
                  value = '-((cquqd1*complex(0,1)*I1d11*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_179 = Coupling(name = 'GC_179',
                  value = '-((cquqd8*complex(0,1)*I1d11*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_180 = Coupling(name = 'GC_180',
                  value = '-((cquqd1*complex(0,1)*I1d12*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_181 = Coupling(name = 'GC_181',
                  value = '-((cquqd8*complex(0,1)*I1d12*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_182 = Coupling(name = 'GC_182',
                  value = '-((cquqd1*complex(0,1)*I1d13*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_183 = Coupling(name = 'GC_183',
                  value = '-((cquqd8*complex(0,1)*I1d13*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((cquqd1*complex(0,1)*I1d21*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((cquqd8*complex(0,1)*I1d21*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_186 = Coupling(name = 'GC_186',
                  value = '-((cquqd1*complex(0,1)*I1d22*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_187 = Coupling(name = 'GC_187',
                  value = '-((cquqd8*complex(0,1)*I1d22*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_188 = Coupling(name = 'GC_188',
                  value = '-((cquqd1*complex(0,1)*I1d23*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_189 = Coupling(name = 'GC_189',
                  value = '-((cquqd8*complex(0,1)*I1d23*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_190 = Coupling(name = 'GC_190',
                  value = '-((cquqd1*complex(0,1)*I1d31*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((cquqd8*complex(0,1)*I1d31*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((cquqd1*complex(0,1)*I1d32*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((cquqd8*complex(0,1)*I1d32*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((cquqd1*complex(0,1)*I1d33*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_195 = Coupling(name = 'GC_195',
                  value = '-((cquqd8*complex(0,1)*I1d33*I6d23)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_196 = Coupling(name = 'GC_196',
                  value = '-((cquqd1*complex(0,1)*I1d11*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((cquqd8*complex(0,1)*I1d11*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_198 = Coupling(name = 'GC_198',
                  value = '-((cquqd1*complex(0,1)*I1d12*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_199 = Coupling(name = 'GC_199',
                  value = '-((cquqd8*complex(0,1)*I1d12*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_200 = Coupling(name = 'GC_200',
                  value = '-((cquqd1*complex(0,1)*I1d13*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_201 = Coupling(name = 'GC_201',
                  value = '-((cquqd8*complex(0,1)*I1d13*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_202 = Coupling(name = 'GC_202',
                  value = '-((cquqd1*complex(0,1)*I1d21*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_203 = Coupling(name = 'GC_203',
                  value = '-((cquqd8*complex(0,1)*I1d21*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_204 = Coupling(name = 'GC_204',
                  value = '-((cquqd1*complex(0,1)*I1d22*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_205 = Coupling(name = 'GC_205',
                  value = '-((cquqd8*complex(0,1)*I1d22*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_206 = Coupling(name = 'GC_206',
                  value = '-((cquqd1*complex(0,1)*I1d23*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_207 = Coupling(name = 'GC_207',
                  value = '-((cquqd8*complex(0,1)*I1d23*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_208 = Coupling(name = 'GC_208',
                  value = '-((cquqd1*complex(0,1)*I1d31*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_209 = Coupling(name = 'GC_209',
                  value = '-((cquqd8*complex(0,1)*I1d31*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_210 = Coupling(name = 'GC_210',
                  value = '-((cquqd1*complex(0,1)*I1d32*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_211 = Coupling(name = 'GC_211',
                  value = '-((cquqd8*complex(0,1)*I1d32*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_212 = Coupling(name = 'GC_212',
                  value = '-((cquqd1*complex(0,1)*I1d33*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_213 = Coupling(name = 'GC_213',
                  value = '-((cquqd8*complex(0,1)*I1d33*I6d31)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_214 = Coupling(name = 'GC_214',
                  value = '-((cquqd1*complex(0,1)*I1d11*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_215 = Coupling(name = 'GC_215',
                  value = '-((cquqd8*complex(0,1)*I1d11*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_216 = Coupling(name = 'GC_216',
                  value = '-((cquqd1*complex(0,1)*I1d12*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_217 = Coupling(name = 'GC_217',
                  value = '-((cquqd8*complex(0,1)*I1d12*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_218 = Coupling(name = 'GC_218',
                  value = '-((cquqd1*complex(0,1)*I1d13*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_219 = Coupling(name = 'GC_219',
                  value = '-((cquqd8*complex(0,1)*I1d13*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_220 = Coupling(name = 'GC_220',
                  value = '-((cquqd1*complex(0,1)*I1d21*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_221 = Coupling(name = 'GC_221',
                  value = '-((cquqd8*complex(0,1)*I1d21*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_222 = Coupling(name = 'GC_222',
                  value = '-((cquqd1*complex(0,1)*I1d22*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_223 = Coupling(name = 'GC_223',
                  value = '-((cquqd8*complex(0,1)*I1d22*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_224 = Coupling(name = 'GC_224',
                  value = '-((cquqd1*complex(0,1)*I1d23*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_225 = Coupling(name = 'GC_225',
                  value = '-((cquqd8*complex(0,1)*I1d23*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_226 = Coupling(name = 'GC_226',
                  value = '-((cquqd1*complex(0,1)*I1d31*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_227 = Coupling(name = 'GC_227',
                  value = '-((cquqd8*complex(0,1)*I1d31*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((cquqd1*complex(0,1)*I1d32*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((cquqd8*complex(0,1)*I1d32*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((cquqd1*complex(0,1)*I1d33*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_231 = Coupling(name = 'GC_231',
                  value = '-((cquqd8*complex(0,1)*I1d33*I6d32)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_232 = Coupling(name = 'GC_232',
                  value = '-((cquqd1*complex(0,1)*I1d11*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_233 = Coupling(name = 'GC_233',
                  value = '-((cquqd8*complex(0,1)*I1d11*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_234 = Coupling(name = 'GC_234',
                  value = '-((cquqd1*complex(0,1)*I1d12*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_235 = Coupling(name = 'GC_235',
                  value = '-((cquqd8*complex(0,1)*I1d12*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_236 = Coupling(name = 'GC_236',
                  value = '-((cquqd1*complex(0,1)*I1d13*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_237 = Coupling(name = 'GC_237',
                  value = '-((cquqd8*complex(0,1)*I1d13*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_238 = Coupling(name = 'GC_238',
                  value = '-((cquqd1*complex(0,1)*I1d21*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_239 = Coupling(name = 'GC_239',
                  value = '-((cquqd8*complex(0,1)*I1d21*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_240 = Coupling(name = 'GC_240',
                  value = '-((cquqd1*complex(0,1)*I1d22*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_241 = Coupling(name = 'GC_241',
                  value = '-((cquqd8*complex(0,1)*I1d22*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_242 = Coupling(name = 'GC_242',
                  value = '-((cquqd1*complex(0,1)*I1d23*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_243 = Coupling(name = 'GC_243',
                  value = '-((cquqd8*complex(0,1)*I1d23*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_244 = Coupling(name = 'GC_244',
                  value = '-((cquqd1*complex(0,1)*I1d31*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_245 = Coupling(name = 'GC_245',
                  value = '-((cquqd8*complex(0,1)*I1d31*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_246 = Coupling(name = 'GC_246',
                  value = '-((cquqd1*complex(0,1)*I1d32*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_247 = Coupling(name = 'GC_247',
                  value = '-((cquqd8*complex(0,1)*I1d32*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_248 = Coupling(name = 'GC_248',
                  value = '-((cquqd1*complex(0,1)*I1d33*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_249 = Coupling(name = 'GC_249',
                  value = '-((cquqd8*complex(0,1)*I1d33*I6d33)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_250 = Coupling(name = 'GC_250',
                  value = '(6*dMH2*complex(0,1)*lam)/MH**2',
                  order = {'NP':1,'NPcH':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '-((dgw*ee**2*complex(0,1))/cth**2) + (dgw*ee**2*complex(0,1))/(cth**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '2*cth**2*dgw*ee**2*complex(0,1) + (2*cth**2*dgw*ee**2*complex(0,1))/sth**2',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_253 = Coupling(name = 'GC_253',
                  value = '(-24*cth**2*cW*ee**3*complex(0,1))/(LambdaSMEFT**2*sth**3)',
                  order = {'NP':1,'NPcW':1,'QED':5})

GC_254 = Coupling(name = 'GC_254',
                  value = '(ee**2*complex(0,1))/(2.*sth**2)',
                  order = {'QED':2})

GC_255 = Coupling(name = 'GC_255',
                  value = '-((ee**2*complex(0,1))/sth**2)',
                  order = {'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(ee**2*complex(0,1))/(2.*cth**2*sth**2)',
                  order = {'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '(cth**2*ee**2*complex(0,1))/sth**2',
                  order = {'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '(dgw*ee**2*complex(0,1))/sth**2',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(-2*dgw*ee**2*complex(0,1))/sth**2',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '(4*cHW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_261 = Coupling(name = 'GC_261',
                  value = '(3*cHDD*ee**2*complex(0,1))/(cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':4})

GC_262 = Coupling(name = 'GC_262',
                  value = '(-4*cHW*cth**2*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_263 = Coupling(name = 'GC_263',
                  value = '(-6*cth*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_264 = Coupling(name = 'GC_264',
                  value = '(-6*cth**3*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_265 = Coupling(name = 'GC_265',
                  value = '(-4*cth*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcWtil':1,'QED':4})

GC_266 = Coupling(name = 'GC_266',
                  value = '(-4*cth**3*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcWtil':1,'QED':4})

GC_267 = Coupling(name = 'GC_267',
                  value = '(-24*cth*cW*ee**3*complex(0,1))/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcW':1,'QED':5})

GC_268 = Coupling(name = 'GC_268',
                  value = '-((ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '-((CKM1x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-((CKM1x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '-((CKM1x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '-((CKM2x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '-((CKM2x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '-((CKM2x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '-((CKM3x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '-((CKM3x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '-((CKM3x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '-(ee*complex(0,1))/(2.*cth*sth)',
                  order = {'QED':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '(ee*complex(0,1))/(2.*cth*sth)',
                  order = {'QED':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '-((cth*ee*complex(0,1))/sth)',
                  order = {'QED':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '-((dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '-((CKM1x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '-((CKM1x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '-((CKM1x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_285 = Coupling(name = 'GC_285',
                  value = '-((CKM2x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '-((CKM2x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_287 = Coupling(name = 'GC_287',
                  value = '-((CKM2x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_288 = Coupling(name = 'GC_288',
                  value = '-((CKM3x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '-((CKM3x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_290 = Coupling(name = 'GC_290',
                  value = '-((CKM3x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_291 = Coupling(name = 'GC_291',
                  value = '-(dgw*ee*complex(0,1))/(2.*cth*sth)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '(dgw*ee*complex(0,1))/(2.*cth*sth)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_293 = Coupling(name = 'GC_293',
                  value = '-(cth*dgw*ee*complex(0,1))/(2.*sth)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_294 = Coupling(name = 'GC_294',
                  value = '(-2*cth*ee**2*complex(0,1))/sth',
                  order = {'QED':2})

GC_295 = Coupling(name = 'GC_295',
                  value = '-((cHl3*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_296 = Coupling(name = 'GC_296',
                  value = '-((cHq3*CKM1x1*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_297 = Coupling(name = 'GC_297',
                  value = '-((cHq3*CKM1x2*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_298 = Coupling(name = 'GC_298',
                  value = '-((cHq3*CKM1x3*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_299 = Coupling(name = 'GC_299',
                  value = '-((cHq3*CKM2x1*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_300 = Coupling(name = 'GC_300',
                  value = '-((cHq3*CKM2x2*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_301 = Coupling(name = 'GC_301',
                  value = '-((cHq3*CKM2x3*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_302 = Coupling(name = 'GC_302',
                  value = '-((cHq3*CKM3x1*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_303 = Coupling(name = 'GC_303',
                  value = '-((cHq3*CKM3x2*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_304 = Coupling(name = 'GC_304',
                  value = '-((cHq3*CKM3x3*ee*complex(0,1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_305 = Coupling(name = 'GC_305',
                  value = '(cHd*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHd':1,'QED':3})

GC_306 = Coupling(name = 'GC_306',
                  value = '(cHe*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':3})

GC_307 = Coupling(name = 'GC_307',
                  value = '(cHl1*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':3})

GC_308 = Coupling(name = 'GC_308',
                  value = '-((cHl3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_309 = Coupling(name = 'GC_309',
                  value = '(cHl3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':3})

GC_310 = Coupling(name = 'GC_310',
                  value = '(cHq1*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHq1':1,'QED':3})

GC_311 = Coupling(name = 'GC_311',
                  value = '-((cHq3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_312 = Coupling(name = 'GC_312',
                  value = '(cHq3*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHq3':1,'QED':3})

GC_313 = Coupling(name = 'GC_313',
                  value = '(cHu*ee*complex(0,1))/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHu':1,'QED':3})

GC_314 = Coupling(name = 'GC_314',
                  value = '(4*cHW*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_315 = Coupling(name = 'GC_315',
                  value = '(-2*cHWB*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':3})

GC_316 = Coupling(name = 'GC_316',
                  value = '(2*cHWBtil*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWBtil':1,'QED':3})

GC_317 = Coupling(name = 'GC_317',
                  value = '(-4*cHWtil*cth*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWtil':1,'QED':3})

GC_318 = Coupling(name = 'GC_318',
                  value = '(6*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_319 = Coupling(name = 'GC_319',
                  value = '(-6*cth**2*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_320 = Coupling(name = 'GC_320',
                  value = '(-2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcWtil':1,'QED':3})

GC_321 = Coupling(name = 'GC_321',
                  value = '(2*cth**2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcWtil':1,'QED':3})

GC_322 = Coupling(name = 'GC_322',
                  value = '(8*cHW*cth*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':4})

GC_323 = Coupling(name = 'GC_323',
                  value = '(-6*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_324 = Coupling(name = 'GC_324',
                  value = '(-6*cth**2*cW*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_325 = Coupling(name = 'GC_325',
                  value = '(4*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcWtil':1,'QED':4})

GC_326 = Coupling(name = 'GC_326',
                  value = '(-4*cth**2*cWtil*ee**2*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcWtil':1,'QED':4})

GC_327 = Coupling(name = 'GC_327',
                  value = '(-24*cW*ee**3*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcW':1,'QED':5})

GC_328 = Coupling(name = 'GC_328',
                  value = '-(ee*complex(0,1)*sth)/(3.*cth)',
                  order = {'QED':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '(2*ee*complex(0,1)*sth)/(3.*cth)',
                  order = {'QED':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '-((ee*complex(0,1)*sth)/cth)',
                  order = {'QED':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '-(dg1*ee*complex(0,1)*sth)/(6.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '-(dg1*ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '(5*dg1*ee*complex(0,1)*sth)/(6.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '(-3*dg1*ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_335 = Coupling(name = 'GC_335',
                  value = 'cth*dg1*ee*complex(0,1)*sth',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '-(dgw*ee*complex(0,1)*sth)/(6.*cth)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '(dgw*ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '(-4*cHB*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '(-4*cHBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'QED':2})

GC_340 = Coupling(name = 'GC_340',
                  value = '(4*cHW*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_341 = Coupling(name = 'GC_341',
                  value = '(-4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_342 = Coupling(name = 'GC_342',
                  value = '(-2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'QED':2})

GC_343 = Coupling(name = 'GC_343',
                  value = '(2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'QED':2})

GC_344 = Coupling(name = 'GC_344',
                  value = '(4*cHWtil*cth*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'QED':2})

GC_345 = Coupling(name = 'GC_345',
                  value = '(6*cW*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':2})

GC_346 = Coupling(name = 'GC_346',
                  value = '(2*cWtil*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcWtil':1,'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '(-6*cW*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':3})

GC_348 = Coupling(name = 'GC_348',
                  value = '(2*cWtil*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcWtil':1,'QED':3})

GC_349 = Coupling(name = 'GC_349',
                  value = '(-12*cW*ee**2*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcW':1,'QED':4})

GC_350 = Coupling(name = 'GC_350',
                  value = '(-4*cWtil*ee**2*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcWtil':1,'QED':4})

GC_351 = Coupling(name = 'GC_351',
                  value = '(dgw*ee*complex(0,1)*sth**2)/3.',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(-2*dgw*ee*complex(0,1)*sth**2)/3.',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '-(dgw*ee*complex(0,1)*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_354 = Coupling(name = 'GC_354',
                  value = 'dgw*ee*complex(0,1)*sth**2',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '2*dgw*ee**2*complex(0,1)*sth**2',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_356 = Coupling(name = 'GC_356',
                  value = '(-2*cHBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'QED':2})

GC_357 = Coupling(name = 'GC_357',
                  value = '(4*cHW*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_358 = Coupling(name = 'GC_358',
                  value = '(-2*cHWtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'QED':2})

GC_359 = Coupling(name = 'GC_359',
                  value = '(dg1*ee*complex(0,1)*sth**3)/(3.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(-2*dg1*ee*complex(0,1)*sth**3)/(3.*cth)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '(dg1*ee*complex(0,1)*sth**3)/cth',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '-(dgw*ee*complex(0,1)*sth**3)/(3.*cth)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '(2*dgw*ee*complex(0,1)*sth**3)/(3.*cth)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '-((dgw*ee*complex(0,1)*sth**3)/cth)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '-((cth*dgw*ee*complex(0,1))/sth) - cth*dgw*ee*complex(0,1)*sth',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '(-2*cth*dg1*ee**2*complex(0,1))/sth + 4*cth*dg1*ee**2*complex(0,1)*sth',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_367 = Coupling(name = 'GC_367',
                  value = '(-2*cth*dgw*ee**2*complex(0,1))/sth - 4*cth*dgw*ee**2*complex(0,1)*sth',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_368 = Coupling(name = 'GC_368',
                  value = '-(dg1*ee*complex(0,1)) + dg1*ee*complex(0,1)*sth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '2*dg1*ee**2*complex(0,1) - 2*dg1*ee**2*complex(0,1)*sth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':2})

GC_370 = Coupling(name = 'GC_370',
                  value = '(4*cHB*complex(0,1))/LambdaSMEFT**2 - (4*cHB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':2})

GC_371 = Coupling(name = 'GC_371',
                  value = '(-2*cHWB*complex(0,1))/LambdaSMEFT**2 + (4*cHWB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_372 = Coupling(name = 'GC_372',
                  value = '(-2*cHWBtil*cth**2*complex(0,1))/LambdaSMEFT**2 + (2*cHWBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'QED':2})

GC_373 = Coupling(name = 'GC_373',
                  value = '(4*cHWB*complex(0,1)*sth)/(cth*LambdaSMEFT**2) - (4*cHWB*complex(0,1)*sth**3)/(cth*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_374 = Coupling(name = 'GC_374',
                  value = '(4*cHB*complex(0,1)*sth**2)/(cth**2*LambdaSMEFT**2) - (4*cHB*complex(0,1)*sth**4)/(cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHB':1,'QED':2})

GC_375 = Coupling(name = 'GC_375',
                  value = '(4*cHW*complex(0,1))/(cth**2*LambdaSMEFT**2) - (8*cHW*complex(0,1)*sth**2)/(cth**2*LambdaSMEFT**2) + (4*cHW*complex(0,1)*sth**4)/(cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_376 = Coupling(name = 'GC_376',
                  value = '(4*complex(0,1)*gHaa)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '(4*complex(0,1)*gHgg)/vevhat',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_378 = Coupling(name = 'GC_378',
                  value = '(2*complex(0,1)*gHza)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '(dg1*ee**2*complex(0,1)*vevhat)/cth**2',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_380 = Coupling(name = 'GC_380',
                  value = '-6*complex(0,1)*lam*vevhat',
                  order = {'QED':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '3*dGf*complex(0,1)*lam*vevhat*cmath.sqrt(2)',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '(90*cH*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcH':1,'QED':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '(-3*cHbox*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '-((cHDD*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_385 = Coupling(name = 'GC_385',
                  value = '(4*cHG*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QED':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '(-2*cHGtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'QED':1})

GC_387 = Coupling(name = 'GC_387',
                  value = '(4*cHW*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '(4*cHWtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'QED':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '(-2*cHBtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'QED':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '(-2*cHWtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'QED':1})

GC_391 = Coupling(name = 'GC_391',
                  value = '(4*cHW*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_392 = Coupling(name = 'GC_392',
                  value = '(2*cHWB*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_393 = Coupling(name = 'GC_393',
                  value = '(-2*cHWBtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'QED':2})

GC_394 = Coupling(name = 'GC_394',
                  value = '(-4*cHWtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'QED':2})

GC_395 = Coupling(name = 'GC_395',
                  value = '(-4*cHW*ee**2*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_396 = Coupling(name = 'GC_396',
                  value = '(-4*cHG*G*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':1,'QED':1})

GC_397 = Coupling(name = 'GC_397',
                  value = '(4*cHGtil*G*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'QCD':1,'QED':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '(-4*cHG*complex(0,1)*G**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHG':1,'QCD':2,'QED':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '(6*dMH2*complex(0,1)*lam*vevhat)/MH**2',
                  order = {'NP':1,'NPcH':1,'NPcHbox':1,'NPcHDD':1,'NPshifts':1,'QED':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '(ee**2*complex(0,1)*vevhat)/(2.*sth**2)',
                  order = {'QED':1})

GC_401 = Coupling(name = 'GC_401',
                  value = '(ee**2*complex(0,1)*vevhat)/(2.*cth**2*sth**2)',
                  order = {'QED':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '(dGf*ee**2*complex(0,1)*vevhat)/(2.*sth**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_403 = Coupling(name = 'GC_403',
                  value = '(dGf*ee**2*complex(0,1)*vevhat)/(2.*cth**2*sth**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_404 = Coupling(name = 'GC_404',
                  value = '(dgw*ee**2*complex(0,1)*vevhat)/sth**2',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_405 = Coupling(name = 'GC_405',
                  value = '(4*cHW*ee**2*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_406 = Coupling(name = 'GC_406',
                  value = '(3*cHDD*ee**2*complex(0,1)*vevhat)/(cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':3})

GC_407 = Coupling(name = 'GC_407',
                  value = '(-4*cHW*cth**2*ee**2*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_408 = Coupling(name = 'GC_408',
                  value = '-((cHl3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_409 = Coupling(name = 'GC_409',
                  value = '-((cHq3*CKM1x1*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_410 = Coupling(name = 'GC_410',
                  value = '-((cHq3*CKM1x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_411 = Coupling(name = 'GC_411',
                  value = '-((cHq3*CKM1x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_412 = Coupling(name = 'GC_412',
                  value = '-((cHq3*CKM2x1*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_413 = Coupling(name = 'GC_413',
                  value = '-((cHq3*CKM2x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_414 = Coupling(name = 'GC_414',
                  value = '-((cHq3*CKM2x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_415 = Coupling(name = 'GC_415',
                  value = '-((cHq3*CKM3x1*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_416 = Coupling(name = 'GC_416',
                  value = '-((cHq3*CKM3x2*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_417 = Coupling(name = 'GC_417',
                  value = '-((cHq3*CKM3x3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_418 = Coupling(name = 'GC_418',
                  value = '(cHd*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHd':1,'QED':2})

GC_419 = Coupling(name = 'GC_419',
                  value = '(cHe*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':2})

GC_420 = Coupling(name = 'GC_420',
                  value = '(cHl1*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':2})

GC_421 = Coupling(name = 'GC_421',
                  value = '-((cHl3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_422 = Coupling(name = 'GC_422',
                  value = '(cHl3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':2})

GC_423 = Coupling(name = 'GC_423',
                  value = '(cHq1*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHq1':1,'QED':2})

GC_424 = Coupling(name = 'GC_424',
                  value = '-((cHq3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_425 = Coupling(name = 'GC_425',
                  value = '(cHq3*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHq3':1,'QED':2})

GC_426 = Coupling(name = 'GC_426',
                  value = '(cHu*ee*complex(0,1)*vevhat)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHu':1,'QED':2})

GC_427 = Coupling(name = 'GC_427',
                  value = '(4*cHW*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '(-2*cHWB*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_429 = Coupling(name = 'GC_429',
                  value = '(2*cHWBtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWBtil':1,'QED':2})

GC_430 = Coupling(name = 'GC_430',
                  value = '(-4*cHWtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWtil':1,'QED':2})

GC_431 = Coupling(name = 'GC_431',
                  value = '(8*cHW*cth*ee**2*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHW':1,'QED':3})

GC_432 = Coupling(name = 'GC_432',
                  value = '(-4*cHB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':1})

GC_433 = Coupling(name = 'GC_433',
                  value = '(-4*cHBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'QED':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '(4*cHW*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '(-4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '(-2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'QED':1})

GC_437 = Coupling(name = 'GC_437',
                  value = '(2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'QED':1})

GC_438 = Coupling(name = 'GC_438',
                  value = '(4*cHWtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'QED':1})

GC_439 = Coupling(name = 'GC_439',
                  value = '(-2*cHBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHBtil':1,'QED':1})

GC_440 = Coupling(name = 'GC_440',
                  value = '(4*cHW*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_441 = Coupling(name = 'GC_441',
                  value = '(-2*cHWtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'QED':1})

GC_442 = Coupling(name = 'GC_442',
                  value = '(45*cH*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcH':1})

GC_443 = Coupling(name = 'GC_443',
                  value = '-(cHWB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '(cHWB*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '-((cHWBtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWBtil':1,'QED':1})

GC_446 = Coupling(name = 'GC_446',
                  value = '(-2*cHWtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWtil':1,'QED':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '(cHWB*ee*complex(0,1)*vevhat**2)/(6.*cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '-(cHWB*ee*complex(0,1)*vevhat**2)/(2.*cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '(2*cHGtil*G*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHGtil':1,'QCD':1})

GC_450 = Coupling(name = 'GC_450',
                  value = '(-24*cHbox*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHbox':1,'QED':2})

GC_451 = Coupling(name = 'GC_451',
                  value = '(6*cHDD*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_452 = Coupling(name = 'GC_452',
                  value = '(cHbox*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '-(cHDD*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '(cHbox*ee**2*complex(0,1)*vevhat**2)/(cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'QED':2})

GC_455 = Coupling(name = 'GC_455',
                  value = '(5*cHDD*ee**2*complex(0,1)*vevhat**2)/(4.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':2})

GC_456 = Coupling(name = 'GC_456',
                  value = '-((cHl3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_457 = Coupling(name = 'GC_457',
                  value = '-((cHq3*CKM1x1*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_458 = Coupling(name = 'GC_458',
                  value = '-((cHq3*CKM1x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_459 = Coupling(name = 'GC_459',
                  value = '-((cHq3*CKM1x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_460 = Coupling(name = 'GC_460',
                  value = '-((cHq3*CKM2x1*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_461 = Coupling(name = 'GC_461',
                  value = '-((cHq3*CKM2x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_462 = Coupling(name = 'GC_462',
                  value = '-((cHq3*CKM2x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_463 = Coupling(name = 'GC_463',
                  value = '-((cHq3*CKM3x1*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_464 = Coupling(name = 'GC_464',
                  value = '-((cHq3*CKM3x2*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_465 = Coupling(name = 'GC_465',
                  value = '-((cHq3*CKM3x3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_466 = Coupling(name = 'GC_466',
                  value = '(cHd*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHd':1,'QED':1})

GC_467 = Coupling(name = 'GC_467',
                  value = '(cHe*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHe':1,'QED':1})

GC_468 = Coupling(name = 'GC_468',
                  value = '(cHl1*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl1':1,'QED':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '-(cHl3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_470 = Coupling(name = 'GC_470',
                  value = '(cHl3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHl3':1,'QED':1})

GC_471 = Coupling(name = 'GC_471',
                  value = '(cHq1*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHq1':1,'QED':1})

GC_472 = Coupling(name = 'GC_472',
                  value = '-(cHq3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_473 = Coupling(name = 'GC_473',
                  value = '(cHq3*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHq3':1,'QED':1})

GC_474 = Coupling(name = 'GC_474',
                  value = '(cHu*ee*complex(0,1)*vevhat**2)/(2.*cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHu':1,'QED':1})

GC_475 = Coupling(name = 'GC_475',
                  value = '-((cHWB*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_476 = Coupling(name = 'GC_476',
                  value = '(cHWBtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWBtil':1,'QED':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '(-2*cHWtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWtil':1,'QED':1})

GC_478 = Coupling(name = 'GC_478',
                  value = '(cHWB*ee**2*complex(0,1)*vevhat**2)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_479 = Coupling(name = 'GC_479',
                  value = '-(cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_480 = Coupling(name = 'GC_480',
                  value = '(2*cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(3.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_481 = Coupling(name = 'GC_481',
                  value = '-((cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_482 = Coupling(name = 'GC_482',
                  value = '(cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_483 = Coupling(name = 'GC_483',
                  value = '(-2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_484 = Coupling(name = 'GC_484',
                  value = '(2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_485 = Coupling(name = 'GC_485',
                  value = '-((cHWB*ee*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '(cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(6.*cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '(-5*cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(6.*cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '(3*cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '-(cHWB*ee*complex(0,1)*sth**4*vevhat**2)/(3.*cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '(2*cHWB*ee*complex(0,1)*sth**4*vevhat**2)/(3.*cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '-((cHWB*ee*complex(0,1)*sth**4*vevhat**2)/(cth**2*LambdaSMEFT**2))',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '(15*cH*complex(0,1)*vevhat**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcH':1,'QED':-1})

GC_493 = Coupling(name = 'GC_493',
                  value = '(-18*cHbox*complex(0,1)*lam*vevhat**3)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '(9*cHDD*complex(0,1)*lam*vevhat**3)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '(cHbox*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '-(cHDD*ee**2*complex(0,1)*vevhat**3)/(8.*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '(cHbox*ee**2*complex(0,1)*vevhat**3)/(2.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '(3*cHDD*ee**2*complex(0,1)*vevhat**3)/(8.*cth**2*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_499 = Coupling(name = 'GC_499',
                  value = '(cHWB*ee**2*complex(0,1)*vevhat**3)/(cth*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_500 = Coupling(name = 'GC_500',
                  value = '-((dgw*ee**2*complex(0,1)*vevhat)/cth**2) + (dgw*ee**2*complex(0,1)*vevhat)/(cth**2*sth**2)',
                  order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_501 = Coupling(name = 'GC_501',
                  value = '(4*cHB*complex(0,1)*vevhat)/LambdaSMEFT**2 - (4*cHB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHB':1,'QED':1})

GC_502 = Coupling(name = 'GC_502',
                  value = '(-2*cHWB*complex(0,1)*vevhat)/LambdaSMEFT**2 + (4*cHWB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_503 = Coupling(name = 'GC_503',
                  value = '(-2*cHWBtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 + (2*cHWBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWBtil':1,'QED':1})

GC_504 = Coupling(name = 'GC_504',
                  value = '(4*cHWB*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (4*cHWB*complex(0,1)*sth**3*vevhat)/(cth*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHWB':1,'QED':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '(4*cHB*complex(0,1)*sth**2*vevhat)/(cth**2*LambdaSMEFT**2) - (4*cHB*complex(0,1)*sth**4*vevhat)/(cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHB':1,'QED':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '(4*cHW*complex(0,1)*vevhat)/(cth**2*LambdaSMEFT**2) - (8*cHW*complex(0,1)*sth**2*vevhat)/(cth**2*LambdaSMEFT**2) + (4*cHW*complex(0,1)*sth**4*vevhat)/(cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'NPcHW':1,'QED':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '(2*cHWB*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (4*cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcHWB':1,'QED':2})

GC_508 = Coupling(name = 'GC_508',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '(dGf*complex(0,1)*yb)/2.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '(cdG*complex(0,1)*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':3})

GC_511 = Coupling(name = 'GC_511',
                  value = '(3*cdH*complex(0,1)*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':3})

GC_512 = Coupling(name = 'GC_512',
                  value = '(cdW*complex(0,1)*yb)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_513 = Coupling(name = 'GC_513',
                  value = '(cdB*cth*complex(0,1)*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_514 = Coupling(name = 'GC_514',
                  value = '-((cdW*cth*complex(0,1)*yb)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_515 = Coupling(name = 'GC_515',
                  value = '-((cdW*ee*complex(0,1)*yb)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_516 = Coupling(name = 'GC_516',
                  value = '(cdG*G*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_517 = Coupling(name = 'GC_517',
                  value = '(cdW*ee*complex(0,1)*yb)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_518 = Coupling(name = 'GC_518',
                  value = '(cdW*cth*ee*complex(0,1)*yb)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_519 = Coupling(name = 'GC_519',
                  value = '-((cdB*complex(0,1)*sth*yb)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_520 = Coupling(name = 'GC_520',
                  value = '-((cdW*complex(0,1)*sth*yb)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_521 = Coupling(name = 'GC_521',
                  value = '(cdG*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':2})

GC_522 = Coupling(name = 'GC_522',
                  value = '(3*cdH*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':2})

GC_523 = Coupling(name = 'GC_523',
                  value = '(cdW*complex(0,1)*vevhat*yb)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_524 = Coupling(name = 'GC_524',
                  value = '(cdB*cth*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_525 = Coupling(name = 'GC_525',
                  value = '-((cdW*cth*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_526 = Coupling(name = 'GC_526',
                  value = '-((cdW*ee*complex(0,1)*vevhat*yb)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_527 = Coupling(name = 'GC_527',
                  value = '(cdG*G*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_528 = Coupling(name = 'GC_528',
                  value = '(cdW*ee*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_529 = Coupling(name = 'GC_529',
                  value = '(cdW*cth*ee*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_530 = Coupling(name = 'GC_530',
                  value = '-((cdB*complex(0,1)*sth*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_531 = Coupling(name = 'GC_531',
                  value = '-((cdW*complex(0,1)*sth*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_532 = Coupling(name = 'GC_532',
                  value = '(cdH*complex(0,1)*vevhat**2*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':1})

GC_533 = Coupling(name = 'GC_533',
                  value = '-((cHbox*complex(0,1)*vevhat**2*yb)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '(cHDD*complex(0,1)*vevhat**2*yb)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '(dGf*complex(0,1)*yc)/2.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '(cth*cuB*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_538 = Coupling(name = 'GC_538',
                  value = '(cuG*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':3})

GC_539 = Coupling(name = 'GC_539',
                  value = '(3*cuH*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':3})

GC_540 = Coupling(name = 'GC_540',
                  value = '(cuW*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_541 = Coupling(name = 'GC_541',
                  value = '(cth*cuW*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_542 = Coupling(name = 'GC_542',
                  value = '(cuW*ee*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_543 = Coupling(name = 'GC_543',
                  value = '(cuG*G*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_544 = Coupling(name = 'GC_544',
                  value = '-((cuW*ee*complex(0,1)*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_545 = Coupling(name = 'GC_545',
                  value = '-((cth*cuW*ee*complex(0,1)*yc)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_546 = Coupling(name = 'GC_546',
                  value = '-((cuB*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_547 = Coupling(name = 'GC_547',
                  value = '(cuW*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_548 = Coupling(name = 'GC_548',
                  value = '(cth*cuB*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_549 = Coupling(name = 'GC_549',
                  value = '(cuG*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':2})

GC_550 = Coupling(name = 'GC_550',
                  value = '(3*cuH*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':2})

GC_551 = Coupling(name = 'GC_551',
                  value = '(cuW*complex(0,1)*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_552 = Coupling(name = 'GC_552',
                  value = '(cth*cuW*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_553 = Coupling(name = 'GC_553',
                  value = '(cuW*ee*complex(0,1)*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_554 = Coupling(name = 'GC_554',
                  value = '(cuG*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_555 = Coupling(name = 'GC_555',
                  value = '-((cuW*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_556 = Coupling(name = 'GC_556',
                  value = '-((cth*cuW*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_557 = Coupling(name = 'GC_557',
                  value = '-((cuB*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_558 = Coupling(name = 'GC_558',
                  value = '(cuW*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_559 = Coupling(name = 'GC_559',
                  value = '-((cHbox*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '(cHDD*complex(0,1)*vevhat**2*yc)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '(cuH*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '(cquqd1*complex(0,1)*yb*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_563 = Coupling(name = 'GC_563',
                  value = '(cquqd8*complex(0,1)*yb*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_564 = Coupling(name = 'GC_564',
                  value = '(cHud*CKM2x3*ee*complex(0,1)*yb*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_565 = Coupling(name = 'GC_565',
                  value = '(cHud*CKM2x3*ee*complex(0,1)*vevhat*yb*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_566 = Coupling(name = 'GC_566',
                  value = '(cHud*CKM2x3*ee*complex(0,1)*vevhat**2*yb*yc)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':3})

GC_567 = Coupling(name = 'GC_567',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '(dGf*complex(0,1)*ydo)/2.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_569 = Coupling(name = 'GC_569',
                  value = '(cdG*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':3})

GC_570 = Coupling(name = 'GC_570',
                  value = '(3*cdH*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':3})

GC_571 = Coupling(name = 'GC_571',
                  value = '(cdW*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_572 = Coupling(name = 'GC_572',
                  value = '(cdB*cth*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_573 = Coupling(name = 'GC_573',
                  value = '-((cdW*cth*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_574 = Coupling(name = 'GC_574',
                  value = '-((cdW*ee*complex(0,1)*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_575 = Coupling(name = 'GC_575',
                  value = '(cdG*G*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_576 = Coupling(name = 'GC_576',
                  value = '(cdW*ee*complex(0,1)*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_577 = Coupling(name = 'GC_577',
                  value = '(cdW*cth*ee*complex(0,1)*ydo)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_578 = Coupling(name = 'GC_578',
                  value = '-((cdB*complex(0,1)*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_579 = Coupling(name = 'GC_579',
                  value = '-((cdW*complex(0,1)*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_580 = Coupling(name = 'GC_580',
                  value = '(cdG*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':2})

GC_581 = Coupling(name = 'GC_581',
                  value = '(3*cdH*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':2})

GC_582 = Coupling(name = 'GC_582',
                  value = '(cdW*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_583 = Coupling(name = 'GC_583',
                  value = '(cdB*cth*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_584 = Coupling(name = 'GC_584',
                  value = '-((cdW*cth*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_585 = Coupling(name = 'GC_585',
                  value = '-((cdW*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_586 = Coupling(name = 'GC_586',
                  value = '(cdG*G*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_587 = Coupling(name = 'GC_587',
                  value = '(cdW*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_588 = Coupling(name = 'GC_588',
                  value = '(cdW*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_589 = Coupling(name = 'GC_589',
                  value = '-((cdB*complex(0,1)*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_590 = Coupling(name = 'GC_590',
                  value = '-((cdW*complex(0,1)*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_591 = Coupling(name = 'GC_591',
                  value = '(cdH*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':1})

GC_592 = Coupling(name = 'GC_592',
                  value = '-((cHbox*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_593 = Coupling(name = 'GC_593',
                  value = '(cHDD*complex(0,1)*vevhat**2*ydo)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_594 = Coupling(name = 'GC_594',
                  value = '(cquqd1*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_595 = Coupling(name = 'GC_595',
                  value = '(cquqd8*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_596 = Coupling(name = 'GC_596',
                  value = '(cHud*CKM2x1*ee*complex(0,1)*yc*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_597 = Coupling(name = 'GC_597',
                  value = '(cHud*CKM2x1*ee*complex(0,1)*vevhat*yc*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_598 = Coupling(name = 'GC_598',
                  value = '(cHud*CKM2x1*ee*complex(0,1)*vevhat**2*yc*ydo)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':3})

GC_599 = Coupling(name = 'GC_599',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_600 = Coupling(name = 'GC_600',
                  value = '(dGf*complex(0,1)*ye)/2.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_601 = Coupling(name = 'GC_601',
                  value = '(3*ceH*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':3})

GC_602 = Coupling(name = 'GC_602',
                  value = '(ceW*complex(0,1)*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_603 = Coupling(name = 'GC_603',
                  value = '(ceB*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_604 = Coupling(name = 'GC_604',
                  value = '-((ceW*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_605 = Coupling(name = 'GC_605',
                  value = '-((ceW*ee*complex(0,1)*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_606 = Coupling(name = 'GC_606',
                  value = '(cledq*complex(0,1)*I3d11*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_607 = Coupling(name = 'GC_607',
                  value = '(cledq*complex(0,1)*I3d12*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_608 = Coupling(name = 'GC_608',
                  value = '(cledq*complex(0,1)*I3d13*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_609 = Coupling(name = 'GC_609',
                  value = '(cledq*complex(0,1)*I3d21*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_610 = Coupling(name = 'GC_610',
                  value = '(cledq*complex(0,1)*I3d22*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_611 = Coupling(name = 'GC_611',
                  value = '(cledq*complex(0,1)*I3d23*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_612 = Coupling(name = 'GC_612',
                  value = '(cledq*complex(0,1)*I3d31*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_613 = Coupling(name = 'GC_613',
                  value = '(cledq*complex(0,1)*I3d32*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_614 = Coupling(name = 'GC_614',
                  value = '(cledq*complex(0,1)*I3d33*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_615 = Coupling(name = 'GC_615',
                  value = '(clequ1*complex(0,1)*I4d11*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_616 = Coupling(name = 'GC_616',
                  value = '(clequ3*complex(0,1)*I4d11*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_617 = Coupling(name = 'GC_617',
                  value = '-(clequ3*complex(0,1)*I4d11*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_618 = Coupling(name = 'GC_618',
                  value = '(clequ1*complex(0,1)*I4d12*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_619 = Coupling(name = 'GC_619',
                  value = '(clequ3*complex(0,1)*I4d12*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_620 = Coupling(name = 'GC_620',
                  value = '-(clequ3*complex(0,1)*I4d12*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_621 = Coupling(name = 'GC_621',
                  value = '(clequ1*complex(0,1)*I4d13*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_622 = Coupling(name = 'GC_622',
                  value = '(clequ3*complex(0,1)*I4d13*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_623 = Coupling(name = 'GC_623',
                  value = '-(clequ3*complex(0,1)*I4d13*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_624 = Coupling(name = 'GC_624',
                  value = '(clequ1*complex(0,1)*I4d21*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_625 = Coupling(name = 'GC_625',
                  value = '(clequ3*complex(0,1)*I4d21*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_626 = Coupling(name = 'GC_626',
                  value = '-(clequ3*complex(0,1)*I4d21*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_627 = Coupling(name = 'GC_627',
                  value = '(clequ1*complex(0,1)*I4d22*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_628 = Coupling(name = 'GC_628',
                  value = '(clequ3*complex(0,1)*I4d22*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_629 = Coupling(name = 'GC_629',
                  value = '-(clequ3*complex(0,1)*I4d22*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_630 = Coupling(name = 'GC_630',
                  value = '(clequ1*complex(0,1)*I4d23*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_631 = Coupling(name = 'GC_631',
                  value = '(clequ3*complex(0,1)*I4d23*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_632 = Coupling(name = 'GC_632',
                  value = '-(clequ3*complex(0,1)*I4d23*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_633 = Coupling(name = 'GC_633',
                  value = '(clequ1*complex(0,1)*I4d31*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_634 = Coupling(name = 'GC_634',
                  value = '(clequ3*complex(0,1)*I4d31*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_635 = Coupling(name = 'GC_635',
                  value = '-(clequ3*complex(0,1)*I4d31*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_636 = Coupling(name = 'GC_636',
                  value = '(clequ1*complex(0,1)*I4d32*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_637 = Coupling(name = 'GC_637',
                  value = '(clequ3*complex(0,1)*I4d32*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_638 = Coupling(name = 'GC_638',
                  value = '-(clequ3*complex(0,1)*I4d32*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_639 = Coupling(name = 'GC_639',
                  value = '(clequ1*complex(0,1)*I4d33*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_640 = Coupling(name = 'GC_640',
                  value = '(clequ3*complex(0,1)*I4d33*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_641 = Coupling(name = 'GC_641',
                  value = '-(clequ3*complex(0,1)*I4d33*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_642 = Coupling(name = 'GC_642',
                  value = '(ceW*ee*complex(0,1)*ye)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_643 = Coupling(name = 'GC_643',
                  value = '(ceW*cth*ee*complex(0,1)*ye)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_644 = Coupling(name = 'GC_644',
                  value = '-((ceB*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_645 = Coupling(name = 'GC_645',
                  value = '-((ceW*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_646 = Coupling(name = 'GC_646',
                  value = '(3*ceH*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':2})

GC_647 = Coupling(name = 'GC_647',
                  value = '(ceW*complex(0,1)*vevhat*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_648 = Coupling(name = 'GC_648',
                  value = '(ceB*cth*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_649 = Coupling(name = 'GC_649',
                  value = '-((ceW*cth*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_650 = Coupling(name = 'GC_650',
                  value = '-((ceW*ee*complex(0,1)*vevhat*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_651 = Coupling(name = 'GC_651',
                  value = '(ceW*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_652 = Coupling(name = 'GC_652',
                  value = '(ceW*cth*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_653 = Coupling(name = 'GC_653',
                  value = '-((ceB*complex(0,1)*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_654 = Coupling(name = 'GC_654',
                  value = '-((ceW*complex(0,1)*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_655 = Coupling(name = 'GC_655',
                  value = '(ceH*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':1})

GC_656 = Coupling(name = 'GC_656',
                  value = '-((cHbox*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_657 = Coupling(name = 'GC_657',
                  value = '(cHDD*complex(0,1)*vevhat**2*ye)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_658 = Coupling(name = 'GC_658',
                  value = '(cledq*complex(0,1)*yb*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_659 = Coupling(name = 'GC_659',
                  value = '-((clequ1*complex(0,1)*yc*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_660 = Coupling(name = 'GC_660',
                  value = '-(clequ3*complex(0,1)*yc*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_661 = Coupling(name = 'GC_661',
                  value = '(clequ3*complex(0,1)*yc*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_662 = Coupling(name = 'GC_662',
                  value = '(cledq*complex(0,1)*ydo*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_663 = Coupling(name = 'GC_663',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_664 = Coupling(name = 'GC_664',
                  value = '(dGf*complex(0,1)*ym)/2.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_665 = Coupling(name = 'GC_665',
                  value = '(3*ceH*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':3})

GC_666 = Coupling(name = 'GC_666',
                  value = '(ceW*complex(0,1)*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_667 = Coupling(name = 'GC_667',
                  value = '(ceB*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_668 = Coupling(name = 'GC_668',
                  value = '-((ceW*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_669 = Coupling(name = 'GC_669',
                  value = '-((ceW*ee*complex(0,1)*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_670 = Coupling(name = 'GC_670',
                  value = '(cledq*complex(0,1)*I3d11*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_671 = Coupling(name = 'GC_671',
                  value = '(cledq*complex(0,1)*I3d12*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_672 = Coupling(name = 'GC_672',
                  value = '(cledq*complex(0,1)*I3d13*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_673 = Coupling(name = 'GC_673',
                  value = '(cledq*complex(0,1)*I3d21*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_674 = Coupling(name = 'GC_674',
                  value = '(cledq*complex(0,1)*I3d22*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_675 = Coupling(name = 'GC_675',
                  value = '(cledq*complex(0,1)*I3d23*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_676 = Coupling(name = 'GC_676',
                  value = '(cledq*complex(0,1)*I3d31*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_677 = Coupling(name = 'GC_677',
                  value = '(cledq*complex(0,1)*I3d32*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_678 = Coupling(name = 'GC_678',
                  value = '(cledq*complex(0,1)*I3d33*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_679 = Coupling(name = 'GC_679',
                  value = '(clequ1*complex(0,1)*I4d11*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_680 = Coupling(name = 'GC_680',
                  value = '(clequ3*complex(0,1)*I4d11*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_681 = Coupling(name = 'GC_681',
                  value = '-(clequ3*complex(0,1)*I4d11*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_682 = Coupling(name = 'GC_682',
                  value = '(clequ1*complex(0,1)*I4d12*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_683 = Coupling(name = 'GC_683',
                  value = '(clequ3*complex(0,1)*I4d12*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_684 = Coupling(name = 'GC_684',
                  value = '-(clequ3*complex(0,1)*I4d12*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_685 = Coupling(name = 'GC_685',
                  value = '(clequ1*complex(0,1)*I4d13*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_686 = Coupling(name = 'GC_686',
                  value = '(clequ3*complex(0,1)*I4d13*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_687 = Coupling(name = 'GC_687',
                  value = '-(clequ3*complex(0,1)*I4d13*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_688 = Coupling(name = 'GC_688',
                  value = '(clequ1*complex(0,1)*I4d21*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_689 = Coupling(name = 'GC_689',
                  value = '(clequ3*complex(0,1)*I4d21*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_690 = Coupling(name = 'GC_690',
                  value = '-(clequ3*complex(0,1)*I4d21*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_691 = Coupling(name = 'GC_691',
                  value = '(clequ1*complex(0,1)*I4d22*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_692 = Coupling(name = 'GC_692',
                  value = '(clequ3*complex(0,1)*I4d22*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_693 = Coupling(name = 'GC_693',
                  value = '-(clequ3*complex(0,1)*I4d22*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_694 = Coupling(name = 'GC_694',
                  value = '(clequ1*complex(0,1)*I4d23*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_695 = Coupling(name = 'GC_695',
                  value = '(clequ3*complex(0,1)*I4d23*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_696 = Coupling(name = 'GC_696',
                  value = '-(clequ3*complex(0,1)*I4d23*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_697 = Coupling(name = 'GC_697',
                  value = '(clequ1*complex(0,1)*I4d31*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_698 = Coupling(name = 'GC_698',
                  value = '(clequ3*complex(0,1)*I4d31*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_699 = Coupling(name = 'GC_699',
                  value = '-(clequ3*complex(0,1)*I4d31*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_700 = Coupling(name = 'GC_700',
                  value = '(clequ1*complex(0,1)*I4d32*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_701 = Coupling(name = 'GC_701',
                  value = '(clequ3*complex(0,1)*I4d32*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_702 = Coupling(name = 'GC_702',
                  value = '-(clequ3*complex(0,1)*I4d32*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_703 = Coupling(name = 'GC_703',
                  value = '(clequ1*complex(0,1)*I4d33*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_704 = Coupling(name = 'GC_704',
                  value = '(clequ3*complex(0,1)*I4d33*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_705 = Coupling(name = 'GC_705',
                  value = '-(clequ3*complex(0,1)*I4d33*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_706 = Coupling(name = 'GC_706',
                  value = '(ceW*ee*complex(0,1)*ym)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_707 = Coupling(name = 'GC_707',
                  value = '(ceW*cth*ee*complex(0,1)*ym)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_708 = Coupling(name = 'GC_708',
                  value = '-((ceB*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_709 = Coupling(name = 'GC_709',
                  value = '-((ceW*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_710 = Coupling(name = 'GC_710',
                  value = '(3*ceH*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':2})

GC_711 = Coupling(name = 'GC_711',
                  value = '(ceW*complex(0,1)*vevhat*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_712 = Coupling(name = 'GC_712',
                  value = '(ceB*cth*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_713 = Coupling(name = 'GC_713',
                  value = '-((ceW*cth*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_714 = Coupling(name = 'GC_714',
                  value = '-((ceW*ee*complex(0,1)*vevhat*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_715 = Coupling(name = 'GC_715',
                  value = '(ceW*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_716 = Coupling(name = 'GC_716',
                  value = '(ceW*cth*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_717 = Coupling(name = 'GC_717',
                  value = '-((ceB*complex(0,1)*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_718 = Coupling(name = 'GC_718',
                  value = '-((ceW*complex(0,1)*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_719 = Coupling(name = 'GC_719',
                  value = '(ceH*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':1})

GC_720 = Coupling(name = 'GC_720',
                  value = '-((cHbox*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_721 = Coupling(name = 'GC_721',
                  value = '(cHDD*complex(0,1)*vevhat**2*ym)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_722 = Coupling(name = 'GC_722',
                  value = '(cledq*complex(0,1)*yb*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_723 = Coupling(name = 'GC_723',
                  value = '-((clequ1*complex(0,1)*yc*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_724 = Coupling(name = 'GC_724',
                  value = '-(clequ3*complex(0,1)*yc*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_725 = Coupling(name = 'GC_725',
                  value = '(clequ3*complex(0,1)*yc*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_726 = Coupling(name = 'GC_726',
                  value = '(cledq*complex(0,1)*ydo*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_727 = Coupling(name = 'GC_727',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_728 = Coupling(name = 'GC_728',
                  value = '(dGf*complex(0,1)*ys)/2.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_729 = Coupling(name = 'GC_729',
                  value = '(cdG*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':3})

GC_730 = Coupling(name = 'GC_730',
                  value = '(3*cdH*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':3})

GC_731 = Coupling(name = 'GC_731',
                  value = '(cdW*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_732 = Coupling(name = 'GC_732',
                  value = '(cdB*cth*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_733 = Coupling(name = 'GC_733',
                  value = '-((cdW*cth*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_734 = Coupling(name = 'GC_734',
                  value = '-((cdW*ee*complex(0,1)*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_735 = Coupling(name = 'GC_735',
                  value = '(cdG*G*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_736 = Coupling(name = 'GC_736',
                  value = '(cdW*ee*complex(0,1)*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_737 = Coupling(name = 'GC_737',
                  value = '(cdW*cth*ee*complex(0,1)*ys)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_738 = Coupling(name = 'GC_738',
                  value = '-((cdB*complex(0,1)*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_739 = Coupling(name = 'GC_739',
                  value = '-((cdW*complex(0,1)*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_740 = Coupling(name = 'GC_740',
                  value = '(cdG*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':2})

GC_741 = Coupling(name = 'GC_741',
                  value = '(3*cdH*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':2})

GC_742 = Coupling(name = 'GC_742',
                  value = '(cdW*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_743 = Coupling(name = 'GC_743',
                  value = '(cdB*cth*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_744 = Coupling(name = 'GC_744',
                  value = '-((cdW*cth*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_745 = Coupling(name = 'GC_745',
                  value = '-((cdW*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_746 = Coupling(name = 'GC_746',
                  value = '(cdG*G*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_747 = Coupling(name = 'GC_747',
                  value = '(cdW*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_748 = Coupling(name = 'GC_748',
                  value = '(cdW*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_749 = Coupling(name = 'GC_749',
                  value = '-((cdB*complex(0,1)*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_750 = Coupling(name = 'GC_750',
                  value = '-((cdW*complex(0,1)*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_751 = Coupling(name = 'GC_751',
                  value = '(cdH*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':1})

GC_752 = Coupling(name = 'GC_752',
                  value = '-((cHbox*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_753 = Coupling(name = 'GC_753',
                  value = '(cHDD*complex(0,1)*vevhat**2*ys)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_754 = Coupling(name = 'GC_754',
                  value = '(cquqd1*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_755 = Coupling(name = 'GC_755',
                  value = '(cquqd8*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_756 = Coupling(name = 'GC_756',
                  value = '(cHud*CKM2x2*ee*complex(0,1)*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_757 = Coupling(name = 'GC_757',
                  value = '(cHud*CKM2x2*ee*complex(0,1)*vevhat*yc*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_758 = Coupling(name = 'GC_758',
                  value = '(cHud*CKM2x2*ee*complex(0,1)*vevhat**2*yc*ys)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':3})

GC_759 = Coupling(name = 'GC_759',
                  value = '(cledq*complex(0,1)*ye*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_760 = Coupling(name = 'GC_760',
                  value = '(cledq*complex(0,1)*ym*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_761 = Coupling(name = 'GC_761',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_762 = Coupling(name = 'GC_762',
                  value = '(dGf*complex(0,1)*yt)/2.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_763 = Coupling(name = 'GC_763',
                  value = '(cth*cuB*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_764 = Coupling(name = 'GC_764',
                  value = '(cuG*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':3})

GC_765 = Coupling(name = 'GC_765',
                  value = '(3*cuH*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':3})

GC_766 = Coupling(name = 'GC_766',
                  value = '(cuW*complex(0,1)*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_767 = Coupling(name = 'GC_767',
                  value = '(cth*cuW*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_768 = Coupling(name = 'GC_768',
                  value = '(cuW*ee*complex(0,1)*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_769 = Coupling(name = 'GC_769',
                  value = '(cuG*G*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_770 = Coupling(name = 'GC_770',
                  value = '-((cuW*ee*complex(0,1)*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_771 = Coupling(name = 'GC_771',
                  value = '-((cth*cuW*ee*complex(0,1)*yt)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_772 = Coupling(name = 'GC_772',
                  value = '-((cuB*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_773 = Coupling(name = 'GC_773',
                  value = '(cuW*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_774 = Coupling(name = 'GC_774',
                  value = '(cth*cuB*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_775 = Coupling(name = 'GC_775',
                  value = '(cuG*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':2})

GC_776 = Coupling(name = 'GC_776',
                  value = '(3*cuH*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':2})

GC_777 = Coupling(name = 'GC_777',
                  value = '(cuW*complex(0,1)*vevhat*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_778 = Coupling(name = 'GC_778',
                  value = '(cth*cuW*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_779 = Coupling(name = 'GC_779',
                  value = '(cuW*ee*complex(0,1)*vevhat*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_780 = Coupling(name = 'GC_780',
                  value = '(cuG*G*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_781 = Coupling(name = 'GC_781',
                  value = '-((cuW*ee*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_782 = Coupling(name = 'GC_782',
                  value = '-((cth*cuW*ee*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_783 = Coupling(name = 'GC_783',
                  value = '-((cuB*complex(0,1)*sth*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_784 = Coupling(name = 'GC_784',
                  value = '(cuW*complex(0,1)*sth*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_785 = Coupling(name = 'GC_785',
                  value = '-((cHbox*complex(0,1)*vevhat**2*yt)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_786 = Coupling(name = 'GC_786',
                  value = '(cHDD*complex(0,1)*vevhat**2*yt)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_787 = Coupling(name = 'GC_787',
                  value = '(cuH*complex(0,1)*vevhat**2*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':1})

GC_788 = Coupling(name = 'GC_788',
                  value = '(cquqd1*complex(0,1)*yb*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_789 = Coupling(name = 'GC_789',
                  value = '(cquqd8*complex(0,1)*yb*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_790 = Coupling(name = 'GC_790',
                  value = '(cHud*CKM3x3*ee*complex(0,1)*yb*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_791 = Coupling(name = 'GC_791',
                  value = '(cHud*CKM3x3*ee*complex(0,1)*vevhat*yb*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_792 = Coupling(name = 'GC_792',
                  value = '(cHud*CKM3x3*ee*complex(0,1)*vevhat**2*yb*yt)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':3})

GC_793 = Coupling(name = 'GC_793',
                  value = '(cquqd1*complex(0,1)*ydo*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_794 = Coupling(name = 'GC_794',
                  value = '(cquqd8*complex(0,1)*ydo*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_795 = Coupling(name = 'GC_795',
                  value = '(cHud*CKM3x1*ee*complex(0,1)*ydo*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_796 = Coupling(name = 'GC_796',
                  value = '(cHud*CKM3x1*ee*complex(0,1)*vevhat*ydo*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_797 = Coupling(name = 'GC_797',
                  value = '(cHud*CKM3x1*ee*complex(0,1)*vevhat**2*ydo*yt)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':3})

GC_798 = Coupling(name = 'GC_798',
                  value = '-((clequ1*complex(0,1)*ye*yt)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_799 = Coupling(name = 'GC_799',
                  value = '-(clequ3*complex(0,1)*ye*yt)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_800 = Coupling(name = 'GC_800',
                  value = '(clequ3*complex(0,1)*ye*yt)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_801 = Coupling(name = 'GC_801',
                  value = '-((clequ1*complex(0,1)*ym*yt)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_802 = Coupling(name = 'GC_802',
                  value = '-(clequ3*complex(0,1)*ym*yt)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_803 = Coupling(name = 'GC_803',
                  value = '(clequ3*complex(0,1)*ym*yt)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_804 = Coupling(name = 'GC_804',
                  value = '(cquqd1*complex(0,1)*ys*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_805 = Coupling(name = 'GC_805',
                  value = '(cquqd8*complex(0,1)*ys*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_806 = Coupling(name = 'GC_806',
                  value = '(cHud*CKM3x2*ee*complex(0,1)*ys*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_807 = Coupling(name = 'GC_807',
                  value = '(cHud*CKM3x2*ee*complex(0,1)*vevhat*ys*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_808 = Coupling(name = 'GC_808',
                  value = '(cHud*CKM3x2*ee*complex(0,1)*vevhat**2*ys*yt)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':3})

GC_809 = Coupling(name = 'GC_809',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_810 = Coupling(name = 'GC_810',
                  value = '(dGf*complex(0,1)*ytau)/2.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_811 = Coupling(name = 'GC_811',
                  value = '(3*ceH*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':3})

GC_812 = Coupling(name = 'GC_812',
                  value = '(ceW*complex(0,1)*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_813 = Coupling(name = 'GC_813',
                  value = '(ceB*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_814 = Coupling(name = 'GC_814',
                  value = '-((ceW*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_815 = Coupling(name = 'GC_815',
                  value = '-((ceW*ee*complex(0,1)*ytau)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_816 = Coupling(name = 'GC_816',
                  value = '(cledq*complex(0,1)*I3d11*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_817 = Coupling(name = 'GC_817',
                  value = '(cledq*complex(0,1)*I3d12*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_818 = Coupling(name = 'GC_818',
                  value = '(cledq*complex(0,1)*I3d13*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_819 = Coupling(name = 'GC_819',
                  value = '(cledq*complex(0,1)*I3d21*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_820 = Coupling(name = 'GC_820',
                  value = '(cledq*complex(0,1)*I3d22*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_821 = Coupling(name = 'GC_821',
                  value = '(cledq*complex(0,1)*I3d23*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_822 = Coupling(name = 'GC_822',
                  value = '(cledq*complex(0,1)*I3d31*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_823 = Coupling(name = 'GC_823',
                  value = '(cledq*complex(0,1)*I3d32*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_824 = Coupling(name = 'GC_824',
                  value = '(cledq*complex(0,1)*I3d33*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_825 = Coupling(name = 'GC_825',
                  value = '(clequ1*complex(0,1)*I4d11*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_826 = Coupling(name = 'GC_826',
                  value = '(clequ3*complex(0,1)*I4d11*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_827 = Coupling(name = 'GC_827',
                  value = '-(clequ3*complex(0,1)*I4d11*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_828 = Coupling(name = 'GC_828',
                  value = '(clequ1*complex(0,1)*I4d12*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_829 = Coupling(name = 'GC_829',
                  value = '(clequ3*complex(0,1)*I4d12*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_830 = Coupling(name = 'GC_830',
                  value = '-(clequ3*complex(0,1)*I4d12*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_831 = Coupling(name = 'GC_831',
                  value = '(clequ1*complex(0,1)*I4d13*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_832 = Coupling(name = 'GC_832',
                  value = '(clequ3*complex(0,1)*I4d13*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_833 = Coupling(name = 'GC_833',
                  value = '-(clequ3*complex(0,1)*I4d13*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_834 = Coupling(name = 'GC_834',
                  value = '(clequ1*complex(0,1)*I4d21*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_835 = Coupling(name = 'GC_835',
                  value = '(clequ3*complex(0,1)*I4d21*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_836 = Coupling(name = 'GC_836',
                  value = '-(clequ3*complex(0,1)*I4d21*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_837 = Coupling(name = 'GC_837',
                  value = '(clequ1*complex(0,1)*I4d22*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_838 = Coupling(name = 'GC_838',
                  value = '(clequ3*complex(0,1)*I4d22*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_839 = Coupling(name = 'GC_839',
                  value = '-(clequ3*complex(0,1)*I4d22*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_840 = Coupling(name = 'GC_840',
                  value = '(clequ1*complex(0,1)*I4d23*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_841 = Coupling(name = 'GC_841',
                  value = '(clequ3*complex(0,1)*I4d23*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_842 = Coupling(name = 'GC_842',
                  value = '-(clequ3*complex(0,1)*I4d23*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_843 = Coupling(name = 'GC_843',
                  value = '(clequ1*complex(0,1)*I4d31*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_844 = Coupling(name = 'GC_844',
                  value = '(clequ3*complex(0,1)*I4d31*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_845 = Coupling(name = 'GC_845',
                  value = '-(clequ3*complex(0,1)*I4d31*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_846 = Coupling(name = 'GC_846',
                  value = '(clequ1*complex(0,1)*I4d32*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_847 = Coupling(name = 'GC_847',
                  value = '(clequ3*complex(0,1)*I4d32*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_848 = Coupling(name = 'GC_848',
                  value = '-(clequ3*complex(0,1)*I4d32*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_849 = Coupling(name = 'GC_849',
                  value = '(clequ1*complex(0,1)*I4d33*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_850 = Coupling(name = 'GC_850',
                  value = '(clequ3*complex(0,1)*I4d33*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_851 = Coupling(name = 'GC_851',
                  value = '-(clequ3*complex(0,1)*I4d33*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_852 = Coupling(name = 'GC_852',
                  value = '(ceW*ee*complex(0,1)*ytau)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_853 = Coupling(name = 'GC_853',
                  value = '(ceW*cth*ee*complex(0,1)*ytau)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':4})

GC_854 = Coupling(name = 'GC_854',
                  value = '-((ceB*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_855 = Coupling(name = 'GC_855',
                  value = '-((ceW*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_856 = Coupling(name = 'GC_856',
                  value = '(3*ceH*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':2})

GC_857 = Coupling(name = 'GC_857',
                  value = '(ceW*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_858 = Coupling(name = 'GC_858',
                  value = '(ceB*cth*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_859 = Coupling(name = 'GC_859',
                  value = '-((ceW*cth*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_860 = Coupling(name = 'GC_860',
                  value = '-((ceW*ee*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_861 = Coupling(name = 'GC_861',
                  value = '(ceW*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_862 = Coupling(name = 'GC_862',
                  value = '(ceW*cth*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'NPceW':1,'QED':3})

GC_863 = Coupling(name = 'GC_863',
                  value = '-((ceB*complex(0,1)*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_864 = Coupling(name = 'GC_864',
                  value = '-((ceW*complex(0,1)*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceW':1,'QED':2})

GC_865 = Coupling(name = 'GC_865',
                  value = '(ceH*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceH':1,'QED':1})

GC_866 = Coupling(name = 'GC_866',
                  value = '-((cHbox*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_867 = Coupling(name = 'GC_867',
                  value = '(cHDD*complex(0,1)*vevhat**2*ytau)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_868 = Coupling(name = 'GC_868',
                  value = '(cledq*complex(0,1)*yb*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_869 = Coupling(name = 'GC_869',
                  value = '-((clequ1*complex(0,1)*yc*ytau)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_870 = Coupling(name = 'GC_870',
                  value = '-(clequ3*complex(0,1)*yc*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_871 = Coupling(name = 'GC_871',
                  value = '(clequ3*complex(0,1)*yc*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_872 = Coupling(name = 'GC_872',
                  value = '(cledq*complex(0,1)*ydo*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_873 = Coupling(name = 'GC_873',
                  value = '(cledq*complex(0,1)*ys*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcledq':1,'QED':4})

GC_874 = Coupling(name = 'GC_874',
                  value = '-((clequ1*complex(0,1)*yt*ytau)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_875 = Coupling(name = 'GC_875',
                  value = '-(clequ3*complex(0,1)*yt*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_876 = Coupling(name = 'GC_876',
                  value = '(clequ3*complex(0,1)*yt*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_877 = Coupling(name = 'GC_877',
                  value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_878 = Coupling(name = 'GC_878',
                  value = '(dGf*complex(0,1)*yup)/2.',
                  order = {'NP':1,'NPcHl3':1,'NPcll1':1,'QED':1})

GC_879 = Coupling(name = 'GC_879',
                  value = '(cth*cuB*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_880 = Coupling(name = 'GC_880',
                  value = '(cuG*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':3})

GC_881 = Coupling(name = 'GC_881',
                  value = '(3*cuH*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':3})

GC_882 = Coupling(name = 'GC_882',
                  value = '(cuW*complex(0,1)*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_883 = Coupling(name = 'GC_883',
                  value = '(cth*cuW*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_884 = Coupling(name = 'GC_884',
                  value = '(cuW*ee*complex(0,1)*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_885 = Coupling(name = 'GC_885',
                  value = '(cuG*G*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_886 = Coupling(name = 'GC_886',
                  value = '-((cuW*ee*complex(0,1)*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_887 = Coupling(name = 'GC_887',
                  value = '-((cth*cuW*ee*complex(0,1)*yup)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':4})

GC_888 = Coupling(name = 'GC_888',
                  value = '-((cuB*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':3})

GC_889 = Coupling(name = 'GC_889',
                  value = '(cuW*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_890 = Coupling(name = 'GC_890',
                  value = '(cth*cuB*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_891 = Coupling(name = 'GC_891',
                  value = '(cuG*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QED':2})

GC_892 = Coupling(name = 'GC_892',
                  value = '(3*cuH*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':2})

GC_893 = Coupling(name = 'GC_893',
                  value = '(cuW*complex(0,1)*vevhat*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_894 = Coupling(name = 'GC_894',
                  value = '(cth*cuW*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_895 = Coupling(name = 'GC_895',
                  value = '(cuW*ee*complex(0,1)*vevhat*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_896 = Coupling(name = 'GC_896',
                  value = '(cuG*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_897 = Coupling(name = 'GC_897',
                  value = '-((cuW*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_898 = Coupling(name = 'GC_898',
                  value = '-((cth*cuW*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcuW':1,'QED':3})

GC_899 = Coupling(name = 'GC_899',
                  value = '-((cuB*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcuB':1,'QED':2})

GC_900 = Coupling(name = 'GC_900',
                  value = '(cuW*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuW':1,'QED':2})

GC_901 = Coupling(name = 'GC_901',
                  value = '-((cHbox*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcHbox':1,'QED':1})

GC_902 = Coupling(name = 'GC_902',
                  value = '(cHDD*complex(0,1)*vevhat**2*yup)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHDD':1,'QED':1})

GC_903 = Coupling(name = 'GC_903',
                  value = '(cuH*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcuH':1,'QED':1})

GC_904 = Coupling(name = 'GC_904',
                  value = '(cquqd1*complex(0,1)*yb*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_905 = Coupling(name = 'GC_905',
                  value = '(cquqd8*complex(0,1)*yb*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_906 = Coupling(name = 'GC_906',
                  value = '(cHud*CKM1x3*ee*complex(0,1)*yb*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_907 = Coupling(name = 'GC_907',
                  value = '(cHud*CKM1x3*ee*complex(0,1)*vevhat*yb*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_908 = Coupling(name = 'GC_908',
                  value = '(cHud*CKM1x3*ee*complex(0,1)*vevhat**2*yb*yup)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':3})

GC_909 = Coupling(name = 'GC_909',
                  value = '(cquqd1*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_910 = Coupling(name = 'GC_910',
                  value = '(cquqd8*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_911 = Coupling(name = 'GC_911',
                  value = '(cHud*CKM1x1*ee*complex(0,1)*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_912 = Coupling(name = 'GC_912',
                  value = '(cHud*CKM1x1*ee*complex(0,1)*vevhat*ydo*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_913 = Coupling(name = 'GC_913',
                  value = '(cHud*CKM1x1*ee*complex(0,1)*vevhat**2*ydo*yup)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':3})

GC_914 = Coupling(name = 'GC_914',
                  value = '-((clequ1*complex(0,1)*ye*yup)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_915 = Coupling(name = 'GC_915',
                  value = '-(clequ3*complex(0,1)*ye*yup)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_916 = Coupling(name = 'GC_916',
                  value = '(clequ3*complex(0,1)*ye*yup)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_917 = Coupling(name = 'GC_917',
                  value = '-((clequ1*complex(0,1)*ym*yup)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_918 = Coupling(name = 'GC_918',
                  value = '-(clequ3*complex(0,1)*ym*yup)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_919 = Coupling(name = 'GC_919',
                  value = '(clequ3*complex(0,1)*ym*yup)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_920 = Coupling(name = 'GC_920',
                  value = '(cquqd1*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_921 = Coupling(name = 'GC_921',
                  value = '(cquqd8*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_922 = Coupling(name = 'GC_922',
                  value = '(cHud*CKM1x2*ee*complex(0,1)*ys*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':5})

GC_923 = Coupling(name = 'GC_923',
                  value = '(cHud*CKM1x2*ee*complex(0,1)*vevhat*ys*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':4})

GC_924 = Coupling(name = 'GC_924',
                  value = '(cHud*CKM1x2*ee*complex(0,1)*vevhat**2*ys*yup)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcHud':1,'QED':3})

GC_925 = Coupling(name = 'GC_925',
                  value = '-((clequ1*complex(0,1)*ytau*yup)/LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ1':1,'QED':4})

GC_926 = Coupling(name = 'GC_926',
                  value = '-(clequ3*complex(0,1)*ytau*yup)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_927 = Coupling(name = 'GC_927',
                  value = '(clequ3*complex(0,1)*ytau*yup)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'NPclequ3':1,'QED':4})

GC_928 = Coupling(name = 'GC_928',
                  value = '(cth*complex(0,1)*yb*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_929 = Coupling(name = 'GC_929',
                  value = '-((complex(0,1)*sth*yb*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_930 = Coupling(name = 'GC_930',
                  value = '(cth*complex(0,1)*vevhat*yb*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_931 = Coupling(name = 'GC_931',
                  value = '-((complex(0,1)*sth*vevhat*yb*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_932 = Coupling(name = 'GC_932',
                  value = '(cth*complex(0,1)*ydo*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_933 = Coupling(name = 'GC_933',
                  value = '-((complex(0,1)*sth*ydo*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_934 = Coupling(name = 'GC_934',
                  value = '(cth*complex(0,1)*vevhat*ydo*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_935 = Coupling(name = 'GC_935',
                  value = '-((complex(0,1)*sth*vevhat*ydo*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_936 = Coupling(name = 'GC_936',
                  value = '(cth*complex(0,1)*ys*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_937 = Coupling(name = 'GC_937',
                  value = '-((complex(0,1)*sth*ys*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':3})

GC_938 = Coupling(name = 'GC_938',
                  value = '(cth*complex(0,1)*vevhat*ys*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_939 = Coupling(name = 'GC_939',
                  value = '-((complex(0,1)*sth*vevhat*ys*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdB':1,'QED':2})

GC_940 = Coupling(name = 'GC_940',
                  value = '(complex(0,1)*yb*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':3})

GC_941 = Coupling(name = 'GC_941',
                  value = '(G*yb*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_942 = Coupling(name = 'GC_942',
                  value = '(complex(0,1)*vevhat*yb*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':2})

GC_943 = Coupling(name = 'GC_943',
                  value = '(G*vevhat*yb*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_944 = Coupling(name = 'GC_944',
                  value = '(complex(0,1)*ydo*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':3})

GC_945 = Coupling(name = 'GC_945',
                  value = '(G*ydo*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_946 = Coupling(name = 'GC_946',
                  value = '(complex(0,1)*vevhat*ydo*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':2})

GC_947 = Coupling(name = 'GC_947',
                  value = '(G*vevhat*ydo*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_948 = Coupling(name = 'GC_948',
                  value = '(complex(0,1)*ys*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':3})

GC_949 = Coupling(name = 'GC_949',
                  value = '(G*ys*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':3})

GC_950 = Coupling(name = 'GC_950',
                  value = '(complex(0,1)*vevhat*ys*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QED':2})

GC_951 = Coupling(name = 'GC_951',
                  value = '(G*vevhat*ys*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdG':1,'QCD':1,'QED':2})

GC_952 = Coupling(name = 'GC_952',
                  value = '(3*complex(0,1)*yb*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':3})

GC_953 = Coupling(name = 'GC_953',
                  value = '(3*complex(0,1)*vevhat*yb*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':2})

GC_954 = Coupling(name = 'GC_954',
                  value = '(complex(0,1)*vevhat**2*yb*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':1})

GC_955 = Coupling(name = 'GC_955',
                  value = '(3*complex(0,1)*ydo*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':3})

GC_956 = Coupling(name = 'GC_956',
                  value = '(3*complex(0,1)*vevhat*ydo*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':2})

GC_957 = Coupling(name = 'GC_957',
                  value = '(complex(0,1)*vevhat**2*ydo*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':1})

GC_958 = Coupling(name = 'GC_958',
                  value = '(3*complex(0,1)*ys*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':3})

GC_959 = Coupling(name = 'GC_959',
                  value = '(3*complex(0,1)*vevhat*ys*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':2})

GC_960 = Coupling(name = 'GC_960',
                  value = '(complex(0,1)*vevhat**2*ys*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdH':1,'QED':1})

GC_961 = Coupling(name = 'GC_961',
                  value = '(complex(0,1)*yb*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_962 = Coupling(name = 'GC_962',
                  value = '-((cth*complex(0,1)*yb*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_963 = Coupling(name = 'GC_963',
                  value = '(ee*complex(0,1)*yb*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_964 = Coupling(name = 'GC_964',
                  value = '(ee*complex(0,1)*yb*complexconjugate(cdW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_965 = Coupling(name = 'GC_965',
                  value = '-((cth*ee*complex(0,1)*yb*complexconjugate(cdW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_966 = Coupling(name = 'GC_966',
                  value = '-((complex(0,1)*sth*yb*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_967 = Coupling(name = 'GC_967',
                  value = '(complex(0,1)*vevhat*yb*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_968 = Coupling(name = 'GC_968',
                  value = '-((cth*complex(0,1)*vevhat*yb*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_969 = Coupling(name = 'GC_969',
                  value = '(ee*complex(0,1)*vevhat*yb*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_970 = Coupling(name = 'GC_970',
                  value = '(ee*complex(0,1)*vevhat*yb*complexconjugate(cdW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_971 = Coupling(name = 'GC_971',
                  value = '-((cth*ee*complex(0,1)*vevhat*yb*complexconjugate(cdW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_972 = Coupling(name = 'GC_972',
                  value = '-((complex(0,1)*sth*vevhat*yb*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_973 = Coupling(name = 'GC_973',
                  value = '(complex(0,1)*ydo*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((cth*complex(0,1)*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_975 = Coupling(name = 'GC_975',
                  value = '(ee*complex(0,1)*ydo*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_976 = Coupling(name = 'GC_976',
                  value = '(ee*complex(0,1)*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_977 = Coupling(name = 'GC_977',
                  value = '-((cth*ee*complex(0,1)*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_978 = Coupling(name = 'GC_978',
                  value = '-((complex(0,1)*sth*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_979 = Coupling(name = 'GC_979',
                  value = '(complex(0,1)*vevhat*ydo*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_980 = Coupling(name = 'GC_980',
                  value = '-((cth*complex(0,1)*vevhat*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_981 = Coupling(name = 'GC_981',
                  value = '(ee*complex(0,1)*vevhat*ydo*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_982 = Coupling(name = 'GC_982',
                  value = '(ee*complex(0,1)*vevhat*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_983 = Coupling(name = 'GC_983',
                  value = '-((cth*ee*complex(0,1)*vevhat*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_984 = Coupling(name = 'GC_984',
                  value = '-((complex(0,1)*sth*vevhat*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_985 = Coupling(name = 'GC_985',
                  value = '(complex(0,1)*ys*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_986 = Coupling(name = 'GC_986',
                  value = '-((cth*complex(0,1)*ys*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_987 = Coupling(name = 'GC_987',
                  value = '(ee*complex(0,1)*ys*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_988 = Coupling(name = 'GC_988',
                  value = '(ee*complex(0,1)*ys*complexconjugate(cdW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_989 = Coupling(name = 'GC_989',
                  value = '-((cth*ee*complex(0,1)*ys*complexconjugate(cdW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':4})

GC_990 = Coupling(name = 'GC_990',
                  value = '-((complex(0,1)*sth*ys*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_991 = Coupling(name = 'GC_991',
                  value = '(complex(0,1)*vevhat*ys*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_992 = Coupling(name = 'GC_992',
                  value = '-((cth*complex(0,1)*vevhat*ys*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_993 = Coupling(name = 'GC_993',
                  value = '(ee*complex(0,1)*vevhat*ys*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_994 = Coupling(name = 'GC_994',
                  value = '(ee*complex(0,1)*vevhat*ys*complexconjugate(cdW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_995 = Coupling(name = 'GC_995',
                  value = '-((cth*ee*complex(0,1)*vevhat*ys*complexconjugate(cdW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'NPcdW':1,'QED':3})

GC_996 = Coupling(name = 'GC_996',
                  value = '-((complex(0,1)*sth*vevhat*ys*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPcdW':1,'QED':2})

GC_997 = Coupling(name = 'GC_997',
                  value = '(cth*complex(0,1)*ye*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_998 = Coupling(name = 'GC_998',
                  value = '-((complex(0,1)*sth*ye*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                  order = {'NP':1,'NPceB':1,'QED':3})

GC_999 = Coupling(name = 'GC_999',
                  value = '(cth*complex(0,1)*vevhat*ye*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'NPceB':1,'QED':2})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '-((complex(0,1)*sth*vevhat*ye*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceB':1,'QED':2})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '(cth*complex(0,1)*ym*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceB':1,'QED':3})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '-((complex(0,1)*sth*ym*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceB':1,'QED':3})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '(cth*complex(0,1)*vevhat*ym*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceB':1,'QED':2})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '-((complex(0,1)*sth*vevhat*ym*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceB':1,'QED':2})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '(cth*complex(0,1)*ytau*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceB':1,'QED':3})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '-((complex(0,1)*sth*ytau*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceB':1,'QED':3})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '(cth*complex(0,1)*vevhat*ytau*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceB':1,'QED':2})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '-((complex(0,1)*sth*vevhat*ytau*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceB':1,'QED':2})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '(3*complex(0,1)*ye*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':3})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '(3*complex(0,1)*vevhat*ye*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':2})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '(complex(0,1)*vevhat**2*ye*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':1})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '(3*complex(0,1)*ym*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':3})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '(3*complex(0,1)*vevhat*ym*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':2})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '(complex(0,1)*vevhat**2*ym*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':1})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '(3*complex(0,1)*ytau*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':3})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '(3*complex(0,1)*vevhat*ytau*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':2})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(complex(0,1)*vevhat**2*ytau*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPceH':1,'QED':1})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '(complex(0,1)*ye*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '-((cth*complex(0,1)*ye*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '(ee*complex(0,1)*ye*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(ee*complex(0,1)*ye*complexconjugate(ceW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '-((cth*ee*complex(0,1)*ye*complexconjugate(ceW))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '-((complex(0,1)*sth*ye*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '(complex(0,1)*vevhat*ye*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '-((cth*complex(0,1)*vevhat*ye*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '(ee*complex(0,1)*vevhat*ye*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '(ee*complex(0,1)*vevhat*ye*complexconjugate(ceW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '-((cth*ee*complex(0,1)*vevhat*ye*complexconjugate(ceW))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '-((complex(0,1)*sth*vevhat*ye*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '(complex(0,1)*ym*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '-((cth*complex(0,1)*ym*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '(ee*complex(0,1)*ym*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '(ee*complex(0,1)*ym*complexconjugate(ceW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '-((cth*ee*complex(0,1)*ym*complexconjugate(ceW))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '-((complex(0,1)*sth*ym*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '(complex(0,1)*vevhat*ym*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '-((cth*complex(0,1)*vevhat*ym*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '(ee*complex(0,1)*vevhat*ym*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '(ee*complex(0,1)*vevhat*ym*complexconjugate(ceW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '-((cth*ee*complex(0,1)*vevhat*ym*complexconjugate(ceW))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '-((complex(0,1)*sth*vevhat*ym*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '(complex(0,1)*ytau*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-((cth*complex(0,1)*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '(ee*complex(0,1)*ytau*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '(ee*complex(0,1)*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '-((cth*ee*complex(0,1)*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'QED':4})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '-((complex(0,1)*sth*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '(complex(0,1)*vevhat*ytau*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '-((cth*complex(0,1)*vevhat*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '(ee*complex(0,1)*vevhat*ytau*complexconjugate(ceW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '(ee*complex(0,1)*vevhat*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((cth*ee*complex(0,1)*vevhat*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPceW':1,'QED':3})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '-((complex(0,1)*sth*vevhat*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPceW':1,'QED':2})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '(2*clq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclq3':1,'QED':2})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '(4*CKM1x1*cqq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '(4*CKM1x2*cqq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '(4*CKM1x3*cqq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '(4*CKM2x1*cqq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '(4*CKM2x2*cqq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '(4*CKM2x3*cqq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '(4*CKM3x1*cqq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '(4*CKM3x2*cqq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '(4*CKM3x3*cqq3*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '(-2*CKM1x1*cqq31*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '(-2*CKM1x2*cqq31*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '(-2*CKM1x3*cqq31*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '(-2*CKM2x1*cqq31*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '(-2*CKM2x2*cqq31*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '(-2*CKM2x3*cqq31*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '(-2*CKM3x1*cqq31*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '(-2*CKM3x2*cqq31*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '(-2*CKM3x3*cqq31*complex(0,1)*complexconjugate(CKM1x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM1x1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM1x1))/(sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '-((cHq3*ee*complex(0,1)*complexconjugate(CKM1x1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':3})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '-((cHq3*ee*complex(0,1)*vevhat*complexconjugate(CKM1x1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':2})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '-((cHq3*ee*complex(0,1)*vevhat**2*complexconjugate(CKM1x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHq3':1,'QED':1})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '(ee*complex(0,1)*ydo*yup*complexconjugate(cHud)*complexconjugate(CKM1x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '(ee*complex(0,1)*vevhat*ydo*yup*complexconjugate(cHud)*complexconjugate(CKM1x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '(ee*complex(0,1)*vevhat**2*ydo*yup*complexconjugate(cHud)*complexconjugate(CKM1x1))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '(2*clq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclq3':1,'QED':2})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '(4*CKM1x1*cqq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '(4*CKM1x2*cqq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '(4*CKM1x3*cqq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '(4*CKM2x1*cqq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '(4*CKM2x2*cqq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '(4*CKM2x3*cqq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '(4*CKM3x1*cqq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '(4*CKM3x2*cqq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '(4*CKM3x3*cqq3*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '(-2*CKM1x1*cqq31*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '(-2*CKM1x2*cqq31*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '(-2*CKM1x3*cqq31*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '(-2*CKM2x1*cqq31*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '(-2*CKM2x2*cqq31*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '(-2*CKM2x3*cqq31*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '(-2*CKM3x1*cqq31*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '(-2*CKM3x2*cqq31*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '(-2*CKM3x3*cqq31*complex(0,1)*complexconjugate(CKM1x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM1x2))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM1x2))/(sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '-((cHq3*ee*complex(0,1)*complexconjugate(CKM1x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':3})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '-((cHq3*ee*complex(0,1)*vevhat*complexconjugate(CKM1x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':2})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '-((cHq3*ee*complex(0,1)*vevhat**2*complexconjugate(CKM1x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHq3':1,'QED':1})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '(ee*complex(0,1)*ys*yup*complexconjugate(cHud)*complexconjugate(CKM1x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '(ee*complex(0,1)*vevhat*ys*yup*complexconjugate(cHud)*complexconjugate(CKM1x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '(ee*complex(0,1)*vevhat**2*ys*yup*complexconjugate(cHud)*complexconjugate(CKM1x2))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '(2*clq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclq3':1,'QED':2})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '(4*CKM1x1*cqq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '(4*CKM1x2*cqq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '(4*CKM1x3*cqq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '(4*CKM2x1*cqq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '(4*CKM2x2*cqq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '(4*CKM2x3*cqq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '(4*CKM3x1*cqq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '(4*CKM3x2*cqq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '(4*CKM3x3*cqq3*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '(-2*CKM1x1*cqq31*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '(-2*CKM1x2*cqq31*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '(-2*CKM1x3*cqq31*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '(-2*CKM2x1*cqq31*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '(-2*CKM2x2*cqq31*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '(-2*CKM2x3*cqq31*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '(-2*CKM3x1*cqq31*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '(-2*CKM3x2*cqq31*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '(-2*CKM3x3*cqq31*complex(0,1)*complexconjugate(CKM1x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM1x3))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM1x3))/(sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '-((cHq3*ee*complex(0,1)*complexconjugate(CKM1x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':3})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '-((cHq3*ee*complex(0,1)*vevhat*complexconjugate(CKM1x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':2})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '-((cHq3*ee*complex(0,1)*vevhat**2*complexconjugate(CKM1x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHq3':1,'QED':1})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '(ee*complex(0,1)*yb*yup*complexconjugate(cHud)*complexconjugate(CKM1x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '(ee*complex(0,1)*vevhat*yb*yup*complexconjugate(cHud)*complexconjugate(CKM1x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '(ee*complex(0,1)*vevhat**2*yb*yup*complexconjugate(cHud)*complexconjugate(CKM1x3))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '(2*clq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclq3':1,'QED':2})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '(4*CKM1x1*cqq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '(4*CKM1x2*cqq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '(4*CKM1x3*cqq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(4*CKM2x1*cqq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '(4*CKM2x2*cqq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '(4*CKM2x3*cqq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '(4*CKM3x1*cqq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '(4*CKM3x2*cqq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '(4*CKM3x3*cqq3*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '(-2*CKM1x1*cqq31*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '(-2*CKM1x2*cqq31*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '(-2*CKM1x3*cqq31*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '(-2*CKM2x1*cqq31*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '(-2*CKM2x2*cqq31*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '(-2*CKM2x3*cqq31*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '(-2*CKM3x1*cqq31*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '(-2*CKM3x2*cqq31*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '(-2*CKM3x3*cqq31*complex(0,1)*complexconjugate(CKM2x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM2x1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM2x1))/(sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '-((cHq3*ee*complex(0,1)*complexconjugate(CKM2x1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':3})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '-((cHq3*ee*complex(0,1)*vevhat*complexconjugate(CKM2x1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':2})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '-((cHq3*ee*complex(0,1)*vevhat**2*complexconjugate(CKM2x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHq3':1,'QED':1})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '(ee*complex(0,1)*yc*ydo*complexconjugate(cHud)*complexconjugate(CKM2x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '(ee*complex(0,1)*vevhat*yc*ydo*complexconjugate(cHud)*complexconjugate(CKM2x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1161 = Coupling(name = 'GC_1161',
                   value = '(ee*complex(0,1)*vevhat**2*yc*ydo*complexconjugate(cHud)*complexconjugate(CKM2x1))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1162 = Coupling(name = 'GC_1162',
                   value = '(2*clq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclq3':1,'QED':2})

GC_1163 = Coupling(name = 'GC_1163',
                   value = '(4*CKM1x1*cqq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1164 = Coupling(name = 'GC_1164',
                   value = '(4*CKM1x2*cqq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1165 = Coupling(name = 'GC_1165',
                   value = '(4*CKM1x3*cqq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1166 = Coupling(name = 'GC_1166',
                   value = '(4*CKM2x1*cqq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1167 = Coupling(name = 'GC_1167',
                   value = '(4*CKM2x2*cqq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1168 = Coupling(name = 'GC_1168',
                   value = '(4*CKM2x3*cqq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1169 = Coupling(name = 'GC_1169',
                   value = '(4*CKM3x1*cqq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1170 = Coupling(name = 'GC_1170',
                   value = '(4*CKM3x2*cqq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1171 = Coupling(name = 'GC_1171',
                   value = '(4*CKM3x3*cqq3*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1172 = Coupling(name = 'GC_1172',
                   value = '(-2*CKM1x1*cqq31*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1173 = Coupling(name = 'GC_1173',
                   value = '(-2*CKM1x2*cqq31*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1174 = Coupling(name = 'GC_1174',
                   value = '(-2*CKM1x3*cqq31*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1175 = Coupling(name = 'GC_1175',
                   value = '(-2*CKM2x1*cqq31*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1176 = Coupling(name = 'GC_1176',
                   value = '(-2*CKM2x2*cqq31*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1177 = Coupling(name = 'GC_1177',
                   value = '(-2*CKM2x3*cqq31*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1178 = Coupling(name = 'GC_1178',
                   value = '(-2*CKM3x1*cqq31*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1179 = Coupling(name = 'GC_1179',
                   value = '(-2*CKM3x2*cqq31*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1180 = Coupling(name = 'GC_1180',
                   value = '(-2*CKM3x3*cqq31*complex(0,1)*complexconjugate(CKM2x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1181 = Coupling(name = 'GC_1181',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM2x2))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1182 = Coupling(name = 'GC_1182',
                   value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM2x2))/(sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1183 = Coupling(name = 'GC_1183',
                   value = '-((cHq3*ee*complex(0,1)*complexconjugate(CKM2x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':3})

GC_1184 = Coupling(name = 'GC_1184',
                   value = '-((cHq3*ee*complex(0,1)*vevhat*complexconjugate(CKM2x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':2})

GC_1185 = Coupling(name = 'GC_1185',
                   value = '-((cHq3*ee*complex(0,1)*vevhat**2*complexconjugate(CKM2x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHq3':1,'QED':1})

GC_1186 = Coupling(name = 'GC_1186',
                   value = '(ee*complex(0,1)*yc*ys*complexconjugate(cHud)*complexconjugate(CKM2x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1187 = Coupling(name = 'GC_1187',
                   value = '(ee*complex(0,1)*vevhat*yc*ys*complexconjugate(cHud)*complexconjugate(CKM2x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1188 = Coupling(name = 'GC_1188',
                   value = '(ee*complex(0,1)*vevhat**2*yc*ys*complexconjugate(cHud)*complexconjugate(CKM2x2))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1189 = Coupling(name = 'GC_1189',
                   value = '(2*clq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclq3':1,'QED':2})

GC_1190 = Coupling(name = 'GC_1190',
                   value = '(4*CKM1x1*cqq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1191 = Coupling(name = 'GC_1191',
                   value = '(4*CKM1x2*cqq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1192 = Coupling(name = 'GC_1192',
                   value = '(4*CKM1x3*cqq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1193 = Coupling(name = 'GC_1193',
                   value = '(4*CKM2x1*cqq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1194 = Coupling(name = 'GC_1194',
                   value = '(4*CKM2x2*cqq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1195 = Coupling(name = 'GC_1195',
                   value = '(4*CKM2x3*cqq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1196 = Coupling(name = 'GC_1196',
                   value = '(4*CKM3x1*cqq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1197 = Coupling(name = 'GC_1197',
                   value = '(4*CKM3x2*cqq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1198 = Coupling(name = 'GC_1198',
                   value = '(4*CKM3x3*cqq3*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1199 = Coupling(name = 'GC_1199',
                   value = '(-2*CKM1x1*cqq31*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1200 = Coupling(name = 'GC_1200',
                   value = '(-2*CKM1x2*cqq31*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1201 = Coupling(name = 'GC_1201',
                   value = '(-2*CKM1x3*cqq31*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1202 = Coupling(name = 'GC_1202',
                   value = '(-2*CKM2x1*cqq31*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1203 = Coupling(name = 'GC_1203',
                   value = '(-2*CKM2x2*cqq31*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1204 = Coupling(name = 'GC_1204',
                   value = '(-2*CKM2x3*cqq31*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1205 = Coupling(name = 'GC_1205',
                   value = '(-2*CKM3x1*cqq31*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1206 = Coupling(name = 'GC_1206',
                   value = '(-2*CKM3x2*cqq31*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1207 = Coupling(name = 'GC_1207',
                   value = '(-2*CKM3x3*cqq31*complex(0,1)*complexconjugate(CKM2x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1208 = Coupling(name = 'GC_1208',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM2x3))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1209 = Coupling(name = 'GC_1209',
                   value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM2x3))/(sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1210 = Coupling(name = 'GC_1210',
                   value = '-((cHq3*ee*complex(0,1)*complexconjugate(CKM2x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':3})

GC_1211 = Coupling(name = 'GC_1211',
                   value = '-((cHq3*ee*complex(0,1)*vevhat*complexconjugate(CKM2x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':2})

GC_1212 = Coupling(name = 'GC_1212',
                   value = '-((cHq3*ee*complex(0,1)*vevhat**2*complexconjugate(CKM2x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHq3':1,'QED':1})

GC_1213 = Coupling(name = 'GC_1213',
                   value = '(ee*complex(0,1)*yb*yc*complexconjugate(cHud)*complexconjugate(CKM2x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1214 = Coupling(name = 'GC_1214',
                   value = '(ee*complex(0,1)*vevhat*yb*yc*complexconjugate(cHud)*complexconjugate(CKM2x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1215 = Coupling(name = 'GC_1215',
                   value = '(ee*complex(0,1)*vevhat**2*yb*yc*complexconjugate(cHud)*complexconjugate(CKM2x3))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1216 = Coupling(name = 'GC_1216',
                   value = '(2*clq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclq3':1,'QED':2})

GC_1217 = Coupling(name = 'GC_1217',
                   value = '(4*CKM1x1*cqq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1218 = Coupling(name = 'GC_1218',
                   value = '(4*CKM1x2*cqq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1219 = Coupling(name = 'GC_1219',
                   value = '(4*CKM1x3*cqq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1220 = Coupling(name = 'GC_1220',
                   value = '(4*CKM2x1*cqq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1221 = Coupling(name = 'GC_1221',
                   value = '(4*CKM2x2*cqq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1222 = Coupling(name = 'GC_1222',
                   value = '(4*CKM2x3*cqq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1223 = Coupling(name = 'GC_1223',
                   value = '(4*CKM3x1*cqq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1224 = Coupling(name = 'GC_1224',
                   value = '(4*CKM3x2*cqq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1225 = Coupling(name = 'GC_1225',
                   value = '(4*CKM3x3*cqq3*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1226 = Coupling(name = 'GC_1226',
                   value = '(-2*CKM1x1*cqq31*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1227 = Coupling(name = 'GC_1227',
                   value = '(-2*CKM1x2*cqq31*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1228 = Coupling(name = 'GC_1228',
                   value = '(-2*CKM1x3*cqq31*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1229 = Coupling(name = 'GC_1229',
                   value = '(-2*CKM2x1*cqq31*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1230 = Coupling(name = 'GC_1230',
                   value = '(-2*CKM2x2*cqq31*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1231 = Coupling(name = 'GC_1231',
                   value = '(-2*CKM2x3*cqq31*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1232 = Coupling(name = 'GC_1232',
                   value = '(-2*CKM3x1*cqq31*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1233 = Coupling(name = 'GC_1233',
                   value = '(-2*CKM3x2*cqq31*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1234 = Coupling(name = 'GC_1234',
                   value = '(-2*CKM3x3*cqq31*complex(0,1)*complexconjugate(CKM3x1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1235 = Coupling(name = 'GC_1235',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM3x1))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1236 = Coupling(name = 'GC_1236',
                   value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM3x1))/(sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1237 = Coupling(name = 'GC_1237',
                   value = '-((cHq3*ee*complex(0,1)*complexconjugate(CKM3x1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':3})

GC_1238 = Coupling(name = 'GC_1238',
                   value = '-((cHq3*ee*complex(0,1)*vevhat*complexconjugate(CKM3x1)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':2})

GC_1239 = Coupling(name = 'GC_1239',
                   value = '-((cHq3*ee*complex(0,1)*vevhat**2*complexconjugate(CKM3x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHq3':1,'QED':1})

GC_1240 = Coupling(name = 'GC_1240',
                   value = '(ee*complex(0,1)*ydo*yt*complexconjugate(cHud)*complexconjugate(CKM3x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1241 = Coupling(name = 'GC_1241',
                   value = '(ee*complex(0,1)*vevhat*ydo*yt*complexconjugate(cHud)*complexconjugate(CKM3x1))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1242 = Coupling(name = 'GC_1242',
                   value = '(ee*complex(0,1)*vevhat**2*ydo*yt*complexconjugate(cHud)*complexconjugate(CKM3x1))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1243 = Coupling(name = 'GC_1243',
                   value = '(2*clq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclq3':1,'QED':2})

GC_1244 = Coupling(name = 'GC_1244',
                   value = '(4*CKM1x1*cqq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1245 = Coupling(name = 'GC_1245',
                   value = '(4*CKM1x2*cqq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1246 = Coupling(name = 'GC_1246',
                   value = '(4*CKM1x3*cqq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1247 = Coupling(name = 'GC_1247',
                   value = '(4*CKM2x1*cqq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1248 = Coupling(name = 'GC_1248',
                   value = '(4*CKM2x2*cqq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1249 = Coupling(name = 'GC_1249',
                   value = '(4*CKM2x3*cqq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1250 = Coupling(name = 'GC_1250',
                   value = '(4*CKM3x1*cqq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1251 = Coupling(name = 'GC_1251',
                   value = '(4*CKM3x2*cqq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1252 = Coupling(name = 'GC_1252',
                   value = '(4*CKM3x3*cqq3*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1253 = Coupling(name = 'GC_1253',
                   value = '(-2*CKM1x1*cqq31*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1254 = Coupling(name = 'GC_1254',
                   value = '(-2*CKM1x2*cqq31*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1255 = Coupling(name = 'GC_1255',
                   value = '(-2*CKM1x3*cqq31*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1256 = Coupling(name = 'GC_1256',
                   value = '(-2*CKM2x1*cqq31*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1257 = Coupling(name = 'GC_1257',
                   value = '(-2*CKM2x2*cqq31*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1258 = Coupling(name = 'GC_1258',
                   value = '(-2*CKM2x3*cqq31*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1259 = Coupling(name = 'GC_1259',
                   value = '(-2*CKM3x1*cqq31*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1260 = Coupling(name = 'GC_1260',
                   value = '(-2*CKM3x2*cqq31*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1261 = Coupling(name = 'GC_1261',
                   value = '(-2*CKM3x3*cqq31*complex(0,1)*complexconjugate(CKM3x2))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1262 = Coupling(name = 'GC_1262',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM3x2))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1263 = Coupling(name = 'GC_1263',
                   value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM3x2))/(sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1264 = Coupling(name = 'GC_1264',
                   value = '-((cHq3*ee*complex(0,1)*complexconjugate(CKM3x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':3})

GC_1265 = Coupling(name = 'GC_1265',
                   value = '-((cHq3*ee*complex(0,1)*vevhat*complexconjugate(CKM3x2)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':2})

GC_1266 = Coupling(name = 'GC_1266',
                   value = '-((cHq3*ee*complex(0,1)*vevhat**2*complexconjugate(CKM3x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHq3':1,'QED':1})

GC_1267 = Coupling(name = 'GC_1267',
                   value = '(ee*complex(0,1)*ys*yt*complexconjugate(cHud)*complexconjugate(CKM3x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1268 = Coupling(name = 'GC_1268',
                   value = '(ee*complex(0,1)*vevhat*ys*yt*complexconjugate(cHud)*complexconjugate(CKM3x2))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1269 = Coupling(name = 'GC_1269',
                   value = '(ee*complex(0,1)*vevhat**2*ys*yt*complexconjugate(cHud)*complexconjugate(CKM3x2))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1270 = Coupling(name = 'GC_1270',
                   value = '(2*clq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclq3':1,'QED':2})

GC_1271 = Coupling(name = 'GC_1271',
                   value = '(4*CKM1x1*cqq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1272 = Coupling(name = 'GC_1272',
                   value = '(4*CKM1x2*cqq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1273 = Coupling(name = 'GC_1273',
                   value = '(4*CKM1x3*cqq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1274 = Coupling(name = 'GC_1274',
                   value = '(4*CKM2x1*cqq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1275 = Coupling(name = 'GC_1275',
                   value = '(4*CKM2x2*cqq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1276 = Coupling(name = 'GC_1276',
                   value = '(4*CKM2x3*cqq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1277 = Coupling(name = 'GC_1277',
                   value = '(4*CKM3x1*cqq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1278 = Coupling(name = 'GC_1278',
                   value = '(4*CKM3x2*cqq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1279 = Coupling(name = 'GC_1279',
                   value = '(4*CKM3x3*cqq3*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq3':1,'QED':2})

GC_1280 = Coupling(name = 'GC_1280',
                   value = '(-2*CKM1x1*cqq31*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1281 = Coupling(name = 'GC_1281',
                   value = '(-2*CKM1x2*cqq31*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1282 = Coupling(name = 'GC_1282',
                   value = '(-2*CKM1x3*cqq31*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1283 = Coupling(name = 'GC_1283',
                   value = '(-2*CKM2x1*cqq31*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1284 = Coupling(name = 'GC_1284',
                   value = '(-2*CKM2x2*cqq31*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1285 = Coupling(name = 'GC_1285',
                   value = '(-2*CKM2x3*cqq31*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1286 = Coupling(name = 'GC_1286',
                   value = '(-2*CKM3x1*cqq31*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1287 = Coupling(name = 'GC_1287',
                   value = '(-2*CKM3x2*cqq31*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1288 = Coupling(name = 'GC_1288',
                   value = '(-2*CKM3x3*cqq31*complex(0,1)*complexconjugate(CKM3x3))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcqq31':1,'QED':2})

GC_1289 = Coupling(name = 'GC_1289',
                   value = '-((ee*complex(0,1)*complexconjugate(CKM3x3))/(sth*cmath.sqrt(2)))',
                   order = {'QED':1})

GC_1290 = Coupling(name = 'GC_1290',
                   value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM3x3))/(sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHDD':1,'NPcHl3':1,'NPcHWB':1,'NPcll1':1,'NPshifts':1,'QED':1})

GC_1291 = Coupling(name = 'GC_1291',
                   value = '-((cHq3*ee*complex(0,1)*complexconjugate(CKM3x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':3})

GC_1292 = Coupling(name = 'GC_1292',
                   value = '-((cHq3*ee*complex(0,1)*vevhat*complexconjugate(CKM3x3)*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                   order = {'NP':1,'NPcHq3':1,'QED':2})

GC_1293 = Coupling(name = 'GC_1293',
                   value = '-((cHq3*ee*complex(0,1)*vevhat**2*complexconjugate(CKM3x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcHq3':1,'QED':1})

GC_1294 = Coupling(name = 'GC_1294',
                   value = '(ee*complex(0,1)*yb*yt*complexconjugate(cHud)*complexconjugate(CKM3x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':5})

GC_1295 = Coupling(name = 'GC_1295',
                   value = '(ee*complex(0,1)*vevhat*yb*yt*complexconjugate(cHud)*complexconjugate(CKM3x3))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':4})

GC_1296 = Coupling(name = 'GC_1296',
                   value = '(ee*complex(0,1)*vevhat**2*yb*yt*complexconjugate(cHud)*complexconjugate(CKM3x3))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                   order = {'NP':1,'NPcHud':1,'QED':3})

GC_1297 = Coupling(name = 'GC_1297',
                   value = '(complex(0,1)*I1d11*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1298 = Coupling(name = 'GC_1298',
                   value = '(complex(0,1)*I1d12*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1299 = Coupling(name = 'GC_1299',
                   value = '(complex(0,1)*I1d13*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1300 = Coupling(name = 'GC_1300',
                   value = '(complex(0,1)*I1d21*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1301 = Coupling(name = 'GC_1301',
                   value = '(complex(0,1)*I1d22*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1302 = Coupling(name = 'GC_1302',
                   value = '(complex(0,1)*I1d23*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1303 = Coupling(name = 'GC_1303',
                   value = '(complex(0,1)*I1d31*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1304 = Coupling(name = 'GC_1304',
                   value = '(complex(0,1)*I1d32*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1305 = Coupling(name = 'GC_1305',
                   value = '(complex(0,1)*I1d33*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1306 = Coupling(name = 'GC_1306',
                   value = '(complex(0,1)*yb*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1307 = Coupling(name = 'GC_1307',
                   value = '(complex(0,1)*ydo*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1308 = Coupling(name = 'GC_1308',
                   value = '(complex(0,1)*I1d11*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1309 = Coupling(name = 'GC_1309',
                   value = '(complex(0,1)*I1d12*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1310 = Coupling(name = 'GC_1310',
                   value = '(complex(0,1)*I1d13*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1311 = Coupling(name = 'GC_1311',
                   value = '(complex(0,1)*I1d21*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1312 = Coupling(name = 'GC_1312',
                   value = '(complex(0,1)*I1d22*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1313 = Coupling(name = 'GC_1313',
                   value = '(complex(0,1)*I1d23*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1314 = Coupling(name = 'GC_1314',
                   value = '(complex(0,1)*I1d31*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1315 = Coupling(name = 'GC_1315',
                   value = '(complex(0,1)*I1d32*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1316 = Coupling(name = 'GC_1316',
                   value = '(complex(0,1)*I1d33*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1317 = Coupling(name = 'GC_1317',
                   value = '(complex(0,1)*yb*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1318 = Coupling(name = 'GC_1318',
                   value = '(complex(0,1)*ydo*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1319 = Coupling(name = 'GC_1319',
                   value = '(complex(0,1)*ye*ys*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1320 = Coupling(name = 'GC_1320',
                   value = '(complex(0,1)*ym*ys*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1321 = Coupling(name = 'GC_1321',
                   value = '(complex(0,1)*I1d11*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1322 = Coupling(name = 'GC_1322',
                   value = '(complex(0,1)*I1d12*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1323 = Coupling(name = 'GC_1323',
                   value = '(complex(0,1)*I1d13*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1324 = Coupling(name = 'GC_1324',
                   value = '(complex(0,1)*I1d21*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1325 = Coupling(name = 'GC_1325',
                   value = '(complex(0,1)*I1d22*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1326 = Coupling(name = 'GC_1326',
                   value = '(complex(0,1)*I1d23*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1327 = Coupling(name = 'GC_1327',
                   value = '(complex(0,1)*I1d31*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1328 = Coupling(name = 'GC_1328',
                   value = '(complex(0,1)*I1d32*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1329 = Coupling(name = 'GC_1329',
                   value = '(complex(0,1)*I1d33*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1330 = Coupling(name = 'GC_1330',
                   value = '(complex(0,1)*yb*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1331 = Coupling(name = 'GC_1331',
                   value = '(complex(0,1)*ydo*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1332 = Coupling(name = 'GC_1332',
                   value = '(complex(0,1)*ys*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcledq':1,'QED':4})

GC_1333 = Coupling(name = 'GC_1333',
                   value = '(complex(0,1)*I2d11*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1334 = Coupling(name = 'GC_1334',
                   value = '(complex(0,1)*I2d12*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1335 = Coupling(name = 'GC_1335',
                   value = '(complex(0,1)*I2d13*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1336 = Coupling(name = 'GC_1336',
                   value = '(complex(0,1)*I2d21*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1337 = Coupling(name = 'GC_1337',
                   value = '(complex(0,1)*I2d22*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1338 = Coupling(name = 'GC_1338',
                   value = '(complex(0,1)*I2d23*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1339 = Coupling(name = 'GC_1339',
                   value = '(complex(0,1)*I2d31*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1340 = Coupling(name = 'GC_1340',
                   value = '(complex(0,1)*I2d32*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1341 = Coupling(name = 'GC_1341',
                   value = '(complex(0,1)*I2d33*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1342 = Coupling(name = 'GC_1342',
                   value = '-((complex(0,1)*yc*ye*complexconjugate(clequ1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1343 = Coupling(name = 'GC_1343',
                   value = '(complex(0,1)*I2d11*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1344 = Coupling(name = 'GC_1344',
                   value = '(complex(0,1)*I2d12*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1345 = Coupling(name = 'GC_1345',
                   value = '(complex(0,1)*I2d13*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1346 = Coupling(name = 'GC_1346',
                   value = '(complex(0,1)*I2d21*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1347 = Coupling(name = 'GC_1347',
                   value = '(complex(0,1)*I2d22*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1348 = Coupling(name = 'GC_1348',
                   value = '(complex(0,1)*I2d23*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1349 = Coupling(name = 'GC_1349',
                   value = '(complex(0,1)*I2d31*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1350 = Coupling(name = 'GC_1350',
                   value = '(complex(0,1)*I2d32*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1351 = Coupling(name = 'GC_1351',
                   value = '(complex(0,1)*I2d33*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1352 = Coupling(name = 'GC_1352',
                   value = '-((complex(0,1)*yc*ym*complexconjugate(clequ1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1353 = Coupling(name = 'GC_1353',
                   value = '-((complex(0,1)*ye*yt*complexconjugate(clequ1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1354 = Coupling(name = 'GC_1354',
                   value = '-((complex(0,1)*ym*yt*complexconjugate(clequ1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1355 = Coupling(name = 'GC_1355',
                   value = '(complex(0,1)*I2d11*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1356 = Coupling(name = 'GC_1356',
                   value = '(complex(0,1)*I2d12*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1357 = Coupling(name = 'GC_1357',
                   value = '(complex(0,1)*I2d13*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1358 = Coupling(name = 'GC_1358',
                   value = '(complex(0,1)*I2d21*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1359 = Coupling(name = 'GC_1359',
                   value = '(complex(0,1)*I2d22*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1360 = Coupling(name = 'GC_1360',
                   value = '(complex(0,1)*I2d23*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1361 = Coupling(name = 'GC_1361',
                   value = '(complex(0,1)*I2d31*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1362 = Coupling(name = 'GC_1362',
                   value = '(complex(0,1)*I2d32*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1363 = Coupling(name = 'GC_1363',
                   value = '(complex(0,1)*I2d33*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1364 = Coupling(name = 'GC_1364',
                   value = '-((complex(0,1)*yc*ytau*complexconjugate(clequ1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1365 = Coupling(name = 'GC_1365',
                   value = '-((complex(0,1)*yt*ytau*complexconjugate(clequ1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1366 = Coupling(name = 'GC_1366',
                   value = '-((complex(0,1)*ye*yup*complexconjugate(clequ1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1367 = Coupling(name = 'GC_1367',
                   value = '-((complex(0,1)*ym*yup*complexconjugate(clequ1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1368 = Coupling(name = 'GC_1368',
                   value = '-((complex(0,1)*ytau*yup*complexconjugate(clequ1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ1':1,'QED':4})

GC_1369 = Coupling(name = 'GC_1369',
                   value = '(complex(0,1)*I2d11*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1370 = Coupling(name = 'GC_1370',
                   value = '-(complex(0,1)*I2d11*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1371 = Coupling(name = 'GC_1371',
                   value = '(complex(0,1)*I2d12*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1372 = Coupling(name = 'GC_1372',
                   value = '-(complex(0,1)*I2d12*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1373 = Coupling(name = 'GC_1373',
                   value = '(complex(0,1)*I2d13*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1374 = Coupling(name = 'GC_1374',
                   value = '-(complex(0,1)*I2d13*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1375 = Coupling(name = 'GC_1375',
                   value = '(complex(0,1)*I2d21*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1376 = Coupling(name = 'GC_1376',
                   value = '-(complex(0,1)*I2d21*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1377 = Coupling(name = 'GC_1377',
                   value = '(complex(0,1)*I2d22*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1378 = Coupling(name = 'GC_1378',
                   value = '-(complex(0,1)*I2d22*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1379 = Coupling(name = 'GC_1379',
                   value = '(complex(0,1)*I2d23*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1380 = Coupling(name = 'GC_1380',
                   value = '-(complex(0,1)*I2d23*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1381 = Coupling(name = 'GC_1381',
                   value = '(complex(0,1)*I2d31*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1382 = Coupling(name = 'GC_1382',
                   value = '-(complex(0,1)*I2d31*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1383 = Coupling(name = 'GC_1383',
                   value = '(complex(0,1)*I2d32*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1384 = Coupling(name = 'GC_1384',
                   value = '-(complex(0,1)*I2d32*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1385 = Coupling(name = 'GC_1385',
                   value = '(complex(0,1)*I2d33*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1386 = Coupling(name = 'GC_1386',
                   value = '-(complex(0,1)*I2d33*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1387 = Coupling(name = 'GC_1387',
                   value = '-(complex(0,1)*yc*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1388 = Coupling(name = 'GC_1388',
                   value = '(complex(0,1)*yc*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1389 = Coupling(name = 'GC_1389',
                   value = '(complex(0,1)*I2d11*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1390 = Coupling(name = 'GC_1390',
                   value = '-(complex(0,1)*I2d11*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1391 = Coupling(name = 'GC_1391',
                   value = '(complex(0,1)*I2d12*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1392 = Coupling(name = 'GC_1392',
                   value = '-(complex(0,1)*I2d12*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1393 = Coupling(name = 'GC_1393',
                   value = '(complex(0,1)*I2d13*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1394 = Coupling(name = 'GC_1394',
                   value = '-(complex(0,1)*I2d13*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1395 = Coupling(name = 'GC_1395',
                   value = '(complex(0,1)*I2d21*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1396 = Coupling(name = 'GC_1396',
                   value = '-(complex(0,1)*I2d21*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1397 = Coupling(name = 'GC_1397',
                   value = '(complex(0,1)*I2d22*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1398 = Coupling(name = 'GC_1398',
                   value = '-(complex(0,1)*I2d22*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1399 = Coupling(name = 'GC_1399',
                   value = '(complex(0,1)*I2d23*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1400 = Coupling(name = 'GC_1400',
                   value = '-(complex(0,1)*I2d23*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1401 = Coupling(name = 'GC_1401',
                   value = '(complex(0,1)*I2d31*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1402 = Coupling(name = 'GC_1402',
                   value = '-(complex(0,1)*I2d31*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1403 = Coupling(name = 'GC_1403',
                   value = '(complex(0,1)*I2d32*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1404 = Coupling(name = 'GC_1404',
                   value = '-(complex(0,1)*I2d32*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1405 = Coupling(name = 'GC_1405',
                   value = '(complex(0,1)*I2d33*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1406 = Coupling(name = 'GC_1406',
                   value = '-(complex(0,1)*I2d33*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1407 = Coupling(name = 'GC_1407',
                   value = '-(complex(0,1)*yc*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1408 = Coupling(name = 'GC_1408',
                   value = '(complex(0,1)*yc*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1409 = Coupling(name = 'GC_1409',
                   value = '-(complex(0,1)*ye*yt*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1410 = Coupling(name = 'GC_1410',
                   value = '(complex(0,1)*ye*yt*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1411 = Coupling(name = 'GC_1411',
                   value = '-(complex(0,1)*ym*yt*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1412 = Coupling(name = 'GC_1412',
                   value = '(complex(0,1)*ym*yt*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1413 = Coupling(name = 'GC_1413',
                   value = '(complex(0,1)*I2d11*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1414 = Coupling(name = 'GC_1414',
                   value = '-(complex(0,1)*I2d11*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1415 = Coupling(name = 'GC_1415',
                   value = '(complex(0,1)*I2d12*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1416 = Coupling(name = 'GC_1416',
                   value = '-(complex(0,1)*I2d12*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1417 = Coupling(name = 'GC_1417',
                   value = '(complex(0,1)*I2d13*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1418 = Coupling(name = 'GC_1418',
                   value = '-(complex(0,1)*I2d13*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1419 = Coupling(name = 'GC_1419',
                   value = '(complex(0,1)*I2d21*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1420 = Coupling(name = 'GC_1420',
                   value = '-(complex(0,1)*I2d21*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1421 = Coupling(name = 'GC_1421',
                   value = '(complex(0,1)*I2d22*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1422 = Coupling(name = 'GC_1422',
                   value = '-(complex(0,1)*I2d22*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1423 = Coupling(name = 'GC_1423',
                   value = '(complex(0,1)*I2d23*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1424 = Coupling(name = 'GC_1424',
                   value = '-(complex(0,1)*I2d23*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1425 = Coupling(name = 'GC_1425',
                   value = '(complex(0,1)*I2d31*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1426 = Coupling(name = 'GC_1426',
                   value = '-(complex(0,1)*I2d31*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1427 = Coupling(name = 'GC_1427',
                   value = '(complex(0,1)*I2d32*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1428 = Coupling(name = 'GC_1428',
                   value = '-(complex(0,1)*I2d32*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1429 = Coupling(name = 'GC_1429',
                   value = '(complex(0,1)*I2d33*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1430 = Coupling(name = 'GC_1430',
                   value = '-(complex(0,1)*I2d33*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1431 = Coupling(name = 'GC_1431',
                   value = '-(complex(0,1)*yc*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1432 = Coupling(name = 'GC_1432',
                   value = '(complex(0,1)*yc*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1433 = Coupling(name = 'GC_1433',
                   value = '-(complex(0,1)*yt*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1434 = Coupling(name = 'GC_1434',
                   value = '(complex(0,1)*yt*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1435 = Coupling(name = 'GC_1435',
                   value = '-(complex(0,1)*ye*yup*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1436 = Coupling(name = 'GC_1436',
                   value = '(complex(0,1)*ye*yup*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1437 = Coupling(name = 'GC_1437',
                   value = '-(complex(0,1)*ym*yup*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1438 = Coupling(name = 'GC_1438',
                   value = '(complex(0,1)*ym*yup*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1439 = Coupling(name = 'GC_1439',
                   value = '-(complex(0,1)*ytau*yup*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1440 = Coupling(name = 'GC_1440',
                   value = '(complex(0,1)*ytau*yup*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                   order = {'NP':1,'NPclequ3':1,'QED':4})

GC_1441 = Coupling(name = 'GC_1441',
                   value = '-((complex(0,1)*I2d11*I5d11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1442 = Coupling(name = 'GC_1442',
                   value = '-((complex(0,1)*I2d12*I5d11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1443 = Coupling(name = 'GC_1443',
                   value = '-((complex(0,1)*I2d13*I5d11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1444 = Coupling(name = 'GC_1444',
                   value = '-((complex(0,1)*I2d21*I5d11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1445 = Coupling(name = 'GC_1445',
                   value = '-((complex(0,1)*I2d22*I5d11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1446 = Coupling(name = 'GC_1446',
                   value = '-((complex(0,1)*I2d23*I5d11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1447 = Coupling(name = 'GC_1447',
                   value = '-((complex(0,1)*I2d31*I5d11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1448 = Coupling(name = 'GC_1448',
                   value = '-((complex(0,1)*I2d32*I5d11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1449 = Coupling(name = 'GC_1449',
                   value = '-((complex(0,1)*I2d33*I5d11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1450 = Coupling(name = 'GC_1450',
                   value = '-((complex(0,1)*I2d11*I5d12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1451 = Coupling(name = 'GC_1451',
                   value = '-((complex(0,1)*I2d12*I5d12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1452 = Coupling(name = 'GC_1452',
                   value = '-((complex(0,1)*I2d13*I5d12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1453 = Coupling(name = 'GC_1453',
                   value = '-((complex(0,1)*I2d21*I5d12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1454 = Coupling(name = 'GC_1454',
                   value = '-((complex(0,1)*I2d22*I5d12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1455 = Coupling(name = 'GC_1455',
                   value = '-((complex(0,1)*I2d23*I5d12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1456 = Coupling(name = 'GC_1456',
                   value = '-((complex(0,1)*I2d31*I5d12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1457 = Coupling(name = 'GC_1457',
                   value = '-((complex(0,1)*I2d32*I5d12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1458 = Coupling(name = 'GC_1458',
                   value = '-((complex(0,1)*I2d33*I5d12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1459 = Coupling(name = 'GC_1459',
                   value = '-((complex(0,1)*I2d11*I5d13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1460 = Coupling(name = 'GC_1460',
                   value = '-((complex(0,1)*I2d12*I5d13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1461 = Coupling(name = 'GC_1461',
                   value = '-((complex(0,1)*I2d13*I5d13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1462 = Coupling(name = 'GC_1462',
                   value = '-((complex(0,1)*I2d21*I5d13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1463 = Coupling(name = 'GC_1463',
                   value = '-((complex(0,1)*I2d22*I5d13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1464 = Coupling(name = 'GC_1464',
                   value = '-((complex(0,1)*I2d23*I5d13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1465 = Coupling(name = 'GC_1465',
                   value = '-((complex(0,1)*I2d31*I5d13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1466 = Coupling(name = 'GC_1466',
                   value = '-((complex(0,1)*I2d32*I5d13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1467 = Coupling(name = 'GC_1467',
                   value = '-((complex(0,1)*I2d33*I5d13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1468 = Coupling(name = 'GC_1468',
                   value = '-((complex(0,1)*I2d11*I5d21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1469 = Coupling(name = 'GC_1469',
                   value = '-((complex(0,1)*I2d12*I5d21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1470 = Coupling(name = 'GC_1470',
                   value = '-((complex(0,1)*I2d13*I5d21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1471 = Coupling(name = 'GC_1471',
                   value = '-((complex(0,1)*I2d21*I5d21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1472 = Coupling(name = 'GC_1472',
                   value = '-((complex(0,1)*I2d22*I5d21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1473 = Coupling(name = 'GC_1473',
                   value = '-((complex(0,1)*I2d23*I5d21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1474 = Coupling(name = 'GC_1474',
                   value = '-((complex(0,1)*I2d31*I5d21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1475 = Coupling(name = 'GC_1475',
                   value = '-((complex(0,1)*I2d32*I5d21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1476 = Coupling(name = 'GC_1476',
                   value = '-((complex(0,1)*I2d33*I5d21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1477 = Coupling(name = 'GC_1477',
                   value = '-((complex(0,1)*I2d11*I5d22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1478 = Coupling(name = 'GC_1478',
                   value = '-((complex(0,1)*I2d12*I5d22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1479 = Coupling(name = 'GC_1479',
                   value = '-((complex(0,1)*I2d13*I5d22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1480 = Coupling(name = 'GC_1480',
                   value = '-((complex(0,1)*I2d21*I5d22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1481 = Coupling(name = 'GC_1481',
                   value = '-((complex(0,1)*I2d22*I5d22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1482 = Coupling(name = 'GC_1482',
                   value = '-((complex(0,1)*I2d23*I5d22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1483 = Coupling(name = 'GC_1483',
                   value = '-((complex(0,1)*I2d31*I5d22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1484 = Coupling(name = 'GC_1484',
                   value = '-((complex(0,1)*I2d32*I5d22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1485 = Coupling(name = 'GC_1485',
                   value = '-((complex(0,1)*I2d33*I5d22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1486 = Coupling(name = 'GC_1486',
                   value = '-((complex(0,1)*I2d11*I5d23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1487 = Coupling(name = 'GC_1487',
                   value = '-((complex(0,1)*I2d12*I5d23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1488 = Coupling(name = 'GC_1488',
                   value = '-((complex(0,1)*I2d13*I5d23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1489 = Coupling(name = 'GC_1489',
                   value = '-((complex(0,1)*I2d21*I5d23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1490 = Coupling(name = 'GC_1490',
                   value = '-((complex(0,1)*I2d22*I5d23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1491 = Coupling(name = 'GC_1491',
                   value = '-((complex(0,1)*I2d23*I5d23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1492 = Coupling(name = 'GC_1492',
                   value = '-((complex(0,1)*I2d31*I5d23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1493 = Coupling(name = 'GC_1493',
                   value = '-((complex(0,1)*I2d32*I5d23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1494 = Coupling(name = 'GC_1494',
                   value = '-((complex(0,1)*I2d33*I5d23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1495 = Coupling(name = 'GC_1495',
                   value = '-((complex(0,1)*I2d11*I5d31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1496 = Coupling(name = 'GC_1496',
                   value = '-((complex(0,1)*I2d12*I5d31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1497 = Coupling(name = 'GC_1497',
                   value = '-((complex(0,1)*I2d13*I5d31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1498 = Coupling(name = 'GC_1498',
                   value = '-((complex(0,1)*I2d21*I5d31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1499 = Coupling(name = 'GC_1499',
                   value = '-((complex(0,1)*I2d22*I5d31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1500 = Coupling(name = 'GC_1500',
                   value = '-((complex(0,1)*I2d23*I5d31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1501 = Coupling(name = 'GC_1501',
                   value = '-((complex(0,1)*I2d31*I5d31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1502 = Coupling(name = 'GC_1502',
                   value = '-((complex(0,1)*I2d32*I5d31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1503 = Coupling(name = 'GC_1503',
                   value = '-((complex(0,1)*I2d33*I5d31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1504 = Coupling(name = 'GC_1504',
                   value = '-((complex(0,1)*I2d11*I5d32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1505 = Coupling(name = 'GC_1505',
                   value = '-((complex(0,1)*I2d12*I5d32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1506 = Coupling(name = 'GC_1506',
                   value = '-((complex(0,1)*I2d13*I5d32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1507 = Coupling(name = 'GC_1507',
                   value = '-((complex(0,1)*I2d21*I5d32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1508 = Coupling(name = 'GC_1508',
                   value = '-((complex(0,1)*I2d22*I5d32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1509 = Coupling(name = 'GC_1509',
                   value = '-((complex(0,1)*I2d23*I5d32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1510 = Coupling(name = 'GC_1510',
                   value = '-((complex(0,1)*I2d31*I5d32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1511 = Coupling(name = 'GC_1511',
                   value = '-((complex(0,1)*I2d32*I5d32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1512 = Coupling(name = 'GC_1512',
                   value = '-((complex(0,1)*I2d33*I5d32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1513 = Coupling(name = 'GC_1513',
                   value = '-((complex(0,1)*I2d11*I5d33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1514 = Coupling(name = 'GC_1514',
                   value = '-((complex(0,1)*I2d12*I5d33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1515 = Coupling(name = 'GC_1515',
                   value = '-((complex(0,1)*I2d13*I5d33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1516 = Coupling(name = 'GC_1516',
                   value = '-((complex(0,1)*I2d21*I5d33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1517 = Coupling(name = 'GC_1517',
                   value = '-((complex(0,1)*I2d22*I5d33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1518 = Coupling(name = 'GC_1518',
                   value = '-((complex(0,1)*I2d23*I5d33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1519 = Coupling(name = 'GC_1519',
                   value = '-((complex(0,1)*I2d31*I5d33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1520 = Coupling(name = 'GC_1520',
                   value = '-((complex(0,1)*I2d32*I5d33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1521 = Coupling(name = 'GC_1521',
                   value = '-((complex(0,1)*I2d33*I5d33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1522 = Coupling(name = 'GC_1522',
                   value = '(complex(0,1)*yb*yc*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1523 = Coupling(name = 'GC_1523',
                   value = '(complex(0,1)*yc*ydo*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1524 = Coupling(name = 'GC_1524',
                   value = '(complex(0,1)*yc*ys*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1525 = Coupling(name = 'GC_1525',
                   value = '(complex(0,1)*yb*yt*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1526 = Coupling(name = 'GC_1526',
                   value = '(complex(0,1)*ydo*yt*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1527 = Coupling(name = 'GC_1527',
                   value = '(complex(0,1)*ys*yt*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1528 = Coupling(name = 'GC_1528',
                   value = '(complex(0,1)*yb*yup*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1529 = Coupling(name = 'GC_1529',
                   value = '(complex(0,1)*ydo*yup*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1530 = Coupling(name = 'GC_1530',
                   value = '(complex(0,1)*ys*yup*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd1':1,'QED':4})

GC_1531 = Coupling(name = 'GC_1531',
                   value = '-((complex(0,1)*I2d11*I5d11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1532 = Coupling(name = 'GC_1532',
                   value = '-((complex(0,1)*I2d12*I5d11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1533 = Coupling(name = 'GC_1533',
                   value = '-((complex(0,1)*I2d13*I5d11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1534 = Coupling(name = 'GC_1534',
                   value = '-((complex(0,1)*I2d21*I5d11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1535 = Coupling(name = 'GC_1535',
                   value = '-((complex(0,1)*I2d22*I5d11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1536 = Coupling(name = 'GC_1536',
                   value = '-((complex(0,1)*I2d23*I5d11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1537 = Coupling(name = 'GC_1537',
                   value = '-((complex(0,1)*I2d31*I5d11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1538 = Coupling(name = 'GC_1538',
                   value = '-((complex(0,1)*I2d32*I5d11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1539 = Coupling(name = 'GC_1539',
                   value = '-((complex(0,1)*I2d33*I5d11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1540 = Coupling(name = 'GC_1540',
                   value = '-((complex(0,1)*I2d11*I5d12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1541 = Coupling(name = 'GC_1541',
                   value = '-((complex(0,1)*I2d12*I5d12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1542 = Coupling(name = 'GC_1542',
                   value = '-((complex(0,1)*I2d13*I5d12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1543 = Coupling(name = 'GC_1543',
                   value = '-((complex(0,1)*I2d21*I5d12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1544 = Coupling(name = 'GC_1544',
                   value = '-((complex(0,1)*I2d22*I5d12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1545 = Coupling(name = 'GC_1545',
                   value = '-((complex(0,1)*I2d23*I5d12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1546 = Coupling(name = 'GC_1546',
                   value = '-((complex(0,1)*I2d31*I5d12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1547 = Coupling(name = 'GC_1547',
                   value = '-((complex(0,1)*I2d32*I5d12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1548 = Coupling(name = 'GC_1548',
                   value = '-((complex(0,1)*I2d33*I5d12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1549 = Coupling(name = 'GC_1549',
                   value = '-((complex(0,1)*I2d11*I5d13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1550 = Coupling(name = 'GC_1550',
                   value = '-((complex(0,1)*I2d12*I5d13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1551 = Coupling(name = 'GC_1551',
                   value = '-((complex(0,1)*I2d13*I5d13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1552 = Coupling(name = 'GC_1552',
                   value = '-((complex(0,1)*I2d21*I5d13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1553 = Coupling(name = 'GC_1553',
                   value = '-((complex(0,1)*I2d22*I5d13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1554 = Coupling(name = 'GC_1554',
                   value = '-((complex(0,1)*I2d23*I5d13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1555 = Coupling(name = 'GC_1555',
                   value = '-((complex(0,1)*I2d31*I5d13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1556 = Coupling(name = 'GC_1556',
                   value = '-((complex(0,1)*I2d32*I5d13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1557 = Coupling(name = 'GC_1557',
                   value = '-((complex(0,1)*I2d33*I5d13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1558 = Coupling(name = 'GC_1558',
                   value = '-((complex(0,1)*I2d11*I5d21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1559 = Coupling(name = 'GC_1559',
                   value = '-((complex(0,1)*I2d12*I5d21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1560 = Coupling(name = 'GC_1560',
                   value = '-((complex(0,1)*I2d13*I5d21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1561 = Coupling(name = 'GC_1561',
                   value = '-((complex(0,1)*I2d21*I5d21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1562 = Coupling(name = 'GC_1562',
                   value = '-((complex(0,1)*I2d22*I5d21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1563 = Coupling(name = 'GC_1563',
                   value = '-((complex(0,1)*I2d23*I5d21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1564 = Coupling(name = 'GC_1564',
                   value = '-((complex(0,1)*I2d31*I5d21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1565 = Coupling(name = 'GC_1565',
                   value = '-((complex(0,1)*I2d32*I5d21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1566 = Coupling(name = 'GC_1566',
                   value = '-((complex(0,1)*I2d33*I5d21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1567 = Coupling(name = 'GC_1567',
                   value = '-((complex(0,1)*I2d11*I5d22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1568 = Coupling(name = 'GC_1568',
                   value = '-((complex(0,1)*I2d12*I5d22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1569 = Coupling(name = 'GC_1569',
                   value = '-((complex(0,1)*I2d13*I5d22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1570 = Coupling(name = 'GC_1570',
                   value = '-((complex(0,1)*I2d21*I5d22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1571 = Coupling(name = 'GC_1571',
                   value = '-((complex(0,1)*I2d22*I5d22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1572 = Coupling(name = 'GC_1572',
                   value = '-((complex(0,1)*I2d23*I5d22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1573 = Coupling(name = 'GC_1573',
                   value = '-((complex(0,1)*I2d31*I5d22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1574 = Coupling(name = 'GC_1574',
                   value = '-((complex(0,1)*I2d32*I5d22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1575 = Coupling(name = 'GC_1575',
                   value = '-((complex(0,1)*I2d33*I5d22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1576 = Coupling(name = 'GC_1576',
                   value = '-((complex(0,1)*I2d11*I5d23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1577 = Coupling(name = 'GC_1577',
                   value = '-((complex(0,1)*I2d12*I5d23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1578 = Coupling(name = 'GC_1578',
                   value = '-((complex(0,1)*I2d13*I5d23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1579 = Coupling(name = 'GC_1579',
                   value = '-((complex(0,1)*I2d21*I5d23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1580 = Coupling(name = 'GC_1580',
                   value = '-((complex(0,1)*I2d22*I5d23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1581 = Coupling(name = 'GC_1581',
                   value = '-((complex(0,1)*I2d23*I5d23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1582 = Coupling(name = 'GC_1582',
                   value = '-((complex(0,1)*I2d31*I5d23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1583 = Coupling(name = 'GC_1583',
                   value = '-((complex(0,1)*I2d32*I5d23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1584 = Coupling(name = 'GC_1584',
                   value = '-((complex(0,1)*I2d33*I5d23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1585 = Coupling(name = 'GC_1585',
                   value = '-((complex(0,1)*I2d11*I5d31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1586 = Coupling(name = 'GC_1586',
                   value = '-((complex(0,1)*I2d12*I5d31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1587 = Coupling(name = 'GC_1587',
                   value = '-((complex(0,1)*I2d13*I5d31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1588 = Coupling(name = 'GC_1588',
                   value = '-((complex(0,1)*I2d21*I5d31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1589 = Coupling(name = 'GC_1589',
                   value = '-((complex(0,1)*I2d22*I5d31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1590 = Coupling(name = 'GC_1590',
                   value = '-((complex(0,1)*I2d23*I5d31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1591 = Coupling(name = 'GC_1591',
                   value = '-((complex(0,1)*I2d31*I5d31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1592 = Coupling(name = 'GC_1592',
                   value = '-((complex(0,1)*I2d32*I5d31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1593 = Coupling(name = 'GC_1593',
                   value = '-((complex(0,1)*I2d33*I5d31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1594 = Coupling(name = 'GC_1594',
                   value = '-((complex(0,1)*I2d11*I5d32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1595 = Coupling(name = 'GC_1595',
                   value = '-((complex(0,1)*I2d12*I5d32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1596 = Coupling(name = 'GC_1596',
                   value = '-((complex(0,1)*I2d13*I5d32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1597 = Coupling(name = 'GC_1597',
                   value = '-((complex(0,1)*I2d21*I5d32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1598 = Coupling(name = 'GC_1598',
                   value = '-((complex(0,1)*I2d22*I5d32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1599 = Coupling(name = 'GC_1599',
                   value = '-((complex(0,1)*I2d23*I5d32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1600 = Coupling(name = 'GC_1600',
                   value = '-((complex(0,1)*I2d31*I5d32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1601 = Coupling(name = 'GC_1601',
                   value = '-((complex(0,1)*I2d32*I5d32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1602 = Coupling(name = 'GC_1602',
                   value = '-((complex(0,1)*I2d33*I5d32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1603 = Coupling(name = 'GC_1603',
                   value = '-((complex(0,1)*I2d11*I5d33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1604 = Coupling(name = 'GC_1604',
                   value = '-((complex(0,1)*I2d12*I5d33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1605 = Coupling(name = 'GC_1605',
                   value = '-((complex(0,1)*I2d13*I5d33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1606 = Coupling(name = 'GC_1606',
                   value = '-((complex(0,1)*I2d21*I5d33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1607 = Coupling(name = 'GC_1607',
                   value = '-((complex(0,1)*I2d22*I5d33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1608 = Coupling(name = 'GC_1608',
                   value = '-((complex(0,1)*I2d23*I5d33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1609 = Coupling(name = 'GC_1609',
                   value = '-((complex(0,1)*I2d31*I5d33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1610 = Coupling(name = 'GC_1610',
                   value = '-((complex(0,1)*I2d32*I5d33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1611 = Coupling(name = 'GC_1611',
                   value = '-((complex(0,1)*I2d33*I5d33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1612 = Coupling(name = 'GC_1612',
                   value = '(complex(0,1)*yb*yc*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1613 = Coupling(name = 'GC_1613',
                   value = '(complex(0,1)*yc*ydo*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1614 = Coupling(name = 'GC_1614',
                   value = '(complex(0,1)*yc*ys*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1615 = Coupling(name = 'GC_1615',
                   value = '(complex(0,1)*yb*yt*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1616 = Coupling(name = 'GC_1616',
                   value = '(complex(0,1)*ydo*yt*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1617 = Coupling(name = 'GC_1617',
                   value = '(complex(0,1)*ys*yt*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1618 = Coupling(name = 'GC_1618',
                   value = '(complex(0,1)*yb*yup*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1619 = Coupling(name = 'GC_1619',
                   value = '(complex(0,1)*ydo*yup*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1620 = Coupling(name = 'GC_1620',
                   value = '(complex(0,1)*ys*yup*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcquqd8':1,'QED':4})

GC_1621 = Coupling(name = 'GC_1621',
                   value = '(cth*complex(0,1)*yc*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1622 = Coupling(name = 'GC_1622',
                   value = '-((complex(0,1)*sth*yc*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1623 = Coupling(name = 'GC_1623',
                   value = '(cth*complex(0,1)*vevhat*yc*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1624 = Coupling(name = 'GC_1624',
                   value = '-((complex(0,1)*sth*vevhat*yc*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1625 = Coupling(name = 'GC_1625',
                   value = '(cth*complex(0,1)*yt*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1626 = Coupling(name = 'GC_1626',
                   value = '-((complex(0,1)*sth*yt*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1627 = Coupling(name = 'GC_1627',
                   value = '(cth*complex(0,1)*vevhat*yt*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1628 = Coupling(name = 'GC_1628',
                   value = '-((complex(0,1)*sth*vevhat*yt*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1629 = Coupling(name = 'GC_1629',
                   value = '(cth*complex(0,1)*yup*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1630 = Coupling(name = 'GC_1630',
                   value = '-((complex(0,1)*sth*yup*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':3})

GC_1631 = Coupling(name = 'GC_1631',
                   value = '(cth*complex(0,1)*vevhat*yup*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1632 = Coupling(name = 'GC_1632',
                   value = '-((complex(0,1)*sth*vevhat*yup*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuB':1,'QED':2})

GC_1633 = Coupling(name = 'GC_1633',
                   value = '(complex(0,1)*yc*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':3})

GC_1634 = Coupling(name = 'GC_1634',
                   value = '(G*yc*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_1635 = Coupling(name = 'GC_1635',
                   value = '(complex(0,1)*vevhat*yc*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':2})

GC_1636 = Coupling(name = 'GC_1636',
                   value = '(G*vevhat*yc*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_1637 = Coupling(name = 'GC_1637',
                   value = '(complex(0,1)*yt*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':3})

GC_1638 = Coupling(name = 'GC_1638',
                   value = '(G*yt*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_1639 = Coupling(name = 'GC_1639',
                   value = '(complex(0,1)*vevhat*yt*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':2})

GC_1640 = Coupling(name = 'GC_1640',
                   value = '(G*vevhat*yt*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_1641 = Coupling(name = 'GC_1641',
                   value = '(complex(0,1)*yup*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':3})

GC_1642 = Coupling(name = 'GC_1642',
                   value = '(G*yup*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':3})

GC_1643 = Coupling(name = 'GC_1643',
                   value = '(complex(0,1)*vevhat*yup*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QED':2})

GC_1644 = Coupling(name = 'GC_1644',
                   value = '(G*vevhat*yup*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuG':1,'QCD':1,'QED':2})

GC_1645 = Coupling(name = 'GC_1645',
                   value = '(3*complex(0,1)*yc*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':3})

GC_1646 = Coupling(name = 'GC_1646',
                   value = '(3*complex(0,1)*vevhat*yc*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':2})

GC_1647 = Coupling(name = 'GC_1647',
                   value = '(complex(0,1)*vevhat**2*yc*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':1})

GC_1648 = Coupling(name = 'GC_1648',
                   value = '(3*complex(0,1)*yt*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':3})

GC_1649 = Coupling(name = 'GC_1649',
                   value = '(3*complex(0,1)*vevhat*yt*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':2})

GC_1650 = Coupling(name = 'GC_1650',
                   value = '(complex(0,1)*vevhat**2*yt*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':1})

GC_1651 = Coupling(name = 'GC_1651',
                   value = '(3*complex(0,1)*yup*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':3})

GC_1652 = Coupling(name = 'GC_1652',
                   value = '(3*complex(0,1)*vevhat*yup*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':2})

GC_1653 = Coupling(name = 'GC_1653',
                   value = '(complex(0,1)*vevhat**2*yup*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuH':1,'QED':1})

GC_1654 = Coupling(name = 'GC_1654',
                   value = '(complex(0,1)*yc*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1655 = Coupling(name = 'GC_1655',
                   value = '(cth*complex(0,1)*yc*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1656 = Coupling(name = 'GC_1656',
                   value = '-((ee*complex(0,1)*yc*complexconjugate(cuW))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1657 = Coupling(name = 'GC_1657',
                   value = '-((ee*complex(0,1)*yc*complexconjugate(cuW))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1658 = Coupling(name = 'GC_1658',
                   value = '(cth*ee*complex(0,1)*yc*complexconjugate(cuW))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1659 = Coupling(name = 'GC_1659',
                   value = '(complex(0,1)*sth*yc*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1660 = Coupling(name = 'GC_1660',
                   value = '(complex(0,1)*vevhat*yc*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1661 = Coupling(name = 'GC_1661',
                   value = '(cth*complex(0,1)*vevhat*yc*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1662 = Coupling(name = 'GC_1662',
                   value = '-((ee*complex(0,1)*vevhat*yc*complexconjugate(cuW))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1663 = Coupling(name = 'GC_1663',
                   value = '-((ee*complex(0,1)*vevhat*yc*complexconjugate(cuW))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1664 = Coupling(name = 'GC_1664',
                   value = '(cth*ee*complex(0,1)*vevhat*yc*complexconjugate(cuW))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1665 = Coupling(name = 'GC_1665',
                   value = '(complex(0,1)*sth*vevhat*yc*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1666 = Coupling(name = 'GC_1666',
                   value = '(complex(0,1)*yt*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1667 = Coupling(name = 'GC_1667',
                   value = '(cth*complex(0,1)*yt*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1668 = Coupling(name = 'GC_1668',
                   value = '-((ee*complex(0,1)*yt*complexconjugate(cuW))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1669 = Coupling(name = 'GC_1669',
                   value = '-((ee*complex(0,1)*yt*complexconjugate(cuW))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1670 = Coupling(name = 'GC_1670',
                   value = '(cth*ee*complex(0,1)*yt*complexconjugate(cuW))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1671 = Coupling(name = 'GC_1671',
                   value = '(complex(0,1)*sth*yt*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1672 = Coupling(name = 'GC_1672',
                   value = '(complex(0,1)*vevhat*yt*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1673 = Coupling(name = 'GC_1673',
                   value = '(cth*complex(0,1)*vevhat*yt*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1674 = Coupling(name = 'GC_1674',
                   value = '-((ee*complex(0,1)*vevhat*yt*complexconjugate(cuW))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1675 = Coupling(name = 'GC_1675',
                   value = '-((ee*complex(0,1)*vevhat*yt*complexconjugate(cuW))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1676 = Coupling(name = 'GC_1676',
                   value = '(cth*ee*complex(0,1)*vevhat*yt*complexconjugate(cuW))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1677 = Coupling(name = 'GC_1677',
                   value = '(complex(0,1)*sth*vevhat*yt*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1678 = Coupling(name = 'GC_1678',
                   value = '(complex(0,1)*yup*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1679 = Coupling(name = 'GC_1679',
                   value = '(cth*complex(0,1)*yup*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1680 = Coupling(name = 'GC_1680',
                   value = '-((ee*complex(0,1)*yup*complexconjugate(cuW))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1681 = Coupling(name = 'GC_1681',
                   value = '-((ee*complex(0,1)*yup*complexconjugate(cuW))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1682 = Coupling(name = 'GC_1682',
                   value = '(cth*ee*complex(0,1)*yup*complexconjugate(cuW))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':4})

GC_1683 = Coupling(name = 'GC_1683',
                   value = '(complex(0,1)*sth*yup*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1684 = Coupling(name = 'GC_1684',
                   value = '(complex(0,1)*vevhat*yup*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1685 = Coupling(name = 'GC_1685',
                   value = '(cth*complex(0,1)*vevhat*yup*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

GC_1686 = Coupling(name = 'GC_1686',
                   value = '-((ee*complex(0,1)*vevhat*yup*complexconjugate(cuW))/LambdaSMEFT**2)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1687 = Coupling(name = 'GC_1687',
                   value = '-((ee*complex(0,1)*vevhat*yup*complexconjugate(cuW))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1688 = Coupling(name = 'GC_1688',
                   value = '(cth*ee*complex(0,1)*vevhat*yup*complexconjugate(cuW))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'NPcuW':1,'QED':3})

GC_1689 = Coupling(name = 'GC_1689',
                   value = '(complex(0,1)*sth*vevhat*yup*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'NPcuW':1,'QED':2})

