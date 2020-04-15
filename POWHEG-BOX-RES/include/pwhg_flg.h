c -*- Fortran -*-

c flg_nlotest: perform calls to outfun for testing NLO output
c flg_withsubtr: counterterms are included in NLO test
c flg_withdamp: Born zero procedure
c flg_withreg: if regular regions exist or not
c flg_smartsig: remember or not equal squared amplitude
c flg_in_smartsig: set to true when the program is comuputing
c                  amplitudes to determine identical ones.
c                  Can be use to turn off kinematical cuts
c                  in the amplitudes
c flg_bornonly: do the Born contribution only
c flg_LOevents: generate events using only the Born. Real and virtual contributions
c               are identically zero

c flg_lightpart_check: in genflavreglist perform or not perform the check
c                     that there are no coloured light partons before flst_lightpart

c flg_debug: outputs extra infos for radiation region and randon numbers on the LHEF   
c flg_withnegweights: allows negative weighted events
c flg_jacsing:  importance sampling for singular jacobians in case of massless FSR
c flg_weightedev:  allows weighted events
c flg_pdfreweight: outputs extra infos useful for pdf's reweighting on the LHEF
c flg_collremnsamp:  importance sampling for collinear remnants
c flg_reweight: outputs extra infos for reweighting LH events
c flg_QEDonly: do ONLY photon radiation. No QCD radiation at all. It is set
c              by the user. No real diagrams with QCD radiation allowed

      logical flg_nlotest,flg_withsubtr,flg_withdamp,flg_withreg,
     1     flg_smartsig,flg_in_smartsig,flg_bornonly,flg_debug,
     2     flg_withnegweights,
     3     flg_jacsing,flg_weightedev,flg_pdfreweight,flg_collremnsamp,
     4     flg_lightpart_check,flg_btlscalereal,flg_btlscalect,
     5     flg_bornzerodamp,flg_ckkwscalup,
     6     flg_minlo,flg_minlo_nnll,flg_minlo_real,
     7     flg_reweight,flg_newweight,flg_fastbtlbound,
     8     flg_storemintupb,flg_doublefsr,flg_monitorubound,
     9     flg_drscheme,flg_withresrad,flg_with_em,flg_QEDonly,
     1     flg_LOevents,flg_evenmaxrat,flg_novirtual,flg_zerowidth,
     2     flg_ingen,flg_newrad,flg_allrad,flg_samexgridasbtilde,
     3     flg_mvemquadprec,flg_tiny_alphas,flg_virtonly,flg_softonly,
     4     flg_for_reweighting,flg_ubexcess_correct,flg_compress_lhe,flg_compress_upb,
     3     flg_rwl,flg_rwl_add,flg_fullrwgt,flg_noevents,
     6     flg_user_reshists_sep
      character * 1 flg_btildepart
      character * 20 flg_processid
      common/pwhg_flg/flg_nlotest,flg_withsubtr,flg_withdamp,
     1     flg_withreg,flg_smartsig,flg_in_smartsig,
     2     flg_bornonly,flg_debug,flg_LOevents,
     3     flg_withnegweights,flg_jacsing,flg_weightedev,
     4     flg_pdfreweight,flg_collremnsamp,flg_lightpart_check,
     5     flg_btlscalereal,flg_btlscalect,
     6     flg_bornzerodamp,flg_ckkwscalup,
     7     flg_minlo,flg_minlo_nnll,flg_minlo_real,
     8     flg_reweight,flg_newweight,flg_fastbtlbound,
     9     flg_storemintupb,flg_doublefsr,flg_monitorubound,
     1     flg_drscheme,flg_withresrad,flg_with_em,flg_QEDonly,
     2     flg_evenmaxrat,flg_novirtual,flg_zerowidth,flg_ingen,
     3     flg_newrad,flg_allrad,flg_samexgridasbtilde,
     4     flg_mvemquadprec,flg_tiny_alphas,flg_virtonly,
     5     flg_softonly,flg_for_reweighting,
     6     flg_ubexcess_correct,
     7     flg_rwl,flg_rwl_add,flg_compress_lhe,flg_compress_upb,
     8     flg_fullrwgt,flg_noevents,flg_user_reshists_sep,
c strings      
     9     flg_btildepart,flg_processid
      save /pwhg_flg/
