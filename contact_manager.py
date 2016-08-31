import contact 



contacts_list = []


def add_new_contact(first_name, last_name):
	new_contact = contact.Contact(first_name, last_name,
				 mobile_number = "", email = "", 
				 work_number = "")
	contacts_list.append(new_contact)
	first_name=first_name.upper().strip
	for info in contacts_list:
		if first_name == info.first_name and last_name == info.last_name:
			print "Error! Contact already exists!"


    # handle cases and whitespace for name parameters
    # handle if contact_list is empty
    # iterate contact_list, check if contact already exists, print error
    # instantiate instance of Contact
    # add to contacts_list

def find_contact(first_name, last_name):
	for contact in contacts_list:
		if contact.first_name == first_name and contact.last_name == last_name:
			return contact
	return None

def edit_exiting_contact(first_name, last_name,
				 mobile_number = "", email = "", 
				 work_number = ""):
	item = find_contact(first_name, last_name)
	if item in contacts_list:
		item.first_name = first_name
		item.last_name = last_name
		item.mobile_number = mobile_number
		item.email = email
		item.work_number = work_number


	 




def delete_contact(first_name, last_name):
    # if not contacts_list:
    item = find_contact(first_name, last_name)
    if item in contacts_list:
    	contacts_list.remove(item)


def current_contact_list():
    # todo: return a sorted list of objects from contacts_list
    for info in contacts_list:
    	print info.first_name, info.last_name
    	# print info.__dict__



# def write_contacts_to_file():
#     pass


# def read_contacts_from_file():
#     pass


def main():
    # test add new contact
    # test edit contact
    # test delete contact
    # test show all contacts
    add_new_contact("Jon", "Snow",)
    add_new_contact("little", "finger")
    print contacts_list
    current_contact_list()
    delete_contact("little", "finger")
    print contacts_list
    edit_exiting_contact("Jon", "Snow", "555-555-5555")
    print contacts_list[0].mobile_number



if __name__ == '__main__':
	main()
