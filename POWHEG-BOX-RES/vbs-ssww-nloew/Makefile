#-*- Makefile -*-
## Choose compiler: gfortran,g77,ifort
#COMPILER=ifort
#COMPILER=gfortran
COMPILER=gfortran
## Choose PDF: native,lhapdf
## LHAPDF package has to be installed separately
PDF = lhapdf
#PDF = native
#Choose Analysis: none, default
## default analysis may require FASTJET package, that has to be installed separately (see below)
#ANALYSIS=default
ANALYSIS=test
#ANALYSIS=mauro
#ANALYSIS=debug
## For static linking uncomment the following
#STATIC= -static
# set to yes to enable compression
WITHZLIB=yes
#
ifeq ("$(COMPILER)","gfortran")	
# use the line BELOW to compile main-PYTHIA82-lhef
#F77= gfortran -fno-automatic -ffixed-line-length-none
F77= gfortran -fno-automatic -ffixed-line-length-none -mcmodel=large
# -mcmodel-large is for having large arrays 
#-fbounds-check
#F77= gfortran -fno-automatic -ggdb -pg -finit-real=nan -ffixed-line-length-none
# -fno-whole-file
## -fbounds-check sometimes causes a weird error due to non-lazy evaluation
## of boolean in gfortran.
#FFLAGS= -Wall -Wimplicit-interface -fbounds-check
## For floating point exception trapping  uncomment the following 
#FPE=-ffpe-trap=invalid,zero,overflow,underflow 
## gfortran 4.4.1 optimized with -O3 yields erroneous results
## Use -O2 to be on the safe side
OPT=-O2
## For debugging uncomment the following
#DEBUG= -ggdb -pg
#DEBUG= -ggdb -pg -O -Wall -fcheck=all -g -fbacktrace
ifdef DEBUG
OPT=-O0
FPE=-ffpe-trap=invalid,zero,overflow
endif
endif


ifeq ("$(COMPILER)","ifort")
F77 = ifort -save  -extend_source
CXX = icpc
LIBS = -limf 
#FFLAGS =  -check
## For floating point exception trapping  uncomment the following 
#FPE = -fpe0
OPT = -O3 #-fast
## For debugging uncomment the following
DEBUG= -debug -g
endif

# Inclusions of Recola
RECOLALOCATION=/PATH/TO/librecola.so
#RECOLAMODULEDIR = $(RECOLALOCATION)/modules
RECOLAMODULEDIR = $(RECOLALOCATION)/include
RECOLALIB       += -L$(RECOLALOCATION) -lrecola
RECFLAGS=-I$(RECOLAMODULEDIR)

OBJ = obj-$(COMPILER)



HEPMCLOCATION=/PATH/TO/HEPMC
LIBSHEPMC += -L$(HEPMCLOCATION)/lib -lHepMC
#PHOTOSCC_LOCATION=/home/fulvio/mauro/rivet/PHOTOS-361
#LIBSPHOTOSCC=-L$(PHOTOSCC_LOCATION)/lib -lPhotospp -lPhotosppHEPEVT -lPhotosppHepMC -lstdc++ -ldl
PYTHIA8LOCATION=/PATH/TO/PHYTIA8
FJCXXFLAGS+=-I$(PYTHIA8LOCATION)/include -I$(PHOTOSCC_LOCATION)/include
LIBPYTHIA8=-L$(PYTHIA8LOCATION)/lib -lpythia8 -lstdc++ -ldl




PWD=$(shell pwd)
WDNAME=$(shell basename $(PWD))
VPATH= ./:../:$(OBJ)/

INCLUDE0=$(PWD)
INCLUDE1=$(shell dirname $(PWD))/include
FF=$(F77) $(FFLAGS) $(FPE) $(OPT) $(DEBUG) -I$(INCLUDE0) -I$(INCLUDE1)


INCLUDE =$(wildcard ../include/*.h *.h include/*.h)

ifeq ("$(PDF)","lhapdf")
LHAPDF_CONFIG=/PATH/TO/lhapdf-config
PDFPACK=lhapdf6if.o lhapdf6ifcc.o
LIBSLHAPDF= -Wl,-rpath,$(shell $(LHAPDF_CONFIG) --libdir)  -L$(shell $(LHAPDF_CONFIG) --libdir) -lLHAPDF -lstdc++
ifeq  ("$(STATIC)","-static") 
## If LHAPDF has been compiled with gfortran and you want to link it statically, you have to include
## libgfortran as well. The same holds for libstdc++. 
## One possible solution is to use fastjet, since $(shell $(FASTJET_CONFIG) --libs --plugins ) -lstdc++
## does perform this inclusion. The path has to be set by the user. 
LIBGFORTRANPATH=/usr/lib/gcc-5/x86_64-redhat-linux/4.1.2
LIBSTDCPP=/lib64
LIBSLHAPDF+=  -L$(LIBGFORTRANPATH)  -lgfortranbegin -lgfortran -L$(LIBSTDCPP) -lstdc++
endif
LIBS+=$(LIBSLHAPDF)
else
PDFPACK=mlmpdfif.o hvqpdfpho.o
endif


PWHGANAL=pwhg_analysis-dummy.o  pwhg_bookhist-multi.o

ifeq ("$(ANALYSIS)","default")
##To include Fastjet configuration uncomment the following lines. 
#FASTJET_CONFIG=$(shell which fastjet-config)
#LIBSFASTJET += $(shell $(FASTJET_CONFIG) --libs --plugins ) -lstdc++
#FJCXXFLAGS+= $(shell $(FASTJET_CONFIG) --cxxflags)
PWHGANAL=pwhg_analysis.o pwhg_bookhist-multi.o
## Also add required Fastjet drivers to PWHGANAL (examples are reported)
#PWHGANAL+= fastjetsisconewrap.o fastjetktwrap.o fastjetCDFMidPointwrap.o fastjetD0RunIIConewrap.o fastjetfortran.o
#PWHGANAL+= fastjetfortran.o
endif

ifeq ("$(ANALYSIS)","test")
##To include Fastjet configuration uncomment the following lines. 
FASTJET_CONFIG=/PATH/TO/fastjet-config
#FASTJET_CONFIG=/home/fulvio/mauro/rivet/local/bin/fastjet-config
#FASTJET_CONFIG=/home/utente/work/rivet/local/bin/fastjet-config
LIBSFASTJET += $(shell $(FASTJET_CONFIG) --libs --plugins ) -lstdc++
FJCXXFLAGS+= $(shell $(FASTJET_CONFIG) --cxxflags)
PWHGANAL=pwhg_analysis-test.o pwhg_bookhist-multi.o
## Also add required Fastjet drivers to PWHGANAL (examples are reported)
#PWHGANAL+= fastjetsisconewrap.o fastjetktwrap.o fastjetCDFMidPointwrap.o fastjetD0RunIIConewrap.o fastjetfortran.o
PWHGANAL+= fastjetfortran.o buildjets.o
endif


ifeq ("$(ANALYSIS)","mauro")
##To include Fastjet configuration uncomment the following lines. 
#FASTJET_CONFIG=$(shell which fastjet-config)
#LIBSFASTJET += $(shell $(FASTJET_CONFIG) --libs --plugins ) -lstdc++
#FJCXXFLAGS+= $(shell $(FASTJET_CONFIG) --cxxflags)
PWHGANAL=pwhg_analysis.o pwhg_bookhist-multi.o
## Also add required Fastjet drivers to PWHGANAL (examples are reported)
#PWHGANAL+= fastjetsisconewrap.o fastjetktwrap.o fastjetCDFMidPointwrap.o fastjetD0RunIIConewrap.o fastjetfortran.o
#PWHGANAL+= fastjetfortran.o
endif

ifeq ("$(ANALYSIS)","debug")
##To include Fastjet configuration uncomment the following lines. 
#FASTJET_CONFIG=$(shell which fastjet-config)
#LIBSFASTJET += $(shell $(FASTJET_CONFIG) --libs --plugins ) -lstdc++
#FJCXXFLAGS+= $(shell $(FASTJET_CONFIG) --cxxflags)
PWHGANAL=pwhg_analysis-debug.o pwhg_bookhist-multi.o
## Also add required Fastjet drivers to PWHGANAL (examples are reported)
#PWHGANAL+= fastjetsisconewrap.o fastjetktwrap.o fastjetCDFMidPointwrap.o fastjetD0RunIIConewrap.o fastjetfortran.o
#PWHGANAL+= fastjetfortran.o
endif

ifeq ("$(WITHZLIB)","yes")
LIBS+=-lz
endif

ifeq ("$(WITHZLIB)","dummy")
LIBZDUMMY=zlibdummy.o
endif

%.o: %.f $(INCLUDE)
	$(FF) -c -o $(OBJ)/$@ $< $(RECFLAGS)
#	$(FF) -c -o $(OBJ)/$@ $<

%.o: %.c
	$(CC) $(DEBUG) -c -o $(OBJ)/$@ $^ 

%.o: %.cc
	$(CXX) $(DEBUG) -c -o $(OBJ)/$@ $^ $(FJCXXFLAGS)  $(PHOTOSFLAGS)


$(shell ../svnversion/svnversion.sh>/dev/null)


USER=init_couplings.o init_processes.o Born_phsp.o Born.o virtual.o	\
     real.o LesHouchesreg.o $(PWHGANAL)

PWHG=pwhg_main.o pwhg_init.o bbinit.o btilde.o lhefwrite.o		\
	LesHouches.o gen_Born_phsp.o find_regions.o	\
	fill_res_histories.o                                        	\
	test_Sudakov.o pt2maxreg.o sigborn.o gen_real_phsp.o maxrat.o	\
	gen_index.o gen_radiation.o Bornzerodamp.o sigremnants.o	\
	sigregular.o build_resonance_hists.o resize_arrays.o	\
	random.o boostrot.o bra_ket_subroutines.o cernroutines.o	\
	init_phys.o powheginput.o pdfcalls.o sigreal.o sigcollremn.o	\
	pwhg_analysis_driver.o checkmomzero.o		\
	setstrongcoupl.o integrator.o newunit.o mwarn.o sigsoftvirt.o	\
	sigcollsoft.o sigvirtual.o reshufflemoms.o \
        setlocalscales.o validflav.o mint_upb.o  \
	mintwrapper.o resweights.o locks.o genericphsp.o boostrot4.o \
	cache_similar.o utils.o PhaseSpaceUtils.o  pwhg_io_interface.o \
        rwl_weightlists.o  fullrwgt.o  s_channel_resonance.o \
        rwl_setup_param_weights.o rwl_setup_param_weights_user.o lhefread.o \
        opencount.o ubprojections-new.o $(PDFPACK) $(USER) $(FPEOBJ) \
        $(LIBZDUMMY)

#        opencount.o ubprojections-new.o buildjets.o $(PDFPACK) $(USER) $(FPEOBJ) \

# target to generate LHEF output
pwhg_main:$(PWHG)
	$(FF) $(patsubst %,$(OBJ)/%,$(PWHG)) $(LIBS) $(RECOLALIB) $(LIBSFASTJET) $(STATIC) -o $@
#	$(FF) $(patsubst %,$(OBJ)/%,$(PWHG)) $(LIBS) $(LIBSFASTJET) $(STATIC) -o $@

LHEF=lhef_analysis.o boostrot.o random.o cernroutines.o		\
     opencount.o powheginput.o $(PWHGANAL)	\
     pwhg_io_interface.o rwl_weightlists.o  locks.o \
     lhefread.o newunit.o pwhg_analysis_driver.o bra_ket_subroutines.o  $(LIBZDUMMY) $(FPEOBJ)


# target to analyze LHEF output
lhef_analysis:$(LHEF)
	$(FF) $(patsubst %,$(OBJ)/%,$(LHEF)) $(LIBS) $(LIBSFASTJET) $(STATIC)  -o $@ 



# Target to read event file, shower events with PYTHIA8.2xx + analysis
PYTHIA82=main-PYTHIA8.o pythia82F77.o boostrot.o powheginput.o rwl_weightlists.o locks.o \
        $(PWHGANAL) lhefread.o pwhg_analysis_driver.o pwhg_io_interface.o cernroutines.o newunit.o bra_ket_subroutines.o $(FPEOBJ)


main-PYTHIA82-lhef: $(PYTHIA82)
	$(FF) $(patsubst %,$(OBJ)/%,$(PYTHIA82)) $(LIBSFASTJET) $(LIBPYTHIA8) $(LIBSHEPMC) $(LIBSPHOTOSCC) $(LIBS) $(STATIC) -o $@



# target to cleanup
.PHONY: clean
clean:
	rm -f $(OBJ)/*.o pwhg_main lhef_analysis  main-PYTHIA82-lhef

lhapdf6ifcc.o: lhapdf6ifcc.cc
	$(CXX) $(DEBUG) -c -o $(OBJ)/$@ $^ $(shell $(LHAPDF_CONFIG) --cxxflags)

pwhg_main.o: svn.version
lhefwrite.o: svn.version
