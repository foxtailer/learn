import argparse3

parser = argparse3.ArgumentParser()

parser.add_argument('-n')
args = parser.parse_args()

for _ in range(int(args.n)):
    print('meow')


