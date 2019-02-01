
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades, 0) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades, 0) == 42


def test_two_grades():
    grades = [2.0,3.0]
    assert compute_hw_average(grades, 0) == 2.5


def test_one_grade_one_dropped():
    grades = [12]
    assert compute_hw_average(grades, 1) == 0


def test_two_grades_one_dropped():
    grades = [1, 2]
    assert compute_hw_average(grades, 1) == 2
