from ScoresRepository import ScoresRepository
from colorama import Fore, Style
def test_add():
    repo = ScoresRepository()
    repo.add_score(10)
    assert repo.scores == [10] , "Should be [10], instead is " + str(repo.scores) + " (add failed)"
    repo.add_score(20)
    assert repo.scores == [10, 20] , "Should be [10, 20], instead is " + str(repo.scores) + " (add failed)" 

def test_add_at_index():
    repo = ScoresRepository()
    repo.add_score(10)
    repo.add_score(20)
    repo.add_score(30)
    repo.add_score_at_index(1, 15)
    assert repo.scores == [10, 15, 20, 30] , "Should be [10, 15, 20, 30], instead is " + str(repo.scores) + " (add_at_index failed)"

def test_remove_at_index():
    repo = ScoresRepository()
    repo.add_score(10)
    repo.add_score(20)
    repo.add_score(30)
    repo.remove_score_at_index(1)
    assert repo.scores == [10, 30] , "Should be [10, 30], instead is " + str(repo.scores) + " (remove_at_index failed)" 

def test_remove_between_indexes():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.remove_scores_between_indexes(1, 4)
    assert repo.scores == [10, 60] , "Should be [10, 60], instead is " + str(repo.scores) + " (remove_between_indexes failed)"

def test_replace_at_index():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.replace_score_at_index(1, 15)
    assert repo.scores == [10, 15, 30, 40, 50, 60] , "Should be [10, 15, 30, 40, 50, 60], instead is " + str(repo.scores) + " (replace_at_index failed)"

def test_get_indexes_with_scores_less_than():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_indexes_with_scores_less_than(30) == [0, 1] , "Should be [0, 1], instead is " + str(repo.get_indexes_with_scores_less_than(30)) + " (get_indexes_with_scores_less_than failed)"

def test_get_indexes_sorted_by_score():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 40, 30, 50, 60])
    assert repo.get_indexes_sorted_by_score() == [0, 1, 3, 2, 4, 5] , "Should be [0, 1, 3, 2, 4, 5], instead is " + str(repo.get_indexes_sorted_by_score()) + " (get_indexes_sorted_by_score failed)"

def test_get_indexes_with_scores_higher_than():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_indexes_with_scores_higher_than(30) == [3, 4, 5] , "Should be [3, 4, 5], instead is " + str(repo.get_indexes_with_scores_higher_than(30)) + " (get_indexes_with_scores_higher_than failed)"

def test_get_average_scores_between_indexes():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_average_scores_between_indexes(1, 4) == 46.67 , "Should be 46.67, instead is " + str(repo.get_average_scores_between_indexes(1, 4)) + " (get_average_scores_between_indexes failed)"

def test_get_minimum_score_between_indexes():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_minimum_score_between_indexes(1, 4) == 20, "Should be 20, instead is " + str(repo.get_minimum_score_between_indexes(1, 4)) + " (get_minimum_score_between_indexes failed)"

def test_get_scores_between_indexes_multiples_of():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_scores_between_indexes_multiples_of(1, 4, 20) == [20, 40], "Should be [20, 40], instead is " + str(repo.get_scores_between_indexes_multiples_of(1, 4, 20)) + " (get_scores_between_indexes_multiples_of failed)"

def test_keep_only_scores_multiple_of():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.keep_only_scores_multiple_of(20)
    assert repo.scores == [20, 40, 60], "Should be [20, 40, 60], instead is " + str(repo.scores) + " (keep_only_scores_multiple_of failed)"

def test_keep_only_scores_higher_than():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.keep_only_scores_higher_than(30)
    assert repo.scores == [40, 50, 60] , "Should be [40, 50, 60], instead is " + str(repo.scores) + " (keep_only_scores_higher_than failed)"

def test_undo():
    '''repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.remove_scores_between_indexes(1, 4)
    repo.undo()
    assert repo.scores == [10, 20, 30, 40, 50, 60] , "Should be [10, 20, 30, 40, 50, 60], instead is " + str(repo.scores) + " (undo failed)"'''
    pass

def test_all():
    string = ""
    try:
        test_add()
        test_add_at_index()
        test_remove_at_index()
        test_remove_between_indexes()
        test_replace_at_index()
        test_get_indexes_with_scores_less_than()
        test_get_indexes_sorted_by_score()
        test_get_indexes_with_scores_higher_than()
        test_get_average_scores_between_indexes()
        test_get_minimum_score_between_indexes()
        test_get_scores_between_indexes_multiples_of()
        test_keep_only_scores_multiple_of()
        test_keep_only_scores_higher_than()
        test_undo()
    except ValueError as ve:
        print(ve)
        string = Fore.RED+"Tests failed!" + Style.RESET_ALL
    except AssertionError as ae:
        print(ae)
        string = Fore.RED+"Tests failed!" + Style.RESET_ALL
    except Exception as e:
        print(e)
        string = Fore.RED+"Tests failed!" + Style.RESET_ALL
    if string == "":
        string += Fore.GREEN + "Tests passed!"
        string += Style.RESET_ALL
    print(string)