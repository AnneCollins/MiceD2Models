"""
This is a file that will run a simple rl model.
"""

import expe
import models

def main():
    '''
    This function will define an expe, run models on it, analyze it.
    :return:
    '''
    print('hello world')
    runrl()

def runrl():
    '''
    This function will run RL models on an experiment
    :return:
    '''
    exp = expe.Expe()
    models.m1(exp)
    models.m2(exp)


if __name__ == "__main__":
    main()