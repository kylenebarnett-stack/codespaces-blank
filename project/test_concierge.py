from project import ListLibrary
from project import OptionList

#from project import adding_rows
#import pytest

#test_init
#librar_location

def test_count_lists():
    list_library = ListLibrary()
    assert list_library.count_lists == 3

def test_name_of_lists():
    list_library = ListLibrary()
    assert list_library.names_of_lists() == "restaurants, seasons, games"

def test_add_list():
    list_library = ListLibrary()
    assert list_library.add_list("spam") == True
    assert list_library.add_list("games") == False

def test_file_exists():
    list_library = ListLibrary()
    assert list_library.file_exists("restaurants") == True
    assert list_library.file_exists("spam") == True
    assert list_library.file_exists("brian") == False

#def test_add_row():
#    option_list = OptionList("spam")
#    assert option_list.add_row(["green eggs"], ["ham"])

def test_delete_list():
    list_library = ListLibrary()
    assert list_library.delete_list("spam","yes")

#test init

def test_source_file():
    option_list = OptionList("restaurants")
    assert option_list.source_file == "restaurants.csv"

def test_column_headers():
    option_list = OptionList("restaurants")
    assert option_list.column_headers == ["restaurant name","style"]

def test_columns_count():
    option_list = OptionList("restaurants")
    assert option_list.columns_count == 2


def test_check_duplicate_row():
    option_list = OptionList("restaurants")
    assert option_list.check_duplicate_row(["Jim & Nicks","BBQ"]) == True

#def test_full_list():
#    option_list = OptionList("restaurants")
#    assert option_list.full_list == "something"

def test_list_length():
    option_list = OptionList("restaurants")
    assert option_list.list_length() == 14

def test_list_length_empty():
    option_list = OptionList("seasons")
    assert option_list.list_length() == 1

def test_find_category_groups():
    option_list = OptionList("restaurants")
    assert option_list.find_category_groups("style") == ("Americana, Asian, BBQ, Burgers, Chicken, Dessert, Indian, Mexican, Sandwiches")

def test_list_contents():
    option_list = OptionList("restaurants")
    assert option_list.list_contents("restaurant name","style","BBQ") == ["Jim & Nicks"]
    assert option_list.list_contents("restaurant name","style","Indian") == ["Taj", "Tandori and Tap"]
