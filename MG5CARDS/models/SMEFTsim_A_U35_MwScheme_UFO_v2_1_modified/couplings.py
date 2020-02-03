# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Fri 9 Mar 2018 13:38:22


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
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-(complex(0,1)*G)',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-6*complex(0,1)*lam',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '(2*cdd*complex(0,1))/LambdaSMEFT**2 + (2*cdd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '(2*cll*complex(0,1))/LambdaSMEFT**2 + (2*cll1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '(clq1*complex(0,1))/LambdaSMEFT**2 - (clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '(clq1*complex(0,1))/LambdaSMEFT**2 + (clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '(2*cqq1*complex(0,1))/LambdaSMEFT**2 - (2*cqq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '(2*cqq1*complex(0,1))/LambdaSMEFT**2 + (2*cqq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '(2*cqq11*complex(0,1))/LambdaSMEFT**2 - (2*cqq31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '(2*cqq1*complex(0,1))/LambdaSMEFT**2 + (2*cqq11*complex(0,1))/LambdaSMEFT**2 - (2*cqq3*complex(0,1))/LambdaSMEFT**2 - (2*cqq31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '(2*cqq11*complex(0,1))/LambdaSMEFT**2 + (2*cqq31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '(2*cqq1*complex(0,1))/LambdaSMEFT**2 + (2*cqq11*complex(0,1))/LambdaSMEFT**2 + (2*cqq3*complex(0,1))/LambdaSMEFT**2 + (2*cqq31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '(4*cqq3*complex(0,1))/LambdaSMEFT**2 + (4*cqq31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_21 = Coupling(name = 'GC_21',
                 value = '(2*cuu*complex(0,1))/LambdaSMEFT**2 + (2*cuu1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '(2*cdd*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '(2*cdd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(ced*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_25 = Coupling(name = 'GC_25',
                 value = '(2*cee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_26 = Coupling(name = 'GC_26',
                 value = '(ceu*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = '(-6*cG)/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = 'cGtil/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(-3*cHbox*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((cHDD*complex(0,1))/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '(4*cHG*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(-2*cHGtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_33 = Coupling(name = 'GC_33',
                 value = '(4*cHW*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_34 = Coupling(name = 'GC_34',
                 value = '(4*cHWtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cld*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(cle*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_37 = Coupling(name = 'GC_37',
                 value = '(2*cll*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '(2*cll1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(2*clq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(clu*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(cqd1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(cqd8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_43 = Coupling(name = 'GC_43',
                 value = '(cqe*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_44 = Coupling(name = 'GC_44',
                 value = '(4*cqq3*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(4*cqq31*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(cqu1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_47 = Coupling(name = 'GC_47',
                 value = '(cqu8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cud1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cud8*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_50 = Coupling(name = 'GC_50',
                 value = '(2*cuu*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_51 = Coupling(name = 'GC_51',
                 value = '(2*cuu1*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_52 = Coupling(name = 'GC_52',
                 value = '(6*cth*cW*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_53 = Coupling(name = 'GC_53',
                 value = '(2*cth*cWtil*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':2})

GC_54 = Coupling(name = 'GC_54',
                 value = '(6*cth*cW*ee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':3})

GC_55 = Coupling(name = 'GC_55',
                 value = '(-2*cth*cWtil*ee*complex(0,1))/LambdaSMEFT**2',
                 order = {'NP':1,'QED':3})

GC_56 = Coupling(name = 'GC_56',
                 value = '(-6*cG*complex(0,1)*G)/LambdaSMEFT**2',
                 order = {'NP':1,'QCD':1,'QED':2})

GC_57 = Coupling(name = 'GC_57',
                 value = '(cGtil*complex(0,1)*G)/LambdaSMEFT**2',
                 order = {'NP':1,'QCD':1,'QED':2})

GC_58 = Coupling(name = 'GC_58',
                 value = '-((cquqd1*complex(0,1)*I1b11*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_59 = Coupling(name = 'GC_59',
                 value = '-((cquqd8*complex(0,1)*I1b11*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_60 = Coupling(name = 'GC_60',
                 value = '-((cquqd1*complex(0,1)*I1b12*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((cquqd8*complex(0,1)*I1b12*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((cquqd1*complex(0,1)*I1b13*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((cquqd8*complex(0,1)*I1b13*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_64 = Coupling(name = 'GC_64',
                 value = '-((cquqd1*complex(0,1)*I1b21*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_65 = Coupling(name = 'GC_65',
                 value = '-((cquqd8*complex(0,1)*I1b21*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((cquqd1*complex(0,1)*I1b22*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_67 = Coupling(name = 'GC_67',
                 value = '-((cquqd8*complex(0,1)*I1b22*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_68 = Coupling(name = 'GC_68',
                 value = '-((cquqd1*complex(0,1)*I1b23*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((cquqd8*complex(0,1)*I1b23*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_70 = Coupling(name = 'GC_70',
                 value = '-((cquqd1*complex(0,1)*I1b31*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((cquqd8*complex(0,1)*I1b31*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_72 = Coupling(name = 'GC_72',
                 value = '-((cquqd1*complex(0,1)*I1b32*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_73 = Coupling(name = 'GC_73',
                 value = '-((cquqd8*complex(0,1)*I1b32*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_74 = Coupling(name = 'GC_74',
                 value = '-((cquqd1*complex(0,1)*I1b33*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((cquqd8*complex(0,1)*I1b33*I6b11)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_76 = Coupling(name = 'GC_76',
                 value = '-((cquqd1*complex(0,1)*I1b11*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((cquqd8*complex(0,1)*I1b11*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((cquqd1*complex(0,1)*I1b12*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((cquqd8*complex(0,1)*I1b12*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_80 = Coupling(name = 'GC_80',
                 value = '-((cquqd1*complex(0,1)*I1b13*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((cquqd8*complex(0,1)*I1b13*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((cquqd1*complex(0,1)*I1b21*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((cquqd8*complex(0,1)*I1b21*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_84 = Coupling(name = 'GC_84',
                 value = '-((cquqd1*complex(0,1)*I1b22*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_85 = Coupling(name = 'GC_85',
                 value = '-((cquqd8*complex(0,1)*I1b22*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_86 = Coupling(name = 'GC_86',
                 value = '-((cquqd1*complex(0,1)*I1b23*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_87 = Coupling(name = 'GC_87',
                 value = '-((cquqd8*complex(0,1)*I1b23*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_88 = Coupling(name = 'GC_88',
                 value = '-((cquqd1*complex(0,1)*I1b31*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((cquqd8*complex(0,1)*I1b31*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_90 = Coupling(name = 'GC_90',
                 value = '-((cquqd1*complex(0,1)*I1b32*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((cquqd8*complex(0,1)*I1b32*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_92 = Coupling(name = 'GC_92',
                 value = '-((cquqd1*complex(0,1)*I1b33*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((cquqd8*complex(0,1)*I1b33*I6b12)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_94 = Coupling(name = 'GC_94',
                 value = '-((cquqd1*complex(0,1)*I1b11*I6b13)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_95 = Coupling(name = 'GC_95',
                 value = '-((cquqd8*complex(0,1)*I1b11*I6b13)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_96 = Coupling(name = 'GC_96',
                 value = '-((cquqd1*complex(0,1)*I1b12*I6b13)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((cquqd8*complex(0,1)*I1b12*I6b13)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_98 = Coupling(name = 'GC_98',
                 value = '-((cquqd1*complex(0,1)*I1b13*I6b13)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((cquqd8*complex(0,1)*I1b13*I6b13)/LambdaSMEFT**2)',
                 order = {'NP':1,'QED':4})

GC_100 = Coupling(name = 'GC_100',
                  value = '-((cquqd1*complex(0,1)*I1b21*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((cquqd8*complex(0,1)*I1b21*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((cquqd1*complex(0,1)*I1b22*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((cquqd8*complex(0,1)*I1b22*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_104 = Coupling(name = 'GC_104',
                  value = '-((cquqd1*complex(0,1)*I1b23*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((cquqd8*complex(0,1)*I1b23*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_106 = Coupling(name = 'GC_106',
                  value = '-((cquqd1*complex(0,1)*I1b31*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_107 = Coupling(name = 'GC_107',
                  value = '-((cquqd8*complex(0,1)*I1b31*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_108 = Coupling(name = 'GC_108',
                  value = '-((cquqd1*complex(0,1)*I1b32*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((cquqd8*complex(0,1)*I1b32*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((cquqd1*complex(0,1)*I1b33*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_111 = Coupling(name = 'GC_111',
                  value = '-((cquqd8*complex(0,1)*I1b33*I6b13)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_112 = Coupling(name = 'GC_112',
                  value = '-((cquqd1*complex(0,1)*I1b11*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_113 = Coupling(name = 'GC_113',
                  value = '-((cquqd8*complex(0,1)*I1b11*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((cquqd1*complex(0,1)*I1b12*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((cquqd8*complex(0,1)*I1b12*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((cquqd1*complex(0,1)*I1b13*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_117 = Coupling(name = 'GC_117',
                  value = '-((cquqd8*complex(0,1)*I1b13*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((cquqd1*complex(0,1)*I1b21*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_119 = Coupling(name = 'GC_119',
                  value = '-((cquqd8*complex(0,1)*I1b21*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_120 = Coupling(name = 'GC_120',
                  value = '-((cquqd1*complex(0,1)*I1b22*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_121 = Coupling(name = 'GC_121',
                  value = '-((cquqd8*complex(0,1)*I1b22*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_122 = Coupling(name = 'GC_122',
                  value = '-((cquqd1*complex(0,1)*I1b23*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_123 = Coupling(name = 'GC_123',
                  value = '-((cquqd8*complex(0,1)*I1b23*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((cquqd1*complex(0,1)*I1b31*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_125 = Coupling(name = 'GC_125',
                  value = '-((cquqd8*complex(0,1)*I1b31*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_126 = Coupling(name = 'GC_126',
                  value = '-((cquqd1*complex(0,1)*I1b32*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_127 = Coupling(name = 'GC_127',
                  value = '-((cquqd8*complex(0,1)*I1b32*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_128 = Coupling(name = 'GC_128',
                  value = '-((cquqd1*complex(0,1)*I1b33*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_129 = Coupling(name = 'GC_129',
                  value = '-((cquqd8*complex(0,1)*I1b33*I6b21)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_130 = Coupling(name = 'GC_130',
                  value = '-((cquqd1*complex(0,1)*I1b11*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_131 = Coupling(name = 'GC_131',
                  value = '-((cquqd8*complex(0,1)*I1b11*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_132 = Coupling(name = 'GC_132',
                  value = '-((cquqd1*complex(0,1)*I1b12*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_133 = Coupling(name = 'GC_133',
                  value = '-((cquqd8*complex(0,1)*I1b12*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_134 = Coupling(name = 'GC_134',
                  value = '-((cquqd1*complex(0,1)*I1b13*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_135 = Coupling(name = 'GC_135',
                  value = '-((cquqd8*complex(0,1)*I1b13*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_136 = Coupling(name = 'GC_136',
                  value = '-((cquqd1*complex(0,1)*I1b21*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_137 = Coupling(name = 'GC_137',
                  value = '-((cquqd8*complex(0,1)*I1b21*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_138 = Coupling(name = 'GC_138',
                  value = '-((cquqd1*complex(0,1)*I1b22*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_139 = Coupling(name = 'GC_139',
                  value = '-((cquqd8*complex(0,1)*I1b22*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_140 = Coupling(name = 'GC_140',
                  value = '-((cquqd1*complex(0,1)*I1b23*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_141 = Coupling(name = 'GC_141',
                  value = '-((cquqd8*complex(0,1)*I1b23*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_142 = Coupling(name = 'GC_142',
                  value = '-((cquqd1*complex(0,1)*I1b31*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((cquqd8*complex(0,1)*I1b31*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_144 = Coupling(name = 'GC_144',
                  value = '-((cquqd1*complex(0,1)*I1b32*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_145 = Coupling(name = 'GC_145',
                  value = '-((cquqd8*complex(0,1)*I1b32*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((cquqd1*complex(0,1)*I1b33*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((cquqd8*complex(0,1)*I1b33*I6b22)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_148 = Coupling(name = 'GC_148',
                  value = '-((cquqd1*complex(0,1)*I1b11*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_149 = Coupling(name = 'GC_149',
                  value = '-((cquqd8*complex(0,1)*I1b11*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_150 = Coupling(name = 'GC_150',
                  value = '-((cquqd1*complex(0,1)*I1b12*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_151 = Coupling(name = 'GC_151',
                  value = '-((cquqd8*complex(0,1)*I1b12*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((cquqd1*complex(0,1)*I1b13*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((cquqd8*complex(0,1)*I1b13*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_154 = Coupling(name = 'GC_154',
                  value = '-((cquqd1*complex(0,1)*I1b21*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_155 = Coupling(name = 'GC_155',
                  value = '-((cquqd8*complex(0,1)*I1b21*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_156 = Coupling(name = 'GC_156',
                  value = '-((cquqd1*complex(0,1)*I1b22*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((cquqd8*complex(0,1)*I1b22*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_158 = Coupling(name = 'GC_158',
                  value = '-((cquqd1*complex(0,1)*I1b23*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_159 = Coupling(name = 'GC_159',
                  value = '-((cquqd8*complex(0,1)*I1b23*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_160 = Coupling(name = 'GC_160',
                  value = '-((cquqd1*complex(0,1)*I1b31*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((cquqd8*complex(0,1)*I1b31*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_162 = Coupling(name = 'GC_162',
                  value = '-((cquqd1*complex(0,1)*I1b32*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((cquqd8*complex(0,1)*I1b32*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_164 = Coupling(name = 'GC_164',
                  value = '-((cquqd1*complex(0,1)*I1b33*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((cquqd8*complex(0,1)*I1b33*I6b23)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_166 = Coupling(name = 'GC_166',
                  value = '-((cquqd1*complex(0,1)*I1b11*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((cquqd8*complex(0,1)*I1b11*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_168 = Coupling(name = 'GC_168',
                  value = '-((cquqd1*complex(0,1)*I1b12*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((cquqd8*complex(0,1)*I1b12*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_170 = Coupling(name = 'GC_170',
                  value = '-((cquqd1*complex(0,1)*I1b13*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_171 = Coupling(name = 'GC_171',
                  value = '-((cquqd8*complex(0,1)*I1b13*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_172 = Coupling(name = 'GC_172',
                  value = '-((cquqd1*complex(0,1)*I1b21*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_173 = Coupling(name = 'GC_173',
                  value = '-((cquqd8*complex(0,1)*I1b21*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_174 = Coupling(name = 'GC_174',
                  value = '-((cquqd1*complex(0,1)*I1b22*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((cquqd8*complex(0,1)*I1b22*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((cquqd1*complex(0,1)*I1b23*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_177 = Coupling(name = 'GC_177',
                  value = '-((cquqd8*complex(0,1)*I1b23*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_178 = Coupling(name = 'GC_178',
                  value = '-((cquqd1*complex(0,1)*I1b31*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_179 = Coupling(name = 'GC_179',
                  value = '-((cquqd8*complex(0,1)*I1b31*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_180 = Coupling(name = 'GC_180',
                  value = '-((cquqd1*complex(0,1)*I1b32*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_181 = Coupling(name = 'GC_181',
                  value = '-((cquqd8*complex(0,1)*I1b32*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_182 = Coupling(name = 'GC_182',
                  value = '-((cquqd1*complex(0,1)*I1b33*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_183 = Coupling(name = 'GC_183',
                  value = '-((cquqd8*complex(0,1)*I1b33*I6b31)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((cquqd1*complex(0,1)*I1b11*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((cquqd8*complex(0,1)*I1b11*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_186 = Coupling(name = 'GC_186',
                  value = '-((cquqd1*complex(0,1)*I1b12*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_187 = Coupling(name = 'GC_187',
                  value = '-((cquqd8*complex(0,1)*I1b12*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_188 = Coupling(name = 'GC_188',
                  value = '-((cquqd1*complex(0,1)*I1b13*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_189 = Coupling(name = 'GC_189',
                  value = '-((cquqd8*complex(0,1)*I1b13*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_190 = Coupling(name = 'GC_190',
                  value = '-((cquqd1*complex(0,1)*I1b21*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((cquqd8*complex(0,1)*I1b21*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((cquqd1*complex(0,1)*I1b22*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((cquqd8*complex(0,1)*I1b22*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((cquqd1*complex(0,1)*I1b23*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_195 = Coupling(name = 'GC_195',
                  value = '-((cquqd8*complex(0,1)*I1b23*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_196 = Coupling(name = 'GC_196',
                  value = '-((cquqd1*complex(0,1)*I1b31*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((cquqd8*complex(0,1)*I1b31*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_198 = Coupling(name = 'GC_198',
                  value = '-((cquqd1*complex(0,1)*I1b32*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_199 = Coupling(name = 'GC_199',
                  value = '-((cquqd8*complex(0,1)*I1b32*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_200 = Coupling(name = 'GC_200',
                  value = '-((cquqd1*complex(0,1)*I1b33*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_201 = Coupling(name = 'GC_201',
                  value = '-((cquqd8*complex(0,1)*I1b33*I6b32)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_202 = Coupling(name = 'GC_202',
                  value = '-((cquqd1*complex(0,1)*I1b11*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_203 = Coupling(name = 'GC_203',
                  value = '-((cquqd8*complex(0,1)*I1b11*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_204 = Coupling(name = 'GC_204',
                  value = '-((cquqd1*complex(0,1)*I1b12*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_205 = Coupling(name = 'GC_205',
                  value = '-((cquqd8*complex(0,1)*I1b12*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_206 = Coupling(name = 'GC_206',
                  value = '-((cquqd1*complex(0,1)*I1b13*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_207 = Coupling(name = 'GC_207',
                  value = '-((cquqd8*complex(0,1)*I1b13*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_208 = Coupling(name = 'GC_208',
                  value = '-((cquqd1*complex(0,1)*I1b21*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_209 = Coupling(name = 'GC_209',
                  value = '-((cquqd8*complex(0,1)*I1b21*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_210 = Coupling(name = 'GC_210',
                  value = '-((cquqd1*complex(0,1)*I1b22*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_211 = Coupling(name = 'GC_211',
                  value = '-((cquqd8*complex(0,1)*I1b22*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_212 = Coupling(name = 'GC_212',
                  value = '-((cquqd1*complex(0,1)*I1b23*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_213 = Coupling(name = 'GC_213',
                  value = '-((cquqd8*complex(0,1)*I1b23*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_214 = Coupling(name = 'GC_214',
                  value = '-((cquqd1*complex(0,1)*I1b31*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_215 = Coupling(name = 'GC_215',
                  value = '-((cquqd8*complex(0,1)*I1b31*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_216 = Coupling(name = 'GC_216',
                  value = '-((cquqd1*complex(0,1)*I1b32*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_217 = Coupling(name = 'GC_217',
                  value = '-((cquqd8*complex(0,1)*I1b32*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_218 = Coupling(name = 'GC_218',
                  value = '-((cquqd1*complex(0,1)*I1b33*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_219 = Coupling(name = 'GC_219',
                  value = '-((cquqd8*complex(0,1)*I1b33*I6b33)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_220 = Coupling(name = 'GC_220',
                  value = '(ee**2*complex(0,1))/(2.*sth**2)',
                  order = {'QED':2})

GC_221 = Coupling(name = 'GC_221',
                  value = '-((ee**2*complex(0,1))/sth**2)',
                  order = {'QED':2})

GC_222 = Coupling(name = 'GC_222',
                  value = '(cth**2*ee**2*complex(0,1))/sth**2',
                  order = {'QED':2})

GC_223 = Coupling(name = 'GC_223',
                  value = '(-2*dgw*ee**2*complex(0,1))/sth**2',
                  order = {'NP':1,'QED':2})

GC_224 = Coupling(name = 'GC_224',
                  value = '-((ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '-((CKM1x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '-((CKM1x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '-((CKM1x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '-((CKM2x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '-((CKM2x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-((CKM2x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '-((CKM3x1*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '-((CKM3x2*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '-((CKM3x3*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '-(cth*ee*complex(0,1))/(2.*sth)',
                  order = {'QED':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '(cth*ee*complex(0,1))/(2.*sth)',
                  order = {'QED':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '-((cth*ee*complex(0,1))/sth)',
                  order = {'QED':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '-((CKM1x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '-((CKM1x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '-((CKM2x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '-((CKM2x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '-((CKM3x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-((CKM3x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '(-2*cth*ee**2*complex(0,1))/sth',
                  order = {'QED':2})

GC_244 = Coupling(name = 'GC_244',
                  value = '(6*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_245 = Coupling(name = 'GC_245',
                  value = '(-6*cth**2*cW*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_246 = Coupling(name = 'GC_246',
                  value = '(-2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_247 = Coupling(name = 'GC_247',
                  value = '(2*cth**2*cWtil*ee*complex(0,1))/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_248 = Coupling(name = 'GC_248',
                  value = '(ee*complex(0,1)*sth)/(6.*cth)',
                  order = {'QED':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '-(ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '(6*cW*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_251 = Coupling(name = 'GC_251',
                  value = '(2*cWtil*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_252 = Coupling(name = 'GC_252',
                  value = '(-6*cW*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_253 = Coupling(name = 'GC_253',
                  value = '(2*cWtil*ee*complex(0,1)*sth)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_254 = Coupling(name = 'GC_254',
                  value = '-(cth*ee*complex(0,1))/(2.*sth) - (ee*complex(0,1)*sth)/(2.*cth)',
                  order = {'QED':1})

GC_255 = Coupling(name = 'GC_255',
                  value = 'ee**2*complex(0,1) + (cth**2*ee**2*complex(0,1))/(2.*sth**2) + (ee**2*complex(0,1)*sth**2)/(2.*cth**2)',
                  order = {'QED':2})

GC_256 = Coupling(name = 'GC_256',
                  value = '(4*cHW*cth**2*complex(0,1))/LambdaSMEFT**2 + (4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_257 = Coupling(name = 'GC_257',
                  value = '(-2*cHWtil*cth**2*complex(0,1))/LambdaSMEFT**2 - (2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2 - (2*cHBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_258 = Coupling(name = 'GC_258',
                  value = '(4*cHB*cth**2*complex(0,1))/LambdaSMEFT**2 - (4*cHWB*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHW*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(-2*cHWB*cth**2*complex(0,1))/LambdaSMEFT**2 - (4*cHB*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHW*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (2*cHWB*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_260 = Coupling(name = 'GC_260',
                  value = '(-2*cHWBtil*cth**2*complex(0,1))/LambdaSMEFT**2 - (4*cHBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (4*cHWtil*cth*complex(0,1)*sth)/LambdaSMEFT**2 + (2*cHWBtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_261 = Coupling(name = 'GC_261',
                  value = '(-2*cHBtil*cth**2*complex(0,1))/LambdaSMEFT**2 + (2*cHWBtil*cth*complex(0,1)*sth)/LambdaSMEFT**2 - (2*cHWtil*complex(0,1)*sth**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_262 = Coupling(name = 'GC_262',
                  value = '(4*complex(0,1)*gHaa)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '(4*complex(0,1)*gHgg)/vevhat',
                  order = {'QCD':2,'QED':1,'SMHLOOP':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '(2*complex(0,1)*gHza)/vevhat',
                  order = {'QED':3,'SMHLOOP':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '-6*complex(0,1)*lam*vevhat',
                  order = {'QED':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '(-3*cHbox*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '-((cHDD*complex(0,1)*vevhat)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '(4*cHG*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '(-2*cHGtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '(4*cHW*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '(4*cHWtil*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '(4*cHW*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_273 = Coupling(name = 'GC_273',
                  value = '(2*cHWB*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_274 = Coupling(name = 'GC_274',
                  value = '(-2*cHWBtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_275 = Coupling(name = 'GC_275',
                  value = '(-4*cHWtil*ee*complex(0,1)*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_276 = Coupling(name = 'GC_276',
                  value = '(-4*cHG*G*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QCD':1,'QED':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '(4*cHGtil*G*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QCD':1,'QED':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '(ee**2*complex(0,1)*vevhat)/(2.*sth**2)',
                  order = {'QED':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '-((cHl3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':2})

GC_280 = Coupling(name = 'GC_280',
                  value = '-((cHq3*ee*complex(0,1)*vevhat*cmath.sqrt(2))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':2})

GC_281 = Coupling(name = 'GC_281',
                  value = '(4*cHW*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':2})

GC_282 = Coupling(name = 'GC_282',
                  value = '(-2*cHWB*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':2})

GC_283 = Coupling(name = 'GC_283',
                  value = '(2*cHWBtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':2})

GC_284 = Coupling(name = 'GC_284',
                  value = '(-4*cHWtil*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':2})

GC_285 = Coupling(name = 'GC_285',
                  value = '(cHud*ee*complex(0,1)*I7b11*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_286 = Coupling(name = 'GC_286',
                  value = '(cHud*ee*complex(0,1)*I7b12*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_287 = Coupling(name = 'GC_287',
                  value = '(cHud*ee*complex(0,1)*I7b13*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_288 = Coupling(name = 'GC_288',
                  value = '(cHud*ee*complex(0,1)*I7b21*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_289 = Coupling(name = 'GC_289',
                  value = '(cHud*ee*complex(0,1)*I7b22*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_290 = Coupling(name = 'GC_290',
                  value = '(cHud*ee*complex(0,1)*I7b23*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_291 = Coupling(name = 'GC_291',
                  value = '(cHud*ee*complex(0,1)*I7b31*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_292 = Coupling(name = 'GC_292',
                  value = '(cHud*ee*complex(0,1)*I7b32*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_293 = Coupling(name = 'GC_293',
                  value = '(cHud*ee*complex(0,1)*I7b33*vevhat)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_294 = Coupling(name = 'GC_294',
                  value = '(45*cH*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1})

GC_295 = Coupling(name = 'GC_295',
                  value = '(cHWB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_296 = Coupling(name = 'GC_296',
                  value = '-((cHWBtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_297 = Coupling(name = 'GC_297',
                  value = '(-2*cHWtil*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '(2*cHGtil*G*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QCD':1})

GC_299 = Coupling(name = 'GC_299',
                  value = '-(cHWB*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':1})

GC_300 = Coupling(name = 'GC_300',
                  value = '(cHWBtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':1})

GC_301 = Coupling(name = 'GC_301',
                  value = '(-2*cHWtil*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '(cHud*ee*complex(0,1)*I7b11*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_303 = Coupling(name = 'GC_303',
                  value = '(cHud*ee*complex(0,1)*I7b12*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_304 = Coupling(name = 'GC_304',
                  value = '(cHud*ee*complex(0,1)*I7b13*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_305 = Coupling(name = 'GC_305',
                  value = '(cHud*ee*complex(0,1)*I7b21*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_306 = Coupling(name = 'GC_306',
                  value = '(cHud*ee*complex(0,1)*I7b22*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_307 = Coupling(name = 'GC_307',
                  value = '(cHud*ee*complex(0,1)*I7b23*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_308 = Coupling(name = 'GC_308',
                  value = '(cHud*ee*complex(0,1)*I7b31*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_309 = Coupling(name = 'GC_309',
                  value = '(cHud*ee*complex(0,1)*I7b32*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_310 = Coupling(name = 'GC_310',
                  value = '(cHud*ee*complex(0,1)*I7b33*vevhat**2)/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_311 = Coupling(name = 'GC_311',
                  value = '(15*cH*complex(0,1)*vevhat**3)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':-1})

GC_312 = Coupling(name = 'GC_312',
                  value = '(cHd*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHd*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_313 = Coupling(name = 'GC_313',
                  value = '(cHe*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHe*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_314 = Coupling(name = 'GC_314',
                  value = '(cHl1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHl3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHl3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_315 = Coupling(name = 'GC_315',
                  value = '(cHl1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHl1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHl3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_316 = Coupling(name = 'GC_316',
                  value = '(cHq1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) - (cHq3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) - (cHq3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_317 = Coupling(name = 'GC_317',
                  value = '(cHq1*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq3*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHq1*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2) + (cHq3*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_318 = Coupling(name = 'GC_318',
                  value = '(cHu*cth*ee*complex(0,1)*vevhat)/(LambdaSMEFT**2*sth) + (cHu*ee*complex(0,1)*sth*vevhat)/(cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_319 = Coupling(name = 'GC_319',
                  value = 'ee**2*complex(0,1)*vevhat + (cth**2*ee**2*complex(0,1)*vevhat)/(2.*sth**2) + (ee**2*complex(0,1)*sth**2*vevhat)/(2.*cth**2)',
                  order = {'QED':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '(4*cHW*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 + (4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '(-2*cHWtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 - (2*cHBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '(4*cHB*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (4*cHWB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHW*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '(-2*cHWB*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (4*cHB*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHW*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (2*cHWB*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '(-2*cHWBtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 - (4*cHBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (4*cHWtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 + (2*cHWBtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '(-2*cHBtil*cth**2*complex(0,1)*vevhat)/LambdaSMEFT**2 + (2*cHWBtil*cth*complex(0,1)*sth*vevhat)/LambdaSMEFT**2 - (2*cHWtil*complex(0,1)*sth**2*vevhat)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '-(dsth2*ee*complex(0,1))/(6.*cth*sth) - (cHWB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '(dsth2*ee*complex(0,1))/(3.*cth*sth) + (cHWB*ee*complex(0,1)*vevhat**2)/(3.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '-(dsth2*ee*complex(0,1))/(2.*cth*sth) - (cHWB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '(6*dMH2*complex(0,1)*lam)/MH**2 - (24*cHbox*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2 + (6*cHDD*complex(0,1)*lam*vevhat**2)/LambdaSMEFT**2 + 6*dGf*complex(0,1)*lam*cmath.sqrt(2)',
                  order = {'NP':1,'QED':2})

GC_330 = Coupling(name = 'GC_330',
                  value = '(dgw*ee**2*complex(0,1))/sth**2 + (cHbox*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) - (cHDD*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2)',
                  order = {'NP':1,'QED':2})

GC_331 = Coupling(name = 'GC_331',
                  value = '-((dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHl3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '-((CKM1x1*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '-((CKM2x2*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '-((CKM3x3*dgw*ee*complex(0,1))/(sth*cmath.sqrt(2))) - (cHq3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '(cHd*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHd*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '(cHe*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHe*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '(cHu*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHu*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '(2*cth**2*dgw*ee**2*complex(0,1))/sth**2 - (dsth2*ee**2*complex(0,1))/sth**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (2*cHW*cth**4*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) - (cHWB*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHWB*cth**3*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_339 = Coupling(name = 'GC_339',
                  value = '-(dgw*ee*complex(0,1))/2. - (dsth2*ee*complex(0,1))/(4.*sth**2) + (cHW*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth) - (cHW*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '(dgw*ee*complex(0,1))/2. + (dsth2*ee*complex(0,1))/(4.*sth**2) - (cHW*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHW*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth) + (cHW*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '-(dgw*ee*complex(0,1)) - (dsth2*ee*complex(0,1))/(2.*sth**2) + (cHW*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (cHW*cth**2*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (cHW*ee*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHq3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHq3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '(cth*dgw*ee*complex(0,1))/(2.*sth) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHl1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '(cth*dgw*ee*complex(0,1))/(2.*sth) + (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHq1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHq1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHq3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '-((cth*dgw*ee*complex(0,1))/sth) + (dsth2*ee*complex(0,1))/(2.*cth*sth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHW*cth*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':1})

GC_346 = Coupling(name = 'GC_346',
                  value = '2*dgw*ee**2*complex(0,1) + (dsth2*ee**2*complex(0,1))/sth**2 - (2*cHW*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (cHWB*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHW*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_347 = Coupling(name = 'GC_347',
                  value = '-((cth*dsth2*ee**2*complex(0,1))/sth**3) - (4*cth*dgw*ee**2*complex(0,1))/sth + (dsth2*ee**2*complex(0,1))/(cth*sth) + (cHWB*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 - (2*cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (4*cHW*cth*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (4*cHW*cth**3*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) - (4*cHW*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 - (2*cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_348 = Coupling(name = 'GC_348',
                  value = '(dg1*ee*complex(0,1)*sth)/(6.*cth) - (cHB*ee*complex(0,1)*sth*vevhat**2)/(6.*cth*LambdaSMEFT**2) + (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '-(dg1*ee*complex(0,1)*sth)/(2.*cth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_350 = Coupling(name = 'GC_350',
                  value = '-(cth*dgw*ee*complex(0,1))/(2.*sth) - (dg1*ee*complex(0,1)*sth)/(2.*cth) - (cHWB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHl1*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHl3*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth**3*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHl1*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHl3*ee*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '-(dg1*ee*complex(0,1))/6. + (dsth2*ee*complex(0,1))/(12.*cth**2) + (cHB*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) - (cHB*cth**2*ee*complex(0,1)*vevhat**2)/(6.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth*vevhat**2)/(12.*cth*LambdaSMEFT**2) + (cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(6.*LambdaSMEFT**2) - (cHB*ee*complex(0,1)*sth**2*vevhat**2)/(6.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth**3*vevhat**2)/(6.*cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(dg1*ee*complex(0,1))/2. - (dsth2*ee*complex(0,1))/(4.*cth**2) - (cHB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*ee*complex(0,1)*sth*vevhat**2)/(4.*cth*LambdaSMEFT**2) - (cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '(dg1*ee*complex(0,1))/2. - (dgw*ee*complex(0,1))/2. - (dsth2*ee*complex(0,1))/(4.*cth**2) - (dsth2*ee*complex(0,1))/(4.*sth**2) - (cHB*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHW*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*cth**2*ee*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth*ee*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth) + (cHWB*ee*complex(0,1)*sth*vevhat**2)/(4.*cth*LambdaSMEFT**2) - (cHWB*cth*ee*complex(0,1)*sth*vevhat**2)/(2.*LambdaSMEFT**2) + (cHB*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*ee*complex(0,1)*sth**2*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*ee*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_354 = Coupling(name = 'GC_354',
                  value = 'dg1*ee**2*complex(0,1) + dgw*ee**2*complex(0,1) + (cth**2*dgw*ee**2*complex(0,1))/sth**2 + (dg1*ee**2*complex(0,1)*sth**2)/cth**2 - (cHB*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (2*cHbox*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (5*cHDD*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHB*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/LambdaSMEFT**2 + (cHbox*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (5*cHDD*cth**2*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2) - (cHW*cth**2*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (cHW*cth**4*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth**2) + (cHWB*cth**3*ee**2*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth) + (2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 + (2*cHB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2 + (cHW*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2 - (cHB*ee**2*complex(0,1)*sth**2*vevhat**2)/(cth**2*LambdaSMEFT**2) + (cHbox*ee**2*complex(0,1)*sth**2*vevhat**2)/(cth**2*LambdaSMEFT**2) + (5*cHDD*ee**2*complex(0,1)*sth**2*vevhat**2)/(4.*cth**2*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**3*vevhat**2)/(cth*LambdaSMEFT**2) + (cHB*ee**2*complex(0,1)*sth**4*vevhat**2)/(cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_355 = Coupling(name = 'GC_355',
                  value = '(cth*dsth2*ee**2*complex(0,1))/(4.*sth**3) - (cth*dg1*ee**2*complex(0,1))/(2.*sth) + (cth*dgw*ee**2*complex(0,1))/(2.*sth) + (dsth2*ee**2*complex(0,1))/(2.*cth*sth) - (dg1*ee**2*complex(0,1)*sth)/(2.*cth) + (dgw*ee**2*complex(0,1)*sth)/(2.*cth) + (dsth2*ee**2*complex(0,1)*sth)/(4.*cth**3) - (cHWB*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) + (cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2) - (cHWB*cth**2*ee**2*complex(0,1)*vevhat**2)/(4.*LambdaSMEFT**2*sth**2) + (cHB*cth*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) - (cHB*cth**3*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee**2*complex(0,1)*vevhat**2)/(2.*LambdaSMEFT**2*sth) + (cHB*ee**2*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*sth*vevhat**2)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 + (cHW*cth*ee**2*complex(0,1)*sth*vevhat**2)/LambdaSMEFT**2 + (cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/LambdaSMEFT**2 - (cHWB*ee**2*complex(0,1)*sth**2*vevhat**2)/(4.*cth**2*LambdaSMEFT**2) - (cHB*ee**2*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHW*ee**2*complex(0,1)*sth**3*vevhat**2)/(2.*cth*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**4*vevhat**2)/(2.*cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':2})

GC_356 = Coupling(name = 'GC_356',
                  value = '(6*dMH2*complex(0,1)*lam*vevhat)/MH**2 - (18*cHbox*complex(0,1)*lam*vevhat**3)/LambdaSMEFT**2 + (9*cHDD*complex(0,1)*lam*vevhat**3)/(2.*LambdaSMEFT**2) + 3*dGf*complex(0,1)*lam*vevhat*cmath.sqrt(2)',
                  order = {'NP':1,'QED':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '(dgw*ee**2*complex(0,1)*vevhat)/sth**2 + (cHbox*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth**2) - (cHDD*ee**2*complex(0,1)*vevhat**3)/(8.*LambdaSMEFT**2*sth**2) + (dGf*ee**2*complex(0,1)*vevhat)/(2.*sth**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_358 = Coupling(name = 'GC_358',
                  value = 'dg1*ee**2*complex(0,1)*vevhat + dgw*ee**2*complex(0,1)*vevhat + (cth**2*dgw*ee**2*complex(0,1)*vevhat)/sth**2 + (dg1*ee**2*complex(0,1)*sth**2*vevhat)/cth**2 - (cHB*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (cHbox*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (3*cHDD*ee**2*complex(0,1)*vevhat**3)/(4.*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (cHB*cth**2*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (2*cHW*cth**2*ee**2*complex(0,1)*vevhat**3)/LambdaSMEFT**2 + (cHbox*cth**2*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth**2) + (3*cHDD*cth**2*ee**2*complex(0,1)*vevhat**3)/(8.*LambdaSMEFT**2*sth**2) - (cHW*cth**2*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*sth**2) + (cHW*cth**4*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*sth**2) + (cHWB*cth**3*ee**2*complex(0,1)*vevhat**3)/(LambdaSMEFT**2*sth) + (2*cHWB*cth*ee**2*complex(0,1)*sth*vevhat**3)/LambdaSMEFT**2 + (2*cHB*ee**2*complex(0,1)*sth**2*vevhat**3)/LambdaSMEFT**2 + (cHW*ee**2*complex(0,1)*sth**2*vevhat**3)/LambdaSMEFT**2 - (cHB*ee**2*complex(0,1)*sth**2*vevhat**3)/(cth**2*LambdaSMEFT**2) + (cHbox*ee**2*complex(0,1)*sth**2*vevhat**3)/(2.*cth**2*LambdaSMEFT**2) + (3*cHDD*ee**2*complex(0,1)*sth**2*vevhat**3)/(8.*cth**2*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**3*vevhat**3)/(cth*LambdaSMEFT**2) + (cHB*ee**2*complex(0,1)*sth**4*vevhat**3)/(cth**2*LambdaSMEFT**2) + (dGf*ee**2*complex(0,1)*vevhat)/cmath.sqrt(2) + (cth**2*dGf*ee**2*complex(0,1)*vevhat)/(2.*sth**2*cmath.sqrt(2)) + (dGf*ee**2*complex(0,1)*sth**2*vevhat)/(2.*cth**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '(cth*dsth2*ee**2*complex(0,1)*vevhat)/(4.*sth**3) - (cth*dg1*ee**2*complex(0,1)*vevhat)/(2.*sth) + (cth*dgw*ee**2*complex(0,1)*vevhat)/(2.*sth) + (dsth2*ee**2*complex(0,1)*vevhat)/(2.*cth*sth) - (dg1*ee**2*complex(0,1)*sth*vevhat)/(2.*cth) + (dgw*ee**2*complex(0,1)*sth*vevhat)/(2.*cth) + (dsth2*ee**2*complex(0,1)*sth*vevhat)/(4.*cth**3) - (cHWB*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2) + (cHWB*cth**2*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2) - (cHWB*cth**2*ee**2*complex(0,1)*vevhat**3)/(4.*LambdaSMEFT**2*sth**2) + (cHB*cth*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) - (cHW*cth*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) - (cHB*cth**3*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) + (cHW*cth**3*ee**2*complex(0,1)*vevhat**3)/(2.*LambdaSMEFT**2*sth) + (cHB*ee**2*complex(0,1)*sth*vevhat**3)/(2.*cth*LambdaSMEFT**2) - (cHW*ee**2*complex(0,1)*sth*vevhat**3)/(2.*cth*LambdaSMEFT**2) - (cHB*cth*ee**2*complex(0,1)*sth*vevhat**3)/LambdaSMEFT**2 + (cHW*cth*ee**2*complex(0,1)*sth*vevhat**3)/LambdaSMEFT**2 + (cHWB*ee**2*complex(0,1)*sth**2*vevhat**3)/LambdaSMEFT**2 - (cHWB*ee**2*complex(0,1)*sth**2*vevhat**3)/(4.*cth**2*LambdaSMEFT**2) - (cHB*ee**2*complex(0,1)*sth**3*vevhat**3)/(2.*cth*LambdaSMEFT**2) + (cHW*ee**2*complex(0,1)*sth**3*vevhat**3)/(2.*cth*LambdaSMEFT**2) + (cHWB*ee**2*complex(0,1)*sth**4*vevhat**3)/(2.*cth**2*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '(cdG*complex(0,1)*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_362 = Coupling(name = 'GC_362',
                  value = '(cdW*complex(0,1)*yb)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_363 = Coupling(name = 'GC_363',
                  value = '(cdG*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_364 = Coupling(name = 'GC_364',
                  value = '(3*cdH*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_365 = Coupling(name = 'GC_365',
                  value = '(cdW*complex(0,1)*vevhat*yb)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_366 = Coupling(name = 'GC_366',
                  value = '-((cdW*ee*complex(0,1)*vevhat*yb)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':3})

GC_367 = Coupling(name = 'GC_367',
                  value = '(cdG*G*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_368 = Coupling(name = 'GC_368',
                  value = '(cdW*ee*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_369 = Coupling(name = 'GC_369',
                  value = '(cdW*cth*ee*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_370 = Coupling(name = 'GC_370',
                  value = '(cdH*complex(0,1)*vevhat**2*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '-((cdW*cth*complex(0,1)*yb)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB*complex(0,1)*sth*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_372 = Coupling(name = 'GC_372',
                  value = '(cdB*cth*complex(0,1)*yb)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW*complex(0,1)*sth*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_373 = Coupling(name = 'GC_373',
                  value = '-((cdW*cth*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB*complex(0,1)*sth*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_374 = Coupling(name = 'GC_374',
                  value = '(cdB*cth*complex(0,1)*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW*complex(0,1)*sth*vevhat*yb)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_375 = Coupling(name = 'GC_375',
                  value = '(dGf*complex(0,1)*yb)/2. - (cHbox*complex(0,1)*vevhat**2*yb)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yb)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_376 = Coupling(name = 'GC_376',
                  value = '(cHbox*dGf*complex(0,1)*vevhat**2*yb)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*yb)/(8.*LambdaSMEFT**2)',
                  order = {'NP':2,'QED':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '-(cdH*cHbox*complex(0,1)*vevhat**4*yb)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cdH*cHDD*complex(0,1)*vevhat**4*yb)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_378 = Coupling(name = 'GC_378',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '(cuG*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_380 = Coupling(name = 'GC_380',
                  value = '(cuW*complex(0,1)*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_381 = Coupling(name = 'GC_381',
                  value = '(cuG*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_382 = Coupling(name = 'GC_382',
                  value = '(3*cuH*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_383 = Coupling(name = 'GC_383',
                  value = '(cuW*complex(0,1)*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_384 = Coupling(name = 'GC_384',
                  value = '(cuW*ee*complex(0,1)*vevhat*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_385 = Coupling(name = 'GC_385',
                  value = '(cuG*G*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_386 = Coupling(name = 'GC_386',
                  value = '-((cuW*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':3})

GC_387 = Coupling(name = 'GC_387',
                  value = '-((cth*cuW*ee*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':3})

GC_388 = Coupling(name = 'GC_388',
                  value = '(cuH*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '(cquqd1*complex(0,1)*yb*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_390 = Coupling(name = 'GC_390',
                  value = '(cquqd8*complex(0,1)*yb*yc)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_391 = Coupling(name = 'GC_391',
                  value = '(cth*cuW*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_392 = Coupling(name = 'GC_392',
                  value = '(cth*cuB*complex(0,1)*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW*complex(0,1)*sth*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_393 = Coupling(name = 'GC_393',
                  value = '(cth*cuW*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_394 = Coupling(name = 'GC_394',
                  value = '(cth*cuB*complex(0,1)*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW*complex(0,1)*sth*vevhat*yc)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_395 = Coupling(name = 'GC_395',
                  value = '(dGf*complex(0,1)*yc)/2. - (cHbox*complex(0,1)*vevhat**2*yc)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yc)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_396 = Coupling(name = 'GC_396',
                  value = '(cHbox*dGf*complex(0,1)*vevhat**2*yc)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*yc)/(8.*LambdaSMEFT**2)',
                  order = {'NP':2,'QED':1})

GC_397 = Coupling(name = 'GC_397',
                  value = '-(cHbox*cuH*complex(0,1)*vevhat**4*yc)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*cuH*complex(0,1)*vevhat**4*yc)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '(cdG*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_400 = Coupling(name = 'GC_400',
                  value = '(cdW*complex(0,1)*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_401 = Coupling(name = 'GC_401',
                  value = '(cdG*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_402 = Coupling(name = 'GC_402',
                  value = '(3*cdH*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_403 = Coupling(name = 'GC_403',
                  value = '(cdW*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_404 = Coupling(name = 'GC_404',
                  value = '-((cdW*ee*complex(0,1)*vevhat*ydo)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':3})

GC_405 = Coupling(name = 'GC_405',
                  value = '(cdG*G*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_406 = Coupling(name = 'GC_406',
                  value = '(cdW*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_407 = Coupling(name = 'GC_407',
                  value = '(cdW*cth*ee*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_408 = Coupling(name = 'GC_408',
                  value = '(cdH*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_409 = Coupling(name = 'GC_409',
                  value = '(cquqd1*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_410 = Coupling(name = 'GC_410',
                  value = '(cquqd8*complex(0,1)*yc*ydo)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_411 = Coupling(name = 'GC_411',
                  value = '-((cdW*cth*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB*complex(0,1)*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_412 = Coupling(name = 'GC_412',
                  value = '(cdB*cth*complex(0,1)*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW*complex(0,1)*sth*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_413 = Coupling(name = 'GC_413',
                  value = '-((cdW*cth*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB*complex(0,1)*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_414 = Coupling(name = 'GC_414',
                  value = '(cdB*cth*complex(0,1)*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW*complex(0,1)*sth*vevhat*ydo)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_415 = Coupling(name = 'GC_415',
                  value = '(dGf*complex(0,1)*ydo)/2. - (cHbox*complex(0,1)*vevhat**2*ydo)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ydo)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_416 = Coupling(name = 'GC_416',
                  value = '(cHbox*dGf*complex(0,1)*vevhat**2*ydo)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*ydo)/(8.*LambdaSMEFT**2)',
                  order = {'NP':2,'QED':1})

GC_417 = Coupling(name = 'GC_417',
                  value = '-(cdH*cHbox*complex(0,1)*vevhat**4*ydo)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cdH*cHDD*complex(0,1)*vevhat**4*ydo)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_418 = Coupling(name = 'GC_418',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_419 = Coupling(name = 'GC_419',
                  value = '(ceW*complex(0,1)*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_420 = Coupling(name = 'GC_420',
                  value = '(cledq*complex(0,1)*I3b11*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_421 = Coupling(name = 'GC_421',
                  value = '(cledq*complex(0,1)*I3b12*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_422 = Coupling(name = 'GC_422',
                  value = '(cledq*complex(0,1)*I3b13*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_423 = Coupling(name = 'GC_423',
                  value = '(cledq*complex(0,1)*I3b21*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_424 = Coupling(name = 'GC_424',
                  value = '(cledq*complex(0,1)*I3b22*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_425 = Coupling(name = 'GC_425',
                  value = '(cledq*complex(0,1)*I3b23*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_426 = Coupling(name = 'GC_426',
                  value = '(cledq*complex(0,1)*I3b31*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_427 = Coupling(name = 'GC_427',
                  value = '(cledq*complex(0,1)*I3b32*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_428 = Coupling(name = 'GC_428',
                  value = '(cledq*complex(0,1)*I3b33*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_429 = Coupling(name = 'GC_429',
                  value = '(clequ1*complex(0,1)*I4b11*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_430 = Coupling(name = 'GC_430',
                  value = '(clequ3*complex(0,1)*I4b11*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_431 = Coupling(name = 'GC_431',
                  value = '-(clequ3*complex(0,1)*I4b11*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_432 = Coupling(name = 'GC_432',
                  value = '(clequ1*complex(0,1)*I4b12*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_433 = Coupling(name = 'GC_433',
                  value = '(clequ3*complex(0,1)*I4b12*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_434 = Coupling(name = 'GC_434',
                  value = '-(clequ3*complex(0,1)*I4b12*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_435 = Coupling(name = 'GC_435',
                  value = '(clequ1*complex(0,1)*I4b13*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_436 = Coupling(name = 'GC_436',
                  value = '(clequ3*complex(0,1)*I4b13*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_437 = Coupling(name = 'GC_437',
                  value = '-(clequ3*complex(0,1)*I4b13*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_438 = Coupling(name = 'GC_438',
                  value = '(clequ1*complex(0,1)*I4b21*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_439 = Coupling(name = 'GC_439',
                  value = '(clequ3*complex(0,1)*I4b21*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_440 = Coupling(name = 'GC_440',
                  value = '-(clequ3*complex(0,1)*I4b21*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_441 = Coupling(name = 'GC_441',
                  value = '(clequ1*complex(0,1)*I4b22*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_442 = Coupling(name = 'GC_442',
                  value = '(clequ3*complex(0,1)*I4b22*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_443 = Coupling(name = 'GC_443',
                  value = '-(clequ3*complex(0,1)*I4b22*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_444 = Coupling(name = 'GC_444',
                  value = '(clequ1*complex(0,1)*I4b23*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_445 = Coupling(name = 'GC_445',
                  value = '(clequ3*complex(0,1)*I4b23*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_446 = Coupling(name = 'GC_446',
                  value = '-(clequ3*complex(0,1)*I4b23*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_447 = Coupling(name = 'GC_447',
                  value = '(clequ1*complex(0,1)*I4b31*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_448 = Coupling(name = 'GC_448',
                  value = '(clequ3*complex(0,1)*I4b31*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_449 = Coupling(name = 'GC_449',
                  value = '-(clequ3*complex(0,1)*I4b31*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_450 = Coupling(name = 'GC_450',
                  value = '(clequ1*complex(0,1)*I4b32*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_451 = Coupling(name = 'GC_451',
                  value = '(clequ3*complex(0,1)*I4b32*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_452 = Coupling(name = 'GC_452',
                  value = '-(clequ3*complex(0,1)*I4b32*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_453 = Coupling(name = 'GC_453',
                  value = '(clequ1*complex(0,1)*I4b33*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_454 = Coupling(name = 'GC_454',
                  value = '(clequ3*complex(0,1)*I4b33*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_455 = Coupling(name = 'GC_455',
                  value = '-(clequ3*complex(0,1)*I4b33*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_456 = Coupling(name = 'GC_456',
                  value = '(3*ceH*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_457 = Coupling(name = 'GC_457',
                  value = '(ceW*complex(0,1)*vevhat*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_458 = Coupling(name = 'GC_458',
                  value = '-((ceW*ee*complex(0,1)*vevhat*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':3})

GC_459 = Coupling(name = 'GC_459',
                  value = '(ceW*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_460 = Coupling(name = 'GC_460',
                  value = '(ceW*cth*ee*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_461 = Coupling(name = 'GC_461',
                  value = '(ceH*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_462 = Coupling(name = 'GC_462',
                  value = '(cledq*complex(0,1)*yb*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_463 = Coupling(name = 'GC_463',
                  value = '-((clequ1*complex(0,1)*yc*ye)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_464 = Coupling(name = 'GC_464',
                  value = '-(clequ3*complex(0,1)*yc*ye)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_465 = Coupling(name = 'GC_465',
                  value = '(clequ3*complex(0,1)*yc*ye)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_466 = Coupling(name = 'GC_466',
                  value = '(cledq*complex(0,1)*ydo*ye)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_467 = Coupling(name = 'GC_467',
                  value = '-((ceW*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_468 = Coupling(name = 'GC_468',
                  value = '(ceB*cth*complex(0,1)*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_469 = Coupling(name = 'GC_469',
                  value = '-((ceW*cth*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_470 = Coupling(name = 'GC_470',
                  value = '(ceB*cth*complex(0,1)*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*vevhat*ye)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_471 = Coupling(name = 'GC_471',
                  value = '(dGf*complex(0,1)*ye)/2. - (cHbox*complex(0,1)*vevhat**2*ye)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ye)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_472 = Coupling(name = 'GC_472',
                  value = '(cHbox*dGf*complex(0,1)*vevhat**2*ye)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*ye)/(8.*LambdaSMEFT**2)',
                  order = {'NP':2,'QED':1})

GC_473 = Coupling(name = 'GC_473',
                  value = '-(ceH*cHbox*complex(0,1)*vevhat**4*ye)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (ceH*cHDD*complex(0,1)*vevhat**4*ye)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_474 = Coupling(name = 'GC_474',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_475 = Coupling(name = 'GC_475',
                  value = '(ceW*complex(0,1)*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_476 = Coupling(name = 'GC_476',
                  value = '(cledq*complex(0,1)*I3b11*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_477 = Coupling(name = 'GC_477',
                  value = '(cledq*complex(0,1)*I3b12*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_478 = Coupling(name = 'GC_478',
                  value = '(cledq*complex(0,1)*I3b13*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_479 = Coupling(name = 'GC_479',
                  value = '(cledq*complex(0,1)*I3b21*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_480 = Coupling(name = 'GC_480',
                  value = '(cledq*complex(0,1)*I3b22*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_481 = Coupling(name = 'GC_481',
                  value = '(cledq*complex(0,1)*I3b23*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_482 = Coupling(name = 'GC_482',
                  value = '(cledq*complex(0,1)*I3b31*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_483 = Coupling(name = 'GC_483',
                  value = '(cledq*complex(0,1)*I3b32*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_484 = Coupling(name = 'GC_484',
                  value = '(cledq*complex(0,1)*I3b33*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_485 = Coupling(name = 'GC_485',
                  value = '(clequ1*complex(0,1)*I4b11*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_486 = Coupling(name = 'GC_486',
                  value = '(clequ3*complex(0,1)*I4b11*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_487 = Coupling(name = 'GC_487',
                  value = '-(clequ3*complex(0,1)*I4b11*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_488 = Coupling(name = 'GC_488',
                  value = '(clequ1*complex(0,1)*I4b12*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_489 = Coupling(name = 'GC_489',
                  value = '(clequ3*complex(0,1)*I4b12*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_490 = Coupling(name = 'GC_490',
                  value = '-(clequ3*complex(0,1)*I4b12*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_491 = Coupling(name = 'GC_491',
                  value = '(clequ1*complex(0,1)*I4b13*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_492 = Coupling(name = 'GC_492',
                  value = '(clequ3*complex(0,1)*I4b13*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_493 = Coupling(name = 'GC_493',
                  value = '-(clequ3*complex(0,1)*I4b13*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_494 = Coupling(name = 'GC_494',
                  value = '(clequ1*complex(0,1)*I4b21*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_495 = Coupling(name = 'GC_495',
                  value = '(clequ3*complex(0,1)*I4b21*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_496 = Coupling(name = 'GC_496',
                  value = '-(clequ3*complex(0,1)*I4b21*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_497 = Coupling(name = 'GC_497',
                  value = '(clequ1*complex(0,1)*I4b22*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_498 = Coupling(name = 'GC_498',
                  value = '(clequ3*complex(0,1)*I4b22*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_499 = Coupling(name = 'GC_499',
                  value = '-(clequ3*complex(0,1)*I4b22*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_500 = Coupling(name = 'GC_500',
                  value = '(clequ1*complex(0,1)*I4b23*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_501 = Coupling(name = 'GC_501',
                  value = '(clequ3*complex(0,1)*I4b23*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_502 = Coupling(name = 'GC_502',
                  value = '-(clequ3*complex(0,1)*I4b23*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_503 = Coupling(name = 'GC_503',
                  value = '(clequ1*complex(0,1)*I4b31*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_504 = Coupling(name = 'GC_504',
                  value = '(clequ3*complex(0,1)*I4b31*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_505 = Coupling(name = 'GC_505',
                  value = '-(clequ3*complex(0,1)*I4b31*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_506 = Coupling(name = 'GC_506',
                  value = '(clequ1*complex(0,1)*I4b32*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_507 = Coupling(name = 'GC_507',
                  value = '(clequ3*complex(0,1)*I4b32*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_508 = Coupling(name = 'GC_508',
                  value = '-(clequ3*complex(0,1)*I4b32*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_509 = Coupling(name = 'GC_509',
                  value = '(clequ1*complex(0,1)*I4b33*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_510 = Coupling(name = 'GC_510',
                  value = '(clequ3*complex(0,1)*I4b33*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_511 = Coupling(name = 'GC_511',
                  value = '-(clequ3*complex(0,1)*I4b33*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_512 = Coupling(name = 'GC_512',
                  value = '(3*ceH*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_513 = Coupling(name = 'GC_513',
                  value = '(ceW*complex(0,1)*vevhat*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_514 = Coupling(name = 'GC_514',
                  value = '-((ceW*ee*complex(0,1)*vevhat*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':3})

GC_515 = Coupling(name = 'GC_515',
                  value = '(ceW*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_516 = Coupling(name = 'GC_516',
                  value = '(ceW*cth*ee*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_517 = Coupling(name = 'GC_517',
                  value = '(ceH*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '(cledq*complex(0,1)*yb*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_519 = Coupling(name = 'GC_519',
                  value = '-((clequ1*complex(0,1)*yc*ym)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_520 = Coupling(name = 'GC_520',
                  value = '-(clequ3*complex(0,1)*yc*ym)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_521 = Coupling(name = 'GC_521',
                  value = '(clequ3*complex(0,1)*yc*ym)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_522 = Coupling(name = 'GC_522',
                  value = '(cledq*complex(0,1)*ydo*ym)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_523 = Coupling(name = 'GC_523',
                  value = '-((ceW*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_524 = Coupling(name = 'GC_524',
                  value = '(ceB*cth*complex(0,1)*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_525 = Coupling(name = 'GC_525',
                  value = '-((ceW*cth*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_526 = Coupling(name = 'GC_526',
                  value = '(ceB*cth*complex(0,1)*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*vevhat*ym)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_527 = Coupling(name = 'GC_527',
                  value = '(dGf*complex(0,1)*ym)/2. - (cHbox*complex(0,1)*vevhat**2*ym)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ym)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '(cHbox*dGf*complex(0,1)*vevhat**2*ym)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*ym)/(8.*LambdaSMEFT**2)',
                  order = {'NP':2,'QED':1})

GC_529 = Coupling(name = 'GC_529',
                  value = '-(ceH*cHbox*complex(0,1)*vevhat**4*ym)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (ceH*cHDD*complex(0,1)*vevhat**4*ym)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '(cdG*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_532 = Coupling(name = 'GC_532',
                  value = '(cdW*complex(0,1)*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_533 = Coupling(name = 'GC_533',
                  value = '(cdG*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_534 = Coupling(name = 'GC_534',
                  value = '(3*cdH*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_535 = Coupling(name = 'GC_535',
                  value = '(cdW*complex(0,1)*vevhat*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_536 = Coupling(name = 'GC_536',
                  value = '-((cdW*ee*complex(0,1)*vevhat*ys)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':3})

GC_537 = Coupling(name = 'GC_537',
                  value = '(cdG*G*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_538 = Coupling(name = 'GC_538',
                  value = '(cdW*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_539 = Coupling(name = 'GC_539',
                  value = '(cdW*cth*ee*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_540 = Coupling(name = 'GC_540',
                  value = '(cdH*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_541 = Coupling(name = 'GC_541',
                  value = '(cquqd1*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_542 = Coupling(name = 'GC_542',
                  value = '(cquqd8*complex(0,1)*yc*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_543 = Coupling(name = 'GC_543',
                  value = '(cledq*complex(0,1)*ye*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_544 = Coupling(name = 'GC_544',
                  value = '(cledq*complex(0,1)*ym*ys)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_545 = Coupling(name = 'GC_545',
                  value = '-((cdW*cth*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB*complex(0,1)*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_546 = Coupling(name = 'GC_546',
                  value = '(cdB*cth*complex(0,1)*ys)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW*complex(0,1)*sth*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_547 = Coupling(name = 'GC_547',
                  value = '-((cdW*cth*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))) - (cdB*complex(0,1)*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_548 = Coupling(name = 'GC_548',
                  value = '(cdB*cth*complex(0,1)*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cdW*complex(0,1)*sth*vevhat*ys)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_549 = Coupling(name = 'GC_549',
                  value = '(dGf*complex(0,1)*ys)/2. - (cHbox*complex(0,1)*vevhat**2*ys)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ys)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '(cHbox*dGf*complex(0,1)*vevhat**2*ys)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*ys)/(8.*LambdaSMEFT**2)',
                  order = {'NP':2,'QED':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '-(cdH*cHbox*complex(0,1)*vevhat**4*ys)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cdH*cHDD*complex(0,1)*vevhat**4*ys)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '(cuG*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_554 = Coupling(name = 'GC_554',
                  value = '(cuW*complex(0,1)*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_555 = Coupling(name = 'GC_555',
                  value = '(cuG*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_556 = Coupling(name = 'GC_556',
                  value = '(3*cuH*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_557 = Coupling(name = 'GC_557',
                  value = '(cuW*complex(0,1)*vevhat*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_558 = Coupling(name = 'GC_558',
                  value = '(cuW*ee*complex(0,1)*vevhat*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_559 = Coupling(name = 'GC_559',
                  value = '(cuG*G*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_560 = Coupling(name = 'GC_560',
                  value = '-((cuW*ee*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':3})

GC_561 = Coupling(name = 'GC_561',
                  value = '-((cth*cuW*ee*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':3})

GC_562 = Coupling(name = 'GC_562',
                  value = '(cuH*complex(0,1)*vevhat**2*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '(cquqd1*complex(0,1)*yb*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_564 = Coupling(name = 'GC_564',
                  value = '(cquqd8*complex(0,1)*yb*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_565 = Coupling(name = 'GC_565',
                  value = '(cquqd1*complex(0,1)*ydo*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_566 = Coupling(name = 'GC_566',
                  value = '(cquqd8*complex(0,1)*ydo*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_567 = Coupling(name = 'GC_567',
                  value = '-((clequ1*complex(0,1)*ye*yt)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_568 = Coupling(name = 'GC_568',
                  value = '-(clequ3*complex(0,1)*ye*yt)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_569 = Coupling(name = 'GC_569',
                  value = '(clequ3*complex(0,1)*ye*yt)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_570 = Coupling(name = 'GC_570',
                  value = '-((clequ1*complex(0,1)*ym*yt)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_571 = Coupling(name = 'GC_571',
                  value = '-(clequ3*complex(0,1)*ym*yt)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_572 = Coupling(name = 'GC_572',
                  value = '(clequ3*complex(0,1)*ym*yt)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_573 = Coupling(name = 'GC_573',
                  value = '(cquqd1*complex(0,1)*ys*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_574 = Coupling(name = 'GC_574',
                  value = '(cquqd8*complex(0,1)*ys*yt)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_575 = Coupling(name = 'GC_575',
                  value = '(cth*cuW*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_576 = Coupling(name = 'GC_576',
                  value = '(cth*cuB*complex(0,1)*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW*complex(0,1)*sth*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_577 = Coupling(name = 'GC_577',
                  value = '(cth*cuW*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB*complex(0,1)*sth*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_578 = Coupling(name = 'GC_578',
                  value = '(cth*cuB*complex(0,1)*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW*complex(0,1)*sth*vevhat*yt)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_579 = Coupling(name = 'GC_579',
                  value = '(dGf*complex(0,1)*yt)/2. - (cHbox*complex(0,1)*vevhat**2*yt)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yt)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_580 = Coupling(name = 'GC_580',
                  value = '(cHbox*dGf*complex(0,1)*vevhat**2*yt)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*yt)/(8.*LambdaSMEFT**2)',
                  order = {'NP':2,'QED':1})

GC_581 = Coupling(name = 'GC_581',
                  value = '-(cHbox*cuH*complex(0,1)*vevhat**4*yt)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*cuH*complex(0,1)*vevhat**4*yt)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_582 = Coupling(name = 'GC_582',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_583 = Coupling(name = 'GC_583',
                  value = '(ceW*complex(0,1)*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_584 = Coupling(name = 'GC_584',
                  value = '(cledq*complex(0,1)*I3b11*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_585 = Coupling(name = 'GC_585',
                  value = '(cledq*complex(0,1)*I3b12*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_586 = Coupling(name = 'GC_586',
                  value = '(cledq*complex(0,1)*I3b13*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_587 = Coupling(name = 'GC_587',
                  value = '(cledq*complex(0,1)*I3b21*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_588 = Coupling(name = 'GC_588',
                  value = '(cledq*complex(0,1)*I3b22*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_589 = Coupling(name = 'GC_589',
                  value = '(cledq*complex(0,1)*I3b23*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_590 = Coupling(name = 'GC_590',
                  value = '(cledq*complex(0,1)*I3b31*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_591 = Coupling(name = 'GC_591',
                  value = '(cledq*complex(0,1)*I3b32*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_592 = Coupling(name = 'GC_592',
                  value = '(cledq*complex(0,1)*I3b33*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_593 = Coupling(name = 'GC_593',
                  value = '(clequ1*complex(0,1)*I4b11*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_594 = Coupling(name = 'GC_594',
                  value = '(clequ3*complex(0,1)*I4b11*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_595 = Coupling(name = 'GC_595',
                  value = '-(clequ3*complex(0,1)*I4b11*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_596 = Coupling(name = 'GC_596',
                  value = '(clequ1*complex(0,1)*I4b12*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_597 = Coupling(name = 'GC_597',
                  value = '(clequ3*complex(0,1)*I4b12*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_598 = Coupling(name = 'GC_598',
                  value = '-(clequ3*complex(0,1)*I4b12*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_599 = Coupling(name = 'GC_599',
                  value = '(clequ1*complex(0,1)*I4b13*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_600 = Coupling(name = 'GC_600',
                  value = '(clequ3*complex(0,1)*I4b13*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_601 = Coupling(name = 'GC_601',
                  value = '-(clequ3*complex(0,1)*I4b13*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_602 = Coupling(name = 'GC_602',
                  value = '(clequ1*complex(0,1)*I4b21*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_603 = Coupling(name = 'GC_603',
                  value = '(clequ3*complex(0,1)*I4b21*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_604 = Coupling(name = 'GC_604',
                  value = '-(clequ3*complex(0,1)*I4b21*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_605 = Coupling(name = 'GC_605',
                  value = '(clequ1*complex(0,1)*I4b22*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_606 = Coupling(name = 'GC_606',
                  value = '(clequ3*complex(0,1)*I4b22*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_607 = Coupling(name = 'GC_607',
                  value = '-(clequ3*complex(0,1)*I4b22*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_608 = Coupling(name = 'GC_608',
                  value = '(clequ1*complex(0,1)*I4b23*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_609 = Coupling(name = 'GC_609',
                  value = '(clequ3*complex(0,1)*I4b23*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_610 = Coupling(name = 'GC_610',
                  value = '-(clequ3*complex(0,1)*I4b23*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_611 = Coupling(name = 'GC_611',
                  value = '(clequ1*complex(0,1)*I4b31*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_612 = Coupling(name = 'GC_612',
                  value = '(clequ3*complex(0,1)*I4b31*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_613 = Coupling(name = 'GC_613',
                  value = '-(clequ3*complex(0,1)*I4b31*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_614 = Coupling(name = 'GC_614',
                  value = '(clequ1*complex(0,1)*I4b32*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_615 = Coupling(name = 'GC_615',
                  value = '(clequ3*complex(0,1)*I4b32*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_616 = Coupling(name = 'GC_616',
                  value = '-(clequ3*complex(0,1)*I4b32*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_617 = Coupling(name = 'GC_617',
                  value = '(clequ1*complex(0,1)*I4b33*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_618 = Coupling(name = 'GC_618',
                  value = '(clequ3*complex(0,1)*I4b33*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_619 = Coupling(name = 'GC_619',
                  value = '-(clequ3*complex(0,1)*I4b33*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_620 = Coupling(name = 'GC_620',
                  value = '(3*ceH*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_621 = Coupling(name = 'GC_621',
                  value = '(ceW*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_622 = Coupling(name = 'GC_622',
                  value = '-((ceW*ee*complex(0,1)*vevhat*ytau)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':3})

GC_623 = Coupling(name = 'GC_623',
                  value = '(ceW*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_624 = Coupling(name = 'GC_624',
                  value = '(ceW*cth*ee*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*sth)',
                  order = {'NP':1,'QED':3})

GC_625 = Coupling(name = 'GC_625',
                  value = '(ceH*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_626 = Coupling(name = 'GC_626',
                  value = '(cledq*complex(0,1)*yb*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_627 = Coupling(name = 'GC_627',
                  value = '-((clequ1*complex(0,1)*yc*ytau)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_628 = Coupling(name = 'GC_628',
                  value = '-(clequ3*complex(0,1)*yc*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_629 = Coupling(name = 'GC_629',
                  value = '(clequ3*complex(0,1)*yc*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_630 = Coupling(name = 'GC_630',
                  value = '(cledq*complex(0,1)*ydo*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_631 = Coupling(name = 'GC_631',
                  value = '(cledq*complex(0,1)*ys*ytau)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_632 = Coupling(name = 'GC_632',
                  value = '-((clequ1*complex(0,1)*yt*ytau)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_633 = Coupling(name = 'GC_633',
                  value = '-(clequ3*complex(0,1)*yt*ytau)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_634 = Coupling(name = 'GC_634',
                  value = '(clequ3*complex(0,1)*yt*ytau)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_635 = Coupling(name = 'GC_635',
                  value = '-((ceW*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_636 = Coupling(name = 'GC_636',
                  value = '(ceB*cth*complex(0,1)*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_637 = Coupling(name = 'GC_637',
                  value = '-((ceW*cth*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))) - (ceB*complex(0,1)*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_638 = Coupling(name = 'GC_638',
                  value = '(ceB*cth*complex(0,1)*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) - (ceW*complex(0,1)*sth*vevhat*ytau)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_639 = Coupling(name = 'GC_639',
                  value = '(dGf*complex(0,1)*ytau)/2. - (cHbox*complex(0,1)*vevhat**2*ytau)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*ytau)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_640 = Coupling(name = 'GC_640',
                  value = '(cHbox*dGf*complex(0,1)*vevhat**2*ytau)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*ytau)/(8.*LambdaSMEFT**2)',
                  order = {'NP':2,'QED':1})

GC_641 = Coupling(name = 'GC_641',
                  value = '-(ceH*cHbox*complex(0,1)*vevhat**4*ytau)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (ceH*cHDD*complex(0,1)*vevhat**4*ytau)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_642 = Coupling(name = 'GC_642',
                  value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_643 = Coupling(name = 'GC_643',
                  value = '(cuG*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_644 = Coupling(name = 'GC_644',
                  value = '(cuW*complex(0,1)*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_645 = Coupling(name = 'GC_645',
                  value = '(cuG*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_646 = Coupling(name = 'GC_646',
                  value = '(3*cuH*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_647 = Coupling(name = 'GC_647',
                  value = '(cuW*complex(0,1)*vevhat*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_648 = Coupling(name = 'GC_648',
                  value = '(cuW*ee*complex(0,1)*vevhat*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_649 = Coupling(name = 'GC_649',
                  value = '(cuG*G*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_650 = Coupling(name = 'GC_650',
                  value = '-((cuW*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':3})

GC_651 = Coupling(name = 'GC_651',
                  value = '-((cth*cuW*ee*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':3})

GC_652 = Coupling(name = 'GC_652',
                  value = '(cuH*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_653 = Coupling(name = 'GC_653',
                  value = '(cquqd1*complex(0,1)*yb*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_654 = Coupling(name = 'GC_654',
                  value = '(cquqd8*complex(0,1)*yb*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_655 = Coupling(name = 'GC_655',
                  value = '(cquqd1*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_656 = Coupling(name = 'GC_656',
                  value = '(cquqd8*complex(0,1)*ydo*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_657 = Coupling(name = 'GC_657',
                  value = '-((clequ1*complex(0,1)*ye*yup)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_658 = Coupling(name = 'GC_658',
                  value = '-(clequ3*complex(0,1)*ye*yup)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_659 = Coupling(name = 'GC_659',
                  value = '(clequ3*complex(0,1)*ye*yup)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_660 = Coupling(name = 'GC_660',
                  value = '-((clequ1*complex(0,1)*ym*yup)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_661 = Coupling(name = 'GC_661',
                  value = '-(clequ3*complex(0,1)*ym*yup)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_662 = Coupling(name = 'GC_662',
                  value = '(clequ3*complex(0,1)*ym*yup)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_663 = Coupling(name = 'GC_663',
                  value = '(cquqd1*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_664 = Coupling(name = 'GC_664',
                  value = '(cquqd8*complex(0,1)*ys*yup)/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_665 = Coupling(name = 'GC_665',
                  value = '-((clequ1*complex(0,1)*ytau*yup)/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_666 = Coupling(name = 'GC_666',
                  value = '-(clequ3*complex(0,1)*ytau*yup)/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_667 = Coupling(name = 'GC_667',
                  value = '(clequ3*complex(0,1)*ytau*yup)/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_668 = Coupling(name = 'GC_668',
                  value = '(cth*cuW*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_669 = Coupling(name = 'GC_669',
                  value = '(cth*cuB*complex(0,1)*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW*complex(0,1)*sth*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_670 = Coupling(name = 'GC_670',
                  value = '(cth*cuW*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) - (cuB*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_671 = Coupling(name = 'GC_671',
                  value = '(cth*cuB*complex(0,1)*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cuW*complex(0,1)*sth*vevhat*yup)/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_672 = Coupling(name = 'GC_672',
                  value = '(dGf*complex(0,1)*yup)/2. - (cHbox*complex(0,1)*vevhat**2*yup)/(LambdaSMEFT**2*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**2*yup)/(4.*LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '(cHbox*dGf*complex(0,1)*vevhat**2*yup)/(2.*LambdaSMEFT**2) - (cHDD*dGf*complex(0,1)*vevhat**2*yup)/(8.*LambdaSMEFT**2)',
                  order = {'NP':2,'QED':1})

GC_674 = Coupling(name = 'GC_674',
                  value = '-(cHbox*cuH*complex(0,1)*vevhat**4*yup)/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*cuH*complex(0,1)*vevhat**4*yup)/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '(complex(0,1)*yb*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_676 = Coupling(name = 'GC_676',
                  value = '(complex(0,1)*vevhat*yb*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_677 = Coupling(name = 'GC_677',
                  value = '(G*vevhat*yb*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_678 = Coupling(name = 'GC_678',
                  value = '(complex(0,1)*ydo*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_679 = Coupling(name = 'GC_679',
                  value = '(complex(0,1)*vevhat*ydo*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_680 = Coupling(name = 'GC_680',
                  value = '(G*vevhat*ydo*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_681 = Coupling(name = 'GC_681',
                  value = '(complex(0,1)*ys*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_682 = Coupling(name = 'GC_682',
                  value = '(complex(0,1)*vevhat*ys*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_683 = Coupling(name = 'GC_683',
                  value = '(G*vevhat*ys*complexconjugate(cdG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QCD':1,'QED':2})

GC_684 = Coupling(name = 'GC_684',
                  value = '(3*complex(0,1)*vevhat*yb*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_685 = Coupling(name = 'GC_685',
                  value = '(complex(0,1)*vevhat**2*yb*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_686 = Coupling(name = 'GC_686',
                  value = '(3*complex(0,1)*vevhat*ydo*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_687 = Coupling(name = 'GC_687',
                  value = '(complex(0,1)*vevhat**2*ydo*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_688 = Coupling(name = 'GC_688',
                  value = '(3*complex(0,1)*vevhat*ys*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_689 = Coupling(name = 'GC_689',
                  value = '(complex(0,1)*vevhat**2*ys*complexconjugate(cdH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_690 = Coupling(name = 'GC_690',
                  value = '-(cHbox*complex(0,1)*vevhat**4*yb*complexconjugate(cdH))/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**4*yb*complexconjugate(cdH))/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_691 = Coupling(name = 'GC_691',
                  value = '-(cHbox*complex(0,1)*vevhat**4*ydo*complexconjugate(cdH))/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**4*ydo*complexconjugate(cdH))/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_692 = Coupling(name = 'GC_692',
                  value = '-(cHbox*complex(0,1)*vevhat**4*ys*complexconjugate(cdH))/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**4*ys*complexconjugate(cdH))/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_693 = Coupling(name = 'GC_693',
                  value = '(complex(0,1)*yb*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_694 = Coupling(name = 'GC_694',
                  value = '(complex(0,1)*vevhat*yb*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_695 = Coupling(name = 'GC_695',
                  value = '(ee*complex(0,1)*vevhat*yb*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_696 = Coupling(name = 'GC_696',
                  value = '(ee*complex(0,1)*vevhat*yb*complexconjugate(cdW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_697 = Coupling(name = 'GC_697',
                  value = '-((cth*ee*complex(0,1)*vevhat*yb*complexconjugate(cdW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':3})

GC_698 = Coupling(name = 'GC_698',
                  value = '(complex(0,1)*ydo*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_699 = Coupling(name = 'GC_699',
                  value = '(complex(0,1)*vevhat*ydo*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_700 = Coupling(name = 'GC_700',
                  value = '(ee*complex(0,1)*vevhat*ydo*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_701 = Coupling(name = 'GC_701',
                  value = '(ee*complex(0,1)*vevhat*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_702 = Coupling(name = 'GC_702',
                  value = '-((cth*ee*complex(0,1)*vevhat*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':3})

GC_703 = Coupling(name = 'GC_703',
                  value = '(complex(0,1)*ys*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_704 = Coupling(name = 'GC_704',
                  value = '(complex(0,1)*vevhat*ys*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_705 = Coupling(name = 'GC_705',
                  value = '(ee*complex(0,1)*vevhat*ys*complexconjugate(cdW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_706 = Coupling(name = 'GC_706',
                  value = '(ee*complex(0,1)*vevhat*ys*complexconjugate(cdW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_707 = Coupling(name = 'GC_707',
                  value = '-((cth*ee*complex(0,1)*vevhat*ys*complexconjugate(cdW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':3})

GC_708 = Coupling(name = 'GC_708',
                  value = '-((complex(0,1)*sth*yb*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*yb*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_709 = Coupling(name = 'GC_709',
                  value = '(cth*complex(0,1)*yb*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*yb*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_710 = Coupling(name = 'GC_710',
                  value = '-((complex(0,1)*sth*vevhat*yb*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*yb*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_711 = Coupling(name = 'GC_711',
                  value = '(cth*complex(0,1)*vevhat*yb*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*yb*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_712 = Coupling(name = 'GC_712',
                  value = '-((complex(0,1)*sth*ydo*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_713 = Coupling(name = 'GC_713',
                  value = '(cth*complex(0,1)*ydo*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_714 = Coupling(name = 'GC_714',
                  value = '-((complex(0,1)*sth*vevhat*ydo*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_715 = Coupling(name = 'GC_715',
                  value = '(cth*complex(0,1)*vevhat*ydo*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*ydo*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_716 = Coupling(name = 'GC_716',
                  value = '-((complex(0,1)*sth*ys*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*ys*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_717 = Coupling(name = 'GC_717',
                  value = '(cth*complex(0,1)*ys*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*ys*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_718 = Coupling(name = 'GC_718',
                  value = '-((complex(0,1)*sth*vevhat*ys*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*ys*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_719 = Coupling(name = 'GC_719',
                  value = '(cth*complex(0,1)*vevhat*ys*complexconjugate(cdB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*ys*complexconjugate(cdW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_720 = Coupling(name = 'GC_720',
                  value = '(3*complex(0,1)*vevhat*ye*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_721 = Coupling(name = 'GC_721',
                  value = '(complex(0,1)*vevhat**2*ye*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_722 = Coupling(name = 'GC_722',
                  value = '(3*complex(0,1)*vevhat*ym*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_723 = Coupling(name = 'GC_723',
                  value = '(complex(0,1)*vevhat**2*ym*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_724 = Coupling(name = 'GC_724',
                  value = '(3*complex(0,1)*vevhat*ytau*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_725 = Coupling(name = 'GC_725',
                  value = '(complex(0,1)*vevhat**2*ytau*complexconjugate(ceH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_726 = Coupling(name = 'GC_726',
                  value = '-(cHbox*complex(0,1)*vevhat**4*ye*complexconjugate(ceH))/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**4*ye*complexconjugate(ceH))/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_727 = Coupling(name = 'GC_727',
                  value = '-(cHbox*complex(0,1)*vevhat**4*ym*complexconjugate(ceH))/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**4*ym*complexconjugate(ceH))/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_728 = Coupling(name = 'GC_728',
                  value = '-(cHbox*complex(0,1)*vevhat**4*ytau*complexconjugate(ceH))/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**4*ytau*complexconjugate(ceH))/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                  order = {'NP':2,'QED':1})

GC_729 = Coupling(name = 'GC_729',
                  value = '(complex(0,1)*ye*complexconjugate(ceW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_730 = Coupling(name = 'GC_730',
                  value = '(complex(0,1)*vevhat*ye*complexconjugate(ceW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_731 = Coupling(name = 'GC_731',
                  value = '(ee*complex(0,1)*vevhat*ye*complexconjugate(ceW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_732 = Coupling(name = 'GC_732',
                  value = '(ee*complex(0,1)*vevhat*ye*complexconjugate(ceW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_733 = Coupling(name = 'GC_733',
                  value = '-((cth*ee*complex(0,1)*vevhat*ye*complexconjugate(ceW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':3})

GC_734 = Coupling(name = 'GC_734',
                  value = '(complex(0,1)*ym*complexconjugate(ceW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_735 = Coupling(name = 'GC_735',
                  value = '(complex(0,1)*vevhat*ym*complexconjugate(ceW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_736 = Coupling(name = 'GC_736',
                  value = '(ee*complex(0,1)*vevhat*ym*complexconjugate(ceW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_737 = Coupling(name = 'GC_737',
                  value = '(ee*complex(0,1)*vevhat*ym*complexconjugate(ceW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_738 = Coupling(name = 'GC_738',
                  value = '-((cth*ee*complex(0,1)*vevhat*ym*complexconjugate(ceW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':3})

GC_739 = Coupling(name = 'GC_739',
                  value = '(complex(0,1)*ytau*complexconjugate(ceW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_740 = Coupling(name = 'GC_740',
                  value = '(complex(0,1)*vevhat*ytau*complexconjugate(ceW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':2})

GC_741 = Coupling(name = 'GC_741',
                  value = '(ee*complex(0,1)*vevhat*ytau*complexconjugate(ceW))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':3})

GC_742 = Coupling(name = 'GC_742',
                  value = '(ee*complex(0,1)*vevhat*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_743 = Coupling(name = 'GC_743',
                  value = '-((cth*ee*complex(0,1)*vevhat*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*sth))',
                  order = {'NP':1,'QED':3})

GC_744 = Coupling(name = 'GC_744',
                  value = '-((complex(0,1)*sth*ye*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*ye*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_745 = Coupling(name = 'GC_745',
                  value = '(cth*complex(0,1)*ye*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*ye*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_746 = Coupling(name = 'GC_746',
                  value = '-((complex(0,1)*sth*vevhat*ye*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*ye*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_747 = Coupling(name = 'GC_747',
                  value = '(cth*complex(0,1)*vevhat*ye*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*ye*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_748 = Coupling(name = 'GC_748',
                  value = '-((complex(0,1)*sth*ym*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*ym*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_749 = Coupling(name = 'GC_749',
                  value = '(cth*complex(0,1)*ym*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*ym*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_750 = Coupling(name = 'GC_750',
                  value = '-((complex(0,1)*sth*vevhat*ym*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*ym*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_751 = Coupling(name = 'GC_751',
                  value = '(cth*complex(0,1)*vevhat*ym*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*ym*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_752 = Coupling(name = 'GC_752',
                  value = '-((complex(0,1)*sth*ytau*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_753 = Coupling(name = 'GC_753',
                  value = '(cth*complex(0,1)*ytau*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_754 = Coupling(name = 'GC_754',
                  value = '-((complex(0,1)*sth*vevhat*ytau*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2))) - (cth*complex(0,1)*vevhat*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_755 = Coupling(name = 'GC_755',
                  value = '(cth*complex(0,1)*vevhat*ytau*complexconjugate(ceB))/(LambdaSMEFT**2*cmath.sqrt(2)) - (complex(0,1)*sth*vevhat*ytau*complexconjugate(ceW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                  order = {'NP':1,'QED':2})

GC_756 = Coupling(name = 'GC_756',
                  value = '(ee*complex(0,1)*I8b11*vevhat*complexconjugate(cHud))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_757 = Coupling(name = 'GC_757',
                  value = '(ee*complex(0,1)*I8b12*vevhat*complexconjugate(cHud))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_758 = Coupling(name = 'GC_758',
                  value = '(ee*complex(0,1)*I8b13*vevhat*complexconjugate(cHud))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_759 = Coupling(name = 'GC_759',
                  value = '(ee*complex(0,1)*I8b21*vevhat*complexconjugate(cHud))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_760 = Coupling(name = 'GC_760',
                  value = '(ee*complex(0,1)*I8b22*vevhat*complexconjugate(cHud))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_761 = Coupling(name = 'GC_761',
                  value = '(ee*complex(0,1)*I8b23*vevhat*complexconjugate(cHud))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_762 = Coupling(name = 'GC_762',
                  value = '(ee*complex(0,1)*I8b31*vevhat*complexconjugate(cHud))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_763 = Coupling(name = 'GC_763',
                  value = '(ee*complex(0,1)*I8b32*vevhat*complexconjugate(cHud))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_764 = Coupling(name = 'GC_764',
                  value = '(ee*complex(0,1)*I8b33*vevhat*complexconjugate(cHud))/(LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':4})

GC_765 = Coupling(name = 'GC_765',
                  value = '(ee*complex(0,1)*I8b11*vevhat**2*complexconjugate(cHud))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_766 = Coupling(name = 'GC_766',
                  value = '(ee*complex(0,1)*I8b12*vevhat**2*complexconjugate(cHud))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_767 = Coupling(name = 'GC_767',
                  value = '(ee*complex(0,1)*I8b13*vevhat**2*complexconjugate(cHud))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_768 = Coupling(name = 'GC_768',
                  value = '(ee*complex(0,1)*I8b21*vevhat**2*complexconjugate(cHud))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_769 = Coupling(name = 'GC_769',
                  value = '(ee*complex(0,1)*I8b22*vevhat**2*complexconjugate(cHud))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_770 = Coupling(name = 'GC_770',
                  value = '(ee*complex(0,1)*I8b23*vevhat**2*complexconjugate(cHud))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_771 = Coupling(name = 'GC_771',
                  value = '(ee*complex(0,1)*I8b31*vevhat**2*complexconjugate(cHud))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_772 = Coupling(name = 'GC_772',
                  value = '(ee*complex(0,1)*I8b32*vevhat**2*complexconjugate(cHud))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_773 = Coupling(name = 'GC_773',
                  value = '(ee*complex(0,1)*I8b33*vevhat**2*complexconjugate(cHud))/(2.*LambdaSMEFT**2*sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':3})

GC_774 = Coupling(name = 'GC_774',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM1x1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_775 = Coupling(name = 'GC_775',
                  value = '-((cHq3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM1x1))/(sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_776 = Coupling(name = 'GC_776',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM1x2))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_777 = Coupling(name = 'GC_777',
                  value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM1x2))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_778 = Coupling(name = 'GC_778',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM1x3))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_779 = Coupling(name = 'GC_779',
                  value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM1x3))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_780 = Coupling(name = 'GC_780',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM2x1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_781 = Coupling(name = 'GC_781',
                  value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM2x1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_782 = Coupling(name = 'GC_782',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM2x2))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_783 = Coupling(name = 'GC_783',
                  value = '-((cHq3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM2x2))/(sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_784 = Coupling(name = 'GC_784',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM2x3))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_785 = Coupling(name = 'GC_785',
                  value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM2x3))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_786 = Coupling(name = 'GC_786',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM3x1))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_787 = Coupling(name = 'GC_787',
                  value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM3x1))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_788 = Coupling(name = 'GC_788',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM3x2))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_789 = Coupling(name = 'GC_789',
                  value = '-((dgw*ee*complex(0,1)*complexconjugate(CKM3x2))/(sth*cmath.sqrt(2)))',
                  order = {'NP':1,'QED':1})

GC_790 = Coupling(name = 'GC_790',
                  value = '-((ee*complex(0,1)*complexconjugate(CKM3x3))/(sth*cmath.sqrt(2)))',
                  order = {'QED':1})

GC_791 = Coupling(name = 'GC_791',
                  value = '-((cHq3*ee*complex(0,1)*vevhat**2)/(LambdaSMEFT**2*sth*cmath.sqrt(2))) - (dgw*ee*complex(0,1)*complexconjugate(CKM3x3))/(sth*cmath.sqrt(2))',
                  order = {'NP':1,'QED':1})

GC_792 = Coupling(name = 'GC_792',
                  value = '(complex(0,1)*I1b11*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_793 = Coupling(name = 'GC_793',
                  value = '(complex(0,1)*I1b12*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_794 = Coupling(name = 'GC_794',
                  value = '(complex(0,1)*I1b13*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_795 = Coupling(name = 'GC_795',
                  value = '(complex(0,1)*I1b21*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_796 = Coupling(name = 'GC_796',
                  value = '(complex(0,1)*I1b22*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_797 = Coupling(name = 'GC_797',
                  value = '(complex(0,1)*I1b23*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_798 = Coupling(name = 'GC_798',
                  value = '(complex(0,1)*I1b31*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_799 = Coupling(name = 'GC_799',
                  value = '(complex(0,1)*I1b32*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_800 = Coupling(name = 'GC_800',
                  value = '(complex(0,1)*I1b33*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_801 = Coupling(name = 'GC_801',
                  value = '(complex(0,1)*yb*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_802 = Coupling(name = 'GC_802',
                  value = '(complex(0,1)*ydo*ye*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_803 = Coupling(name = 'GC_803',
                  value = '(complex(0,1)*I1b11*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_804 = Coupling(name = 'GC_804',
                  value = '(complex(0,1)*I1b12*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_805 = Coupling(name = 'GC_805',
                  value = '(complex(0,1)*I1b13*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_806 = Coupling(name = 'GC_806',
                  value = '(complex(0,1)*I1b21*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_807 = Coupling(name = 'GC_807',
                  value = '(complex(0,1)*I1b22*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_808 = Coupling(name = 'GC_808',
                  value = '(complex(0,1)*I1b23*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_809 = Coupling(name = 'GC_809',
                  value = '(complex(0,1)*I1b31*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_810 = Coupling(name = 'GC_810',
                  value = '(complex(0,1)*I1b32*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_811 = Coupling(name = 'GC_811',
                  value = '(complex(0,1)*I1b33*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_812 = Coupling(name = 'GC_812',
                  value = '(complex(0,1)*yb*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_813 = Coupling(name = 'GC_813',
                  value = '(complex(0,1)*ydo*ym*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_814 = Coupling(name = 'GC_814',
                  value = '(complex(0,1)*ye*ys*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_815 = Coupling(name = 'GC_815',
                  value = '(complex(0,1)*ym*ys*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_816 = Coupling(name = 'GC_816',
                  value = '(complex(0,1)*I1b11*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_817 = Coupling(name = 'GC_817',
                  value = '(complex(0,1)*I1b12*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_818 = Coupling(name = 'GC_818',
                  value = '(complex(0,1)*I1b13*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_819 = Coupling(name = 'GC_819',
                  value = '(complex(0,1)*I1b21*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_820 = Coupling(name = 'GC_820',
                  value = '(complex(0,1)*I1b22*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_821 = Coupling(name = 'GC_821',
                  value = '(complex(0,1)*I1b23*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_822 = Coupling(name = 'GC_822',
                  value = '(complex(0,1)*I1b31*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_823 = Coupling(name = 'GC_823',
                  value = '(complex(0,1)*I1b32*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_824 = Coupling(name = 'GC_824',
                  value = '(complex(0,1)*I1b33*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_825 = Coupling(name = 'GC_825',
                  value = '(complex(0,1)*yb*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_826 = Coupling(name = 'GC_826',
                  value = '(complex(0,1)*ydo*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_827 = Coupling(name = 'GC_827',
                  value = '(complex(0,1)*ys*ytau*complexconjugate(cledq))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_828 = Coupling(name = 'GC_828',
                  value = '(complex(0,1)*I2b11*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_829 = Coupling(name = 'GC_829',
                  value = '(complex(0,1)*I2b12*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_830 = Coupling(name = 'GC_830',
                  value = '(complex(0,1)*I2b13*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_831 = Coupling(name = 'GC_831',
                  value = '(complex(0,1)*I2b21*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_832 = Coupling(name = 'GC_832',
                  value = '(complex(0,1)*I2b22*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_833 = Coupling(name = 'GC_833',
                  value = '(complex(0,1)*I2b23*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_834 = Coupling(name = 'GC_834',
                  value = '(complex(0,1)*I2b31*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_835 = Coupling(name = 'GC_835',
                  value = '(complex(0,1)*I2b32*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_836 = Coupling(name = 'GC_836',
                  value = '(complex(0,1)*I2b33*ye*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_837 = Coupling(name = 'GC_837',
                  value = '-((complex(0,1)*yc*ye*complexconjugate(clequ1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_838 = Coupling(name = 'GC_838',
                  value = '(complex(0,1)*I2b11*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_839 = Coupling(name = 'GC_839',
                  value = '(complex(0,1)*I2b12*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_840 = Coupling(name = 'GC_840',
                  value = '(complex(0,1)*I2b13*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_841 = Coupling(name = 'GC_841',
                  value = '(complex(0,1)*I2b21*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_842 = Coupling(name = 'GC_842',
                  value = '(complex(0,1)*I2b22*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_843 = Coupling(name = 'GC_843',
                  value = '(complex(0,1)*I2b23*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_844 = Coupling(name = 'GC_844',
                  value = '(complex(0,1)*I2b31*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_845 = Coupling(name = 'GC_845',
                  value = '(complex(0,1)*I2b32*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_846 = Coupling(name = 'GC_846',
                  value = '(complex(0,1)*I2b33*ym*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_847 = Coupling(name = 'GC_847',
                  value = '-((complex(0,1)*yc*ym*complexconjugate(clequ1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_848 = Coupling(name = 'GC_848',
                  value = '-((complex(0,1)*ye*yt*complexconjugate(clequ1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_849 = Coupling(name = 'GC_849',
                  value = '-((complex(0,1)*ym*yt*complexconjugate(clequ1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_850 = Coupling(name = 'GC_850',
                  value = '(complex(0,1)*I2b11*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_851 = Coupling(name = 'GC_851',
                  value = '(complex(0,1)*I2b12*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_852 = Coupling(name = 'GC_852',
                  value = '(complex(0,1)*I2b13*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_853 = Coupling(name = 'GC_853',
                  value = '(complex(0,1)*I2b21*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_854 = Coupling(name = 'GC_854',
                  value = '(complex(0,1)*I2b22*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_855 = Coupling(name = 'GC_855',
                  value = '(complex(0,1)*I2b23*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_856 = Coupling(name = 'GC_856',
                  value = '(complex(0,1)*I2b31*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_857 = Coupling(name = 'GC_857',
                  value = '(complex(0,1)*I2b32*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_858 = Coupling(name = 'GC_858',
                  value = '(complex(0,1)*I2b33*ytau*complexconjugate(clequ1))/LambdaSMEFT**2',
                  order = {'NP':1,'QED':4})

GC_859 = Coupling(name = 'GC_859',
                  value = '-((complex(0,1)*yc*ytau*complexconjugate(clequ1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_860 = Coupling(name = 'GC_860',
                  value = '-((complex(0,1)*yt*ytau*complexconjugate(clequ1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_861 = Coupling(name = 'GC_861',
                  value = '-((complex(0,1)*ye*yup*complexconjugate(clequ1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_862 = Coupling(name = 'GC_862',
                  value = '-((complex(0,1)*ym*yup*complexconjugate(clequ1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_863 = Coupling(name = 'GC_863',
                  value = '-((complex(0,1)*ytau*yup*complexconjugate(clequ1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_864 = Coupling(name = 'GC_864',
                  value = '(complex(0,1)*I2b11*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_865 = Coupling(name = 'GC_865',
                  value = '-(complex(0,1)*I2b11*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_866 = Coupling(name = 'GC_866',
                  value = '(complex(0,1)*I2b12*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_867 = Coupling(name = 'GC_867',
                  value = '-(complex(0,1)*I2b12*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_868 = Coupling(name = 'GC_868',
                  value = '(complex(0,1)*I2b13*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_869 = Coupling(name = 'GC_869',
                  value = '-(complex(0,1)*I2b13*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_870 = Coupling(name = 'GC_870',
                  value = '(complex(0,1)*I2b21*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_871 = Coupling(name = 'GC_871',
                  value = '-(complex(0,1)*I2b21*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_872 = Coupling(name = 'GC_872',
                  value = '(complex(0,1)*I2b22*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_873 = Coupling(name = 'GC_873',
                  value = '-(complex(0,1)*I2b22*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_874 = Coupling(name = 'GC_874',
                  value = '(complex(0,1)*I2b23*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_875 = Coupling(name = 'GC_875',
                  value = '-(complex(0,1)*I2b23*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_876 = Coupling(name = 'GC_876',
                  value = '(complex(0,1)*I2b31*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_877 = Coupling(name = 'GC_877',
                  value = '-(complex(0,1)*I2b31*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_878 = Coupling(name = 'GC_878',
                  value = '(complex(0,1)*I2b32*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_879 = Coupling(name = 'GC_879',
                  value = '-(complex(0,1)*I2b32*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_880 = Coupling(name = 'GC_880',
                  value = '(complex(0,1)*I2b33*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_881 = Coupling(name = 'GC_881',
                  value = '-(complex(0,1)*I2b33*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_882 = Coupling(name = 'GC_882',
                  value = '-(complex(0,1)*yc*ye*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_883 = Coupling(name = 'GC_883',
                  value = '(complex(0,1)*yc*ye*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_884 = Coupling(name = 'GC_884',
                  value = '(complex(0,1)*I2b11*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_885 = Coupling(name = 'GC_885',
                  value = '-(complex(0,1)*I2b11*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_886 = Coupling(name = 'GC_886',
                  value = '(complex(0,1)*I2b12*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_887 = Coupling(name = 'GC_887',
                  value = '-(complex(0,1)*I2b12*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_888 = Coupling(name = 'GC_888',
                  value = '(complex(0,1)*I2b13*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_889 = Coupling(name = 'GC_889',
                  value = '-(complex(0,1)*I2b13*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_890 = Coupling(name = 'GC_890',
                  value = '(complex(0,1)*I2b21*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_891 = Coupling(name = 'GC_891',
                  value = '-(complex(0,1)*I2b21*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_892 = Coupling(name = 'GC_892',
                  value = '(complex(0,1)*I2b22*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_893 = Coupling(name = 'GC_893',
                  value = '-(complex(0,1)*I2b22*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_894 = Coupling(name = 'GC_894',
                  value = '(complex(0,1)*I2b23*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_895 = Coupling(name = 'GC_895',
                  value = '-(complex(0,1)*I2b23*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_896 = Coupling(name = 'GC_896',
                  value = '(complex(0,1)*I2b31*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_897 = Coupling(name = 'GC_897',
                  value = '-(complex(0,1)*I2b31*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_898 = Coupling(name = 'GC_898',
                  value = '(complex(0,1)*I2b32*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_899 = Coupling(name = 'GC_899',
                  value = '-(complex(0,1)*I2b32*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_900 = Coupling(name = 'GC_900',
                  value = '(complex(0,1)*I2b33*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_901 = Coupling(name = 'GC_901',
                  value = '-(complex(0,1)*I2b33*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_902 = Coupling(name = 'GC_902',
                  value = '-(complex(0,1)*yc*ym*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_903 = Coupling(name = 'GC_903',
                  value = '(complex(0,1)*yc*ym*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_904 = Coupling(name = 'GC_904',
                  value = '-(complex(0,1)*ye*yt*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_905 = Coupling(name = 'GC_905',
                  value = '(complex(0,1)*ye*yt*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_906 = Coupling(name = 'GC_906',
                  value = '-(complex(0,1)*ym*yt*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_907 = Coupling(name = 'GC_907',
                  value = '(complex(0,1)*ym*yt*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_908 = Coupling(name = 'GC_908',
                  value = '(complex(0,1)*I2b11*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_909 = Coupling(name = 'GC_909',
                  value = '-(complex(0,1)*I2b11*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_910 = Coupling(name = 'GC_910',
                  value = '(complex(0,1)*I2b12*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_911 = Coupling(name = 'GC_911',
                  value = '-(complex(0,1)*I2b12*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_912 = Coupling(name = 'GC_912',
                  value = '(complex(0,1)*I2b13*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_913 = Coupling(name = 'GC_913',
                  value = '-(complex(0,1)*I2b13*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_914 = Coupling(name = 'GC_914',
                  value = '(complex(0,1)*I2b21*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_915 = Coupling(name = 'GC_915',
                  value = '-(complex(0,1)*I2b21*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_916 = Coupling(name = 'GC_916',
                  value = '(complex(0,1)*I2b22*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_917 = Coupling(name = 'GC_917',
                  value = '-(complex(0,1)*I2b22*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_918 = Coupling(name = 'GC_918',
                  value = '(complex(0,1)*I2b23*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_919 = Coupling(name = 'GC_919',
                  value = '-(complex(0,1)*I2b23*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_920 = Coupling(name = 'GC_920',
                  value = '(complex(0,1)*I2b31*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_921 = Coupling(name = 'GC_921',
                  value = '-(complex(0,1)*I2b31*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_922 = Coupling(name = 'GC_922',
                  value = '(complex(0,1)*I2b32*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_923 = Coupling(name = 'GC_923',
                  value = '-(complex(0,1)*I2b32*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_924 = Coupling(name = 'GC_924',
                  value = '(complex(0,1)*I2b33*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_925 = Coupling(name = 'GC_925',
                  value = '-(complex(0,1)*I2b33*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_926 = Coupling(name = 'GC_926',
                  value = '-(complex(0,1)*yc*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_927 = Coupling(name = 'GC_927',
                  value = '(complex(0,1)*yc*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_928 = Coupling(name = 'GC_928',
                  value = '-(complex(0,1)*yt*ytau*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_929 = Coupling(name = 'GC_929',
                  value = '(complex(0,1)*yt*ytau*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_930 = Coupling(name = 'GC_930',
                  value = '-(complex(0,1)*ye*yup*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_931 = Coupling(name = 'GC_931',
                  value = '(complex(0,1)*ye*yup*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_932 = Coupling(name = 'GC_932',
                  value = '-(complex(0,1)*ym*yup*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_933 = Coupling(name = 'GC_933',
                  value = '(complex(0,1)*ym*yup*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_934 = Coupling(name = 'GC_934',
                  value = '-(complex(0,1)*ytau*yup*complexconjugate(clequ3))/(4.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_935 = Coupling(name = 'GC_935',
                  value = '(complex(0,1)*ytau*yup*complexconjugate(clequ3))/(2.*LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_936 = Coupling(name = 'GC_936',
                  value = '-((complex(0,1)*I2b11*I5b11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_937 = Coupling(name = 'GC_937',
                  value = '-((complex(0,1)*I2b12*I5b11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_938 = Coupling(name = 'GC_938',
                  value = '-((complex(0,1)*I2b13*I5b11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_939 = Coupling(name = 'GC_939',
                  value = '-((complex(0,1)*I2b21*I5b11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_940 = Coupling(name = 'GC_940',
                  value = '-((complex(0,1)*I2b22*I5b11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_941 = Coupling(name = 'GC_941',
                  value = '-((complex(0,1)*I2b23*I5b11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_942 = Coupling(name = 'GC_942',
                  value = '-((complex(0,1)*I2b31*I5b11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_943 = Coupling(name = 'GC_943',
                  value = '-((complex(0,1)*I2b32*I5b11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_944 = Coupling(name = 'GC_944',
                  value = '-((complex(0,1)*I2b33*I5b11*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_945 = Coupling(name = 'GC_945',
                  value = '-((complex(0,1)*I2b11*I5b12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_946 = Coupling(name = 'GC_946',
                  value = '-((complex(0,1)*I2b12*I5b12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_947 = Coupling(name = 'GC_947',
                  value = '-((complex(0,1)*I2b13*I5b12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_948 = Coupling(name = 'GC_948',
                  value = '-((complex(0,1)*I2b21*I5b12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_949 = Coupling(name = 'GC_949',
                  value = '-((complex(0,1)*I2b22*I5b12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_950 = Coupling(name = 'GC_950',
                  value = '-((complex(0,1)*I2b23*I5b12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_951 = Coupling(name = 'GC_951',
                  value = '-((complex(0,1)*I2b31*I5b12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_952 = Coupling(name = 'GC_952',
                  value = '-((complex(0,1)*I2b32*I5b12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_953 = Coupling(name = 'GC_953',
                  value = '-((complex(0,1)*I2b33*I5b12*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_954 = Coupling(name = 'GC_954',
                  value = '-((complex(0,1)*I2b11*I5b13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_955 = Coupling(name = 'GC_955',
                  value = '-((complex(0,1)*I2b12*I5b13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_956 = Coupling(name = 'GC_956',
                  value = '-((complex(0,1)*I2b13*I5b13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_957 = Coupling(name = 'GC_957',
                  value = '-((complex(0,1)*I2b21*I5b13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_958 = Coupling(name = 'GC_958',
                  value = '-((complex(0,1)*I2b22*I5b13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_959 = Coupling(name = 'GC_959',
                  value = '-((complex(0,1)*I2b23*I5b13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_960 = Coupling(name = 'GC_960',
                  value = '-((complex(0,1)*I2b31*I5b13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_961 = Coupling(name = 'GC_961',
                  value = '-((complex(0,1)*I2b32*I5b13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_962 = Coupling(name = 'GC_962',
                  value = '-((complex(0,1)*I2b33*I5b13*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_963 = Coupling(name = 'GC_963',
                  value = '-((complex(0,1)*I2b11*I5b21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_964 = Coupling(name = 'GC_964',
                  value = '-((complex(0,1)*I2b12*I5b21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_965 = Coupling(name = 'GC_965',
                  value = '-((complex(0,1)*I2b13*I5b21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_966 = Coupling(name = 'GC_966',
                  value = '-((complex(0,1)*I2b21*I5b21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_967 = Coupling(name = 'GC_967',
                  value = '-((complex(0,1)*I2b22*I5b21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_968 = Coupling(name = 'GC_968',
                  value = '-((complex(0,1)*I2b23*I5b21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_969 = Coupling(name = 'GC_969',
                  value = '-((complex(0,1)*I2b31*I5b21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_970 = Coupling(name = 'GC_970',
                  value = '-((complex(0,1)*I2b32*I5b21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_971 = Coupling(name = 'GC_971',
                  value = '-((complex(0,1)*I2b33*I5b21*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_972 = Coupling(name = 'GC_972',
                  value = '-((complex(0,1)*I2b11*I5b22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_973 = Coupling(name = 'GC_973',
                  value = '-((complex(0,1)*I2b12*I5b22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_974 = Coupling(name = 'GC_974',
                  value = '-((complex(0,1)*I2b13*I5b22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_975 = Coupling(name = 'GC_975',
                  value = '-((complex(0,1)*I2b21*I5b22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_976 = Coupling(name = 'GC_976',
                  value = '-((complex(0,1)*I2b22*I5b22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_977 = Coupling(name = 'GC_977',
                  value = '-((complex(0,1)*I2b23*I5b22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_978 = Coupling(name = 'GC_978',
                  value = '-((complex(0,1)*I2b31*I5b22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_979 = Coupling(name = 'GC_979',
                  value = '-((complex(0,1)*I2b32*I5b22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_980 = Coupling(name = 'GC_980',
                  value = '-((complex(0,1)*I2b33*I5b22*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_981 = Coupling(name = 'GC_981',
                  value = '-((complex(0,1)*I2b11*I5b23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_982 = Coupling(name = 'GC_982',
                  value = '-((complex(0,1)*I2b12*I5b23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_983 = Coupling(name = 'GC_983',
                  value = '-((complex(0,1)*I2b13*I5b23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_984 = Coupling(name = 'GC_984',
                  value = '-((complex(0,1)*I2b21*I5b23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_985 = Coupling(name = 'GC_985',
                  value = '-((complex(0,1)*I2b22*I5b23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_986 = Coupling(name = 'GC_986',
                  value = '-((complex(0,1)*I2b23*I5b23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_987 = Coupling(name = 'GC_987',
                  value = '-((complex(0,1)*I2b31*I5b23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_988 = Coupling(name = 'GC_988',
                  value = '-((complex(0,1)*I2b32*I5b23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_989 = Coupling(name = 'GC_989',
                  value = '-((complex(0,1)*I2b33*I5b23*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_990 = Coupling(name = 'GC_990',
                  value = '-((complex(0,1)*I2b11*I5b31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_991 = Coupling(name = 'GC_991',
                  value = '-((complex(0,1)*I2b12*I5b31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_992 = Coupling(name = 'GC_992',
                  value = '-((complex(0,1)*I2b13*I5b31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_993 = Coupling(name = 'GC_993',
                  value = '-((complex(0,1)*I2b21*I5b31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_994 = Coupling(name = 'GC_994',
                  value = '-((complex(0,1)*I2b22*I5b31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_995 = Coupling(name = 'GC_995',
                  value = '-((complex(0,1)*I2b23*I5b31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_996 = Coupling(name = 'GC_996',
                  value = '-((complex(0,1)*I2b31*I5b31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_997 = Coupling(name = 'GC_997',
                  value = '-((complex(0,1)*I2b32*I5b31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_998 = Coupling(name = 'GC_998',
                  value = '-((complex(0,1)*I2b33*I5b31*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_999 = Coupling(name = 'GC_999',
                  value = '-((complex(0,1)*I2b11*I5b32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                  order = {'NP':1,'QED':4})

GC_1000 = Coupling(name = 'GC_1000',
                   value = '-((complex(0,1)*I2b12*I5b32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1001 = Coupling(name = 'GC_1001',
                   value = '-((complex(0,1)*I2b13*I5b32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1002 = Coupling(name = 'GC_1002',
                   value = '-((complex(0,1)*I2b21*I5b32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1003 = Coupling(name = 'GC_1003',
                   value = '-((complex(0,1)*I2b22*I5b32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1004 = Coupling(name = 'GC_1004',
                   value = '-((complex(0,1)*I2b23*I5b32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1005 = Coupling(name = 'GC_1005',
                   value = '-((complex(0,1)*I2b31*I5b32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1006 = Coupling(name = 'GC_1006',
                   value = '-((complex(0,1)*I2b32*I5b32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1007 = Coupling(name = 'GC_1007',
                   value = '-((complex(0,1)*I2b33*I5b32*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1008 = Coupling(name = 'GC_1008',
                   value = '-((complex(0,1)*I2b11*I5b33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1009 = Coupling(name = 'GC_1009',
                   value = '-((complex(0,1)*I2b12*I5b33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1010 = Coupling(name = 'GC_1010',
                   value = '-((complex(0,1)*I2b13*I5b33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1011 = Coupling(name = 'GC_1011',
                   value = '-((complex(0,1)*I2b21*I5b33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1012 = Coupling(name = 'GC_1012',
                   value = '-((complex(0,1)*I2b22*I5b33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1013 = Coupling(name = 'GC_1013',
                   value = '-((complex(0,1)*I2b23*I5b33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1014 = Coupling(name = 'GC_1014',
                   value = '-((complex(0,1)*I2b31*I5b33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1015 = Coupling(name = 'GC_1015',
                   value = '-((complex(0,1)*I2b32*I5b33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1016 = Coupling(name = 'GC_1016',
                   value = '-((complex(0,1)*I2b33*I5b33*complexconjugate(cquqd1))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1017 = Coupling(name = 'GC_1017',
                   value = '(complex(0,1)*yb*yc*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1018 = Coupling(name = 'GC_1018',
                   value = '(complex(0,1)*yc*ydo*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1019 = Coupling(name = 'GC_1019',
                   value = '(complex(0,1)*yc*ys*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1020 = Coupling(name = 'GC_1020',
                   value = '(complex(0,1)*yb*yt*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1021 = Coupling(name = 'GC_1021',
                   value = '(complex(0,1)*ydo*yt*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1022 = Coupling(name = 'GC_1022',
                   value = '(complex(0,1)*ys*yt*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1023 = Coupling(name = 'GC_1023',
                   value = '(complex(0,1)*yb*yup*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1024 = Coupling(name = 'GC_1024',
                   value = '(complex(0,1)*ydo*yup*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1025 = Coupling(name = 'GC_1025',
                   value = '(complex(0,1)*ys*yup*complexconjugate(cquqd1))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1026 = Coupling(name = 'GC_1026',
                   value = '-((complex(0,1)*I2b11*I5b11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1027 = Coupling(name = 'GC_1027',
                   value = '-((complex(0,1)*I2b12*I5b11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1028 = Coupling(name = 'GC_1028',
                   value = '-((complex(0,1)*I2b13*I5b11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1029 = Coupling(name = 'GC_1029',
                   value = '-((complex(0,1)*I2b21*I5b11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1030 = Coupling(name = 'GC_1030',
                   value = '-((complex(0,1)*I2b22*I5b11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1031 = Coupling(name = 'GC_1031',
                   value = '-((complex(0,1)*I2b23*I5b11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1032 = Coupling(name = 'GC_1032',
                   value = '-((complex(0,1)*I2b31*I5b11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1033 = Coupling(name = 'GC_1033',
                   value = '-((complex(0,1)*I2b32*I5b11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1034 = Coupling(name = 'GC_1034',
                   value = '-((complex(0,1)*I2b33*I5b11*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1035 = Coupling(name = 'GC_1035',
                   value = '-((complex(0,1)*I2b11*I5b12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1036 = Coupling(name = 'GC_1036',
                   value = '-((complex(0,1)*I2b12*I5b12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1037 = Coupling(name = 'GC_1037',
                   value = '-((complex(0,1)*I2b13*I5b12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1038 = Coupling(name = 'GC_1038',
                   value = '-((complex(0,1)*I2b21*I5b12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1039 = Coupling(name = 'GC_1039',
                   value = '-((complex(0,1)*I2b22*I5b12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1040 = Coupling(name = 'GC_1040',
                   value = '-((complex(0,1)*I2b23*I5b12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1041 = Coupling(name = 'GC_1041',
                   value = '-((complex(0,1)*I2b31*I5b12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1042 = Coupling(name = 'GC_1042',
                   value = '-((complex(0,1)*I2b32*I5b12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1043 = Coupling(name = 'GC_1043',
                   value = '-((complex(0,1)*I2b33*I5b12*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1044 = Coupling(name = 'GC_1044',
                   value = '-((complex(0,1)*I2b11*I5b13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1045 = Coupling(name = 'GC_1045',
                   value = '-((complex(0,1)*I2b12*I5b13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1046 = Coupling(name = 'GC_1046',
                   value = '-((complex(0,1)*I2b13*I5b13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1047 = Coupling(name = 'GC_1047',
                   value = '-((complex(0,1)*I2b21*I5b13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1048 = Coupling(name = 'GC_1048',
                   value = '-((complex(0,1)*I2b22*I5b13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1049 = Coupling(name = 'GC_1049',
                   value = '-((complex(0,1)*I2b23*I5b13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1050 = Coupling(name = 'GC_1050',
                   value = '-((complex(0,1)*I2b31*I5b13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1051 = Coupling(name = 'GC_1051',
                   value = '-((complex(0,1)*I2b32*I5b13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1052 = Coupling(name = 'GC_1052',
                   value = '-((complex(0,1)*I2b33*I5b13*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1053 = Coupling(name = 'GC_1053',
                   value = '-((complex(0,1)*I2b11*I5b21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1054 = Coupling(name = 'GC_1054',
                   value = '-((complex(0,1)*I2b12*I5b21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1055 = Coupling(name = 'GC_1055',
                   value = '-((complex(0,1)*I2b13*I5b21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1056 = Coupling(name = 'GC_1056',
                   value = '-((complex(0,1)*I2b21*I5b21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1057 = Coupling(name = 'GC_1057',
                   value = '-((complex(0,1)*I2b22*I5b21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1058 = Coupling(name = 'GC_1058',
                   value = '-((complex(0,1)*I2b23*I5b21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1059 = Coupling(name = 'GC_1059',
                   value = '-((complex(0,1)*I2b31*I5b21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1060 = Coupling(name = 'GC_1060',
                   value = '-((complex(0,1)*I2b32*I5b21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1061 = Coupling(name = 'GC_1061',
                   value = '-((complex(0,1)*I2b33*I5b21*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1062 = Coupling(name = 'GC_1062',
                   value = '-((complex(0,1)*I2b11*I5b22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1063 = Coupling(name = 'GC_1063',
                   value = '-((complex(0,1)*I2b12*I5b22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1064 = Coupling(name = 'GC_1064',
                   value = '-((complex(0,1)*I2b13*I5b22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1065 = Coupling(name = 'GC_1065',
                   value = '-((complex(0,1)*I2b21*I5b22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1066 = Coupling(name = 'GC_1066',
                   value = '-((complex(0,1)*I2b22*I5b22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1067 = Coupling(name = 'GC_1067',
                   value = '-((complex(0,1)*I2b23*I5b22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1068 = Coupling(name = 'GC_1068',
                   value = '-((complex(0,1)*I2b31*I5b22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1069 = Coupling(name = 'GC_1069',
                   value = '-((complex(0,1)*I2b32*I5b22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1070 = Coupling(name = 'GC_1070',
                   value = '-((complex(0,1)*I2b33*I5b22*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1071 = Coupling(name = 'GC_1071',
                   value = '-((complex(0,1)*I2b11*I5b23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1072 = Coupling(name = 'GC_1072',
                   value = '-((complex(0,1)*I2b12*I5b23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1073 = Coupling(name = 'GC_1073',
                   value = '-((complex(0,1)*I2b13*I5b23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1074 = Coupling(name = 'GC_1074',
                   value = '-((complex(0,1)*I2b21*I5b23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1075 = Coupling(name = 'GC_1075',
                   value = '-((complex(0,1)*I2b22*I5b23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1076 = Coupling(name = 'GC_1076',
                   value = '-((complex(0,1)*I2b23*I5b23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1077 = Coupling(name = 'GC_1077',
                   value = '-((complex(0,1)*I2b31*I5b23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1078 = Coupling(name = 'GC_1078',
                   value = '-((complex(0,1)*I2b32*I5b23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1079 = Coupling(name = 'GC_1079',
                   value = '-((complex(0,1)*I2b33*I5b23*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1080 = Coupling(name = 'GC_1080',
                   value = '-((complex(0,1)*I2b11*I5b31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1081 = Coupling(name = 'GC_1081',
                   value = '-((complex(0,1)*I2b12*I5b31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1082 = Coupling(name = 'GC_1082',
                   value = '-((complex(0,1)*I2b13*I5b31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1083 = Coupling(name = 'GC_1083',
                   value = '-((complex(0,1)*I2b21*I5b31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1084 = Coupling(name = 'GC_1084',
                   value = '-((complex(0,1)*I2b22*I5b31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1085 = Coupling(name = 'GC_1085',
                   value = '-((complex(0,1)*I2b23*I5b31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1086 = Coupling(name = 'GC_1086',
                   value = '-((complex(0,1)*I2b31*I5b31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1087 = Coupling(name = 'GC_1087',
                   value = '-((complex(0,1)*I2b32*I5b31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1088 = Coupling(name = 'GC_1088',
                   value = '-((complex(0,1)*I2b33*I5b31*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1089 = Coupling(name = 'GC_1089',
                   value = '-((complex(0,1)*I2b11*I5b32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1090 = Coupling(name = 'GC_1090',
                   value = '-((complex(0,1)*I2b12*I5b32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1091 = Coupling(name = 'GC_1091',
                   value = '-((complex(0,1)*I2b13*I5b32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1092 = Coupling(name = 'GC_1092',
                   value = '-((complex(0,1)*I2b21*I5b32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1093 = Coupling(name = 'GC_1093',
                   value = '-((complex(0,1)*I2b22*I5b32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1094 = Coupling(name = 'GC_1094',
                   value = '-((complex(0,1)*I2b23*I5b32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1095 = Coupling(name = 'GC_1095',
                   value = '-((complex(0,1)*I2b31*I5b32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1096 = Coupling(name = 'GC_1096',
                   value = '-((complex(0,1)*I2b32*I5b32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1097 = Coupling(name = 'GC_1097',
                   value = '-((complex(0,1)*I2b33*I5b32*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1098 = Coupling(name = 'GC_1098',
                   value = '-((complex(0,1)*I2b11*I5b33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1099 = Coupling(name = 'GC_1099',
                   value = '-((complex(0,1)*I2b12*I5b33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1100 = Coupling(name = 'GC_1100',
                   value = '-((complex(0,1)*I2b13*I5b33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1101 = Coupling(name = 'GC_1101',
                   value = '-((complex(0,1)*I2b21*I5b33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1102 = Coupling(name = 'GC_1102',
                   value = '-((complex(0,1)*I2b22*I5b33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1103 = Coupling(name = 'GC_1103',
                   value = '-((complex(0,1)*I2b23*I5b33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1104 = Coupling(name = 'GC_1104',
                   value = '-((complex(0,1)*I2b31*I5b33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1105 = Coupling(name = 'GC_1105',
                   value = '-((complex(0,1)*I2b32*I5b33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1106 = Coupling(name = 'GC_1106',
                   value = '-((complex(0,1)*I2b33*I5b33*complexconjugate(cquqd8))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':4})

GC_1107 = Coupling(name = 'GC_1107',
                   value = '(complex(0,1)*yb*yc*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1108 = Coupling(name = 'GC_1108',
                   value = '(complex(0,1)*yc*ydo*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1109 = Coupling(name = 'GC_1109',
                   value = '(complex(0,1)*yc*ys*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1110 = Coupling(name = 'GC_1110',
                   value = '(complex(0,1)*yb*yt*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1111 = Coupling(name = 'GC_1111',
                   value = '(complex(0,1)*ydo*yt*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1112 = Coupling(name = 'GC_1112',
                   value = '(complex(0,1)*ys*yt*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1113 = Coupling(name = 'GC_1113',
                   value = '(complex(0,1)*yb*yup*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1114 = Coupling(name = 'GC_1114',
                   value = '(complex(0,1)*ydo*yup*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1115 = Coupling(name = 'GC_1115',
                   value = '(complex(0,1)*ys*yup*complexconjugate(cquqd8))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':4})

GC_1116 = Coupling(name = 'GC_1116',
                   value = '(complex(0,1)*yc*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1117 = Coupling(name = 'GC_1117',
                   value = '(complex(0,1)*vevhat*yc*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1118 = Coupling(name = 'GC_1118',
                   value = '(G*vevhat*yc*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1119 = Coupling(name = 'GC_1119',
                   value = '(complex(0,1)*yt*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1120 = Coupling(name = 'GC_1120',
                   value = '(complex(0,1)*vevhat*yt*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1121 = Coupling(name = 'GC_1121',
                   value = '(G*vevhat*yt*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1122 = Coupling(name = 'GC_1122',
                   value = '(complex(0,1)*yup*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1123 = Coupling(name = 'GC_1123',
                   value = '(complex(0,1)*vevhat*yup*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1124 = Coupling(name = 'GC_1124',
                   value = '(G*vevhat*yup*complexconjugate(cuG))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QCD':1,'QED':2})

GC_1125 = Coupling(name = 'GC_1125',
                   value = '(3*complex(0,1)*vevhat*yc*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1126 = Coupling(name = 'GC_1126',
                   value = '(complex(0,1)*vevhat**2*yc*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1127 = Coupling(name = 'GC_1127',
                   value = '(3*complex(0,1)*vevhat*yt*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1128 = Coupling(name = 'GC_1128',
                   value = '(complex(0,1)*vevhat**2*yt*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1129 = Coupling(name = 'GC_1129',
                   value = '(3*complex(0,1)*vevhat*yup*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1130 = Coupling(name = 'GC_1130',
                   value = '(complex(0,1)*vevhat**2*yup*complexconjugate(cuH))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':1})

GC_1131 = Coupling(name = 'GC_1131',
                   value = '-(cHbox*complex(0,1)*vevhat**4*yc*complexconjugate(cuH))/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**4*yc*complexconjugate(cuH))/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                   order = {'NP':2,'QED':1})

GC_1132 = Coupling(name = 'GC_1132',
                   value = '-(cHbox*complex(0,1)*vevhat**4*yt*complexconjugate(cuH))/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**4*yt*complexconjugate(cuH))/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                   order = {'NP':2,'QED':1})

GC_1133 = Coupling(name = 'GC_1133',
                   value = '-(cHbox*complex(0,1)*vevhat**4*yup*complexconjugate(cuH))/(2.*LambdaSMEFT**4*cmath.sqrt(2)) + (cHDD*complex(0,1)*vevhat**4*yup*complexconjugate(cuH))/(8.*LambdaSMEFT**4*cmath.sqrt(2))',
                   order = {'NP':2,'QED':1})

GC_1134 = Coupling(name = 'GC_1134',
                   value = '(complex(0,1)*yc*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1135 = Coupling(name = 'GC_1135',
                   value = '(complex(0,1)*vevhat*yc*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1136 = Coupling(name = 'GC_1136',
                   value = '-((ee*complex(0,1)*vevhat*yc*complexconjugate(cuW))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':3})

GC_1137 = Coupling(name = 'GC_1137',
                   value = '-((ee*complex(0,1)*vevhat*yc*complexconjugate(cuW))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1138 = Coupling(name = 'GC_1138',
                   value = '(cth*ee*complex(0,1)*vevhat*yc*complexconjugate(cuW))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1139 = Coupling(name = 'GC_1139',
                   value = '(complex(0,1)*yt*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1140 = Coupling(name = 'GC_1140',
                   value = '(complex(0,1)*vevhat*yt*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1141 = Coupling(name = 'GC_1141',
                   value = '-((ee*complex(0,1)*vevhat*yt*complexconjugate(cuW))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':3})

GC_1142 = Coupling(name = 'GC_1142',
                   value = '-((ee*complex(0,1)*vevhat*yt*complexconjugate(cuW))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1143 = Coupling(name = 'GC_1143',
                   value = '(cth*ee*complex(0,1)*vevhat*yt*complexconjugate(cuW))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1144 = Coupling(name = 'GC_1144',
                   value = '(complex(0,1)*yup*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':3})

GC_1145 = Coupling(name = 'GC_1145',
                   value = '(complex(0,1)*vevhat*yup*complexconjugate(cuW))/LambdaSMEFT**2',
                   order = {'NP':1,'QED':2})

GC_1146 = Coupling(name = 'GC_1146',
                   value = '-((ee*complex(0,1)*vevhat*yup*complexconjugate(cuW))/LambdaSMEFT**2)',
                   order = {'NP':1,'QED':3})

GC_1147 = Coupling(name = 'GC_1147',
                   value = '-((ee*complex(0,1)*vevhat*yup*complexconjugate(cuW))/(LambdaSMEFT**2*sth*cmath.sqrt(2)))',
                   order = {'NP':1,'QED':3})

GC_1148 = Coupling(name = 'GC_1148',
                   value = '(cth*ee*complex(0,1)*vevhat*yup*complexconjugate(cuW))/(LambdaSMEFT**2*sth)',
                   order = {'NP':1,'QED':3})

GC_1149 = Coupling(name = 'GC_1149',
                   value = '-((complex(0,1)*sth*yc*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*yc*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1150 = Coupling(name = 'GC_1150',
                   value = '(cth*complex(0,1)*yc*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*yc*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1151 = Coupling(name = 'GC_1151',
                   value = '-((complex(0,1)*sth*vevhat*yc*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*yc*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1152 = Coupling(name = 'GC_1152',
                   value = '(cth*complex(0,1)*vevhat*yc*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*yc*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1153 = Coupling(name = 'GC_1153',
                   value = '-((complex(0,1)*sth*yt*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*yt*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1154 = Coupling(name = 'GC_1154',
                   value = '(cth*complex(0,1)*yt*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*yt*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1155 = Coupling(name = 'GC_1155',
                   value = '-((complex(0,1)*sth*vevhat*yt*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*yt*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1156 = Coupling(name = 'GC_1156',
                   value = '(cth*complex(0,1)*vevhat*yt*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*yt*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1157 = Coupling(name = 'GC_1157',
                   value = '-((complex(0,1)*sth*yup*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*yup*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1158 = Coupling(name = 'GC_1158',
                   value = '(cth*complex(0,1)*yup*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*yup*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':3})

GC_1159 = Coupling(name = 'GC_1159',
                   value = '-((complex(0,1)*sth*vevhat*yup*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2))) + (cth*complex(0,1)*vevhat*yup*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

GC_1160 = Coupling(name = 'GC_1160',
                   value = '(cth*complex(0,1)*vevhat*yup*complexconjugate(cuB))/(LambdaSMEFT**2*cmath.sqrt(2)) + (complex(0,1)*sth*vevhat*yup*complexconjugate(cuW))/(LambdaSMEFT**2*cmath.sqrt(2))',
                   order = {'NP':1,'QED':2})

