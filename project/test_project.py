from project import *

def test_scoreboard():

    assert scoreboard() == True

def test_get_highest_score():

    expected = get_highest_score()
    assert get_highest_score() == expected

def test_save_score():

    assert save_score(310) == True
    assert save_score(-130) == False
    assert save_score(230) == True
    assert save_score(-105) == False

def test_game_board():
    assert game_board() == True