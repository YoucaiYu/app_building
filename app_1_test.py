import json
from difflib import get_close_matches
from difflib import SequenceMatcher

json_data = json.load(open('jason_data.json'))

def eng_translate():
    while True:
        in_word = input("\nEnter the word or enter 12 to exit: ")
        needed_word = in_word.lower()

        if needed_word in json_data.keys():
            sum_mean = len(json_data[needed_word])
            if sum_mean > 1:
                print("There are %s means" % str(sum_mean))
                print("\nThe meanings of the word are followed: ")
                
            else:
                print("\nThe meaning of the word is: ")
                
            for word_means in json_data[needed_word]: 
                print(word_means)

        elif needed_word.title() in json_data.keys():  # solve the problem, that words started with uppercase.
            for word_means in json_data[needed_word.title()]:
                print(word_means)
        
        elif needed_word.upper() in json_data.keys():  # solve the problem, that inputed word consit if uppercases
            for word_means in json_data[needed_word.upper()]:
                print(word_means)
                
        elif len(get_close_matches(needed_word, json_data.keys())) > 0:
            double_check = input("Do you mean %s instead?" % get_close_matches(needed_word, json_data.keys())[0])
            if double_check == "Y":
                print(json_data[get_close_matches(needed_word, json_data.keys())[0]])
            elif double_check == "N":
                print("There is no word like this.") 
                
        elif in_word == "12": # use number to stop the app 
            break
            
        elif needed_word not in json_data.keys():
            print("There is no word like this.")
            print("\nYou can re-enter the word or enter 12 to exit.\n")
            

eng_translate()

