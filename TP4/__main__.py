from TP4.kohonen.kohonen import Kohonen


def main():
    print('Hello world')
    kohonen = Kohonen([[1,2], [2,3]], 15, 10, 2)
    kohonen.initialize_weights()
    activations = kohonen.train(10)
    print(activations)




if __name__ == "__main__":
    main()
