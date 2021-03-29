def calc_output(inputs: [], weights: [], bias):
    out = bias
    for x in range(len(inputs)):
        out += inputs[x] * weights[x]
    return out


def main():
    inputs = [1, 2, 3]
    weights = [1.1, 1.2, 1.3]
    bias = 2

    output = calc_output(inputs, weights, bias)
    print(output)


main()
