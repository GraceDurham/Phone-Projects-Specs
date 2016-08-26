# contacts_manager.py
import contact

def main():
	new_contacts = []
	first_name = raw_input("What is your first name?")
	last_name = raw_input("What is your last name?")
	mobile = raw_input("What is your mobile?")
	email = raw_input("What is your email?")

	js = contact.Contact(first_name, last_name, mobile, email)
	new_contacts.append(js)

	for contact_object in new_contacts:
		print contact_object.first_name
		print contact_object.last_name
		print contact_object.mobile_number
		print contact_object.email

if __name__ == '__main__':
	main()