import argparse
import json
import os
import torch
import sys

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def get_args():
    """
    Returns a namedtuple with arguments extracted from the command line.
    :return: A namedtuple with arguments
    """
    parser = argparse.ArgumentParser(
        description='Welcome to the MLP course\'s Pytorch training and inference helper script')

    parser.add_argument('--use_gpu', nargs="?", type=str2bool, default=False,
                        help='A flag indicating whether we will use GPU acceleration or not')

    parser.add_argument('--feedback', type=str, default="implicit", help="implicit/explicit")    

    parser.add_argument('--model', type=str, default="mf", help="mf/mlp: Train baseline, either matrix factorization or neural network")    

    parser.add_argument('--dataset', type=str, default="100K", help="100K/1M/10M/20M")    

    parser.add_argument('--experiment_name', type=str, default="matrix_model", help="Name of resulting experiment")    
    
    parser.add_argument('--embedding_dim', type=int, default=200, help="latents dimensions of matrix factorization models")
    
    parser.add_argument('--training_epochs', type=int, default=50, help="training epochs")

    parser.add_argument('--batch_size', type=int, default=512, help="training epochs")

    parser.add_argument('--learning_rate', type=float, default=1e-3, help=" learning rate")

    parser.add_argument('--l2_regularizer', type=float, default=1e-5, help="l2 normalization constant")

    parser.add_argument('--on_cluster', type=str2bool,default = False, help="Flag to specify where the data will be held")                

    parser.add_argument('--optim', type=str, default="adam", help="adam/sgd: optimizer to train the model")    

    parser.add_argument('--k', type=int, default=5, help="k:Variable to evaluate prec@k and rec@k")
    
    parser.add_argument('--neg_examples', type=int, default=5, help="number of negative examples per positive")
    
    args = parser.parse_args()
    return args