## Plots for VBS POWHEG+RECOLA paper

You need Python 3 to generate the plots. In addition you need the following
packages:

+ matplotlib 2.2.2
+ scipy      1.1.0
+ numpy      1.16.3


To install 3rd party dependencies use pip:

    pip install --user matplotlib scipy numpy

* * *

Generate NLO EW comparison plots by running:

    python genplots_comparison.py

Generate NLO+PS plots by running:

    python genplots_shower.py

Generate NLO EW W+W+/W-W- plots by running:

    python genplots_shower.py


each plotting routine will generate only a single plot corresponding to a
particular observable. Comment/Uncomment the corresponding lines to plot another
observable.

* * *
