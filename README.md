
Interactive matplot lib script.

Reads in json file and makes interactive plots

>  py -i pyPlot.py test/testInputs.json
>  py -i pyPlot.py test/testInputs.json    test/testInputs2.json  

Examples:

> ls()
> plot(["var2","var2"],["dataSetA/dummy","dataSetB/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=False,rlim=[0.,2.],xlim=[0,2])
> plot(["var2","var2"],["dataSetA/dummy","dataSetB/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=True,rlim=[0.,2.],xlim=[0,2])
> plot(["var1","var1"],["dataSetB/dummy","dataSetA/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=True,rlim=[0,2],xlim=[-0.5,2],yscale="linear",labels=["var","d"],rebin=2)