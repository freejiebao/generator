# This file was automatically created by FeynRules 2.3.29
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Fri 9 Mar 2018 13:38:22


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS2, L.SSSS3 ],
             couplings = {(0,0):C.GC_9,(0,2):C.GC_29,(0,1):C.GC_30})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_329})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_294})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1, L.SSS2, L.SSS3 ],
             couplings = {(0,0):C.GC_265,(0,2):C.GC_266,(0,1):C.GC_267})

V_5 = Vertex(name = 'V_5',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_356})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_311})

V_7 = Vertex(name = 'V_7',
             particles = [ P.a, P.a, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVS2, L.VVS4 ],
             couplings = {(0,0):C.GC_325,(0,1):C.GC_262})

V_8 = Vertex(name = 'V_8',
             particles = [ P.a, P.a, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVS4 ],
             couplings = {(0,0):C.GC_322})

V_9 = Vertex(name = 'V_9',
             particles = [ P.a, P.a, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.VVSS2, L.VVSS4 ],
             couplings = {(0,0):C.GC_261,(0,1):C.GC_258})

V_10 = Vertex(name = 'V_10',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_269,(0,1):C.GC_263})

V_11 = Vertex(name = 'V_11',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_268})

V_12 = Vertex(name = 'V_12',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_32,(0,1):C.GC_31})

V_13 = Vertex(name = 'V_13',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_34,(0,2):C.GC_33,(0,1):C.GC_220})

V_14 = Vertex(name = 'V_14',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_330})

V_15 = Vertex(name = 'V_15',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_271,(0,2):C.GC_270,(0,1):C.GC_278})

V_16 = Vertex(name = 'V_16',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_357})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1, L.VVV3, L.VVV5, L.VVV6, L.VVV7, L.VVV9 ],
              couplings = {(0,1):C.GC_297,(0,0):C.GC_300,(0,5):C.GC_251,(0,4):C.GC_250,(0,2):C.GC_3,(0,3):C.GC_299})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV5 ],
              couplings = {(0,0):C.GC_341})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_324,(0,2):C.GC_264,(0,1):C.GC_359})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_323})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_260,(0,2):C.GC_259,(0,1):C.GC_355})

V_22 = Vertex(name = 'V_22',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_257,(0,2):C.GC_256,(0,1):C.GC_255})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_354})

V_24 = Vertex(name = 'V_24',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_321,(0,2):C.GC_320,(0,1):C.GC_319})

V_25 = Vertex(name = 'V_25',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_358})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV7, L.VVV9 ],
              couplings = {(0,1):C.GC_301,(0,0):C.GC_296,(0,5):C.GC_53,(0,4):C.GC_52,(0,3):C.GC_236,(0,2):C.GC_295})

V_27 = Vertex(name = 'V_27',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV5 ],
              couplings = {(0,0):C.GC_345})

V_28 = Vertex(name = 'V_28',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_7})

V_29 = Vertex(name = 'V_29',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV3, L.VVV5, L.VVV7, L.VVV8 ],
              couplings = {(0,0):C.GC_298,(0,3):C.GC_28,(0,2):C.GC_27,(0,1):C.GC_7})

V_30 = Vertex(name = 'V_30',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3, L.VVVS6 ],
              couplings = {(0,0):C.GC_277,(0,1):C.GC_276})

V_31 = Vertex(name = 'V_31',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV10, L.VVVV12, L.VVVV13, L.VVVV2, L.VVVV3, L.VVVV4, L.VVVV6, L.VVVV9 ],
              couplings = {(0,7):C.GC_57,(1,6):C.GC_57,(2,5):C.GC_57,(0,4):C.GC_56,(1,3):C.GC_56,(2,2):C.GC_56,(1,8):C.GC_8,(0,0):C.GC_8,(2,1):C.GC_8})

V_32 = Vertex(name = 'V_32',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_398,(0,0):C.GC_687,(0,1):C.GC_408})

V_33 = Vertex(name = 'V_33',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_415,(0,0):C.GC_691,(0,1):C.GC_417})

V_34 = Vertex(name = 'V_34',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_416})

V_35 = Vertex(name = 'V_35',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_530,(0,0):C.GC_689,(0,1):C.GC_540})

V_36 = Vertex(name = 'V_36',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_549,(0,0):C.GC_692,(0,1):C.GC_551})

V_37 = Vertex(name = 'V_37',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_550})

V_38 = Vertex(name = 'V_38',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_360,(0,0):C.GC_685,(0,1):C.GC_370})

V_39 = Vertex(name = 'V_39',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_375,(0,0):C.GC_690,(0,1):C.GC_377})

V_40 = Vertex(name = 'V_40',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_376})

V_41 = Vertex(name = 'V_41',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_418,(0,0):C.GC_721,(0,1):C.GC_461})

V_42 = Vertex(name = 'V_42',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_471,(0,0):C.GC_726,(0,1):C.GC_473})

V_43 = Vertex(name = 'V_43',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_472})

V_44 = Vertex(name = 'V_44',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_474,(0,0):C.GC_723,(0,1):C.GC_517})

V_45 = Vertex(name = 'V_45',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_527,(0,0):C.GC_727,(0,1):C.GC_529})

V_46 = Vertex(name = 'V_46',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_528})

V_47 = Vertex(name = 'V_47',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_582,(0,0):C.GC_725,(0,1):C.GC_625})

V_48 = Vertex(name = 'V_48',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_639,(0,0):C.GC_728,(0,1):C.GC_641})

V_49 = Vertex(name = 'V_49',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_640})

V_50 = Vertex(name = 'V_50',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_642,(0,0):C.GC_1130,(0,1):C.GC_652})

V_51 = Vertex(name = 'V_51',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_672,(0,0):C.GC_1133,(0,1):C.GC_674})

V_52 = Vertex(name = 'V_52',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_673})

V_53 = Vertex(name = 'V_53',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_378,(0,0):C.GC_1126,(0,1):C.GC_388})

V_54 = Vertex(name = 'V_54',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_395,(0,0):C.GC_1131,(0,1):C.GC_397})

V_55 = Vertex(name = 'V_55',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_396})

V_56 = Vertex(name = 'V_56',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_552,(0,0):C.GC_1128,(0,1):C.GC_562})

V_57 = Vertex(name = 'V_57',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,2):C.GC_579,(0,0):C.GC_1132,(0,1):C.GC_581})

V_58 = Vertex(name = 'V_58',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_580})

V_59 = Vertex(name = 'V_59',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS1, L.VVVS3, L.VVVS4, L.VVVS6 ],
              couplings = {(0,1):C.GC_275,(0,0):C.GC_283,(0,3):C.GC_272,(0,2):C.GC_282})

V_60 = Vertex(name = 'V_60',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_253,(0,0):C.GC_252,(0,2):C.GC_5})

V_61 = Vertex(name = 'V_61',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_346})

V_62 = Vertex(name = 'V_62',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11, L.VVVV14, L.VVVV7 ],
              couplings = {(0,2):C.GC_55,(0,1):C.GC_54,(0,0):C.GC_347})

V_63 = Vertex(name = 'V_63',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV11 ],
              couplings = {(0,0):C.GC_243})

V_64 = Vertex(name = 'V_64',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS2, L.VVVS3, L.VVVS5, L.VVVS6 ],
              couplings = {(0,1):C.GC_284,(0,0):C.GC_274,(0,3):C.GC_281,(0,2):C.GC_273})

V_65 = Vertex(name = 'V_65',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
              couplings = {(0,1):C.GC_246,(0,0):C.GC_244,(0,2):C.GC_221})

V_66 = Vertex(name = 'V_66',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV8 ],
              couplings = {(0,0):C.GC_223})

V_67 = Vertex(name = 'V_67',
              particles = [ P.d__tilde__, P.d, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_686,(0,1):C.GC_402})

V_68 = Vertex(name = 'V_68',
              particles = [ P.s__tilde__, P.s, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_688,(0,1):C.GC_534})

V_69 = Vertex(name = 'V_69',
              particles = [ P.b__tilde__, P.b, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_684,(0,1):C.GC_364})

V_70 = Vertex(name = 'V_70',
              particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_720,(0,1):C.GC_456})

V_71 = Vertex(name = 'V_71',
              particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_722,(0,1):C.GC_512})

V_72 = Vertex(name = 'V_72',
              particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2 ],
              couplings = {(0,0):C.GC_724,(0,1):C.GC_620})

V_73 = Vertex(name = 'V_73',
              particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,2):C.GC_39,(0,5):C.GC_865,(0,3):C.GC_864,(0,4):C.GC_864,(0,1):C.GC_828,(0,0):C.GC_792})

V_74 = Vertex(name = 'V_74',
              particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_867,(0,2):C.GC_866,(0,3):C.GC_866,(0,1):C.GC_829,(0,0):C.GC_793})

V_75 = Vertex(name = 'V_75',
              particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_869,(0,2):C.GC_868,(0,3):C.GC_868,(0,1):C.GC_830,(0,0):C.GC_794})

V_76 = Vertex(name = 'V_76',
              particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_871,(0,2):C.GC_870,(0,3):C.GC_870,(0,1):C.GC_831,(0,0):C.GC_795})

V_77 = Vertex(name = 'V_77',
              particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,2):C.GC_39,(0,5):C.GC_873,(0,3):C.GC_872,(0,4):C.GC_872,(0,1):C.GC_832,(0,0):C.GC_796})

V_78 = Vertex(name = 'V_78',
              particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_875,(0,2):C.GC_874,(0,3):C.GC_874,(0,1):C.GC_833,(0,0):C.GC_797})

V_79 = Vertex(name = 'V_79',
              particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_877,(0,2):C.GC_876,(0,3):C.GC_876,(0,1):C.GC_834,(0,0):C.GC_798})

V_80 = Vertex(name = 'V_80',
              particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7 ],
              couplings = {(0,2):C.GC_878,(0,4):C.GC_878,(0,3):C.GC_879,(0,1):C.GC_835,(0,0):C.GC_799})

V_81 = Vertex(name = 'V_81',
              particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,2):C.GC_39,(0,5):C.GC_881,(0,3):C.GC_880,(0,4):C.GC_880,(0,1):C.GC_836,(0,0):C.GC_800})

V_82 = Vertex(name = 'V_82',
              particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,2):C.GC_39,(0,5):C.GC_885,(0,3):C.GC_884,(0,4):C.GC_884,(0,1):C.GC_838,(0,0):C.GC_803})

V_83 = Vertex(name = 'V_83',
              particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_887,(0,2):C.GC_886,(0,3):C.GC_886,(0,1):C.GC_839,(0,0):C.GC_804})

V_84 = Vertex(name = 'V_84',
              particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_889,(0,2):C.GC_888,(0,3):C.GC_888,(0,1):C.GC_840,(0,0):C.GC_805})

V_85 = Vertex(name = 'V_85',
              particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_891,(0,2):C.GC_890,(0,3):C.GC_890,(0,1):C.GC_841,(0,0):C.GC_806})

V_86 = Vertex(name = 'V_86',
              particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,2):C.GC_39,(0,5):C.GC_893,(0,3):C.GC_892,(0,4):C.GC_892,(0,1):C.GC_842,(0,0):C.GC_807})

V_87 = Vertex(name = 'V_87',
              particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_895,(0,2):C.GC_894,(0,3):C.GC_894,(0,1):C.GC_843,(0,0):C.GC_808})

V_88 = Vertex(name = 'V_88',
              particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_897,(0,2):C.GC_896,(0,3):C.GC_896,(0,1):C.GC_844,(0,0):C.GC_809})

V_89 = Vertex(name = 'V_89',
              particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_899,(0,2):C.GC_898,(0,3):C.GC_898,(0,1):C.GC_845,(0,0):C.GC_810})

V_90 = Vertex(name = 'V_90',
              particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,2):C.GC_39,(0,5):C.GC_901,(0,3):C.GC_900,(0,4):C.GC_900,(0,1):C.GC_846,(0,0):C.GC_811})

V_91 = Vertex(name = 'V_91',
              particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,2):C.GC_39,(0,5):C.GC_909,(0,3):C.GC_908,(0,4):C.GC_908,(0,1):C.GC_850,(0,0):C.GC_816})

V_92 = Vertex(name = 'V_92',
              particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_911,(0,2):C.GC_910,(0,3):C.GC_910,(0,1):C.GC_851,(0,0):C.GC_817})

V_93 = Vertex(name = 'V_93',
              particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_913,(0,2):C.GC_912,(0,3):C.GC_912,(0,1):C.GC_852,(0,0):C.GC_818})

V_94 = Vertex(name = 'V_94',
              particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_915,(0,2):C.GC_914,(0,3):C.GC_914,(0,1):C.GC_853,(0,0):C.GC_819})

V_95 = Vertex(name = 'V_95',
              particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,2):C.GC_39,(0,5):C.GC_917,(0,3):C.GC_916,(0,4):C.GC_916,(0,1):C.GC_854,(0,0):C.GC_820})

V_96 = Vertex(name = 'V_96',
              particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_919,(0,2):C.GC_918,(0,3):C.GC_918,(0,1):C.GC_855,(0,0):C.GC_821})

V_97 = Vertex(name = 'V_97',
              particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_921,(0,2):C.GC_920,(0,3):C.GC_920,(0,1):C.GC_856,(0,0):C.GC_822})

V_98 = Vertex(name = 'V_98',
              particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,4):C.GC_923,(0,2):C.GC_922,(0,3):C.GC_922,(0,1):C.GC_857,(0,0):C.GC_823})

V_99 = Vertex(name = 'V_99',
              particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF11, L.FFFF2, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
              couplings = {(0,2):C.GC_39,(0,5):C.GC_925,(0,3):C.GC_924,(0,4):C.GC_924,(0,1):C.GC_858,(0,0):C.GC_824})

V_100 = Vertex(name = 'V_100',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_39,(0,4):C.GC_431,(0,2):C.GC_430,(0,3):C.GC_430,(0,0):C.GC_420,(0,1):C.GC_429})

V_101 = Vertex(name = 'V_101',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_434,(0,2):C.GC_433,(0,3):C.GC_433,(0,0):C.GC_421,(0,1):C.GC_432})

V_102 = Vertex(name = 'V_102',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_437,(0,2):C.GC_436,(0,3):C.GC_436,(0,0):C.GC_422,(0,1):C.GC_435})

V_103 = Vertex(name = 'V_103',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_39,(0,4):C.GC_487,(0,2):C.GC_486,(0,3):C.GC_486,(0,0):C.GC_476,(0,1):C.GC_485})

V_104 = Vertex(name = 'V_104',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_490,(0,2):C.GC_489,(0,3):C.GC_489,(0,0):C.GC_477,(0,1):C.GC_488})

V_105 = Vertex(name = 'V_105',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_493,(0,2):C.GC_492,(0,3):C.GC_492,(0,0):C.GC_478,(0,1):C.GC_491})

V_106 = Vertex(name = 'V_106',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_39,(0,4):C.GC_595,(0,2):C.GC_594,(0,3):C.GC_594,(0,0):C.GC_584,(0,1):C.GC_593})

V_107 = Vertex(name = 'V_107',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_598,(0,2):C.GC_597,(0,3):C.GC_597,(0,0):C.GC_585,(0,1):C.GC_596})

V_108 = Vertex(name = 'V_108',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_601,(0,2):C.GC_600,(0,3):C.GC_600,(0,0):C.GC_586,(0,1):C.GC_599})

V_109 = Vertex(name = 'V_109',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_440,(0,2):C.GC_439,(0,3):C.GC_439,(0,0):C.GC_423,(0,1):C.GC_438})

V_110 = Vertex(name = 'V_110',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_39,(0,4):C.GC_443,(0,2):C.GC_442,(0,3):C.GC_442,(0,0):C.GC_424,(0,1):C.GC_441})

V_111 = Vertex(name = 'V_111',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_446,(0,2):C.GC_445,(0,3):C.GC_445,(0,0):C.GC_425,(0,1):C.GC_444})

V_112 = Vertex(name = 'V_112',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_496,(0,2):C.GC_495,(0,3):C.GC_495,(0,0):C.GC_479,(0,1):C.GC_494})

V_113 = Vertex(name = 'V_113',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_39,(0,4):C.GC_499,(0,2):C.GC_498,(0,3):C.GC_498,(0,0):C.GC_480,(0,1):C.GC_497})

V_114 = Vertex(name = 'V_114',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_502,(0,2):C.GC_501,(0,3):C.GC_501,(0,0):C.GC_481,(0,1):C.GC_500})

V_115 = Vertex(name = 'V_115',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_604,(0,2):C.GC_603,(0,3):C.GC_603,(0,0):C.GC_587,(0,1):C.GC_602})

V_116 = Vertex(name = 'V_116',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_39,(0,4):C.GC_607,(0,2):C.GC_606,(0,3):C.GC_606,(0,0):C.GC_588,(0,1):C.GC_605})

V_117 = Vertex(name = 'V_117',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_610,(0,2):C.GC_609,(0,3):C.GC_609,(0,0):C.GC_589,(0,1):C.GC_608})

V_118 = Vertex(name = 'V_118',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_449,(0,2):C.GC_448,(0,3):C.GC_448,(0,0):C.GC_426,(0,1):C.GC_447})

V_119 = Vertex(name = 'V_119',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_452,(0,2):C.GC_451,(0,3):C.GC_451,(0,0):C.GC_427,(0,1):C.GC_450})

V_120 = Vertex(name = 'V_120',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_39,(0,4):C.GC_455,(0,2):C.GC_454,(0,3):C.GC_454,(0,0):C.GC_428,(0,1):C.GC_453})

V_121 = Vertex(name = 'V_121',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_505,(0,2):C.GC_504,(0,3):C.GC_504,(0,0):C.GC_482,(0,1):C.GC_503})

V_122 = Vertex(name = 'V_122',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_508,(0,2):C.GC_507,(0,3):C.GC_507,(0,0):C.GC_483,(0,1):C.GC_506})

V_123 = Vertex(name = 'V_123',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_39,(0,4):C.GC_511,(0,2):C.GC_510,(0,3):C.GC_510,(0,0):C.GC_484,(0,1):C.GC_509})

V_124 = Vertex(name = 'V_124',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_613,(0,2):C.GC_612,(0,3):C.GC_612,(0,0):C.GC_590,(0,1):C.GC_611})

V_125 = Vertex(name = 'V_125',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21 ],
               couplings = {(0,4):C.GC_616,(0,2):C.GC_615,(0,3):C.GC_615,(0,0):C.GC_591,(0,1):C.GC_614})

V_126 = Vertex(name = 'V_126',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF11, L.FFFF12, L.FFFF19, L.FFFF20, L.FFFF21, L.FFFF4 ],
               couplings = {(0,5):C.GC_39,(0,4):C.GC_619,(0,2):C.GC_618,(0,3):C.GC_618,(0,0):C.GC_592,(0,1):C.GC_617})

V_127 = Vertex(name = 'V_127',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_13,(0,1):C.GC_43,(0,2):C.GC_35,(0,3):C.GC_24,(0,5):C.GC_466,(0,0):C.GC_802})

V_128 = Vertex(name = 'V_128',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_13,(0,1):C.GC_43,(0,2):C.GC_35,(0,3):C.GC_24,(0,5):C.GC_522,(0,0):C.GC_813})

V_129 = Vertex(name = 'V_129',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_13,(0,1):C.GC_43,(0,2):C.GC_35,(0,3):C.GC_24,(0,5):C.GC_630,(0,0):C.GC_826})

V_130 = Vertex(name = 'V_130',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_13,(0,1):C.GC_43,(0,2):C.GC_35,(0,3):C.GC_24,(0,5):C.GC_543,(0,0):C.GC_814})

V_131 = Vertex(name = 'V_131',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_13,(0,1):C.GC_43,(0,2):C.GC_35,(0,3):C.GC_24,(0,5):C.GC_544,(0,0):C.GC_815})

V_132 = Vertex(name = 'V_132',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_13,(0,1):C.GC_43,(0,2):C.GC_35,(0,3):C.GC_24,(0,5):C.GC_631,(0,0):C.GC_827})

V_133 = Vertex(name = 'V_133',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_13,(0,1):C.GC_43,(0,2):C.GC_35,(0,3):C.GC_24,(0,5):C.GC_462,(0,0):C.GC_801})

V_134 = Vertex(name = 'V_134',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_13,(0,1):C.GC_43,(0,2):C.GC_35,(0,3):C.GC_24,(0,5):C.GC_518,(0,0):C.GC_812})

V_135 = Vertex(name = 'V_135',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF4, L.FFFF9 ],
               couplings = {(0,4):C.GC_13,(0,1):C.GC_43,(0,2):C.GC_35,(0,3):C.GC_24,(0,5):C.GC_626,(0,0):C.GC_825})

V_136 = Vertex(name = 'V_136',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1129,(0,1):C.GC_646})

V_137 = Vertex(name = 'V_137',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1125,(0,1):C.GC_382})

V_138 = Vertex(name = 'V_138',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_1127,(0,1):C.GC_556})

V_139 = Vertex(name = 'V_139',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_12,(0,11):C.GC_931,(0,9):C.GC_930,(0,10):C.GC_930,(0,5):C.GC_861,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_26,(0,7):C.GC_659,(0,4):C.GC_658,(0,6):C.GC_658,(0,0):C.GC_657})

V_140 = Vertex(name = 'V_140',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_12,(0,11):C.GC_883,(0,9):C.GC_882,(0,10):C.GC_882,(0,5):C.GC_837,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_26,(0,7):C.GC_465,(0,4):C.GC_464,(0,6):C.GC_464,(0,0):C.GC_463})

V_141 = Vertex(name = 'V_141',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_12,(0,11):C.GC_905,(0,9):C.GC_904,(0,10):C.GC_904,(0,5):C.GC_848,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_26,(0,7):C.GC_569,(0,4):C.GC_568,(0,6):C.GC_568,(0,0):C.GC_567})

V_142 = Vertex(name = 'V_142',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_12,(0,11):C.GC_933,(0,9):C.GC_932,(0,10):C.GC_932,(0,5):C.GC_862,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_26,(0,7):C.GC_662,(0,4):C.GC_661,(0,6):C.GC_661,(0,0):C.GC_660})

V_143 = Vertex(name = 'V_143',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_12,(0,11):C.GC_903,(0,9):C.GC_902,(0,10):C.GC_902,(0,5):C.GC_847,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_26,(0,7):C.GC_521,(0,4):C.GC_520,(0,6):C.GC_520,(0,0):C.GC_519})

V_144 = Vertex(name = 'V_144',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_12,(0,11):C.GC_907,(0,9):C.GC_906,(0,10):C.GC_906,(0,5):C.GC_849,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_26,(0,7):C.GC_572,(0,4):C.GC_571,(0,6):C.GC_571,(0,0):C.GC_570})

V_145 = Vertex(name = 'V_145',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF6, L.FFFF7 ],
               couplings = {(0,9):C.GC_934,(0,11):C.GC_934,(0,8):C.GC_12,(0,10):C.GC_935,(0,5):C.GC_863,(0,7):C.GC_667,(0,4):C.GC_666,(0,6):C.GC_666,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_26,(0,0):C.GC_665})

V_146 = Vertex(name = 'V_146',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_12,(0,11):C.GC_927,(0,9):C.GC_926,(0,10):C.GC_926,(0,5):C.GC_859,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_26,(0,7):C.GC_629,(0,4):C.GC_628,(0,6):C.GC_628,(0,0):C.GC_627})

V_147 = Vertex(name = 'V_147',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF4, L.FFFF5, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_12,(0,11):C.GC_929,(0,9):C.GC_928,(0,10):C.GC_928,(0,5):C.GC_860,(0,1):C.GC_43,(0,2):C.GC_40,(0,3):C.GC_26,(0,7):C.GC_634,(0,4):C.GC_633,(0,6):C.GC_633,(0,0):C.GC_632})

V_148 = Vertex(name = 'V_148',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_17,(0,8):C.GC_20,(1,0):C.GC_1024,(3,0):C.GC_1114,(0,6):C.GC_936,(2,6):C.GC_1026,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_46,(3,3):C.GC_47,(1,4):C.GC_48,(3,4):C.GC_49,(1,1):C.GC_655,(3,1):C.GC_656,(0,2):C.GC_58,(2,2):C.GC_59})

V_149 = Vertex(name = 'V_149',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_945,(1,1):C.GC_1035,(0,0):C.GC_76,(1,0):C.GC_77})

V_150 = Vertex(name = 'V_150',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_954,(1,1):C.GC_1044,(0,0):C.GC_94,(1,0):C.GC_95})

V_151 = Vertex(name = 'V_151',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_937,(1,1):C.GC_1027,(0,0):C.GC_60,(1,0):C.GC_61})

V_152 = Vertex(name = 'V_152',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_14,(0,8):C.GC_45,(1,0):C.GC_1018,(3,0):C.GC_1108,(0,6):C.GC_946,(2,6):C.GC_1036,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_46,(3,3):C.GC_47,(1,4):C.GC_48,(3,4):C.GC_49,(1,1):C.GC_409,(3,1):C.GC_410,(0,2):C.GC_78,(2,2):C.GC_79})

V_153 = Vertex(name = 'V_153',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_955,(1,1):C.GC_1045,(0,0):C.GC_96,(1,0):C.GC_97})

V_154 = Vertex(name = 'V_154',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_938,(1,1):C.GC_1028,(0,0):C.GC_62,(1,0):C.GC_63})

V_155 = Vertex(name = 'V_155',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_947,(1,1):C.GC_1037,(0,0):C.GC_80,(1,0):C.GC_81})

V_156 = Vertex(name = 'V_156',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_14,(0,8):C.GC_45,(1,0):C.GC_1021,(3,0):C.GC_1111,(0,6):C.GC_956,(2,6):C.GC_1046,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_46,(3,3):C.GC_47,(1,4):C.GC_48,(3,4):C.GC_49,(1,1):C.GC_565,(3,1):C.GC_566,(0,2):C.GC_98,(2,2):C.GC_99})

V_157 = Vertex(name = 'V_157',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_939,(1,1):C.GC_1029,(0,0):C.GC_64,(1,0):C.GC_65})

V_158 = Vertex(name = 'V_158',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_948,(1,1):C.GC_1038,(0,0):C.GC_82,(1,0):C.GC_83})

V_159 = Vertex(name = 'V_159',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_957,(1,1):C.GC_1047,(0,0):C.GC_100,(1,0):C.GC_101})

V_160 = Vertex(name = 'V_160',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_16,(0,3):C.GC_44,(0,1):C.GC_940,(2,1):C.GC_1030,(0,0):C.GC_66,(2,0):C.GC_67})

V_161 = Vertex(name = 'V_161',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_949,(1,1):C.GC_1039,(0,0):C.GC_84,(1,0):C.GC_85})

V_162 = Vertex(name = 'V_162',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_958,(1,1):C.GC_1048,(0,0):C.GC_102,(1,0):C.GC_103})

V_163 = Vertex(name = 'V_163',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_941,(1,1):C.GC_1031,(0,0):C.GC_68,(1,0):C.GC_69})

V_164 = Vertex(name = 'V_164',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_950,(1,1):C.GC_1040,(0,0):C.GC_86,(1,0):C.GC_87})

V_165 = Vertex(name = 'V_165',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_959,(1,1):C.GC_1049,(0,0):C.GC_104,(1,0):C.GC_105})

V_166 = Vertex(name = 'V_166',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_942,(1,1):C.GC_1032,(0,0):C.GC_70,(1,0):C.GC_71})

V_167 = Vertex(name = 'V_167',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_951,(1,1):C.GC_1041,(0,0):C.GC_88,(1,0):C.GC_89})

V_168 = Vertex(name = 'V_168',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_960,(1,1):C.GC_1050,(0,0):C.GC_106,(1,0):C.GC_107})

V_169 = Vertex(name = 'V_169',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_943,(1,1):C.GC_1033,(0,0):C.GC_72,(1,0):C.GC_73})

V_170 = Vertex(name = 'V_170',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_952,(1,1):C.GC_1042,(0,0):C.GC_90,(1,0):C.GC_91})

V_171 = Vertex(name = 'V_171',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_961,(1,1):C.GC_1051,(0,0):C.GC_108,(1,0):C.GC_109})

V_172 = Vertex(name = 'V_172',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_16,(0,3):C.GC_44,(0,1):C.GC_944,(2,1):C.GC_1034,(0,0):C.GC_74,(2,0):C.GC_75})

V_173 = Vertex(name = 'V_173',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_953,(1,1):C.GC_1043,(0,0):C.GC_92,(1,0):C.GC_93})

V_174 = Vertex(name = 'V_174',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_962,(1,1):C.GC_1052,(0,0):C.GC_110,(1,0):C.GC_111})

V_175 = Vertex(name = 'V_175',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_963,(1,1):C.GC_1053,(0,0):C.GC_112,(1,0):C.GC_113})

V_176 = Vertex(name = 'V_176',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_16,(0,3):C.GC_44,(0,1):C.GC_972,(2,1):C.GC_1062,(0,0):C.GC_130,(2,0):C.GC_131})

V_177 = Vertex(name = 'V_177',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_981,(1,1):C.GC_1071,(0,0):C.GC_148,(1,0):C.GC_149})

V_178 = Vertex(name = 'V_178',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_964,(1,1):C.GC_1054,(0,0):C.GC_114,(1,0):C.GC_115})

V_179 = Vertex(name = 'V_179',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_973,(1,1):C.GC_1063,(0,0):C.GC_132,(1,0):C.GC_133})

V_180 = Vertex(name = 'V_180',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_982,(1,1):C.GC_1072,(0,0):C.GC_150,(1,0):C.GC_151})

V_181 = Vertex(name = 'V_181',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_965,(1,1):C.GC_1055,(0,0):C.GC_116,(1,0):C.GC_117})

V_182 = Vertex(name = 'V_182',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_974,(1,1):C.GC_1064,(0,0):C.GC_134,(1,0):C.GC_135})

V_183 = Vertex(name = 'V_183',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_983,(1,1):C.GC_1073,(0,0):C.GC_152,(1,0):C.GC_153})

V_184 = Vertex(name = 'V_184',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_14,(0,8):C.GC_45,(1,0):C.GC_1025,(3,0):C.GC_1115,(0,6):C.GC_966,(2,6):C.GC_1056,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_46,(3,3):C.GC_47,(1,4):C.GC_48,(3,4):C.GC_49,(1,1):C.GC_663,(3,1):C.GC_664,(0,2):C.GC_118,(2,2):C.GC_119})

V_185 = Vertex(name = 'V_185',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_975,(1,1):C.GC_1065,(0,0):C.GC_136,(1,0):C.GC_137})

V_186 = Vertex(name = 'V_186',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_984,(1,1):C.GC_1074,(0,0):C.GC_154,(1,0):C.GC_155})

V_187 = Vertex(name = 'V_187',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_967,(1,1):C.GC_1057,(0,0):C.GC_120,(1,0):C.GC_121})

V_188 = Vertex(name = 'V_188',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_17,(0,8):C.GC_20,(1,0):C.GC_1019,(3,0):C.GC_1109,(0,6):C.GC_976,(2,6):C.GC_1066,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_46,(3,3):C.GC_47,(1,4):C.GC_48,(3,4):C.GC_49,(1,1):C.GC_541,(3,1):C.GC_542,(0,2):C.GC_138,(2,2):C.GC_139})

V_189 = Vertex(name = 'V_189',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_985,(1,1):C.GC_1075,(0,0):C.GC_156,(1,0):C.GC_157})

V_190 = Vertex(name = 'V_190',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_968,(1,1):C.GC_1058,(0,0):C.GC_122,(1,0):C.GC_123})

V_191 = Vertex(name = 'V_191',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_977,(1,1):C.GC_1067,(0,0):C.GC_140,(1,0):C.GC_141})

V_192 = Vertex(name = 'V_192',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_14,(0,8):C.GC_45,(1,0):C.GC_1022,(3,0):C.GC_1112,(0,6):C.GC_986,(2,6):C.GC_1076,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_46,(3,3):C.GC_47,(1,4):C.GC_48,(3,4):C.GC_49,(1,1):C.GC_573,(3,1):C.GC_574,(0,2):C.GC_158,(2,2):C.GC_159})

V_193 = Vertex(name = 'V_193',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_969,(1,1):C.GC_1059,(0,0):C.GC_124,(1,0):C.GC_125})

V_194 = Vertex(name = 'V_194',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_978,(1,1):C.GC_1068,(0,0):C.GC_142,(1,0):C.GC_143})

V_195 = Vertex(name = 'V_195',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_987,(1,1):C.GC_1077,(0,0):C.GC_160,(1,0):C.GC_161})

V_196 = Vertex(name = 'V_196',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_970,(1,1):C.GC_1060,(0,0):C.GC_126,(1,0):C.GC_127})

V_197 = Vertex(name = 'V_197',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_979,(1,1):C.GC_1069,(0,0):C.GC_144,(1,0):C.GC_145})

V_198 = Vertex(name = 'V_198',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_988,(1,1):C.GC_1078,(0,0):C.GC_162,(1,0):C.GC_163})

V_199 = Vertex(name = 'V_199',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_971,(1,1):C.GC_1061,(0,0):C.GC_128,(1,0):C.GC_129})

V_200 = Vertex(name = 'V_200',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_16,(0,3):C.GC_44,(0,1):C.GC_980,(2,1):C.GC_1070,(0,0):C.GC_146,(2,0):C.GC_147})

V_201 = Vertex(name = 'V_201',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_989,(1,1):C.GC_1079,(0,0):C.GC_164,(1,0):C.GC_165})

V_202 = Vertex(name = 'V_202',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_990,(1,1):C.GC_1080,(0,0):C.GC_166,(1,0):C.GC_167})

V_203 = Vertex(name = 'V_203',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_999,(1,1):C.GC_1089,(0,0):C.GC_184,(1,0):C.GC_185})

V_204 = Vertex(name = 'V_204',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_16,(0,3):C.GC_44,(0,1):C.GC_1008,(2,1):C.GC_1098,(0,0):C.GC_202,(2,0):C.GC_203})

V_205 = Vertex(name = 'V_205',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_991,(1,1):C.GC_1081,(0,0):C.GC_168,(1,0):C.GC_169})

V_206 = Vertex(name = 'V_206',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1000,(1,1):C.GC_1090,(0,0):C.GC_186,(1,0):C.GC_187})

V_207 = Vertex(name = 'V_207',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1009,(1,1):C.GC_1099,(0,0):C.GC_204,(1,0):C.GC_205})

V_208 = Vertex(name = 'V_208',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_992,(1,1):C.GC_1082,(0,0):C.GC_170,(1,0):C.GC_171})

V_209 = Vertex(name = 'V_209',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1001,(1,1):C.GC_1091,(0,0):C.GC_188,(1,0):C.GC_189})

V_210 = Vertex(name = 'V_210',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1010,(1,1):C.GC_1100,(0,0):C.GC_206,(1,0):C.GC_207})

V_211 = Vertex(name = 'V_211',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_993,(1,1):C.GC_1083,(0,0):C.GC_172,(1,0):C.GC_173})

V_212 = Vertex(name = 'V_212',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1002,(1,1):C.GC_1092,(0,0):C.GC_190,(1,0):C.GC_191})

V_213 = Vertex(name = 'V_213',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1011,(1,1):C.GC_1101,(0,0):C.GC_208,(1,0):C.GC_209})

V_214 = Vertex(name = 'V_214',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_994,(1,1):C.GC_1084,(0,0):C.GC_174,(1,0):C.GC_175})

V_215 = Vertex(name = 'V_215',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1003,(1,1):C.GC_1093,(0,0):C.GC_192,(1,0):C.GC_193})

V_216 = Vertex(name = 'V_216',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,2):C.GC_16,(0,3):C.GC_44,(0,1):C.GC_1012,(2,1):C.GC_1102,(0,0):C.GC_210,(2,0):C.GC_211})

V_217 = Vertex(name = 'V_217',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_995,(1,1):C.GC_1085,(0,0):C.GC_176,(1,0):C.GC_177})

V_218 = Vertex(name = 'V_218',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1004,(1,1):C.GC_1094,(0,0):C.GC_194,(1,0):C.GC_195})

V_219 = Vertex(name = 'V_219',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1013,(1,1):C.GC_1103,(0,0):C.GC_212,(1,0):C.GC_213})

V_220 = Vertex(name = 'V_220',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_14,(0,8):C.GC_45,(1,0):C.GC_1023,(3,0):C.GC_1113,(0,6):C.GC_996,(2,6):C.GC_1086,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_46,(3,3):C.GC_47,(1,4):C.GC_48,(3,4):C.GC_49,(1,1):C.GC_653,(3,1):C.GC_654,(0,2):C.GC_178,(2,2):C.GC_179})

V_221 = Vertex(name = 'V_221',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1005,(1,1):C.GC_1095,(0,0):C.GC_196,(1,0):C.GC_197})

V_222 = Vertex(name = 'V_222',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1014,(1,1):C.GC_1104,(0,0):C.GC_214,(1,0):C.GC_215})

V_223 = Vertex(name = 'V_223',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_997,(1,1):C.GC_1087,(0,0):C.GC_180,(1,0):C.GC_181})

V_224 = Vertex(name = 'V_224',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_14,(0,8):C.GC_45,(1,0):C.GC_1017,(3,0):C.GC_1107,(0,6):C.GC_1006,(2,6):C.GC_1096,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_46,(3,3):C.GC_47,(1,4):C.GC_48,(3,4):C.GC_49,(1,1):C.GC_389,(3,1):C.GC_390,(0,2):C.GC_198,(2,2):C.GC_199})

V_225 = Vertex(name = 'V_225',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1015,(1,1):C.GC_1105,(0,0):C.GC_216,(1,0):C.GC_217})

V_226 = Vertex(name = 'V_226',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_998,(1,1):C.GC_1088,(0,0):C.GC_182,(1,0):C.GC_183})

V_227 = Vertex(name = 'V_227',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF12, L.FFFF2 ],
               couplings = {(0,1):C.GC_1007,(1,1):C.GC_1097,(0,0):C.GC_200,(1,0):C.GC_201})

V_228 = Vertex(name = 'V_228',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF2, L.FFFF3, L.FFFF4 ],
               couplings = {(1,7):C.GC_17,(0,8):C.GC_20,(1,0):C.GC_1020,(3,0):C.GC_1110,(0,6):C.GC_1016,(2,6):C.GC_1106,(1,5):C.GC_41,(3,5):C.GC_42,(1,3):C.GC_46,(3,3):C.GC_47,(1,4):C.GC_48,(3,4):C.GC_49,(1,1):C.GC_563,(3,1):C.GC_564,(0,2):C.GC_218,(2,2):C.GC_219})

V_229 = Vertex(name = 'V_229',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
               couplings = {(0,1):C.GC_247,(0,0):C.GC_245,(0,2):C.GC_222})

V_230 = Vertex(name = 'V_230',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_338})

V_231 = Vertex(name = 'V_231',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,3):C.GC_1,(0,2):C.GC_351,(0,0):C.GC_340,(0,1):C.GC_715,(0,4):C.GC_414})

V_232 = Vertex(name = 'V_232',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,3):C.GC_1,(0,2):C.GC_351,(0,0):C.GC_340,(0,1):C.GC_719,(0,4):C.GC_548})

V_233 = Vertex(name = 'V_233',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,3):C.GC_1,(0,2):C.GC_351,(0,0):C.GC_340,(0,1):C.GC_711,(0,4):C.GC_374})

V_234 = Vertex(name = 'V_234',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,2):C.GC_4,(0,3):C.GC_352,(0,0):C.GC_340,(0,1):C.GC_747,(0,4):C.GC_470})

V_235 = Vertex(name = 'V_235',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,2):C.GC_4,(0,3):C.GC_352,(0,0):C.GC_340,(0,1):C.GC_751,(0,4):C.GC_526})

V_236 = Vertex(name = 'V_236',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,3):C.GC_352,(0,0):C.GC_340,(0,2):C.GC_4,(0,1):C.GC_755,(0,4):C.GC_638})

V_237 = Vertex(name = 'V_237',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_2,(0,3):C.GC_351,(0,0):C.GC_339,(0,1):C.GC_1160,(0,4):C.GC_671})

V_238 = Vertex(name = 'V_238',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_2,(0,3):C.GC_351,(0,0):C.GC_339,(0,1):C.GC_1152,(0,4):C.GC_394})

V_239 = Vertex(name = 'V_239',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_2,(0,3):C.GC_351,(0,0):C.GC_339,(0,1):C.GC_1156,(0,4):C.GC_578})

V_240 = Vertex(name = 'V_240',
               particles = [ P.ve__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_353})

V_241 = Vertex(name = 'V_241',
               particles = [ P.vm__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_353})

V_242 = Vertex(name = 'V_242',
               particles = [ P.vt__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_353})

V_243 = Vertex(name = 'V_243',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_679,(0,2):C.GC_401})

V_244 = Vertex(name = 'V_244',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_682,(0,2):C.GC_533})

V_245 = Vertex(name = 'V_245',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_676,(0,2):C.GC_363})

V_246 = Vertex(name = 'V_246',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_1123,(0,2):C.GC_645})

V_247 = Vertex(name = 'V_247',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_1117,(0,2):C.GC_381})

V_248 = Vertex(name = 'V_248',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV2, L.FFV5, L.FFV8 ],
               couplings = {(0,1):C.GC_6,(0,0):C.GC_1120,(0,2):C.GC_555})

V_249 = Vertex(name = 'V_249',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_1144,(0,3):C.GC_400,(0,2):C.GC_285,(0,0):C.GC_280})

V_250 = Vertex(name = 'V_250',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_286})

V_251 = Vertex(name = 'V_251',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_287})

V_252 = Vertex(name = 'V_252',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_288})

V_253 = Vertex(name = 'V_253',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_1134,(0,3):C.GC_532,(0,2):C.GC_289,(0,0):C.GC_280})

V_254 = Vertex(name = 'V_254',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_290})

V_255 = Vertex(name = 'V_255',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_291})

V_256 = Vertex(name = 'V_256',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_292})

V_257 = Vertex(name = 'V_257',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_1139,(0,3):C.GC_362,(0,2):C.GC_293,(0,0):C.GC_280})

V_258 = Vertex(name = 'V_258',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_1145,(0,3):C.GC_403,(0,0):C.GC_225,(0,2):C.GC_302})

V_259 = Vertex(name = 'V_259',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_332})

V_260 = Vertex(name = 'V_260',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_226,(0,1):C.GC_303})

V_261 = Vertex(name = 'V_261',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_237})

V_262 = Vertex(name = 'V_262',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_227,(0,1):C.GC_304})

V_263 = Vertex(name = 'V_263',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_238})

V_264 = Vertex(name = 'V_264',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_228,(0,1):C.GC_305})

V_265 = Vertex(name = 'V_265',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_239})

V_266 = Vertex(name = 'V_266',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_1135,(0,3):C.GC_535,(0,0):C.GC_229,(0,2):C.GC_306})

V_267 = Vertex(name = 'V_267',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_333})

V_268 = Vertex(name = 'V_268',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_230,(0,1):C.GC_307})

V_269 = Vertex(name = 'V_269',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_240})

V_270 = Vertex(name = 'V_270',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_231,(0,1):C.GC_308})

V_271 = Vertex(name = 'V_271',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_241})

V_272 = Vertex(name = 'V_272',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_232,(0,1):C.GC_309})

V_273 = Vertex(name = 'V_273',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_242})

V_274 = Vertex(name = 'V_274',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_1140,(0,3):C.GC_365,(0,0):C.GC_233,(0,2):C.GC_310})

V_275 = Vertex(name = 'V_275',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_334})

V_276 = Vertex(name = 'V_276',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_457,(0,0):C.GC_224})

V_277 = Vertex(name = 'V_277',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_331})

V_278 = Vertex(name = 'V_278',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_513,(0,0):C.GC_224})

V_279 = Vertex(name = 'V_279',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_331})

V_280 = Vertex(name = 'V_280',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_621,(0,0):C.GC_224})

V_281 = Vertex(name = 'V_281',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_331})

V_282 = Vertex(name = 'V_282',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_419,(0,0):C.GC_279})

V_283 = Vertex(name = 'V_283',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_475,(0,0):C.GC_279})

V_284 = Vertex(name = 'V_284',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,1):C.GC_583,(0,0):C.GC_279})

V_285 = Vertex(name = 'V_285',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_698,(0,3):C.GC_644,(0,2):C.GC_756,(0,0):C.GC_280})

V_286 = Vertex(name = 'V_286',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_757})

V_287 = Vertex(name = 'V_287',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_758})

V_288 = Vertex(name = 'V_288',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_759})

V_289 = Vertex(name = 'V_289',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_703,(0,3):C.GC_380,(0,2):C.GC_760,(0,0):C.GC_280})

V_290 = Vertex(name = 'V_290',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_761})

V_291 = Vertex(name = 'V_291',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_762})

V_292 = Vertex(name = 'V_292',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS3 ],
               couplings = {(0,0):C.GC_763})

V_293 = Vertex(name = 'V_293',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,1):C.GC_693,(0,3):C.GC_554,(0,2):C.GC_764,(0,0):C.GC_280})

V_294 = Vertex(name = 'V_294',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_699,(0,3):C.GC_647,(0,0):C.GC_775,(0,2):C.GC_765})

V_295 = Vertex(name = 'V_295',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_774})

V_296 = Vertex(name = 'V_296',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_780,(0,1):C.GC_766})

V_297 = Vertex(name = 'V_297',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_781})

V_298 = Vertex(name = 'V_298',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_786,(0,1):C.GC_767})

V_299 = Vertex(name = 'V_299',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_787})

V_300 = Vertex(name = 'V_300',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_776,(0,1):C.GC_768})

V_301 = Vertex(name = 'V_301',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_777})

V_302 = Vertex(name = 'V_302',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_704,(0,3):C.GC_383,(0,0):C.GC_783,(0,2):C.GC_769})

V_303 = Vertex(name = 'V_303',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_782})

V_304 = Vertex(name = 'V_304',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_788,(0,1):C.GC_770})

V_305 = Vertex(name = 'V_305',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_789})

V_306 = Vertex(name = 'V_306',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_778,(0,1):C.GC_771})

V_307 = Vertex(name = 'V_307',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_779})

V_308 = Vertex(name = 'V_308',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV3 ],
               couplings = {(0,0):C.GC_784,(0,1):C.GC_772})

V_309 = Vertex(name = 'V_309',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_785})

V_310 = Vertex(name = 'V_310',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV8 ],
               couplings = {(0,1):C.GC_694,(0,3):C.GC_557,(0,0):C.GC_791,(0,2):C.GC_773})

V_311 = Vertex(name = 'V_311',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_790})

V_312 = Vertex(name = 'V_312',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_730,(0,0):C.GC_224})

V_313 = Vertex(name = 'V_313',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_331})

V_314 = Vertex(name = 'V_314',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_735,(0,0):C.GC_224})

V_315 = Vertex(name = 'V_315',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_331})

V_316 = Vertex(name = 'V_316',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2 ],
               couplings = {(0,1):C.GC_740,(0,0):C.GC_224})

V_317 = Vertex(name = 'V_317',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_331})

V_318 = Vertex(name = 'V_318',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_729,(0,0):C.GC_279})

V_319 = Vertex(name = 'V_319',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_734,(0,0):C.GC_279})

V_320 = Vertex(name = 'V_320',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2 ],
               couplings = {(0,1):C.GC_739,(0,0):C.GC_279})

V_321 = Vertex(name = 'V_321',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_235,(0,4):C.GC_326,(0,3):C.GC_248,(0,2):C.GC_335,(0,1):C.GC_714,(0,5):C.GC_413})

V_322 = Vertex(name = 'V_322',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_344,(0,1):C.GC_348})

V_323 = Vertex(name = 'V_323',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_235,(0,4):C.GC_326,(0,3):C.GC_248,(0,2):C.GC_335,(0,1):C.GC_718,(0,5):C.GC_547})

V_324 = Vertex(name = 'V_324',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_344,(0,1):C.GC_348})

V_325 = Vertex(name = 'V_325',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,0):C.GC_235,(0,4):C.GC_326,(0,3):C.GC_248,(0,2):C.GC_335,(0,1):C.GC_710,(0,5):C.GC_373})

V_326 = Vertex(name = 'V_326',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_344,(0,1):C.GC_348})

V_327 = Vertex(name = 'V_327',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_317,(0,2):C.GC_312,(0,1):C.GC_712,(0,3):C.GC_411})

V_328 = Vertex(name = 'V_328',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_317,(0,2):C.GC_312,(0,1):C.GC_716,(0,3):C.GC_545})

V_329 = Vertex(name = 'V_329',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_317,(0,2):C.GC_312,(0,1):C.GC_708,(0,3):C.GC_371})

V_330 = Vertex(name = 'V_330',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_235,(0,3):C.GC_328,(0,4):C.GC_249,(0,2):C.GC_336,(0,1):C.GC_746,(0,5):C.GC_469})

V_331 = Vertex(name = 'V_331',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_343,(0,1):C.GC_349})

V_332 = Vertex(name = 'V_332',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_235,(0,3):C.GC_328,(0,4):C.GC_249,(0,2):C.GC_336,(0,1):C.GC_750,(0,5):C.GC_525})

V_333 = Vertex(name = 'V_333',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_343,(0,1):C.GC_349})

V_334 = Vertex(name = 'V_334',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV6, L.FFV8 ],
               couplings = {(0,0):C.GC_235,(0,3):C.GC_328,(0,4):C.GC_249,(0,2):C.GC_336,(0,1):C.GC_754,(0,5):C.GC_637})

V_335 = Vertex(name = 'V_335',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_343,(0,1):C.GC_349})

V_336 = Vertex(name = 'V_336',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_315,(0,2):C.GC_313,(0,1):C.GC_744,(0,3):C.GC_467})

V_337 = Vertex(name = 'V_337',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_315,(0,2):C.GC_313,(0,1):C.GC_748,(0,3):C.GC_523})

V_338 = Vertex(name = 'V_338',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_315,(0,2):C.GC_313,(0,1):C.GC_752,(0,3):C.GC_635})

V_339 = Vertex(name = 'V_339',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_234,(0,4):C.GC_248,(0,3):C.GC_327,(0,2):C.GC_337,(0,1):C.GC_1159,(0,5):C.GC_670})

V_340 = Vertex(name = 'V_340',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7 ],
               couplings = {(0,0):C.GC_342,(0,1):C.GC_348})

V_341 = Vertex(name = 'V_341',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_234,(0,3):C.GC_327,(0,4):C.GC_248,(0,2):C.GC_337,(0,1):C.GC_1151,(0,5):C.GC_393})

V_342 = Vertex(name = 'V_342',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7 ],
               couplings = {(0,0):C.GC_342,(0,1):C.GC_348})

V_343 = Vertex(name = 'V_343',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV5, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_234,(0,3):C.GC_327,(0,4):C.GC_248,(0,2):C.GC_337,(0,1):C.GC_1155,(0,5):C.GC_577})

V_344 = Vertex(name = 'V_344',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7 ],
               couplings = {(0,0):C.GC_342,(0,1):C.GC_348})

V_345 = Vertex(name = 'V_345',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_316,(0,2):C.GC_318,(0,1):C.GC_1157,(0,3):C.GC_668})

V_346 = Vertex(name = 'V_346',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_316,(0,2):C.GC_318,(0,1):C.GC_1149,(0,3):C.GC_391})

V_347 = Vertex(name = 'V_347',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4 ],
               couplings = {(0,0):C.GC_316,(0,2):C.GC_318,(0,1):C.GC_1153,(0,3):C.GC_575})

V_348 = Vertex(name = 'V_348',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_254})

V_349 = Vertex(name = 'V_349',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_350})

V_350 = Vertex(name = 'V_350',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_254})

V_351 = Vertex(name = 'V_351',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_350})

V_352 = Vertex(name = 'V_352',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_254})

V_353 = Vertex(name = 'V_353',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_350})

V_354 = Vertex(name = 'V_354',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_314})

V_355 = Vertex(name = 'V_355',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_314})

V_356 = Vertex(name = 'V_356',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_314})

V_357 = Vertex(name = 'V_357',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_19,(0,7):C.GC_19,(0,0):C.GC_41,(2,0):C.GC_42,(1,3):C.GC_41,(3,3):C.GC_42,(1,1):C.GC_41,(3,1):C.GC_42,(1,2):C.GC_10,(0,4):C.GC_41,(2,4):C.GC_42,(0,5):C.GC_10})

V_358 = Vertex(name = 'V_358',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_15,(0,5):C.GC_18,(1,2):C.GC_41,(2,2):C.GC_42,(1,0):C.GC_41,(2,0):C.GC_42,(1,1):C.GC_22,(0,3):C.GC_23})

V_359 = Vertex(name = 'V_359',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_15,(0,5):C.GC_18,(1,2):C.GC_41,(2,2):C.GC_42,(1,0):C.GC_41,(2,0):C.GC_42,(1,1):C.GC_22,(0,3):C.GC_23})

V_360 = Vertex(name = 'V_360',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_19,(0,7):C.GC_19,(0,0):C.GC_41,(2,0):C.GC_42,(1,3):C.GC_41,(3,3):C.GC_42,(1,1):C.GC_41,(3,1):C.GC_42,(1,2):C.GC_10,(0,4):C.GC_41,(2,4):C.GC_42,(0,5):C.GC_10})

V_361 = Vertex(name = 'V_361',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_15,(0,5):C.GC_18,(1,2):C.GC_41,(2,2):C.GC_42,(1,0):C.GC_41,(2,0):C.GC_42,(1,1):C.GC_22,(0,3):C.GC_23})

V_362 = Vertex(name = 'V_362',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_19,(0,7):C.GC_19,(0,0):C.GC_41,(2,0):C.GC_42,(1,3):C.GC_41,(3,3):C.GC_42,(1,1):C.GC_41,(3,1):C.GC_42,(1,2):C.GC_10,(0,4):C.GC_41,(2,4):C.GC_42,(0,5):C.GC_10})

V_363 = Vertex(name = 'V_363',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_11,(0,7):C.GC_11,(0,0):C.GC_36,(0,3):C.GC_36,(0,1):C.GC_36,(0,2):C.GC_25,(0,4):C.GC_36,(0,5):C.GC_25})

V_364 = Vertex(name = 'V_364',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_37,(0,4):C.GC_38,(0,2):C.GC_36,(0,0):C.GC_36,(0,1):C.GC_25})

V_365 = Vertex(name = 'V_365',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_37,(0,4):C.GC_38,(0,2):C.GC_36,(0,0):C.GC_36,(0,1):C.GC_25})

V_366 = Vertex(name = 'V_366',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_11,(0,7):C.GC_11,(0,0):C.GC_36,(0,3):C.GC_36,(0,1):C.GC_36,(0,2):C.GC_25,(0,4):C.GC_36,(0,5):C.GC_25})

V_367 = Vertex(name = 'V_367',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF3, L.FFFF4 ],
               couplings = {(0,3):C.GC_37,(0,4):C.GC_38,(0,2):C.GC_36,(0,0):C.GC_36,(0,1):C.GC_25})

V_368 = Vertex(name = 'V_368',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(0,6):C.GC_11,(0,7):C.GC_11,(0,0):C.GC_36,(0,3):C.GC_36,(0,1):C.GC_36,(0,2):C.GC_25,(0,4):C.GC_36,(0,5):C.GC_25})

V_369 = Vertex(name = 'V_369',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_19,(0,7):C.GC_19,(0,0):C.GC_46,(2,0):C.GC_47,(1,3):C.GC_46,(3,3):C.GC_47,(1,1):C.GC_46,(3,1):C.GC_47,(1,2):C.GC_21,(0,4):C.GC_46,(2,4):C.GC_47,(0,5):C.GC_21})

V_370 = Vertex(name = 'V_370',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_15,(0,5):C.GC_18,(1,2):C.GC_46,(2,2):C.GC_47,(1,0):C.GC_46,(2,0):C.GC_47,(1,1):C.GC_50,(0,3):C.GC_51})

V_371 = Vertex(name = 'V_371',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_15,(0,5):C.GC_18,(1,2):C.GC_46,(2,2):C.GC_47,(1,0):C.GC_46,(2,0):C.GC_47,(1,1):C.GC_50,(0,3):C.GC_51})

V_372 = Vertex(name = 'V_372',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_19,(0,7):C.GC_19,(0,0):C.GC_46,(2,0):C.GC_47,(1,3):C.GC_46,(3,3):C.GC_47,(1,1):C.GC_46,(3,1):C.GC_47,(1,2):C.GC_21,(0,4):C.GC_46,(2,4):C.GC_47,(0,5):C.GC_21})

V_373 = Vertex(name = 'V_373',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,4):C.GC_15,(0,5):C.GC_18,(1,2):C.GC_46,(2,2):C.GC_47,(1,0):C.GC_46,(2,0):C.GC_47,(1,1):C.GC_50,(0,3):C.GC_51})

V_374 = Vertex(name = 'V_374',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF3, L.FFFF4 ],
               couplings = {(1,6):C.GC_19,(0,7):C.GC_19,(0,0):C.GC_46,(2,0):C.GC_47,(1,3):C.GC_46,(3,3):C.GC_47,(1,1):C.GC_46,(3,1):C.GC_47,(1,2):C.GC_21,(0,4):C.GC_46,(2,4):C.GC_47,(0,5):C.GC_21})

V_375 = Vertex(name = 'V_375',
               particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_11,(0,0):C.GC_36})

V_376 = Vertex(name = 'V_376',
               particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_37,(0,0):C.GC_36})

V_377 = Vertex(name = 'V_377',
               particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_37,(0,0):C.GC_36})

V_378 = Vertex(name = 'V_378',
               particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_38})

V_379 = Vertex(name = 'V_379',
               particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_38})

V_380 = Vertex(name = 'V_380',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_38})

V_381 = Vertex(name = 'V_381',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_37,(0,0):C.GC_36})

V_382 = Vertex(name = 'V_382',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_11,(0,0):C.GC_36})

V_383 = Vertex(name = 'V_383',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_37,(0,0):C.GC_36})

V_384 = Vertex(name = 'V_384',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_38})

V_385 = Vertex(name = 'V_385',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_38})

V_386 = Vertex(name = 'V_386',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF4 ],
               couplings = {(0,0):C.GC_38})

V_387 = Vertex(name = 'V_387',
               particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_37,(0,0):C.GC_36})

V_388 = Vertex(name = 'V_388',
               particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_37,(0,0):C.GC_36})

V_389 = Vertex(name = 'V_389',
               particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_11,(0,0):C.GC_36})

V_390 = Vertex(name = 'V_390',
               particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_11,(0,1):C.GC_11})

V_391 = Vertex(name = 'V_391',
               particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_37,(0,1):C.GC_38})

V_392 = Vertex(name = 'V_392',
               particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_37,(0,1):C.GC_38})

V_393 = Vertex(name = 'V_393',
               particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_11,(0,1):C.GC_11})

V_394 = Vertex(name = 'V_394',
               particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_37,(0,1):C.GC_38})

V_395 = Vertex(name = 'V_395',
               particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF4 ],
               couplings = {(0,0):C.GC_11,(0,1):C.GC_11})

V_396 = Vertex(name = 'V_396',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_12,(0,0):C.GC_35})

V_397 = Vertex(name = 'V_397',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_12,(0,0):C.GC_35})

V_398 = Vertex(name = 'V_398',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_12,(0,0):C.GC_35})

V_399 = Vertex(name = 'V_399',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_12,(0,0):C.GC_35})

V_400 = Vertex(name = 'V_400',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_12,(0,0):C.GC_35})

V_401 = Vertex(name = 'V_401',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_12,(0,0):C.GC_35})

V_402 = Vertex(name = 'V_402',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_12,(0,0):C.GC_35})

V_403 = Vertex(name = 'V_403',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_12,(0,0):C.GC_35})

V_404 = Vertex(name = 'V_404',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_12,(0,0):C.GC_35})

V_405 = Vertex(name = 'V_405',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_13,(0,0):C.GC_40})

V_406 = Vertex(name = 'V_406',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_13,(0,0):C.GC_40})

V_407 = Vertex(name = 'V_407',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_13,(0,0):C.GC_40})

V_408 = Vertex(name = 'V_408',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_13,(0,0):C.GC_40})

V_409 = Vertex(name = 'V_409',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_13,(0,0):C.GC_40})

V_410 = Vertex(name = 'V_410',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_13,(0,0):C.GC_40})

V_411 = Vertex(name = 'V_411',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_13,(0,0):C.GC_40})

V_412 = Vertex(name = 'V_412',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_13,(0,0):C.GC_40})

V_413 = Vertex(name = 'V_413',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF4 ],
               couplings = {(0,1):C.GC_13,(0,0):C.GC_40})

V_414 = Vertex(name = 'V_414',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_713,(0,1):C.GC_412})

V_415 = Vertex(name = 'V_415',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_717,(0,1):C.GC_546})

V_416 = Vertex(name = 'V_416',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_709,(0,1):C.GC_372})

V_417 = Vertex(name = 'V_417',
               particles = [ P.d__tilde__, P.d, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_678,(0,1):C.GC_399})

V_418 = Vertex(name = 'V_418',
               particles = [ P.s__tilde__, P.s, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_681,(0,1):C.GC_531})

V_419 = Vertex(name = 'V_419',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_675,(0,1):C.GC_361})

V_420 = Vertex(name = 'V_420',
               particles = [ P.d__tilde__, P.d, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_680,(0,1):C.GC_405})

V_421 = Vertex(name = 'V_421',
               particles = [ P.s__tilde__, P.s, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_683,(0,1):C.GC_537})

V_422 = Vertex(name = 'V_422',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_677,(0,1):C.GC_367})

V_423 = Vertex(name = 'V_423',
               particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_700,(0,1):C.GC_648})

V_424 = Vertex(name = 'V_424',
               particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_705,(0,1):C.GC_384})

V_425 = Vertex(name = 'V_425',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_695,(0,1):C.GC_558})

V_426 = Vertex(name = 'V_426',
               particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_701,(0,1):C.GC_406})

V_427 = Vertex(name = 'V_427',
               particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_706,(0,1):C.GC_538})

V_428 = Vertex(name = 'V_428',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_696,(0,1):C.GC_368})

V_429 = Vertex(name = 'V_429',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_745,(0,1):C.GC_468})

V_430 = Vertex(name = 'V_430',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_749,(0,1):C.GC_524})

V_431 = Vertex(name = 'V_431',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_753,(0,1):C.GC_636})

V_432 = Vertex(name = 'V_432',
               particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_731})

V_433 = Vertex(name = 'V_433',
               particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_736})

V_434 = Vertex(name = 'V_434',
               particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_741})

V_435 = Vertex(name = 'V_435',
               particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_732,(0,1):C.GC_459})

V_436 = Vertex(name = 'V_436',
               particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_737,(0,1):C.GC_515})

V_437 = Vertex(name = 'V_437',
               particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_742,(0,1):C.GC_623})

V_438 = Vertex(name = 'V_438',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_1158,(0,1):C.GC_669})

V_439 = Vertex(name = 'V_439',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_1150,(0,1):C.GC_392})

V_440 = Vertex(name = 'V_440',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_1154,(0,1):C.GC_576})

V_441 = Vertex(name = 'V_441',
               particles = [ P.u__tilde__, P.u, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_1122,(0,1):C.GC_643})

V_442 = Vertex(name = 'V_442',
               particles = [ P.c__tilde__, P.c, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_1116,(0,1):C.GC_379})

V_443 = Vertex(name = 'V_443',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS2, L.FFVS4 ],
               couplings = {(0,0):C.GC_1119,(0,1):C.GC_553})

V_444 = Vertex(name = 'V_444',
               particles = [ P.u__tilde__, P.u, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1124,(0,1):C.GC_649})

V_445 = Vertex(name = 'V_445',
               particles = [ P.c__tilde__, P.c, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1118,(0,1):C.GC_385})

V_446 = Vertex(name = 'V_446',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1121,(0,1):C.GC_559})

V_447 = Vertex(name = 'V_447',
               particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1146,(0,1):C.GC_404})

V_448 = Vertex(name = 'V_448',
               particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1136,(0,1):C.GC_536})

V_449 = Vertex(name = 'V_449',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1141,(0,1):C.GC_366})

V_450 = Vertex(name = 'V_450',
               particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1147,(0,1):C.GC_650})

V_451 = Vertex(name = 'V_451',
               particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1137,(0,1):C.GC_386})

V_452 = Vertex(name = 'V_452',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1142,(0,1):C.GC_560})

V_453 = Vertex(name = 'V_453',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_702,(0,1):C.GC_651})

V_454 = Vertex(name = 'V_454',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_707,(0,1):C.GC_387})

V_455 = Vertex(name = 'V_455',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_697,(0,1):C.GC_561})

V_456 = Vertex(name = 'V_456',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_733})

V_457 = Vertex(name = 'V_457',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_738})

V_458 = Vertex(name = 'V_458',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_743})

V_459 = Vertex(name = 'V_459',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1148,(0,1):C.GC_407})

V_460 = Vertex(name = 'V_460',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1138,(0,1):C.GC_539})

V_461 = Vertex(name = 'V_461',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1143,(0,1):C.GC_369})

V_462 = Vertex(name = 'V_462',
               particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_458})

V_463 = Vertex(name = 'V_463',
               particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_514})

V_464 = Vertex(name = 'V_464',
               particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_622})

V_465 = Vertex(name = 'V_465',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_460})

V_466 = Vertex(name = 'V_466',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_516})

V_467 = Vertex(name = 'V_467',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_624})

