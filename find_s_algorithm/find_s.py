def find_s_algorithm(training_data):
    num_attribute = len(training_data[0]) - 1
    hypothesis = ['0'] * num_attribute

    for i in range(len(training_data)):
        if training_data[i][num_attribute] == '1':
            print("\nInstance ", i + 1, " is", training_data[i], " and is Positive Instance")
            for j in range(num_attribute):
                if hypothesis[j] == '0' or hypothesis[j] == training_data[i][j]:
                    hypothesis[j] = training_data[i][j]
                else:
                    hypothesis[j] = '?'
            print("The hypothesis for training instance", i + 1, " is: ", hypothesis, "\n")

        if training_data[i][num_attribute] == '0':
            print("\nInstance ", i + 1, " is", training_data[i], " and is Negative Instance Hence Ignored")
            print("The hypothesis for training instance", i + 1, " is: ", hypothesis, "\n")

    return hypothesis

def main():
    training_data = [
        ['Monday', 'No', 'Easygoing', 'Evening', '1'],
        ['Monday', 'No', 'Annoyed', 'Evening', '0'],
        ['Saturday', 'Yes', 'Easygoing', 'Lunchtime', '0'],
        ['Monday', 'No', 'Easygoing', 'Morning', '1']
    ]

    print("\nThe total number of training instances are: ", len(training_data))

    print("\nThe initial hypothesis is:")
    initial_hypothesis = ['0'] * (len(training_data[0]) - 1)
    print(initial_hypothesis)

    final_hypothesis = find_s_algorithm(training_data)

    print("\nThe Maximally specific hypothesis for the training instance is ", final_hypothesis)

if __name__ == "__main__":
    main()

