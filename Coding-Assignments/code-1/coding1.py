# COMS3203 DISCRETE MATHEMATICS
# CODING ASSIGNMENT 1

# YOUR NAME(s):
# YOUR UNI(s):

'''
Returns the number of vowels in a given string s.

Parameters:
s (string): lowercase string without spaces

Returns:
int: number of vowels
'''
def vowel_counter(s):
    count = 0
    
    for i in s:
        if i in 'aeiou':
            count += 1
            
    return count # int

'''
Implements the 'sometimes y' rule on given string s.

Parameters:
s (string): The target number to generate primes up to.

Returns:
boolean: True/False depending on whether the string has y
int: number of vowels in the string originally (wihout sometimes y rule)
int: number of vowels in the string after sometimes y rule
'''
def sometimes_y(s):
    y_in_string = False
    original_count = vowel_counter(s)
    new_count = original_count 
    
    letter_count = len(s)
    
    if 'y' in s:
        y_in_string = True 
        if s[letter_count - 1] == 'y':
            new_count = (original_count + 1)
        
    
        
    return y_in_string, original_count, new_count # boolean, int, int

'''
Returns a list of the number of vowels in each word in a sentence.

Parameters:
sentence (string): A string of a sentence.

Returns:
list: a list of the number of vowels for each word in the sentence.
'''
def sentence_counter(sentence):
       
    special_chars = '.,!?'
    
    for special_char in special_chars:
        sentence.replace(special_char, '')
        
    sentence = sentence.lower()
    
    words = sentence.split()
    
    counts = [0 for number in range(len(words))]
    
    for index, word in enumerate(words):
        count = sometimes_y(word)[2]
        counts[index] += count
    
    return counts # list

'''
Returns an an integer that is the nth Fibonacci number.

Parameters:
n (int): The nth Fibonacci number you want.

Returns:
int: the nth fibonacci number.
'''
def recursive_fib(n):
    if  n < 2:
        fib_n = n
        return fib_n
        
    fib_n = recursive_fib(n - 1) + recursive_fib(n - 2)

    return fib_n # int

'''
Returns an an integer that is the nth Fibonacci number.

Parameters:
n (int): The nth Fibonacci number you want.

Returns:
int: the nth fibonacci number.
'''
def iterative_fib(n):
    
    numbers = [0,1]
    total = 1
    
    fib_n = 0
    
    for i in range(1, n):
        
        if len(numbers) != n:
            print(numbers[i])
            total = numbers[i] + numbers[i - 1]

            numbers.append(total)
            
            
    fib_n = total + numbers[n - 2]
    
    if n == 1:
        fib_n = 1
    
    return fib_n # int

#'''
#Returns whether two sentences are synonyms or not, given a list of synonyms.

#Parameters:
#synonyms (list): A list of tuples of the synonyms you should store.
#sentences (tuple): A 2-tuple containing two sentences you want to compare.

#Returns:
#boolean: Whether the sentences are synonyms or not.
#'''
#def synonym_checker(synonyms, sentences):
    # WRITE YOUR CODE HERE
#    return is_synonym # boolean

######################################################################
### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
######################################################################
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 1: Python Introduction!")
    print("#######################################")
    print()

    print("---------------------------------------")
    print("PART A: Vowel Counting")
    print("---------------------------------------")
    vowel_tests = [['abcdef', 'abcdefy', 'abc def y'], ['cat', 'catty', 'The big cat.'], ['dog', 'ydog', 'I love dogs!']]
    vowel_answers = [[2, (True, 2, 3), [1, 1, 1]], [1, (True, 1, 2), [1, 1, 1]], [1, (True, 1, 1), [1, 2, 1]]]
    for count, test in enumerate(vowel_tests):
        if(vowel_answers[count][0] == vowel_counter(test[0]) and
        vowel_answers[count][1] == sometimes_y(test[1]) and
        vowel_answers[count][2] == sentence_counter(test[2])):
            passed = "PASSED!"
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print("Vowel Count (Correct): ", vowel_answers[count][0])
        print("Vowel Count (Your Answer): ", vowel_counter(test[0]))
        print("Vowel Count with y (Correct): ", vowel_answers[count][1])
        print("Vowel Count with y (Your Answer): ", sometimes_y(test[1]))
        print("Sentence Count (Correct): ", vowel_answers[count][2])
        print("Sentence Count (Your Answer): ", sentence_counter(test[2]))

    print("---------------------------------------")
    print("PART B: Fibonacci")
    print("---------------------------------------")
    tests = [[1, 1], [4, 4], [10, 10]]
    answers = [[1, 1], [3, 3], [55, 55]]
    for count, test in enumerate(tests):
        if(answers[count][0] == recursive_fib(test[0]) and
            answers[count][1] == iterative_fib(test[1])):
            passed = "PASSED!"
        else:
            passed = "FAILED!"

        print("Test #{}: {}".format(count + 1, passed))
        print("Recursive Fibonacci (Correct): ", answers[count][0])
        print("Recursive Fibonacci (Your Answer): ", recursive_fib(test[0]))
        print("Iterative Fibonacci (Correct): ", answers[count][1])
        print("Iterative Fibonacci (Your Answer): ", iterative_fib(test[1]))


#    print("---------------------------------------")
#    print("PART C: Synonym Checker")
#    print("---------------------------------------")
#    tests = [
#        [[("movie", "film"), ("reviews", "ratings")], ("I heard that movie got good ratings.", "I heard that film got good reviews.")],
#        [[("movie", "film")], ("I heard that movie got good ratings.", "I heard that film got good reviews.")],
#        [[("movie", "film"), ("reviews", "ratings")], ("I heard that work of cinema got good ratings.", "I heard that film got good reviews.")]
#   ]
#    answers = [True, False, False]
#    for count, test in enumerate(tests):
#        if(answers[count] == synonym_checker(test[0], test[1])):
#            passed = "PASSED!"
#        else:
#            passed = "FAILED!"
#
#        print("Test #{}: {}".format(count + 1, passed))
#       print("Synonyms:", test[0])
#        print("Sentences:", test[1])
#       print("Synonym? (Correct): ", answers[count])
#        print("Synonym? (Your Answer): ", synonym_checker(test[0], test[1]))


