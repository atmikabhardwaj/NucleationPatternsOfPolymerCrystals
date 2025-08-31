# This file relates to the work: Atmika Bhardwaj, Jens-Uwe Sommer, Marco Werner; "Nucleation patterns of polymer crystals analyzed by machine learning models".
# Here, we define the common plotting instructions shared within all the plotted graphs. 

import numpy as np

def write_color_stylefile(c):
    
    f = open("our_colors.sty", "w")
    
    for k in c.keys():
        r,g,b=str(c[k][0]),str(c[k][1]),str(c[k][2])
        line="\definecolor{c"+k+"}{rgb}{"+r+","+g+","+b+"}\n"
        f.write(line)

def generate_colors():
    
    colors_int,colors_f=dict(),dict()

    colors_int["AE"]=[8, 164, 255]
    colors_int["SF"]=[126, 168, 191]
    colors_int["AO"]=[250, 158, 0]
    colors_int["AO2"]=[250, 78, 0]
    colors_int["SL"]=[204, 181, 143]
    
    colors_int["gray"]=[117, 117, 117]
    colors_int["t_pre"]=[240, 40, 240]
    colors_int["t_tr"]=[190, 50, 190]
    colors_int["t_min"]=[140, 70, 140]
    colors_int["t_end"]=[90, 90, 90]
    colors_int["amorph"]=[200, 200, 200]
    
    for k in colors_int.keys():
        colors_int[k]=np.array(colors_int[k]).astype(int)
        colors_f[k]=1.*colors_int[k]/256.0    
        
    write_color_stylefile(colors_f)
    
    return colors_f

def generate_labels():
    labels=dict()

    labels["xAE"]="ML (machine l.)"
    labels["xSF"]="REMOVE"
    labels["xAO"]="AO (human)"
    labels["xSL"]="SL (human)"
   
    labels["sAE"]="${ML}$"
    labels["sSF"]="$\mathbf{REMOVE}$"
    labels["sAO"]="${AO}$"
    labels["sSL"]="${SL}$"
    
    labels["sAEII"]="${ML}^{*}$"
    labels["sAOII"]="${AO}^{*}$"
    labels["sSLII"]="${SL}^{*}$"

    f = open("our_labels.sty", "w")
    for k in labels.keys():
        line="\\newcommand{\\"+k+"}[0]{\\textcolor{c"+k[1:]+"}{\\bf "+labels[k]+"}}\n"
        f.write(line)
        line="\\newcommand{\\"+"b"+k+"}[0]{{"+labels[k]+"}}\n"
        f.write(line)
        
    labels["cr"]=" cryst."
    labels["am"]=" amorph."

    return labels


def formatMap(plt):
    #plt.xlabel('Bottleneck neuron, $a_2$', fontsize = 20)
    #plt.ylabel('Bottleneck neuron, $a_1$',  fontsize = 20)
    plt.xlabel('$a_2$', fontsize = 20)
    plt.ylabel('$a_1$',  fontsize = 20)
    #lgnd     = plt.legend(fontsize=18)
   
    plt.tight_layout()
    plt.xlim(-0.55, 2.55)
    plt.ylim(-0.3, 1.03)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
    plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.5))
    
generate_colors()
generate_labels()

class PlotStyle:
    LLF=30
    LF=24
    SF=20
