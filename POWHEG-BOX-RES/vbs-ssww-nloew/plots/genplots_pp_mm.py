################################################################################
#                              genplots_pp_mm.py                               #
################################################################################

"""
File: genplots_pp_mm.py
Author: J.-N. Lang
Email: jlang@physik.uzh.ch
Description: vbs W+W+/W-W- plots
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

yticks = None
xlim = None
ylimup = None
ylogscale = None

powheg_label = '$\\texttt{POWHEG}\;\\mathrm{NLO\; EW}+\\mathrm{PS}$'
mocanlo_label_lo_mm = '$\\mathrm{LO}^{--}$'
mocanlo_label_nlo_mm = '$\\mathrm{NLO\; EW}^{--}$'
mocanlo_label_lo_pp = '$\\mathrm{LO}^{++}$'
mocanlo_label_nlo_pp = '$\\mathrm{NLO\; EW}^{++}$'


###################
#  plot settings  #
###################


# obsmclo = 'histogram_transverse_momentum_j1_born.dat'
# obsmcnlo = 'histogram_transverse_momentum_j1_nlo.dat'
# rescale_mc=1
# uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} p_{\mathrm{T},\mathrm{j}_1}\mathrm{[GeV]}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$p_{\\mathrm{T},\mathrm{j}_1} \mathrm{[GeV]}$'
# oname = 'histogram_transverse_momentum_j1.pdf'
# xlim = (0, 700)
# ylimup = (0.00001,0.01)
# ylimlp = (-40,0)
# yticks = arange(-50,20,10)
# rebin = 1
# bins = 200
# ylogscale = True

# obsmclo = 'histogram_invariant_mass_mjj12_born.dat'
# obsmcnlo = 'histogram_invariant_mass_mjj12_nlo.dat'
# rescale_mc=1
# uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} m_\mathrm{jj}\mathrm{[GeV]}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$m_\mathrm{jj} \mathrm{[GeV]}$'
# oname = 'histogram_invariant_mass_mjj12.pdf'
# xlim = (500, 2000)
# ylimup = (0.00001,0.003)
# ylimlp = (-25,-0)
# yticks = arange(-50,20,10)
# rebin = 1
# bins = 200
# ylogscale = True

obsmclo = 'histogram_rapidity_j1j2_born.dat'
obsmcnlo = 'histogram_rapidity_j1j2_nlo.dat'
rescale_mc=1
uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} y_\mathrm{jj}$'
lylabel = '$\delta[\%]$'
xlabel = '$y_\mathrm{jj}$'
oname = 'histogram_rapidity_j1j2.pdf'
xlim = (-3, 3)
ylimup = (0,1.1)
ylimlp = (-20,-0)
rebin = 1
bins = 10000

# obsmclo = 'histogram_invariant_mass_truth_4l_born.dat'
# obsmcnlo = 'histogram_invariant_mass_truth_4l_nlo.dat'
# rescale_mc=1
# uylabel = '$\mathrm{d}\sigma\mathrm{[fb]}/\mathrm{d} m_{4\ell}\mathrm{[GeV]}$'
# lylabel = '$\delta[\%]$'
# xlabel = '$m_{4\ell} \mathrm{[GeV]}$'
# oname = 'histogram_invariant_mass_truth_4l.pdf'
# xlim = (150, 1000)
# ylimup = (0.00001,0.01)
# ylimlp = (-40,0)
# yticks = arange(-50,20,10)
# rebin = 1
# bins = 2000
# ylogscale = True




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

  if 'left' not in datac and 'right' not in datac:
    assert('middle' in datac)
    binsize = datac['middle'][1]-datac['middle'][0]
    datac['left'] = [u-binsize/2 for u in datac['middle']]
    datac['right'] = [u+binsize/2 for u in datac['middle']]

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

def parse_mocanlo_mm_data(obs,**kwargs):
  mcpath = 'data/MoCaNLO/data_mm/'
  data_structure = {'bin': 1,
                    'left': 2,
                    'right': 3,
                    'value': 4,
                    'error': 5,
                    'hits': 6}
  return parse_data(obs, mcpath, data_structure, **kwargs)

def parse_mocanlo_pp_data(obs,**kwargs):
  mcpath = 'data/MoCaNLO/data_pp/'
  data_structure = {'bin': 1,
                    'left': 2,
                    'right': 3,
                    'value': 4,
                    'error': 5,
                    'hits': 6}
  return parse_data(obs, mcpath, data_structure, **kwargs)

def compare_bins(y1,y1err,y2,y2err):
  ydiff = [100.*(y1[u]-y2[u])/(abs(y2[u])) for u in range(len(y2))]
  ydifferr = [100.*sqrt((y1err[u]/y1[u])**2+(y2err[u]/y2[u])**2)
         for u in range(len(y2))]
  return ydiff, ydifferr

################
#  upper plot  #
################

if ylogscale is True:
  up.axes.set_yscale('log')

plotstyle = {'color': 'purple',
             'drawstyle': 'steps-post',
             'linestyle': '--',
             'linewidth': 1}
x,y,yerr,m = parse_mocanlo_pp_data(obsmclo, rebin=rebin,
    rescale_value=rescale_mc)
x2 = x[:bins]
m2 = m[:bins]
y2 = y[:bins]
y2err = yerr[:bins]
up.plot(x2, y2, label=mocanlo_label_lo_pp, **plotstyle)

plotstyle = {'color': 'blue',
             'drawstyle': 'steps-post',
             'linewidth': 1}
x,y,yerr,m = parse_mocanlo_pp_data(obsmcnlo, rebin=rebin,
    rescale_value=rescale_mc)
x2nlo = x[:bins]
y2nlo = y[:bins]
y2errnlo = yerr[:bins]
up.plot(x2nlo, y2nlo, label=mocanlo_label_nlo_pp, **plotstyle)

y3, y3err = compare_bins(y2nlo,y2errnlo,y2,y2err)
plotstyle = {'color': 'blue',
             'drawstyle': 'steps-post',
             'linewidth': 1}
lp.plot(x2, y3,  **plotstyle)
capsize=2
elinewidth=0.8
lp.errorbar(m2, y3, yerr=y3err, fmt='none',
            drawstyle='mid', capsize=capsize, elinewidth=elinewidth, color='blue')




plotstyle = {'color': 'red',
             'drawstyle': 'steps-post',
             'linestyle': '-.',
             'linewidth': 1}

plotstyle = {'color': 'orange',
             'drawstyle': 'steps-post',
             'linestyle': '--',
             'linewidth': 1}
x,y,yerr,m = parse_mocanlo_mm_data(obsmclo, rebin=rebin,
    rescale_value=rescale_mc)
x2 = x[:bins]
y2 = y[:bins]
y2err = yerr[:bins]
up.plot(x2, y2, label=mocanlo_label_lo_mm, **plotstyle)

plotstyle = {'color': 'red',
             'drawstyle': 'steps-post',
             'linewidth': 1}
x,y,yerr,m = parse_mocanlo_mm_data(obsmcnlo, rebin=rebin,
    rescale_value=rescale_mc)
x2nlo = x[:bins]
y2nlo = y[:bins]
y2errnlo = yerr[:bins]
up.plot(x2nlo, y2nlo, label=mocanlo_label_nlo_mm, **plotstyle)
plotstyle = {'color': 'red',
             'drawstyle': 'steps-post',
             'linestyle': '-.',
             'linewidth': 1}

y3, y3err = compare_bins(y2nlo,y2errnlo,y2,y2err)
plotstyle = {'color': 'red',
             'drawstyle': 'steps-post',
             'linewidth': 1}
lp.plot(x2, y3,  **plotstyle)
capsize=2
elinewidth=0.8
lp.errorbar(m2, y3, yerr=y3err, fmt='none',
            drawstyle='mid', capsize=capsize, elinewidth=elinewidth, color='red')




# x,y,yerr,m = parse_pwhg_data(obspwhgps, rebin=rebin,
#     rescale_value=rescale_pwgh)
# x1 = x[:bins]
# m1 = m[:bins]
# y1 = [u for u in y[:bins]]
# y1err = [u for u in yerr[:bins]]
# up.plot(x1, y1, label=powheg_label, **plotstyle)


################
#  lower plot  #
################



#
# plotstyle = {'color': 'red',
#              'drawstyle': 'steps-post',
#              'linewidth': 1}
# y3, y3err = compare_bins(y1,y1err,y2,y2err)
# lp.plot(x1, y3,  **plotstyle)
# capsize=2
# elinewidth=0.8
# lp.errorbar(m1, y3, yerr=y3err, fmt='none',
#             drawstyle='mid', capsize=capsize, elinewidth=elinewidth, color='black')
#
# plotstyle = {'color': 'blue',
#              'drawstyle': 'steps-post',
#              'linewidth': 1}
# y4, y4err = compare_bins(y2nlo,y2errnlo,y2,y2err)
# lp.plot(x1, y4,  **plotstyle)
# capsize=2
# elinewidth=0.8
# lp.errorbar(m1, y4, yerr=y4err, fmt='none',
#             drawstyle='mid', capsize=capsize, elinewidth=elinewidth,
#             color='black')
if yticks is not None:
  lp.yaxis.set_ticks(yticks)
if ylimup is not None:
  up.set_ylim(*ylimup)
lp.set_ylim(*ylimlp)

if xlim is not None:
  up.set_xlim(*xlim)
  lp.set_xlim(*xlim)


##############################
#  legend,label,annotations  #
##############################

handles, labels = up.get_legend_handles_labels()
up.legend(handles, labels, ncol=2, handlelength=1.0, frameon=False, fontsize=fontsize,
          prop={'size': fontsize}, loc='best')


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
