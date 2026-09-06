# CHOICE CONCIERGE SERVICE
#### Video Demo: <url here>
#### Description: The Choice Concierge Service is here to help with making decisions!

Welcome to the Choice Concierge Service! Within this service, you will be prompted to create lists to save information that you regularly choose from while making decisions, like which restaurant to visit for dinner or which game to play for the evening. The concierge will then help you make choices from those lists by narrowing down the choices, based on information that you provided during the list creation, or giving you a recommendation chosen at random.

You can add as many lists as you'd like, with as many items on those lists as you like, and as many different categories for those lists as you'd like, with the one requirement that the list contains no less than two categories, and the name of the item, like the restaurant name, is the first item on that record.

#### Let’s get into the details on the capabilities of this service:

**Creating a list:** If you choose to create a new list, the concierge will ask you to provide a list name and then will save that as a .csv file. You will then be prompted to provide categories for the items on this list, with the first one being the names of the item and a required second column, and then as many additional columns for additional information as desired. These are the headers of the columns in the .csv file that is being created, which will be used to contain the list, once items are added. The concierge will check that there is not already a list with the same name, to avoid writing over an existing list. If the concierge notices that no lists exist, then it will automatically prompt you to create a list.

**Adding items to a list:** The concierge  will ask you to select a list (or you might choose to get here during list creation), and then will provide the category groups (column headers) for the list. It will prompt you to enter information for those groups, in order to add items to the list. It does check that the record being added has not already been added exactly that way in order to avoid duplicated records. It does, however, allow for the item to be added with different information in the categories. For example, if a Mexican restaurant also has excellent dessert options, then it may be added as “Del Sur, Mexican” and then again as “Del Sur, Desserts”.

**Choosing items from a list:** This is the real essence of the Choice Concierge service. The concierge will ask you to select a list and then will provide the category groups (column headers) to choose from, if there are more than two on the list. (If there are only 2 categories, then the category selection is not necessary and it skips that step.) Once a category is selected (or automatically selected), the list of available options will be shown for that category in alphabetical order (and no duplicates). For example, using the Restaurants list, the category "Style" would provide a list of restaurant styles like "Americana, BBQ, Burgers, Chinese, Desserts, Mexican", from which the user should type into the prompt one of those styles. If the user types, “Mexican,” the concierge will then provide the names of the Mexican restaurants on the list, in alphabetical order. At this point, the service will ask if you would like the service to select from this list at random. After providing a random selection, the service will ask if this choice was satisfactory or if you would like it to choose again, and it will continue to choose at random from the selection until you are satisfied.

**Deleting a list:** The option also exists to delete a list if it's not wanted anymore. The concierge will prompt once to make sure that you really do want to delete the list. If you say "yes," then the list will be deleted.

#### Considered but not implemented:

The choice to be able to make changes to an existing list or an item on an existing list has not yet been developed. If this program was to be used more extensively, then the option would be recommended. But at this point, the changes can be made directly into the .csv files as needed, and adding functionality is adding more time than the student-programmer would prefer to be spending at the moment.

Additionally, adding shortcuts to the user input choices, where they could identify the selection with a number next to the choices instead of typing in exactly the exact wording would also make for a better, less error-prone user experience. But the student-programmer has not yet allocated the time for this refinement.

If the student-programmer had further education on it, she would prefer the option of buttons instead of typed-out options for most of the user choices, but she doesn’t know how to do that yet.

The option to have ranked options and sort by those, and not only by the name of the item alphabetically, is also outside of the scope of this project at the moment. But it would be an interesting addition to have, for example, a restaurant price scale or a favorites ranking, and then be able to sort the lists by those choices, if desired. This would go hand-in-hand with making changes to existing items on the list, which is not a current capability.

The student-programmer is also a big fan of personal metrics, and would like it if the concierge kept track of the selections that were chosen, when those options were chosen, and how many times those options are chosen, compared to the options that are not chosen. But that’s getting too much into the weeds of minutia for this type of project and she doesn’t have the time nor inclination when she could instead be eating Oreo fried ice cream at Del Sur.
