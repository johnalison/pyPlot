
Interactive matplot lib script.

Reads in json file and makes interactive plots

>  py -i pyPlot.py test/testInputs.json
>  py -i pyPlot.py test/testInputs.json    test/testInputs2.json  

Examples:

> ls()
> plot(["var2","var2"],["dataSetA/dummy","dataSetB/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=False,rlim=[0.,2.],xlim=[0,2])
> plot(["var2","var2"],["dataSetA/dummy","dataSetB/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=True,rlim=[0.,2.],xlim=[0,2])
> plot(["var1","var1"],["dataSetB/dummy","dataSetA/dummy"],xMin=1,ylabel="Entries",xlabel="var2",doratio=True,rlim=[0,2],xlim=[-0.5,2],yscale="linear",labels=["var","d"],rebin=2)


# Initial Setup (only need once)

>  python3 -m venv myPyPlotEnv
>  cd myPyPlotEnv
>  source bin/activate
>  python3 -m pip install -r ../requirements.txt
>  cd ../

# Then each time

> source setup.sh


# Initial Development

> python3 -m venv pyPlotEnv
> cd pyPlotEnv/
> source bin/activate
> python3 -m pip install numpy
> python3 -m pip install --upgrade pip
> python3 -m pip install matplotlib
