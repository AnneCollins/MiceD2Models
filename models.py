# This encodes the different models

def m1(expe,alphaG = .1,alphaN=.1,alphaC=.1,betaG=1,betaN=1):
    """
    This encodes RL model type 1
    :param Expe: is the structure of the experiment through which M1 is run
    :param alphaG: G learning rate
    :param alphaN: N learning rate
    :param alphaC: critic learning rate
    :param betaG: G weight
    :param betaN: N weight
    :return: nothing for now
    """
    print("Fishes " * expe.n)



def m2(expe,alphaG = .1,alphaN=.1,alphaC=.1,betaG=1,betaN=1):
    """
    This encodes RL model type 2
    :param Expe: is the structure of the experiment through which M1 is run
    :param alphaG: G learning rate
    :param alphaN: N learning rate
    :param alphaC: critic learning rate
    :param betaG: G weight
    :param betaN: N weight
    :return: nothing for now
    """
    print("Birds " * 2*expe.n)