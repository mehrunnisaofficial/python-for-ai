email = input("Enter your email: ").strip()

# checking is the user enter valid emial or not
# more general 

if '@' in email:        # this more general can work but there is so many break cases here if u enter only @ this than this also valid email according to our code
    print("Valid")
else:
    print("Invalid")


# another is we can check . too
# break cases @.   , $%^&*@. ,  Hello@.   , sjd@kd.jdl@
if ('@' in email) and ('.' in email):
    print("Valid")
else:
    print("Invalid")


# more detail is using split
# still there is break cases
# for example hello@.   

username, domain = email.split("@")

if (username) and ('.' in domain):
    print("Valid")
else:
    print("Invalid")


if (username) and (domain.endswith(".edu")):
    print("Valid")
else:
    print("Invalid")

# breakcases __@.edu  
# but if we go by like this it will take years to check whether the email is valid or not
# thats why we gonna use regular expression regex