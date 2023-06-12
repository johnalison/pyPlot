import numpy as np 
import json
import matplotlib.pyplot as plt 

inFile = "test/testInputs.json"

with open(inFile, 'r') as f:
  data = json.load(f)


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


def getData(path):

    keys = path.split("/")
    plotData = data
    for k in keys:
        plotData = plotData[k]

    plotData["bins"] = np.array(plotData["bins"])
    plotData["n"]    = np.array(plotData["n"])
    return plotData


def binCenters(bins):
    return 0.5*(bins[0:len(bins)-1] + bins[1:len(bins)] )


def configAxis(inAxis, **kwargs):
    if "ylabel" in kwargs: inAxis.set_ylabel(kwargs["ylabel"])
    if "xlabel" in kwargs: inAxis.set_xlabel(kwargs["xlabel"])
    if "ylim"   in kwargs: inAxis.set_ylim  (kwargs["ylim"])
    if "xlim"   in kwargs: inAxis.set_xlim  (kwargs["xlim"])
        



def plotRatio(dataToPlot, **kwargs):
    debug = kwargs["debug"] if "debug" in kwargs else False
    
    if debug:
        print(f'Called plotRatio')
        print_parameters(**kwargs)

    fig, axs = plt.subplots(2,1,figsize=(6,5), gridspec_kw={'height_ratios': [3, 1]})
    plt.subplots_adjust(hspace=0.05)


    axs[0].errorbar(
        binCenters(dataToPlot[0]["bins"]),
        dataToPlot[0]["n"],
        yerr = dataToPlot[0]["n"]**0.5,
        marker = '.',
        fmt = '.k'
    )
    axs[0].step(binCenters(dataToPlot[1]["bins"]) ,dataToPlot[1]["n"] ,fillstyle="full",where='mid')    

    axs[0].set_xticklabels([])
    axs[0].set_xticks([])

    if "ylabel" in kwargs: axs[0].set_ylabel(kwargs["ylabel"])
    if "ylim"   in kwargs: axs[0].set_ylim  (kwargs["ylim"])
    if "xlim"   in kwargs:
        axs[0].set_xlim  (kwargs["xlim"])
        axs[1].set_xlim  (kwargs["xlim"])
    
    #
    #  Plot Ratio
    #
    epsilon = 0#1e-4
    ratio = (dataToPlot[0]["n"]/(dataToPlot[1]["n"]+epsilon))
    axs[1].plot(binCenters(dataToPlot[0]["bins"]), ratio)

    xMin = dataToPlot[0]["bins"][0]
    xMax = dataToPlot[0]["bins"][-1]
    axs[1].plot([xMin,xMax],[1,1],"k:")
    
    
    if "xlabel" in kwargs: axs[1].set_xlabel(kwargs["xlabel"])
    if "rlabel" in kwargs:
        axs[1].set_ylabel(kwargs["rlabel"])
    else:
        axs[1].set_ylabel("Ratio")

    if "rlim" in kwargs: axs[1].set_ylim(kwargs["rlim"])    

        
    #axs[1].plot([xMin,xMax],[1,1],"k:")
    plt.show()

        
    
def plotHists(dataToPlot, **kwargs):

    debug = kwargs["debug"] if "debug" in kwargs else False
    
    if debug:
        print(f'Called plot')
        print_parameters(**kwargs)

    if "doratio" in kwargs and kwargs["doratio"]:
        plotRatio(dataToPlot, **kwargs)
        return

        
    fig, ax = plt.subplots(1,1,figsize=(6,5))
        

    ax.errorbar(
        binCenters(dataToPlot[0]["bins"]),
        dataToPlot[0]["n"],
        yerr = dataToPlot[0]["n"]**0.5,
        marker = '.',
        fmt = '.k'
    )
    
    if len(dataToPlot) == 2:
        ax.step(binCenters(dataToPlot[1]["bins"]) ,dataToPlot[1]["n"] ,where='mid')

    configAxis(ax,**kwargs)
    
    plt.show()

def checkList(inList, hasLength = 2):
    if not len(inList) == hasLength:
        print("Error: can only plot from two directories at a time")
        return

def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

    
def plot(var,inDir, **kwargs):

    debug = kwargs["debug"] if "debug" in kwargs else False

    if debug:
        print(f'Called plot with var={var} and inDir={inDir}')
        print_parameters(**kwargs)
        
    dataToPlot = []

    # plot 2 differnet vars from 2 differnet dirs
    if type(inDir) == list and type(var) == list:

        checkList(inDir)
        checkList(var)

        dataToPlot.append(getData(inDir[0]+"/"+var[0]))
        dataToPlot.append(getData(inDir[1]+"/"+var[1]))

    # plot 1 vars from 2 differnet dirs
    elif type(inDir) == list and not type(var) == list:

        checkList(inDir)

        dataToPlot.append(getData(inDir[0]+"/"+var))
        dataToPlot.append(getData(inDir[1]+"/"+var))

    # plot 2 different vars from 1  dirs        
    elif not type(inDir) == list and type(var) == list:

        checkList(var)

        dataToPlot.append(getData(inDir+"/"+var[0]))
        dataToPlot.append(getData(inDir+"/"+var[1]))

        
    # plot 1 vars from 1  dirs
    else:
        dataToPlot.append(getData(inDir+"/"+var))


    #
    # plotHits
    #
    plotHists(dataToPlot, **kwargs)
    
