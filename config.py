import argparse

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1', True):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0', False):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')



parser = argparse.ArgumentParser(description='')

#Image setting
parser.add_argument('--input_width', dest='input_width', default=32, help='input image width')
parser.add_argument('--input_height', dest='input_height', default=32, help='input image height')
parser.add_argument('--input_channel', dest='input_channel', default=3, help='input image channel')

#Training Settings
parser.add_argument('--continue_training', dest='continue_training', default=False, type=str2bool, help='flag to continue training')

parser.add_argument('--data', dest='data', default='celebA', help='cats image train path')
parser.add_argument('--root_path', dest='root_path', default='./data/', help='cats image train path')

parser.add_argument('--epochs', dest='epochs', default=10, help='total number of epochs')
parser.add_argument('--batch_size', dest='batch_size', default=64, help='batch size')

parser.add_argument('--learning_rate', dest='learning_rate', default=1e-5, help='learning rate of the optimizer')
parser.add_argument('--momentum', dest='momentum', default=0.5, help='momentum of the optimizer')

#Extra folders setting
parser.add_argument('--checkpoints_path', dest='checkpoints_path', default='./checkpoints/', help='saved model checkpoint path')
parser.add_argument('--graph_path', dest='graph_path', default='./graphs/', help='tensorboard graph')

args = parser.parse_args()