import numpy as np 
import json
import matplotlib.pyplot as plt

def getData(n, mu1=0, sig1=0.1, mu2=1, sig2=0.3, frac1=0.7):
    data1 = np.random.normal(mu1, sig1, int(n*frac1))
    data2 = np.random.normal(mu2, sig2, int(n*(1-frac1)))
    dataC = np.concatenate((data1,data2))
    np.random.shuffle(dataC)
    return dataC

outputData = {}

def addDataSet(name,dataSetVar1, dataSetVar2):

    bins = np.linspace(-1,2,60)
    n1, bins1, _ = plt.hist(dataSetVar1, bins=bins)
    n2, bins2, _ = plt.hist(dataSetVar2, bins=bins)

    outputData[name] = {"dummy":
                        { "var1": { "n" :  n1.tolist() , "bins": bins1.tolist()},
                          "var2": { "n"  : n2.tolist() , "bins": bins2.tolist()},
                         }
                        }
    

dataSetA_v1 = getData(n=10000)
dataSetA_v2 = getData(n=10000, mu1=0.5)                   
addDataSet("dataSetA",dataSetA_v1,dataSetA_v2)


dataSetB_v1 = getData(n=10000)
dataSetB_v2 = getData(n=10000, mu1=0.5)                   
addDataSet("dataSetB",dataSetB_v1,dataSetB_v2)


with open('testInputs.json', 'w') as json_file:
  json.dump(outputData, json_file)
