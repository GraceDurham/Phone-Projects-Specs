class Contact(object):
	def __init__(self, first_name, last_name,
				 mobile_number = "", email = "", 
				 work_number = ""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile_number = mobile_number
		self.email = email
		self.work_number = work_number

	def send_text(self):
		print "To: %s - Hello! How are you?" %  (self.mobile_number) 



def main():
	contact_jen = Contact("Jennifer", "Kim", mobile_number = "333-333-3333")
	contact_Stephanie = Contact("Stephanie","Boyette")
	contact_js = Contact("Jenn", "Boyette", mobile_number = "555-555-5555")

	contact_list = []
	contact_list.append(contact_jen)
	contact_list.append(contact_Stephanie)
	contact_list.append(contact_js)
	
	# print contact_list

	# print contact_Stephanie.first_name

	for contact_object in contact_list:
		print contact_object.first_name
		print contact_object.last_name
		contact_object.send_text()

print __name__

if __name__ == '__main__':
	main()