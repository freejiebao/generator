# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.0.0 for Linux x86 (64-bit) (April 7, 2019)
# Date: Tue 18 Feb 2020 12:04:44



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

CKMlambda = Parameter(name = 'CKMlambda',
                      nature = 'external',
                      type = 'real',
                      value = 0.22506,
                      texname = '\\text{CKMlambda}',
                      lhablock = 'CKMBLOCK',
                      lhacode = [ 2 ])

CKMA = Parameter(name = 'CKMA',
                 nature = 'external',
                 type = 'real',
                 value = 0.811,
                 texname = '\\text{CKMA}',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 3 ])

CKMrho = Parameter(name = 'CKMrho',
                   nature = 'external',
                   type = 'real',
                   value = 0.124,
                   texname = '\\text{CKMrho}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 4 ])

CKMeta = Parameter(name = 'CKMeta',
                   nature = 'external',
                   type = 'real',
                   value = 0.356,
                   texname = '\\text{CKMeta}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 5 ])

MW0 = Parameter(name = 'MW0',
                nature = 'external',
                type = 'real',
                value = 80.387,
                texname = 'M_W',
                lhablock = 'SMINPUTS',
                lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011663787,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1181,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.0047,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.0022,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.096,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.28,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.18,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 173.2,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

ceWIm = Parameter(name = 'ceWIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ceWIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 1 ])

ceBIm = Parameter(name = 'ceBIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ceBIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 2 ])

cuGIm = Parameter(name = 'cuGIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuGIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 3 ])

cuWIm = Parameter(name = 'cuWIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuWIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 4 ])

cuBIm = Parameter(name = 'cuBIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuBIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 5 ])

cdGIm = Parameter(name = 'cdGIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdGIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 6 ])

cdWIm = Parameter(name = 'cdWIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdWIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 7 ])

cdBIm = Parameter(name = 'cdBIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdBIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 8 ])

cHudIm = Parameter(name = 'cHudIm',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{cHudIm}',
                   lhablock = 'FRBlock',
                   lhacode = [ 9 ])

ceHIm = Parameter(name = 'ceHIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ceHIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 10 ])

cuHIm = Parameter(name = 'cuHIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuHIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 11 ])

cdHIm = Parameter(name = 'cdHIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdHIm}',
                  lhablock = 'FRBlock',
                  lhacode = [ 12 ])

cledqIm = Parameter(name = 'cledqIm',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cledqIm}',
                    lhablock = 'FRBlock',
                    lhacode = [ 13 ])

cquqd1Im = Parameter(name = 'cquqd1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cquqd1Im}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

cquqd8Im = Parameter(name = 'cquqd8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cquqd8Im}',
                     lhablock = 'FRBlock',
                     lhacode = [ 15 ])

clequ1Im = Parameter(name = 'clequ1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{clequ1Im}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

clequ3Im = Parameter(name = 'clequ3Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{clequ3Im}',
                     lhablock = 'FRBlock',
                     lhacode = [ 17 ])

LambdaSMEFT = Parameter(name = 'LambdaSMEFT',
                        nature = 'external',
                        type = 'real',
                        value = 1000,
                        texname = '\\Lambda',
                        lhablock = 'FRBlock',
                        lhacode = [ 18 ])

cG = Parameter(name = 'cG',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'c_G',
               lhablock = 'FRBlock',
               lhacode = [ 19 ])

cGtil = Parameter(name = 'cGtil',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\tilde{G}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 20 ])

cW = Parameter(name = 'cW',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'c_W',
               lhablock = 'FRBlock',
               lhacode = [ 21 ])

cWtil = Parameter(name = 'cWtil',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\tilde{W}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 22 ])

cH = Parameter(name = 'cH',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'c_H',
               lhablock = 'FRBlock',
               lhacode = [ 23 ])

cHbox = Parameter(name = 'cHbox',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{H \\square }',
                  lhablock = 'FRBlock',
                  lhacode = [ 24 ])

cHDD = Parameter(name = 'cHDD',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{HD}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 25 ])

cHG = Parameter(name = 'cHG',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HG}}',
                lhablock = 'FRBlock',
                lhacode = [ 26 ])

cHGtil = Parameter(name = 'cHGtil',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{H \\tilde{G}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 27 ])

cHW = Parameter(name = 'cHW',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HW}}',
                lhablock = 'FRBlock',
                lhacode = [ 28 ])

cHWtil = Parameter(name = 'cHWtil',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{H \\tilde{W}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 29 ])

cHB = Parameter(name = 'cHB',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HB}}',
                lhablock = 'FRBlock',
                lhacode = [ 30 ])

cHBtil = Parameter(name = 'cHBtil',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{H \\tilde{B}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 31 ])

cHWB = Parameter(name = 'cHWB',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{HWB}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 32 ])

cHWBtil = Parameter(name = 'cHWBtil',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{B H \\tilde{W}}',
                    lhablock = 'FRBlock',
                    lhacode = [ 33 ])

ceHRe = Parameter(name = 'ceHRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ceHRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 34 ])

cuHRe = Parameter(name = 'cuHRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuHRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 35 ])

cdHRe = Parameter(name = 'cdHRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdHRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 36 ])

ceWRe = Parameter(name = 'ceWRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ceWRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 37 ])

ceBRe = Parameter(name = 'ceBRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ceBRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 38 ])

cuGRe = Parameter(name = 'cuGRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuGRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 39 ])

cuWRe = Parameter(name = 'cuWRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuWRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 40 ])

cuBRe = Parameter(name = 'cuBRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuBRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 41 ])

cdGRe = Parameter(name = 'cdGRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdGRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 42 ])

cdWRe = Parameter(name = 'cdWRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdWRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 43 ])

cdBRe = Parameter(name = 'cdBRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdBRe}',
                  lhablock = 'FRBlock',
                  lhacode = [ 44 ])

cHl1 = Parameter(name = 'cHl1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{Hl},1]',
                 lhablock = 'FRBlock',
                 lhacode = [ 45 ])

cHl3 = Parameter(name = 'cHl3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{Hl},3]',
                 lhablock = 'FRBlock',
                 lhacode = [ 46 ])

cHe = Parameter(name = 'cHe',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{He}}',
                lhablock = 'FRBlock',
                lhacode = [ 47 ])

cHq1 = Parameter(name = 'cHq1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{Hq},1]',
                 lhablock = 'FRBlock',
                 lhacode = [ 48 ])

cHq3 = Parameter(name = 'cHq3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{Hq},3]',
                 lhablock = 'FRBlock',
                 lhacode = [ 49 ])

cHu = Parameter(name = 'cHu',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{Hu}}',
                lhablock = 'FRBlock',
                lhacode = [ 50 ])

cHd = Parameter(name = 'cHd',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{Hd}}',
                lhablock = 'FRBlock',
                lhacode = [ 51 ])

cHudRe = Parameter(name = 'cHudRe',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{cHudRe}',
                   lhablock = 'FRBlock',
                   lhacode = [ 52 ])

cll = Parameter(name = 'cll',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{ll}}',
                lhablock = 'FRBlock',
                lhacode = [ 53 ])

cll1 = Parameter(name = 'cll1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{ll},\\text{Prime}]',
                 lhablock = 'FRBlock',
                 lhacode = [ 54 ])

cqq1 = Parameter(name = 'cqq1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{qq},1]',
                 lhablock = 'FRBlock',
                 lhacode = [ 55 ])

cqq11 = Parameter(name = 'cqq11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{Subsuperscript}[c,\\text{qq},\\text{Prime}]',
                  lhablock = 'FRBlock',
                  lhacode = [ 56 ])

cqq3 = Parameter(name = 'cqq3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{qq},3]',
                 lhablock = 'FRBlock',
                 lhacode = [ 57 ])

cqq31 = Parameter(name = 'cqq31',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{Subsuperscript}[c,\\text{qq},3 \\text{Prime}]',
                  lhablock = 'FRBlock',
                  lhacode = [ 58 ])

clq1 = Parameter(name = 'clq1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{lq},1]',
                 lhablock = 'FRBlock',
                 lhacode = [ 59 ])

clq3 = Parameter(name = 'clq3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{lq},3]',
                 lhablock = 'FRBlock',
                 lhacode = [ 60 ])

cee = Parameter(name = 'cee',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{ee}}',
                lhablock = 'FRBlock',
                lhacode = [ 61 ])

cuu = Parameter(name = 'cuu',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{uu}}',
                lhablock = 'FRBlock',
                lhacode = [ 62 ])

cuu1 = Parameter(name = 'cuu1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{uu},\\text{Prime}]',
                 lhablock = 'FRBlock',
                 lhacode = [ 63 ])

cdd = Parameter(name = 'cdd',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{dd}}',
                lhablock = 'FRBlock',
                lhacode = [ 64 ])

cdd1 = Parameter(name = 'cdd1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{dd},\\text{Prime}]',
                 lhablock = 'FRBlock',
                 lhacode = [ 65 ])

ceu = Parameter(name = 'ceu',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{eu}}',
                lhablock = 'FRBlock',
                lhacode = [ 66 ])

ced = Parameter(name = 'ced',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{ed}}',
                lhablock = 'FRBlock',
                lhacode = [ 67 ])

cud1 = Parameter(name = 'cud1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{ud},1]',
                 lhablock = 'FRBlock',
                 lhacode = [ 68 ])

cud8 = Parameter(name = 'cud8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{ud},8]',
                 lhablock = 'FRBlock',
                 lhacode = [ 69 ])

cle = Parameter(name = 'cle',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{le}}',
                lhablock = 'FRBlock',
                lhacode = [ 70 ])

clu = Parameter(name = 'clu',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{lu}}',
                lhablock = 'FRBlock',
                lhacode = [ 71 ])

cld = Parameter(name = 'cld',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{ld}}',
                lhablock = 'FRBlock',
                lhacode = [ 72 ])

cqe = Parameter(name = 'cqe',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{qe}}',
                lhablock = 'FRBlock',
                lhacode = [ 73 ])

cqu1 = Parameter(name = 'cqu1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{qu},1]',
                 lhablock = 'FRBlock',
                 lhacode = [ 74 ])

cqu8 = Parameter(name = 'cqu8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{qu},8]',
                 lhablock = 'FRBlock',
                 lhacode = [ 75 ])

cqd1 = Parameter(name = 'cqd1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{qd},1]',
                 lhablock = 'FRBlock',
                 lhacode = [ 76 ])

cqd8 = Parameter(name = 'cqd8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{Subsuperscript}[c,\\text{qd},8]',
                 lhablock = 'FRBlock',
                 lhacode = [ 77 ])

cledqRe = Parameter(name = 'cledqRe',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{cledqRe}',
                    lhablock = 'FRBlock',
                    lhacode = [ 78 ])

cquqd1Re = Parameter(name = 'cquqd1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cquqd1Re}',
                     lhablock = 'FRBlock',
                     lhacode = [ 79 ])

cquqd8Re = Parameter(name = 'cquqd8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cquqd8Re}',
                     lhablock = 'FRBlock',
                     lhacode = [ 80 ])

clequ1Re = Parameter(name = 'clequ1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{clequ1Re}',
                     lhablock = 'FRBlock',
                     lhacode = [ 81 ])

clequ3Re = Parameter(name = 'clequ3Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{clequ3Re}',
                     lhablock = 'FRBlock',
                     lhacode = [ 82 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.0022,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.28,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 173.2,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.0047,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.096,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.18,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.09,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

ceH = Parameter(name = 'ceH',
                nature = 'internal',
                type = 'complex',
                value = 'ceHRe + ceHIm*complex(0,1)',
                texname = 'c_{\\text{eH}}')

cuH = Parameter(name = 'cuH',
                nature = 'internal',
                type = 'complex',
                value = 'cuHRe + cuHIm*complex(0,1)',
                texname = 'c_{\\text{uH}}')

cdH = Parameter(name = 'cdH',
                nature = 'internal',
                type = 'complex',
                value = 'cdHRe + cdHIm*complex(0,1)',
                texname = 'c_{\\text{dH}}')

ceW = Parameter(name = 'ceW',
                nature = 'internal',
                type = 'complex',
                value = 'ceWRe + ceWIm*complex(0,1)',
                texname = 'c_{\\text{eW}}')

ceB = Parameter(name = 'ceB',
                nature = 'internal',
                type = 'complex',
                value = 'ceBRe + ceBIm*complex(0,1)',
                texname = 'c_{\\text{eB}}')

cuG = Parameter(name = 'cuG',
                nature = 'internal',
                type = 'complex',
                value = 'cuGRe + cuGIm*complex(0,1)',
                texname = 'c_{\\text{uG}}')

cuW = Parameter(name = 'cuW',
                nature = 'internal',
                type = 'complex',
                value = 'cuWRe + cuWIm*complex(0,1)',
                texname = 'c_{\\text{uW}}')

cuB = Parameter(name = 'cuB',
                nature = 'internal',
                type = 'complex',
                value = 'cuBRe + cuBIm*complex(0,1)',
                texname = 'c_{\\text{uB}}')

cdG = Parameter(name = 'cdG',
                nature = 'internal',
                type = 'complex',
                value = 'cdGRe + cdGIm*complex(0,1)',
                texname = 'c_{\\text{dG}}')

cdW = Parameter(name = 'cdW',
                nature = 'internal',
                type = 'complex',
                value = 'cdWRe + cdWIm*complex(0,1)',
                texname = 'c_{\\text{dW}}')

cdB = Parameter(name = 'cdB',
                nature = 'internal',
                type = 'complex',
                value = 'cdBRe + cdBIm*complex(0,1)',
                texname = 'c_{\\text{dB}}')

cHud = Parameter(name = 'cHud',
                 nature = 'internal',
                 type = 'complex',
                 value = 'cHudRe + cHudIm*complex(0,1)',
                 texname = 'c_{\\text{Hud}}')

cledq = Parameter(name = 'cledq',
                  nature = 'internal',
                  type = 'complex',
                  value = 'cledqRe + cledqIm*complex(0,1)',
                  texname = 'c_{\\text{ledq}}')

cquqd1 = Parameter(name = 'cquqd1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cquqd1Re + cquqd1Im*complex(0,1)',
                   texname = '\\text{Subsuperscript}[c,\\text{quqd},1]')

cquqd8 = Parameter(name = 'cquqd8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cquqd8Re + cquqd8Im*complex(0,1)',
                   texname = '\\text{Subsuperscript}[c,\\text{quqd},8]')

clequ1 = Parameter(name = 'clequ1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'clequ1Re + clequ1Im*complex(0,1)',
                   texname = '\\text{Subsuperscript}[c,\\text{lequ},1]')

clequ3 = Parameter(name = 'clequ3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'clequ3Re + clequ3Im*complex(0,1)',
                   texname = '\\text{Subsuperscript}[c,\\text{lequ},3]')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'MW0',
               texname = 'M_W')

vevhat = Parameter(name = 'vevhat',
                   nature = 'internal',
                   type = 'real',
                   value = '1/(2**0.25*cmath.sqrt(Gf))',
                   texname = '\\hat{v}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = '(Gf*MH**2)/cmath.sqrt(2)',
                texname = '\\text{lam}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - CKMlambda**2/2.',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMlambda',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**3*(CKMrho - CKMeta*complex(0,1))',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-CKMlambda',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - CKMlambda**2/2.',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**2',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**3*(1 - CKMrho - CKMeta*complex(0,1))',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(CKMA*CKMlambda**2)',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

sth2 = Parameter(name = 'sth2',
                 nature = 'internal',
                 type = 'real',
                 value = '1 - MW**2/MZ**2',
                 texname = '\\text{sth2}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '(Gf*MW**2*(1 - MW**2/MZ**2)*cmath.sqrt(2))/cmath.pi',
                texname = '\\alpha _{\\text{EW}}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vevhat',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vevhat',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vevhat',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vevhat',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vevhat',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vevhat',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vevhat',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vevhat',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vevhat',
                texname = '\\text{yup}')

gHgg = Parameter(name = 'gHgg',
                 nature = 'internal',
                 type = 'real',
                 value = '(G**2*(0.3333333333333333 + (13*MH**6)/(50400.*MT**6) + MH**4/(504.*MT**4) + (7*MH**2)/(360.*MT**2)))/(16.*cmath.pi**2)',
                 texname = 'g_{\\text{HGG}}')

dGf = Parameter(name = 'dGf',
                nature = 'internal',
                type = 'real',
                value = '(vevhat**2*(-(cll1/cmath.sqrt(2)) + cHl3*cmath.sqrt(2)))/LambdaSMEFT**2',
                texname = '\\text{dGf}')

dMH2 = Parameter(name = 'dMH2',
                 nature = 'internal',
                 type = 'real',
                 value = '((2*cHbox - cHDD/2. - (3*cH)/(2.*lam))*MH**2*vevhat**2)/LambdaSMEFT**2',
                 texname = '\\text{dMH2}')

barlam = Parameter(name = 'barlam',
                   nature = 'internal',
                   type = 'real',
                   value = 'lam*(1 - dMH2/MH**2 - dGf*cmath.sqrt(2))',
                   texname = '\\text{barlam}')

cth = Parameter(name = 'cth',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - sth2)',
                texname = 'c_{\\theta }')

sth = Parameter(name = 'sth',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(sth2)',
                texname = 's_{\\theta }')

vevT = Parameter(name = 'vevT',
                 nature = 'internal',
                 type = 'real',
                 value = 'vevhat*(1 + dGf/cmath.sqrt(2))',
                 texname = '\\text{vevT}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

dgw = Parameter(name = 'dgw',
                nature = 'internal',
                type = 'real',
                value = '-(dGf/cmath.sqrt(2))',
                texname = '\\text{dgw}')

gwsh = Parameter(name = 'gwsh',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee*(1 + dgw - (cHW*vevhat**2)/LambdaSMEFT**2))/sth',
                 texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(1 - (3*cH*vevhat**2)/(8.*lam*LambdaSMEFT**2))*vevT',
                texname = '\\text{vev}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cth',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sth',
               texname = 'g_w')

gHaa = Parameter(name = 'gHaa',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee**2*(-1.75 + (4*(0.3333333333333333 + (13*MH**6)/(50400.*MT**6) + MH**4/(504.*MT**4) + (7*MH**2)/(360.*MT**2)))/3. - (29*MH**6)/(16800.*MW0**6) - (19*MH**4)/(1680.*MW0**4) - (11*MH**2)/(120.*MW0**2)))/(8.*cmath.pi**2)',
                 texname = 'g_{\\text{H$\\gamma \\gamma $}}')

gHza = Parameter(name = 'gHza',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee**2*(((0.4583333333333333 + (29*MH**6)/(100800.*MW0**6) + (19*MH**4)/(10080.*MW0**4) + (11*MH**2)/(720.*MW0**2) + (MH**4*MZ**2)/(2100.*MW0**6) + (MH**2*MZ**2)/(280.*MW0**4) + (7*MZ**2)/(180.*MW0**2) + (67*MH**2*MZ**4)/(100800.*MW0**6) + (53*MZ**4)/(10080.*MW0**4) + (43*MZ**6)/(50400.*MW0**6) - (31*cth**2)/(24.*sth**2) - (29*cth**2*MH**6)/(20160.*MW0**6*sth**2) - (19*cth**2*MH**4)/(2016.*MW0**4*sth**2) - (11*cth**2*MH**2)/(144.*MW0**2*sth**2) - (cth**2*MH**4*MZ**2)/(560.*MW0**6*sth**2) - (31*cth**2*MH**2*MZ**2)/(2520.*MW0**4*sth**2) - (cth**2*MZ**2)/(9.*MW0**2*sth**2) - (43*cth**2*MH**2*MZ**4)/(20160.*MW0**6*sth**2) - (17*cth**2*MZ**4)/(1120.*MW0**4*sth**2) - (5*cth**2*MZ**6)/(2016.*MW0**6*sth**2))*sth)/cth + ((0.3333333333333333 + (13*MH**6)/(50400.*MT**6) + MH**4/(504.*MT**4) + (7*MH**2)/(360.*MT**2) + (MH**4*MZ**2)/(2400.*MT**6) + (MH**2*MZ**2)/(315.*MT**4) + (11*MZ**2)/(360.*MT**2) + (29*MH**2*MZ**4)/(50400.*MT**6) + (11*MZ**4)/(2520.*MT**4) + (37*MZ**6)/(50400.*MT**6))*(0.5 - (4*sth**2)/3.))/(cth*sth)))/(4.*cmath.pi**2)',
                 texname = 'g_{\\text{HZ$\\gamma $}}')

dMZ2 = Parameter(name = 'dMZ2',
                 nature = 'internal',
                 type = 'real',
                 value = '(MZ**2*(cHDD/2. + 2*cHWB*cth*sth)*vevhat**2)/LambdaSMEFT**2',
                 texname = '\\text{dMZ2}')

dg1 = Parameter(name = 'dg1',
                nature = 'internal',
                type = 'real',
                value = '(-(dMZ2/(MZ**2*sth**2)) - dGf*cmath.sqrt(2))/2.',
                texname = '\\text{dg1}')

g1sh = Parameter(name = 'g1sh',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee*(1 + dg1 - (cHB*vevhat**2)/LambdaSMEFT**2))/cth',
                 texname = 'g_1')

dsth2 = Parameter(name = 'dsth2',
                  nature = 'internal',
                  type = 'real',
                  value = '2*cth**2*(dg1 - dgw)*sth**2 + (cHWB*cth*sth*(1 - 2*sth**2)*vevhat**2)/LambdaSMEFT**2',
                  texname = '\\text{dsth2}')

I1d11 = Parameter(name = 'I1d11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*ydo',
                  texname = '\\text{I1d11}')

I1d12 = Parameter(name = 'I1d12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*ydo',
                  texname = '\\text{I1d12}')

I1d13 = Parameter(name = 'I1d13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*ydo',
                  texname = '\\text{I1d13}')

I1d21 = Parameter(name = 'I1d21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*ys',
                  texname = '\\text{I1d21}')

I1d22 = Parameter(name = 'I1d22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*ys',
                  texname = '\\text{I1d22}')

I1d23 = Parameter(name = 'I1d23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*ys',
                  texname = '\\text{I1d23}')

I1d31 = Parameter(name = 'I1d31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yb',
                  texname = '\\text{I1d31}')

I1d32 = Parameter(name = 'I1d32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yb',
                  texname = '\\text{I1d32}')

I1d33 = Parameter(name = 'I1d33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yb',
                  texname = '\\text{I1d33}')

I2d11 = Parameter(name = 'I2d11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x1*yup',
                  texname = '\\text{I2d11}')

I2d12 = Parameter(name = 'I2d12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x1*yc',
                  texname = '\\text{I2d12}')

I2d13 = Parameter(name = 'I2d13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x1*yt',
                  texname = '\\text{I2d13}')

I2d21 = Parameter(name = 'I2d21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x2*yup',
                  texname = '\\text{I2d21}')

I2d22 = Parameter(name = 'I2d22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x2*yc',
                  texname = '\\text{I2d22}')

I2d23 = Parameter(name = 'I2d23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x2*yt',
                  texname = '\\text{I2d23}')

I2d31 = Parameter(name = 'I2d31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM1x3*yup',
                  texname = '\\text{I2d31}')

I2d32 = Parameter(name = 'I2d32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM2x3*yc',
                  texname = '\\text{I2d32}')

I2d33 = Parameter(name = 'I2d33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'CKM3x3*yt',
                  texname = '\\text{I2d33}')

I3d11 = Parameter(name = 'I3d11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  texname = '\\text{I3d11}')

I3d12 = Parameter(name = 'I3d12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  texname = '\\text{I3d12}')

I3d13 = Parameter(name = 'I3d13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  texname = '\\text{I3d13}')

I3d21 = Parameter(name = 'I3d21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM1x2)',
                  texname = '\\text{I3d21}')

I3d22 = Parameter(name = 'I3d22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM2x2)',
                  texname = '\\text{I3d22}')

I3d23 = Parameter(name = 'I3d23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM3x2)',
                  texname = '\\text{I3d23}')

I3d31 = Parameter(name = 'I3d31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM1x3)',
                  texname = '\\text{I3d31}')

I3d32 = Parameter(name = 'I3d32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM2x3)',
                  texname = '\\text{I3d32}')

I3d33 = Parameter(name = 'I3d33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM3x3)',
                  texname = '\\text{I3d33}')

I4d11 = Parameter(name = 'I4d11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x1)',
                  texname = '\\text{I4d11}')

I4d12 = Parameter(name = 'I4d12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x1)',
                  texname = '\\text{I4d12}')

I4d13 = Parameter(name = 'I4d13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x1)',
                  texname = '\\text{I4d13}')

I4d21 = Parameter(name = 'I4d21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x2)',
                  texname = '\\text{I4d21}')

I4d22 = Parameter(name = 'I4d22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x2)',
                  texname = '\\text{I4d22}')

I4d23 = Parameter(name = 'I4d23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x2)',
                  texname = '\\text{I4d23}')

I4d31 = Parameter(name = 'I4d31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x3)',
                  texname = '\\text{I4d31}')

I4d32 = Parameter(name = 'I4d32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x3)',
                  texname = '\\text{I4d32}')

I4d33 = Parameter(name = 'I4d33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x3)',
                  texname = '\\text{I4d33}')

I5d11 = Parameter(name = 'I5d11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM1x1)',
                  texname = '\\text{I5d11}')

I5d12 = Parameter(name = 'I5d12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM2x1)',
                  texname = '\\text{I5d12}')

I5d13 = Parameter(name = 'I5d13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ydo*complexconjugate(CKM3x1)',
                  texname = '\\text{I5d13}')

I5d21 = Parameter(name = 'I5d21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM1x2)',
                  texname = '\\text{I5d21}')

I5d22 = Parameter(name = 'I5d22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM2x2)',
                  texname = '\\text{I5d22}')

I5d23 = Parameter(name = 'I5d23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ys*complexconjugate(CKM3x2)',
                  texname = '\\text{I5d23}')

I5d31 = Parameter(name = 'I5d31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM1x3)',
                  texname = '\\text{I5d31}')

I5d32 = Parameter(name = 'I5d32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM2x3)',
                  texname = '\\text{I5d32}')

I5d33 = Parameter(name = 'I5d33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yb*complexconjugate(CKM3x3)',
                  texname = '\\text{I5d33}')

I6d11 = Parameter(name = 'I6d11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x1)',
                  texname = '\\text{I6d11}')

I6d12 = Parameter(name = 'I6d12',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x1)',
                  texname = '\\text{I6d12}')

I6d13 = Parameter(name = 'I6d13',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x1)',
                  texname = '\\text{I6d13}')

I6d21 = Parameter(name = 'I6d21',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x2)',
                  texname = '\\text{I6d21}')

I6d22 = Parameter(name = 'I6d22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x2)',
                  texname = '\\text{I6d22}')

I6d23 = Parameter(name = 'I6d23',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x2)',
                  texname = '\\text{I6d23}')

I6d31 = Parameter(name = 'I6d31',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yup*complexconjugate(CKM1x3)',
                  texname = '\\text{I6d31}')

I6d32 = Parameter(name = 'I6d32',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yc*complexconjugate(CKM2x3)',
                  texname = '\\text{I6d32}')

I6d33 = Parameter(name = 'I6d33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'yt*complexconjugate(CKM3x3)',
                  texname = '\\text{I6d33}')

