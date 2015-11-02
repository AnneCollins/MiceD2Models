"""
Runs learning models on a defined experiment.
"""

from experiment import Experiment
import models

def run_rl():
    '''
    Run RL models on an experiment.
    :return:
    '''
    exp = Experiment()
    models.opal1(exp)
    models.opal2(exp)


def main():
    '''
    Defines an experiment, run models on it, analyzes it.
    :return:
    '''
    print('hello world')
    run_rl()

if __name__ == "__main__":
    main()
