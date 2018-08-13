import argparse


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser()
# parser.add_argument('-map',type=bool,default=True,help='show friends loaction distribution map')
# parser.add_argument('-fig',type=bool,default=True,help='show friends gender distribution fig')
parser.add_argument("-map", type=str2bool, nargs='?',const=True, default=True,help='show friends loaction distribution map')
parser.add_argument("-fig", type=str2bool, nargs='?',const=True, default=True,help='show friends gender distribution fig')


args = parser.parse_args()
print(args.map,args.fig)