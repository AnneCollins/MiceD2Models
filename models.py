'''
Encodes the different models.
'''

def opal1(exp,alpha_g=0.1, alpha_n=0.1, alpha_c=0.1, beta_g=1, beta_n=1):
    """
    Encodes OpAL model type 1.
    :param exp: Experiment instance describing the structure of the experiment through which the model is run
    :param alpha_g: G actor learning rate. 0<alpha_g<1
    :param alpha_n: N actor learning rate. 0<alpha_n<1
    :param alpha_c: critic learning rate. 0<alpha_c<1
    :param beta_g: G actor weight. beta_g>0
    :param beta_n: N actor weight. beta_g>0
    :return: nothing for now
    """
    print("Fishes " * exp.n)



def opal2(exp, alpha_g=0.1, alpha_n=0.1, alpha_c=0.1, beta_g=1, beta_n=1):
    """
    Encodes OpAL model type 2.
    :param exp: Experiment instance describing the structure of the experiment through which the model is run
    :param alpha_g: G actor learning rate. 0<alpha_g<1
    :param alpha_n: N actor learning rate. 0<alpha_n<1
    :param alpha_c: critic learning rate. 0<alpha_c<1
    :param beta_g: G actor weight. beta_g>0
    :param beta_n: N actor weight. beta_g>0
    :return: nothing for now
    """
    print("Birds " * 2*exp.n)
