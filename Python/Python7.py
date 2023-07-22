email = input("Enter email address: ")
at_index = email.index("@")
company_name = email[at_index+1:]
company_name = company_name[:-4]
print("Company name:", company_name)
