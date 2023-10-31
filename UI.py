from ScoresRepository import ScoresRepository
from colorama import Fore, Style
from tests import test_all
#Menu:
def display_menu():
    print(Fore.YELLOW)
    print("0. Exit")
    print("1. Add a new score")
    print("2. Insert a new score at a given index")
    print("3. Remove the score at a given index")
    print("4. Remove scores between two indexes")
    print("5. Replace the score at a given index")
    print("6. Get indexes with scores less than a given value")
    print("7. Get all indexes sorted by their score")
    print("8. Get indexes with scores higher than a given value and sorted")
    print("9. Get the average scores between two indexes")
    print("10. Get the minimum score between two indexes")
    print("11. Get the scores of participants between two indexes that are multiples of a given value")
    print("12. Keep only the scores that are multiples of a given value")
    print("13. Keep only the scores that are higher than a given value")
    print("14. Undo")
    print("15. Show the list of scores")
    print("16. Read the list of scores from a file")
    print("17. Write the list of scores to a file")
    print(Style.RESET_ALL)

#UI
def ui():
    repo = ScoresRepository()
    #repo.add_scores([10, 20, 30, 40, 50, 60])
    test_all()
    while 1>0:  
        try:
            display_menu()
            i = int(input(Fore.LIGHTCYAN_EX+"Give the command: " + Style.RESET_ALL))
            if i==1:
                score = int(input("Give the score: "))
                repo.add_score(score)
            elif i==2:
                index = int(input("Give the index: "))
                score = int(input("Give the score: "))
                repo.add_score_at_index(index, score)
            elif i==3:
                index = int(input("Give the index: "))
                repo.remove_score_at_index(index)
            elif i==4:
                index1 = int(input("Give the first index: "))
                index2 = int(input("Give the second index: "))
                repo.remove_scores_between_indexes(index1, index2)
            elif i==5:
                index = int(input("Give the index: "))
                score = int(input("Give the score: "))
                repo.replace_score_at_index(index, score)
            elif i==6:
                value = int(input("Give the value: "))
                print(repo.get_indexes_with_scores_less_than(value))
            elif i==7:
                print(repo.get_indexes_sorted_by_score())
            elif i==8:
                value = int(input("Give the value: "))
                print(repo.get_indexes_with_scores_higher_than(value))
            elif i==9:
                index1 = int(input("Give the first index: "))
                index2 = int(input("Give the second index: "))
                print(repo.get_average_scores_between_indexes(index1, index2))
            elif i==10:
                index1 = int(input("Give the first index: "))
                index2 = int(input("Give the second index: "))
                print(repo.get_minimum_score_between_indexes(index1, index2))
            elif i==11:
                index1 = int(input("Give the first index: "))
                index2 = int(input("Give the second index: "))
                value = int(input("Give the value: "))
                print(repo.get_scores_between_indexes_multiples_of(index1, index2, value))
            elif i==12:
                value = int(input("Give the value: "))
                repo.keep_only_scores_multiple_of(value)
            elif i==13:
                value = int(input("Give the value: "))
                repo.keep_only_scores_higher_than(value)
            elif i==14:
                repo.undo()
            elif i==15:
                print(repo)
            elif i==16:
                repo.read_list_from_file()
            elif i==17:
                repo.write_list_to_file()
            elif i==0:
                print(Fore.LIGHTGREEN_EX+"Program ended successfully!")
                print(Style.RESET_ALL)
                break
            elif i<0 or i>17:
                raise Exception("Invalid command!")
        except ValueError:
            print("Invalid value!")
        except Exception as e:
            print(e)