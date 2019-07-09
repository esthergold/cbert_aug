from sklearn.grid_search import ParameterGrid

def main():

    param_grid = {'model': ['cnn', 'rnn', 'bow']}

    grid = ParameterGrid(param_grid)

    for params in grid:
        train_mock(params['param1'], params['param2'])


if __name__ == '__main__':
    main()

def train_mock(args, print_log):
    print(args.dataset)
    return 0.1






