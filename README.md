My first line of code is to import re because I will utilize regular expressions to enter emails and phone numbers. I then define an empty list, conatct_list = {} for storage later and define next_id = 1 as a counter to help with unique identifiers.

Next, I work on the main () function and begin a while loop. Afterward, the while loop begins, the print() displays the menu. Then, the user can input their selection by selecting the corresponding number from the menu. 

Though I didn't set the input to an int type, my try/except block will return a message that the choice must be between 1 and 8.

The next function is add_contact(). This function allows the user to input a name, phone, email, and additional info. This function continues with an if statement which calls a separate function to validate the phone and email. Using Regex, the input is checked against the validation rules and if either phone OR email does not comply, a message is displayed, alerting the user that one or the other is invalid, and try again.

If everything passes that checkpoint, the information is added to my contact_list dictionary with a unique identifier number. Afterward, a message is displayed to show that the Contact {name} with the {next_id} is added. The next_id counter goes up by one to avoid duplicates. 

The next block of code is the edit_contact() function. This allows the user to call the contact information to edit by inputting their unique id number. I use a try/except block to prevent crashing the program if invalid data is entered. 

TThe unique id/contact is checked in the contact_list and then proceeds to allow the user to write over the prior data. The phone and email are checked again for proper validation using the regex rules. If all is proper, a confirmation message is displayed.

The next function is delete_contact(). Simply deleted the contact info and the linked unique identifying from the contact_list.

search_contact() with call the conact information linked to the unique identiifer. and then print the contact info.

find_all_contacts() will print the full list of contacts and their info.

export_contact() will allow the user to save their contacts to a text file The user will input what the want the filename to be. I utilize regex validations and the "with" for better reliablitity in opening and closing the document. 

import_contact() will bring an external file into the contact list and give it a unique identifying number for reference.




