from ScoresRepository import ScoresRepository

def test_add():
    repo = ScoresRepository()
    repo.add_score(10)
    assert repo.scores == [10]
    repo.add_score(20)
    assert repo.scores == [10, 20]
    repo.add_score(30)

def test_add_at_index():
    repo = ScoresRepository()
    repo.add_score(10)
    repo.add_score(20)
    repo.add_score(30)
    repo.add_score_at_index(1, 15)
    assert repo.scores == [10, 15, 20, 30]

def test_remove_at_index():
    repo = ScoresRepository()
    repo.add_score(10)
    repo.add_score(20)
    repo.add_score(30)
    repo.remove_score_at_index(1)
    assert repo.scores == [10, 30]

def test_remove_between_indexes():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.remove_scores_between_indexes(1, 4)
    assert repo.scores == [10, 60]

def test_replace_at_index():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.replace_score_at_index(1, 15)
    assert repo.scores == [10, 15, 30, 40, 50, 60]

def test_get_indexes_with_scores_less_than():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_indexes_with_scores_less_than(30) == [0, 1]

def test_get_indexes_sorted_by_score():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 40, 30, 50, 60])
    assert repo.get_indexes_sorted_by_score() == [0, 1, 3, 2, 4, 5]

def test_get_indexes_with_scores_higher_than():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_indexes_with_scores_higher_than(30) == [3, 4, 5]

def test_get_average_scores_between_indexes():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_average_scores_between_indexes(1, 4) == 46.67

def test_get_minimum_score_between_indexes():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_minimum_score_between_indexes(1, 4) == 20

def test_get_scores_between_indexes_multiples_of():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    assert repo.get_scores_between_indexes_multiples_of(1, 4, 20) == [20, 40]

def test_keep_only_scores_multiple_of():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.keep_only_scores_multiple_of(20)
    assert repo.scores == [20, 40, 60]

def test_keep_only_scores_higher_than():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.keep_only_scores_higher_than(30)
    assert repo.scores == [40, 50, 60]

def test_undo():
    repo = ScoresRepository()
    repo.add_scores([10, 20, 30, 40, 50, 60])
    repo.remove_scores_between_indexes(1, 4)
    repo.undo()
    assert repo.scores == [10, 20, 30, 40, 50, 60]

def test_all():
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
    