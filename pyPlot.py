import os
import numpy as np 
import json
import matplotlib.pyplot as plt 
from copy import copy

myyellow = (1, 1, 84./255)

from pyUtils import parseOpts
(options, args) = parseOpts()


nInputs = len(args)
print(f"Will read from {nInputs} input files")

with open(args[0], 'r') as f:
    inputData0 = json.load(f)

if nInputs > 1:
    with open(args[1], 'r') as f:
        inputData1 = json.load(f)
else:
    inputData1 = inputData0


if not os.path.exists(options.output):
    os.mkdir(options.output)

    

        
def printDir(data, level=0, maxLevel=-1):
    if not hasattr(data,"keys"):
        return

    if maxLevel >= 0 and level > maxLevel:
        return
    
    for k in data.keys():
        tab = '\t'
        print(f'{tab*level} {k}')
        printDir(data[k], level=(level+1), maxLevel=maxLevel)
  
def ls(d=None, maxLevel = -1):
    if d is None:
        printDir(data, level = 0, maxLevel = maxLevel)
    else:
        printDir(data[d], level = 0, maxLevel = maxLevel)


def rebinData(inData,rebin):
    print(f'rebining with rebin={rebin}')

    n = inData["n"]
    bins = inData["bins"]
    rebinnedBins = bins[0::rebin]
    rebinnedIndices = np.where(np.isin(bins, rebinnedBins))[0]
    rebinnedData = [np.sum( n[rebinnedIndices[i]:rebinnedIndices[i+1]])  for i in range(len(rebinnedIndices)-1)]

    inData["n"] = np.array(rebinnedData)
    inData["bins"] = rebinnedBins
    
    
def getData(dataSet, path, rebin=None):

    keys = path.split("/")

    # The copies here all us to rebin
    plotData = copy(dataSet)
    for k in keys:
        plotData = copy(plotData[k])
        
    plotData["bins"] = np.array(plotData["bins"])
    plotData["n"]    = np.array(plotData["n"])
    plotData["name"] = path.replace("/","_")
    
    #print(f'Bins before {plotData["bins"]}')
    
    if rebin: rebinData(plotData, rebin)

    #print(f'Bins after {plotData["bins"]}')
        
    return plotData


def binCenters(bins):
    return 0.5*(bins[0:len(bins)-1] + bins[1:len(bins)] )


def configAxes(inAxis, **kwargs):
    if "ylabel" in kwargs: inAxis.set_ylabel(kwargs["ylabel"])
    if "ylim"   in kwargs: inAxis.set_ylim  (kwargs["ylim"])
    if "yscale" in kwargs: inAxis.set_yscale(kwargs["yscale"])

    if "xlim"   in kwargs: inAxis.set_xlim  (kwargs["xlim"])
    if "xlabel" in kwargs: inAxis.set_xlabel(kwargs["xlabel"])




def plotRatio(dataToPlot, **kwargs):
    debug = kwargs.get("debug",False)
    
    if debug:
        print(f'Called plotRatio')
        print_parameters(**kwargs)

    fig, axs = plt.subplots(2,1,figsize=(7,5*4/3), gridspec_kw={'height_ratios': [3, 1]})
    plt.subplots_adjust(hspace=0.05)
    

    axs[0].errorbar(
        binCenters(dataToPlot[0]["bins"]),
        dataToPlot[0]["n"],
        yerr = dataToPlot[0]["n"]**0.5,
        #marker = '.',
        fmt = '.k',
        linewidth=2,
        markersize=10,
        label=kwargs.get("labels",["",""])[0]
    )

    axs[0].hist(binCenters(dataToPlot[1]["bins"]) ,bins=dataToPlot[1]["bins"], weights=dataToPlot[1]["n"],histtype="stepfilled",color=myyellow,ec="k",linewidth=1.5, label=kwargs.get("labels",["",""])[1])

    
    axs[0].set_xticklabels([])
    axs[0].set_xticks([])

    
    configAxes(axs[0],**kwargs)
    axs[0].set_xlabel("")

    #
    #  Legend
    # 
    handles, labels = axs[0].get_legend_handles_labels()
    if len(labels):
        order = [1,0]
        axs[0].legend([handles[idx] for idx in order],[labels[idx] for idx in order],loc="best",frameon=False) 

        
    #
    #  Plot Ratio
    #
    epsilon = 0#1e-4
    ratio = (dataToPlot[0]["n"]/(dataToPlot[1]["n"]+epsilon))

    # sigma_r / r = sigma_n / n (inquad) sigma_d / d
    sigmaNoverN = dataToPlot[0]["n"]**0.5 / dataToPlot[0]["n"]
    sigmaDoverD = dataToPlot[1]["n"]**0.5 / dataToPlot[1]["n"]
    relErr = (sigmaNoverN*sigmaNoverN + sigmaDoverD* sigmaDoverD)**0.5
    ratioErr = relErr * ratio
    
    axs[1].set_yscale("linear")    
    configAxes(axs[1],**kwargs)    
    axs[1].set_yscale("linear")
    
    if "rlabel" in kwargs:
        axs[1].set_ylabel(kwargs["rlabel"])
    else:
        axs[1].set_ylabel("Ratio")

    if "rlim" in kwargs: axs[1].set_ylim(kwargs["rlim"])    
    
    #axs[1].plot(binCenters(dataToPlot[0]["bins"]), ratio,c="k")
    axs[1].errorbar(
        binCenters(dataToPlot[0]["bins"]),
        ratio,
        yerr = ratioErr,
        #marker = '.',
        fmt = '.k',
        linewidth=2,
        markersize=10
    )

    
    xMin = dataToPlot[0]["bins"][0]
    xMax = dataToPlot[0]["bins"][-1]
    axs[1].plot([xMin,xMax],[1,1],"k:")

    plt.savefig(options.output+"/"+dataToPlot[0]["name"]+"_vs_"+dataToPlot[1]["name"]+".pdf")    
    plt.show()

    return
        
    
def plotHists(dataToPlot, **kwargs):

    debug = kwargs.get("debug",False)
    
    if debug:
        print(f'Called plot')
        print_parameters(**kwargs)

    if kwargs.get("doratio",False)  and len(dataToPlot) > 1:
        plotRatio(dataToPlot, **kwargs)
        return

        
    fig, ax = plt.subplots(1,1,figsize=(7,5))
        
        
    if len(dataToPlot) == 2:

        ax.errorbar(
            binCenters(dataToPlot[0]["bins"]),
            dataToPlot[0]["n"],
            yerr = dataToPlot[0]["n"]**0.5,
            marker = '.',
            fmt = '.k',
            markersize=10,
            label=kwargs.get("labels",["",""])[0]
        )
            
        ax.hist(binCenters(dataToPlot[1]["bins"]) ,bins=dataToPlot[1]["bins"], weights=dataToPlot[1]["n"],histtype="stepfilled",color=myyellow, ec="k",linewidth=1.5,label=kwargs.get("labels",["",""])[1])
        leg_order = [1,0]

    else:
        ax.hist(binCenters(dataToPlot[0]["bins"]) ,bins=dataToPlot[0]["bins"], weights=dataToPlot[0]["n"],histtype="stepfilled",color=myyellow, ec="k",linewidth=1.5,label=kwargs.get("labels",["",""])[0])
        leg_order = [0]

        
    configAxes(ax,**kwargs)

    #
    #  Legend
    # 
    handles, labels = ax.get_legend_handles_labels()

    if len(labels):
        ax.legend([handles[idx] for idx in leg_order],[labels[idx] for idx in leg_order],loc="best",frameon=False) 

    
    plt.show()
    return

def checkList(inList, hasLength = 2):
    if not len(inList) == hasLength:
        print("Error: can only plot from two directories at a time")
        return

def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

    
def plot(var,inDir, **kwargs):

    debug = kwargs.get("debug",False)

    if debug:
        print(f'Called plot with var={var} and inDir={inDir}')
        print_parameters(**kwargs)
        
    dataToPlot = []

    # plot 2 differnet vars from 2 differnet dirs
    if type(inDir) == list and type(var) == list:

        checkList(inDir)
        checkList(var)

        dataToPlot.append(getData(inputData0,inDir[0]+"/"+var[0], rebin=kwargs.get("rebin",None)))
        dataToPlot.append(getData(inputData1,inDir[1]+"/"+var[1], rebin=kwargs.get("rebin",None)))

    # plot 1 vars from 2 differnet dirs
    elif type(inDir) == list and not type(var) == list:

        checkList(inDir)

        dataToPlot.append(getData(inputData0,inDir[0]+"/"+var, rebin=kwargs.get("rebin",None)))
        dataToPlot.append(getData(inputData1,inDir[1]+"/"+var, rebin=kwargs.get("rebin",None)))

    # plot 2 different vars from 1  dirs        
    elif not type(inDir) == list and type(var) == list:

        checkList(var)

        dataToPlot.append(getData(inputData0,inDir+"/"+var[0], rebin=kwargs.get("rebin",None)))
        dataToPlot.append(getData(inputData1,inDir+"/"+var[1], rebin=kwargs.get("rebin",None)))

        
    # plot 1 vars from 1  dirs
    else:
        dataToPlot.append(getData(inputData0,inDir+"/"+var, rebin=kwargs.get("rebin",None)))
        if nInputs > 1: dataToPlot.append(getData(inputData1,inDir+"/"+var, rebin=kwargs.get("rebin",None)))
            
        

    #
    # plotHits
    #
    plotHists(dataToPlot, **kwargs)
    
