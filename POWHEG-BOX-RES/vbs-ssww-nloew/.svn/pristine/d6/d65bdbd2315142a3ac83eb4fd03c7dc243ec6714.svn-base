################################################################################
#                                 gen_plots.py                                 #
################################################################################
"""
File: genplots_comparison.py
Author: J.-N. Lang
Email: jlang@physik.uzh.ch
Description: vbs comparison plots
"""

#############
#  Globals  #
#############

from __future__ import unicode_literals
import os
from matplotlib import ticker
from matplotlib import pyplot as plt
from matplotlib.gridspec import GridSpec
from numpy import linspace, loadtxt, arange
from scipy.interpolate import interp1d
from math import sqrt

fontsize=16
plt.rc('text', usetex=True)
plt.rc('text.latex', unicode=True)
plt.rc('font', family='serif', size=fontsize)
plt.rc('mathtext',
       fontset='custom',
       rm='Bitstream Vera Sans',
       it='Bitstream Vera Sans:italic',
       bf='Bitstream Vera Sans:bold')
fig = plt.figure(num=None, figsize=(5, 6), dpi=120, facecolor='w', edgecolor='k')

plot_margin_left = 0.13
plot_margin_right = 0.95
plot_margin_top = 0.98
plot_margin_bottom = 0.1
plt.subplots_adjust(left=plot_margin_left, right=plot_margin_right,
                    top=plot_margin_top, bottom=plot_margin_bottom)
gridspec_y_ticks = 13
gridspec_x_ticks = 1
gs = GridSpec(gridspec_y_ticks, gridspec_x_ticks)
mid = 9
top_end = 13
up = plt.subplot(gs[1:mid-1, :])
lp = plt.subplot(gs[mid:top_end, :])

powheg_label = '$\\texttt{POWHEG}$'
mocanlo_label = '$\\texttt{MoCaNLO}$'

###################
#  plot settings  #
###################

# obsmc = 'histogram_transverse_momentum_j1_nlo.dat'
# rescale_mc=1.
# rescale_pwgh=1000.
# obspwhg = 'sum_j1_pt'
# uylabel = '$\mathrm{d}\sigma\mathrm{[pb]}/\mathrm{d} p_{\mathrm{T},j_1}\mathrm{[GeV]}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$p_{\\mathrm{T},j_1} \mathrm{[GeV]}$'
# oname = 'ptj1.pdf'
# xlim = (0, 700)
# rebin = 2
# bins = 20

# obsmc = 'histogram_transverse_momentum_j2_nlo.dat'
# rescale_mc=1.
# rescale_pwgh=1000.
# obspwhg = 'sum_j2_pt'
# uylabel = '$\mathrm{d}\sigma\mathrm{[pb]}/\mathrm{d} p_{\mathrm{T},j_2}\mathrm{[GeV]}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$p_{\\mathrm{T},j_2} \mathrm{[GeV]}$'
# oname = 'ptj2.pdf'
# xlim = (0, 500)
# rebin = 3
# bins = 20

# obsmc = 'histogram_invariant_mass_mjj12_nlo.dat'
# obspwhg = 'sum_jj_m'
# rescale_mc=1.
# rescale_pwgh=1000.
# uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} m_{\mathrm{jj}}\mathrm{[GeV]}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$m_{\mathrm{jj}} \mathrm{[GeV]}$'
# xlim = (500, 2000)
# ylimup = (0.00001,0.003)
# ylimlp = (-35,-0)
# oname = 'mjj.pdf'
# rebin = 2
# bins = 200
# ylogscale = True

# obsmc = 'histogram_transverse_momentum_positron_nlo.dat'
# obspwhg = 'sum_e_pt'
# rescale_mc=10.**3
# rescale_pwgh=10.**6
# uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} p_{\mathrm{T},e^+}\mathrm{[GeV]}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$p_{\\mathrm{T},e^+} \mathrm{[GeV]}$'
# oname = 'pte.pdf'
# xlim = (0, 500)
# rebin = 3
# bins = 20

# obsmc = 'histogram_rapidity_positron_nlo.dat'
# obspwhg = 'sum_e_y'
# rescale_mc=10.**3
# rescale_pwgh=10.**6
# uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} y_{e^+}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$y_{e^+}$'
# oname = 'ye.pdf'
# xlim = (-2.4, 2.4)
# rebin = 2
# bins = 800
#
#
# obsmc = 'histogram_rapidity_j1_nlo.dat'
# obspwhg = 'sum_j1_y'
# rescale_mc=10.**3
# rescale_pwgh=10.**6
# uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} y_{j_1}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$y_{j_1}$'
# oname = 'yj1.pdf'
# xlim = (-2.4, 2.4)
# rebin = 2
# bins = 800

# obsmc = 'histogram_rapidity_j2_nlo.dat'
# obspwhg = 'sum_j2_y'
# rescale_mc=10.**3
# rescale_pwgh=10.**6
# uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} y_{j_2}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$y_{j_2}$'
# oname = 'yj2.pdf'
# xlim = (-2.4, 2.4)
# rebin = 2
# bins = 800

obsmc = 'histogram_rapidity_separation_j1j2_nlo.dat'
obspwhg = 'sum_jj_dy'
rescale_mc=10.**0
rescale_pwgh=10.**3
uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} \Delta y_\mathrm{jj}$'
lylabel = '$\delta[\%]$'
xlabel = '$\Delta y_\mathrm{jj}$'
oname = 'dyjj.pdf'
ylimup = (0., 0.25)
# ylimup = None
xlim = (2.4, 7.)
rebin = 2
bins = 800
ylogscale = None

# obsmc = 'histogram_transverse_momentum_truth_missing_nlo.dat'
# obspwhg = 'sum_miss_pt'
# rescale_mc=10.**3
# rescale_pwgh=10.**6
# uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} p_{\mathrm{T}}^\mathrm{miss}\mathrm{[GeV]}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$p_{\\mathrm{T}}^\mathrm{miss} \mathrm{[GeV]}$'
# oname = 'ptmiss.pdf'
# xlim = (0, 500)
# rebin = 3
# bins = 20

def join_value(d,pos,n,err=False):
  r = 0.
  for j in range(n):
    if err:
      r = sqrt(r**2 + d[pos+j]**2)
    else:
      r += d[pos+j]
  r = r/n
  return r

def join_err(d,pos,n):
  r = 0.
  for j in range(n):
    r = sqrt(r**2 + d[pos+j]**2)
  r = r/n
  return r

def join_bounds(d,pos,n):
  r = (d['left'][pos] + d['right'][pos+n-1])/2
  return r

def parse_data(obs,mcpath, data_structure, rebin=False,
               rescale_value=None,
               **kwargs):
  fname = os.path.join(mcpath, obs)
  data = loadtxt(fname)
  bins = len(data)
  datac = {}
  for d in data_structure:
    datac[d] = data[:bins, data_structure[d]-1]

  x = [datac['left'][u] for u in range(bins)]
  x += [datac['right'][bins-1]]
  m = [(datac['left'][u] + datac['right'][u])/2. for u in range(bins)]
  if rescale_value:
    y = [u*rescale_value for u in datac['value']]
    y += [y[-1]]
    yerr = [u*rescale_value for u in datac['error']]
  else:
    y = datac['value']
    yerr = datac['error']

  if rebin:
    nbins = (bins//rebin)*rebin
    x = [datac['left'][i] for i in range(0, nbins, rebin)]
    #  TODO:  <09-05-19, J.-N. Lang> #
    # if nbins < bins need to combine last bin by hand (due to smaller size)

    # I add another (fake0 point to continue the line when plotting with
    # steps-post option.
    x += [datac['right'][nbins-1]]
    y = [join_value(y, i, rebin) for i in range(0, nbins, rebin)]
    y += [y[-1]]
    m = [join_bounds(datac, i, rebin) for i in range(0, nbins, rebin)]
    m += [m[-1]]
    yerr = [join_err(yerr, i, rebin) for i in range(0, nbins, rebin)]
    yerr += [yerr[-1]]

  return x,y,yerr,m

def parse_mocanlo_data(obs,**kwargs):
  mcpath = 'data/MoCaNLO/data_16/'
  data_structure = {'bin': 1,
                    'left': 2,
                    'right': 3,
                    'value': 4,
                    'error': 5,
                    'hits': 6}
  return parse_data(obs, mcpath, data_structure, **kwargs)

def parse_pwhg_data(obs, **kwargs):
  pwhgpath = 'data/Powheg/data_42/'
  data_structure = {'left': 1,
                    'right': 2,
                    'value': 3,
                    'error': 4}
  return parse_data(obs, pwhgpath, data_structure, **kwargs)

################
#  upper plot  #
################

if ylogscale is True:
  up.axes.set_yscale('log')
plotstyle = {'color': 'black',
             'drawstyle': 'steps-post',
             'linewidth': 1}
x,y,yerr,m = parse_pwhg_data(obspwhg, rebin=rebin,
    rescale_value=rescale_pwgh)
x1 = x[:bins]
m1 = m[:bins]
y1 = [u for u in y[:bins]]
y1err = [u for u in yerr[:bins]]
up.plot(x1, y1, label=powheg_label, **plotstyle)


plotstyle = {'color': 'red',
             'drawstyle': 'steps-post',
             'linewidth': 1}
x,y,yerr,m = parse_mocanlo_data(obsmc, rebin=rebin,
    rescale_value=rescale_mc)
x2 = x[:bins]
y2 = y[:bins]
y2err = yerr[:bins]
up.plot(x2, y2, label=mocanlo_label, **plotstyle)
up.set_xlim(*xlim)


################
#  lower plot  #
################

plotstyle = {'color': 'blue',
             'drawstyle': 'steps-post',
             'linewidth': 1}

def compare_bins(y1,y1err,y2,y2err):
  ydiff = [100.*(y1[u]-y2[u])/(abs(y1[u])) for u in range(len(y2))]
  ydifferr = [100.*sqrt((y1err[u]/y1[u])**2+(y2err[u]/y2[u])**2)
         for u in range(len(y2))]
  return ydiff, ydifferr

y3, y3err = compare_bins(y1,y1err,y2,y2err)
lp.plot(x1, y3,  **plotstyle)
capsize=2
elinewidth=0.8
lp.errorbar(m1, y3, yerr=y3err, fmt='none',
            drawstyle='mid', capsize=capsize, elinewidth=elinewidth, color='black')
lp.yaxis.set_ticks(arange(-10, 10, 2))
up.set_ylim(*ylimup)
lp.set_ylim(-6, 6)
lp.set_xlim(*xlim)


##############################
#  legend,label,annotations  #
##############################

handles, labels = up.get_legend_handles_labels()
up.legend(handles, labels, handlelength=1., frameon=False, fontsize=fontsize, prop={'size':
  fontsize},
loc='best')


plt.text(0.1, 1.05, uylabel,
       horizontalalignment='center',
       fontsize=fontsize,
       transform=up.transAxes)

plt.text(0.0, 1.06, lylabel,
         horizontalalignment='center',
         fontsize=fontsize,
         transform=lp.transAxes)

lp.set_xlabel(xlabel, fontsize=fontsize)


plt.setp(up.axes.get_xticklabels(), visible=False)

# plt.show()
fig.savefig(oname, dpi=120, bbox='standard', pad_inches=20)
