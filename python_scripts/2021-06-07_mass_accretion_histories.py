#load system relevant packages
from __future__ import print_function
import os, sys, compileall
import numpy as np
system_info = os.getcwd()
start = system_info.find('anaconda')
if start==-1:
    mycomp='/home/doris/'
else:
    mycomp = system_info[:start]
    
compileall.compile_dir(mycomp+'anaconda/pro/PyLysis', force=1)
sys.path.insert(0, mycomp+'/anaconda/pro/PyLysis/')

#load own packages
import halo_startup_512
from halo_startup_512 import ReturnData2Jupyter as rDJ
load_data = rDJ()
data = load_data.return_data2jupyter()

#Load plot related packages
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import NullFormatter
nullfmt = NullFormatter()
mpl.style.use('classic')            
mpl.mathtext.use_cm = False
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.tt'] = 'Typewriter'
mpl.mathtext.fallback_to_cm = True


def get_styles(ncols):
#Style options 'colors', 'linestyles', 'marker'
#=----------------------
    if ncols<=3:
        cols=['#225588', '#ffab00', '#CC6677', '#AA4499','#117733', 'k']
        ls=['-','-','--','-','-.',':']
        marker= ['o','','','','','']
    else:
        cols = ['#332288', '#88CCEE', '#44AA99', '#117733', '#999933', '#DDCC77', '#ffab00', '#CC6677', '#AA4499', '#7439A6', '#661100', '#333333', '#d2691e']
        ls=['-','--','-.',':','-','--','-',':','--','--','-.',':']
        marker= ['o','','','','*','','v','','','','','','','']
        
    markerfcols = cols
    
    return cols, ls, marker, markerfcols

#load references or observations
ref_list=['12517939528','12517940890','12518448507']#,'2','3']
a=len(data.keys())
print('a:', a)
size_ref_list=len(ref_list)
data_ref={}
for i,item in enumerate(ref_list):
    #mypath='/home/doris/anaconda/pro/OBS/HMF_SMDPL_Rockstar_z_'+item+'_M200c_Msun_Nhalos.txt'
    #mypath='/home/doris/anaconda/pro/data/SMDPL_Rockstar_400Mpc/MMP_at_116/MMP_SMDPL_116'+item+'.txt' 
    mypath='/data/3840_VSMDPL_160Mpc/halo_files/trees/VSMDPL3840_160Mpc_tree_2_5_0_CT-v1.01_MB_rootID'+str(ref_list[i])+'.txt'
    mydata= np.genfromtxt(mypath, dtype=np.float32, delimiter='\t', comments='#')
    mydata=mydata[np.where(mydata[:,19]==0)[:][0]]
    data_ref.update({i+a: mydata})
    

ref_list=['','_2','_3']#,'2','3']
#size_ref_list+=len(ref_list)
a=len(data.keys())+len(data_ref.keys())

for i,item in enumerate(ref_list):
    #mypath='/home/doris/anaconda/pro/OBS/HMF_SMDPL_Rockstar_z_'+item+'_M200c_Msun_Nhalos.txt'
    mypath='/home/doris/anaconda/pro/data/SMDPL_Rockstar_400Mpc/trees/MMP_SMDPL_67'+item+'.txt' 
    mydata= np.genfromtxt(mypath, dtype=np.float32, delimiter='\t', comments='#')

    data_ref.update({i+a: mydata})    
    
def get_a(z):
    
    return 1.0/(z+1)

def get_z(a):
    
    return 1.0/a-1.0


def mass_para(M_0, a, alpha=1.33):
    #mass accrection history parameterization from Wechsler+02 Eq.4 and Eq.5
    S     = 2.0
    a_0   = a[a.size-1]
    a_c   = a_0 * alpha/S
    print('M_0:', M_0, 'a_0:', a_0, 'alpha:', alpha)

    return M_0*np.exp(-a_c*S*(a_0/a-1))/M_0


#initialize figure and axes 
#----------------------
fig, ax = plt.subplots(figsize=(16,10), facecolor='w')

myparam=False
if myparam==True:
    for i, myalpha, M_0 in zip(range(0,4,1),[0.5,0.75,1.5,2],[1e12,1e13,1e14,1e15]):
        #data_para = mass_para(10**data[str(0)]['mhalo1_log50'][data[str(0)].size-1], a, alpha=myalpha)
        data_para = mass_para(M_0, a, alpha=myalpha)
        ax.plot(a, 
                data_para, 
                label='alpha='+str(myalpha)+'\n$M_0$='+str(M_0),
                color='k',
                lw=4,
                ls=myls[i],
                markersize=5,
                markeredgewidth=2,
                markerfacecolor='k',
                alpha=1.0)

rootTreeID=data.keys()
mylist=np.append(rootTreeID,data_ref.keys())
print(mylist)
err_fill_between = False

mycols, myls, mymarker, mymarkerfcols = get_styles(len(mylist))

for i, item in enumerate(mylist):

    if i>=len(data.keys()):
        size=data_ref[item][:,0].size
        if i>=len(data.keys())+size_ref_list:
            mylabel='3840-SMDPL-'+str(item)            
            col_scale=2
            col_prop=7 #Mvir
            #col_prop=8 #Vmax             
        else:
            mylabel='3840-VSMDPL-'+str(item)
            col_scale=1
            col_prop=14 #Mvir
            #col_prop=15 #Vmax
            
        data_x = data_ref[item][1:size,col_scale] #growth between snapshots
        data_x = data_ref[item][:,col_scale]#mass accrection history
        
        data_y = data_ref[item][:,col_prop][1:size]-data_ref[item][:,col_prop][0:size-1] #delatM (M2-M1)
        data_y = 100.0/data_ref[item][:,col_prop][0:size-1]*(data_ref[item][:,col_prop][1:size]-data_ref[item][:,col_prop][0:size-1]) #fraction of mass growth of M1 
        data_y = data_ref[item][:,col_prop]/data_ref[item][0,col_prop]#mass growth history normalised by final mass
        #data_y = data_ref[item][:,col_prop] #mass growth history
    else:
        prop='mhalo'
        size=data[item][prop].size

        data_x = data[item]['a'][1:size] #growth between snapshots
        data_x = data[item]['a'] #mass accrection history

        data_y = data[item][prop][1:size]-data[item][prop][0:size-1] #delatM (M2-M1)
        data_y = 100.0/data[item][prop][0:size-1]*(data[item][prop][1:size]-data[item][prop][0:size-1]) #fraction of mass growth of M1 
        data_y = data[item][prop]/data[item][prop][data[item].size-1] #mass growth history normalised by final mass
        #data_y = data[item][prop]
        if item==-1:
            mylabel  = 'main branch'
        else:
            mylabel  = '512-Cholla-'+str(i)
    
    #print(data_y)
    
    col=mycols[i]
    #col    = 'r'
    ls     = myls[i]
    marker = mymarker[i]
    fcol   = 'w'#mymarkerfcols[i]    
        
    if i!=0:
        key_sub1 = ax
        key_sub2 = 'axis' + str(i)
        key_sub1.set_zorder(25)                  
                
    ax.plot(data_x, 
            data_y, 
            label=mylabel,
            color=col,           
            lw=6,
            ls=ls,
            marker=marker,
            markersize=5,
            markeredgewidth=0,
            markerfacecolor=fcol,
            alpha=1.0)

    #if true uncertainties are plotted as shaded region
    if err_fill_between==True:
        ax.fill_between(data_x, 
                        yerr_data2, 
                        yerr_data1, 
                        color=col, 
                        facecolor=col, 
                        alpha=0.1,
                        interpolate=False,
                        lw=1.5,
                        linestyle='-') 
    
#Format labels, axes styles, and legend
#----------------------
#ax.set_title("Selected main branches from various simulations", color='k', fontsize=35, pad=25)

ax.set_xscale('linear')
ax.set_xlabel('a', color='k', fontsize=35) 
ax.set_xlim(0.1,0.4)

y_label='$V_{max}$ [km/s]'
#y_label='$M_{vir}$ [h$^{-1}M_{\odot}$]'
y_label='$M_{vir}/M_{vir_0}$'
#y_label='$\Delta_{M_{vir}}$ [%]'

ax.set_ylabel(y_label, color='k', fontsize=30, labelpad=15)
ax.set_yscale('log')
#ax.set_ylim(10,2e3)
#ax.set_ylim(1e8,1e15)
ax.set_ylim(0,2)
#ax.set_ylim(-50,+50)

ax.legend(loc=(1.02,0.05),
           ncol=1,
           fontsize=25,
           shadow=False, 
           fancybox=False,
           borderaxespad=1,
           facecolor='w',
           numpoints=1, 
           frameon=False,
           labelspacing=0.3,
           handlelength=1.6,
           columnspacing=0.95,
           handletextpad=0.5)

fig.subplots_adjust(hspace=0.0,
                    wspace=0.0, 
                    left=0.10, 
                    bottom=0.1, 
                    right=0.78, 
                    top=0.96) 

for axis in ['top','bottom','left','right']: ax.spines[axis].set_linewidth(4)   
ax.tick_params(axis='both', 
               which='major', 
               top='on', 
               bottom='on',
               left='on',
               right='on',
               pad=10, 
               labelsize=30,
               length=12.5,
               width=4,
               direction='in',
               zorder=20)
ax.tick_params(axis='both', 
               which='minor', 
               top='on', 
               bottom='on',
               left='on',
               right='on',
               pad=10, 
               labelsize=30,
               length=10,
               width=2.5,
               direction='in',
               zorder=20)

fig.subplots_adjust(hspace=0.0,
                    wspace=0.0, 
                    left=0.12, 
                    bottom=0.12, 
                    right=0.74, 
                    top=0.96)

#Print into file
#----------------------
pp = PdfPages('/data/mass_growth_history.pdf')
plt.savefig(pp, format='pdf', rasterized=True, pad_inches=0.05, bbox_inches=None, transparent=True)
pp.close()

#Print figure on screen
plt.show()
