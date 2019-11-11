#WH
Aim to setup Higgs boson production in association with a W boson and jets, and the Higgs decay to $W^{+}W^{-}$, and one of the W bosons leptonic decay, another one hadronic decay. It will look like:

~~~~
p p > W H , W > lv ; H > W(lv) W(jj) 
~~~~

We want to control the leptonic decay W on shell according [this](https://sherpa.hepforge.org/doc/SHERPA-MC-2.2.8.html#DecayOS). MG5 cards cannot do this.

However, now the configurations have bugs. You can check the Run.dat_WHWW_4Channel and it's log file error_WHWW_4Channel.log, Run.dat_WH_1 and it's log file error_WH_1.log. We mainly refer to [this](https://sherpa.hepforge.org/doc/SHERPA-MC-2.2.8.html#LHC_005fWHJets) for WH production. 