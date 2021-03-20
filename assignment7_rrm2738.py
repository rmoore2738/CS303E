# Homework 7
# Rebecca Moore RRM2738

from string import punctuation

# Part 1


def make_matrix(rows, columns):
    import random
    matrix = [] # Create an empty list

    for row in range(rows):
        matrix.append([]) # Add an empty new row
        for column in range(columns):
            matrix[row].append(random.randint(0, 1))
    return matrix

def even_cols(matrix):
    evens = [] # Create a new empty list
    for row in range(len(matrix)):
        column_sum = 0
        for column in range(len(matrix[row])):
            if matrix[row][column] == 1:
                column_sum += 1
        if column_sum % 2 == 0:
            evens.append(column)
    return evens

#Part 2

stop_words = {"a","am","an", "and","are", "as", "at",
              "be","but", "by", "for", "i", "if", "in", "into",
              "is", "it", "its", "my", "nor", "not", "of", "on",
              "or", "so", "than", "that", "the", "then", "this",
              "to", "too", "will", "with"}
              #doesnt count these words

def count_words(infile):
    word_counts = {}
    for line in infile:
        processLine(line.lower(), word_counts)
    return word_counts

#count each word in the line
def processLine(line, word_counts):
    line = strip_punctuation(line)
    words = line.split()
    for word in words:
        if word not in stop_words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

#remove the punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

#finds the word counted the most
def find_max(word_counts):
    max_count = 0
    for key in word_counts:
        if word_counts.get(key) > max_count:
            max_count = word_counts[key]
            max_count_key = key
    return {max_count_key: max_count}


def print_word_count(dictionary, word):
    print("Count of \"" + word + "\" is:", dictionary[word])


# calls all of the functions defined above
def main():
    rows = eval(input("Enter the number of rows: "))
    columns = eval(input("Enter the number of columns: "))
    matrix = make_matrix(rows, columns)
    matrix_6 = make_matrix(6, 6)
    print(matrix_6)
    print(even_cols(matrix_6))
    file = open("raven.txt", "r")
    word_counts = count_words(file)
    max = find_max(word_counts)
    print_word_count(word_counts, list(max.keys())[0])
    print_word_count(word_counts, 'raven')
    print_word_count(word_counts, 'nevermore')

main()
