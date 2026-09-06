import csv, os, random, sys, pyfiglet
from tabulate import tabulate
import pandas as pandasForSortingCSV

# TODO: make it so "Menu" brings the user back to start

class ListLibrary():
    def __init__(self):
        ...

    #getter
    @property
    def library_location(self):
        return os.listdir(".")

    #getter
    @property
    def count_lists(self): #tested OK
        list_counts = 0
        for files in self.library_location:
            if files.endswith(".csv"):
                list_counts += 1
        return list_counts

    def names_of_lists(self): #tested OK
        my_lists = []
        for files in self.library_location:
            if files.endswith(".csv"):
                files = str(files).replace(".csv", "")
                my_lists.append(files)
        return ", ".join(my_lists)

    def add_list(self, list_name): #tested OK
        if self.file_exists(list_name):
            return False #already exists, do not add
        else:
            open(list_name + ".csv", "w", newline="")
            return True

    def file_exists(self, list_name): #tested OK
        for files in self.library_location:
            if files == list_name.lower() + ".csv":
                return True
        return False

    def delete_list(self, list_name, confirmation): #tested OK
        if confirmation == "yes":
            if self.file_exists(list_name):
                os.remove(list_name.lower() + ".csv")
                return True
            return False
        else:
            return False

class OptionList():
    def __init__(self, list_name):
        if not list_name:
            raise ValueError("Invalid list name")
        self.list_name = list_name

    #getter
    @property
    def source_file(self): #tested OK
        return self.list_name.lower() + ".csv"

    #getter
    @property
    def column_headers(self): #tested OK
        with open(self.source_file) as data:
            my_reader = csv.reader(data)
            return next(my_reader)

    #getter
    @property
    def columns_count(self): #tested OK
        return len(self.column_headers)

    def add_row(self, item_name, column_values): #item_name str, column_values list
        new_row = [item_name] + column_values
        if self.check_duplicate_row(new_row):
            return False
        with open(self.source_file, "a") as file:
            file.write(",".join(new_row) + "\n")
            return True

    def check_duplicate_row(self, new_row): #tested OK
        with open(self.source_file) as data:
            my_reader = csv.reader(data)
            for row in my_reader:
                if new_row == row:
                    return True
        return False  # True = duplicated / False = not duplicated

    def full_list(self):
        my_list = pandasForSortingCSV.read_csv(self.source_file)
        my_list.sort_values(my_list.columns[0],
                    inplace=True)
        return(my_list)

    def list_length(self): #tested OK
        row_counter = 0
        with open(self.source_file) as data:
            my_reader = csv.reader(data)
            for row in my_reader:
                if not row == "":
                    row_counter += 1
        return row_counter

    def find_category_groups(self, col_header): #tested OK
        my_info = []
        with open(self.source_file) as data:
            my_reader = csv.DictReader(data)
            for row in my_reader:
                my_dictionary = row
                col_header_values = my_dictionary.get(col_header)
                my_info.append(col_header_values)
        this_list = list(dict.fromkeys(my_info))
        this_list.sort()
        return ", ".join(this_list)

    #can this use the one above instead of all this again?
    def list_contents(self, item_name, col_header, subgroup):
        my_info = []
        with open(self.source_file) as data:
            my_reader = csv.DictReader(data)
            for row in my_reader:
                my_dictionary = row
                col_header_values = my_dictionary.get(col_header)
                if col_header_values == subgroup:
                    pick_from_list = my_dictionary.get(item_name)
                    my_info.append(pick_from_list)
        this_list = list(dict.fromkeys(my_info))
        this_list.sort()
        return this_list

    def pick_randomly(self, list_shown):
        if type(list_shown) == str:
            pick_from_list = list_shown.split(",")
        else:
            pick_from_list = list_shown.get(self.column_headers[0])
        return random.choice(pick_from_list)

def main():
    list_library = ListLibrary()
    print(pyfiglet.figlet_format("Welcome!", font="big", justify="center"))
    print(("Welcome to your Choice Concierge service!").center(100, "~"))
    if ListLibrary.count_lists == 0:
        print("You have no lists! Let's go create one.")
        creating_list()
    else:
        if ListLibrary.count_lists == 1:
            print("You have 1 list: ", list_library.names_of_lists().title())
        else:
            print("You have these lists: ", list_library.names_of_lists().title())
        user_direction = input("Do you want to choose from a list, add items to a list, create a new list, or delete an exising list? (Choose/Add/Create/Delete) ").lower()
        if user_direction == "choose":
            list_name = input("Which list are we choosing from? ").lower()
            choosing_items(list_name)
        elif user_direction == "add":
            list_name = input("Which list are we adding to? ").lower()
            adding_rows(list_name)
        elif user_direction == "create":
            list_name = input("What is this new list called? ").lower()
            creating_list(list_name)
        elif user_direction == "delete":
            list_name = input("Which list did you want to delete? ").lower()
            deleting_list(list_name)
        else:
            print("No user direction given.")


def first_check(list_name):
    list_library = ListLibrary()
    if list_library.file_exists(list_name) == True:
        found_it = True
        return list_name
    else:
        found_it = False
        x = 1
        while found_it == False:
            while x < 4:
                list_name = input(f"I can't find that one. Let's try that again. (Retry {x} of 3.) What list do you want? ").lower()
                x += 1
                if list_library.file_exists(list_name) == True:
                    found_it = True
                    return list_name
            no_list = input("Looks like that list might not exist. Did you want to add it? (Yes/No) ").lower()
            if no_list == "yes":
                creating_list(list_name)
            else:
                sys.exit("Sorry, I'm not able to help you at this time. Have a great day!")


def choosing_items(list_name):
    list_name = first_check(list_name)
    option_list = OptionList(list_name)
    if option_list.list_length() == 1:
        add_instead = input("This list is empty. Do you want to add items to it instead? (Yes/No) ").lower()
        if add_instead == "yes":
            adding_rows(list_name)
        else:
            sys.exit("Sorry, I can't be of any help.")
    error_loop = False
    ask_one = input("Did you want to see the whole list or pick from a sub-section of this list? (All/Sub) ").lower()
    if ask_one == "all":
        list_shown = option_list.full_list()
        my_headers = option_list.column_headers
        print(tabulate(list_shown, tablefmt="rst", headers=my_headers, showindex=False))
        random_yn = input("Do you want me to pick an item from this list at random? (Yes/No) ").lower()
        if random_yn == "yes":
            picking_randomly(list_name, list_shown)
    elif ask_one == "sub":
        item_name = option_list.column_headers[0]
        if option_list.columns_count == 2:
            col_header = option_list.column_headers[-1]
        else:
            while error_loop == False:
                header_list = ", ".join(option_list.column_headers[1:])
                print(f"Categories to choose from in this list are: {header_list.title()}")
                col_header = input("Which category would you like to choose from? ").lower()
                if col_header == "":
                    print("No category selected. Let's try that again.")
                elif not col_header in header_list:
                    print("That's not an item from the available options. Try that again.")
                else:
                    error_loop = True  # escape the loop
        if not col_header == "":
            print(f"Choices under {col_header.title()} are:" ,option_list.find_category_groups(col_header))
            subgroup = input(f"What is your {col_header.title()} choice? ")# TOODO capitalization matters!!
            list_shown = option_list.list_contents(item_name, col_header, subgroup)
            item_count = len(list_shown)
            if item_count == 1:
                print(f"Looks like the only option is:")
                print(tabulate(list(map(lambda x:[x], list_shown)), tablefmt="rst", headers=[subgroup], showindex=False))
                print("Have a great day!")
            elif item_count > 1:
                print(f"Choices are:")
                print(tabulate(list(map(lambda x:[x], list_shown)), tablefmt="rst", headers=[subgroup], showindex=False))
                random_yn = input("Do you want me to pick an item from this list at random? (Yes/No) ").lower()
                random_yn = "yes"
                if random_yn == "yes":
                    picking_randomly(list_name, list_shown)
        else:
            print("No choice given.")

def picking_randomly(list_name, list_shown):
    option_list = OptionList(list_name)
    pick_another = True
    while pick_another == True:
        random_choice = option_list.pick_randomly(list_shown)
        print(f"My recommendation is: {random_choice}.")
        go_again = input("Does that one work? (Yes/No) ").lower()
        if go_again == "yes":
            sys.exit("Have a great day!")
        elif go_again == "no":
            pick_another = True
        else:
            sys.exit("No choice given.")

def adding_rows(list_name):
    list_name = first_check(list_name)
    option_list = OptionList(list_name)
    my_headers = ", ".join(option_list.column_headers)
    print(f"{list_name.title()} has the following categories: {my_headers.title()}")
    add_another = True
    while add_another == True:
        x = 0
        my_headers = option_list.column_headers[x]
        item_name = input(f"{my_headers.title()}: ")
        column_values = []
        x = 1
        while x < option_list.columns_count:
            my_headers = option_list.column_headers[x]
            x_item = input(f"{my_headers.title()}: ")
            x += 1
            column_values.append(x_item)
        if option_list.add_row(item_name, column_values) == False:
            print("This item already exists on this list.")
        go_again = input(f"Do you want to add another item to {list_name.title()}? (Yes/No) ").lower()
        if go_again == "yes":
            add_another = True
        elif go_again == "no":
            add_another = False
        else:
            print("No choice given")


def creating_list(list_name):
    list_library = ListLibrary()
    option_list = OptionList(list_name)
    if list_library.add_list(list_name) == False:
        user_direction = input("This list already exists. Do you want to choose items from this list or add items to it? (Choose/Add) ").lower()
        if user_direction == "choose":
            choosing_items(list_name)
        elif user_direction == "add":
            adding_rows(list_name)
        else:
            sys.exit("No user direction given. Have a great day!")
    else:
        add_headers = True
        x = 1
        column_values = []
        print("What are the categories in this list? The first one should be the name of the thing. (Ex. Restaurant Name) ")
        while add_headers == True:
            if x == 1:
                item_name = input("Category 1 (Name): ").lower()
                x += 1
            else:
                x_names = input(f"Category {x}: ").lower()
                x += 1
                column_values.append(x_names)
            if x > 2:
                go_again = input("Do you want to add another category? (Yes/No) ").lower()
                if go_again == "yes":
                    add_headers = True
                else:
                    add_headers = False
            else:
                add_headers = True
        option_list.add_row(item_name, column_values)
    go_on = input("Would you like to add items to this list? (Yes/No) ").lower()
    if go_on == "yes":
        adding_rows(list_name)
    else:
        sys.exit("Have a great day!")


def deleting_list(list_name):
    list_name = first_check(list_name)
    list_library = ListLibrary()
    confirmation = input(f"Are you sure you want to delete {list_name.title()}? (Yes/No) ")
    if confirmation == "yes":
        if not list_library.delete_list(list_name, confirmation) == False:
            list_library.delete_list(list_name, confirmation)
            print(f"{list_name.title()} has been deleted.")
        else:
            print(f"I cannot delete that. {list_name.title()} does not exist.")
    else:
        print(f"OK - {list_name.title()} was not deleted.")


if __name__ == "__main__":
    main()
