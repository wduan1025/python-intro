# Given a list of email addresses, count the number of 
# each email provider by taking the suffix of the email
# address, and calculate the share of markets that this 
# email provider comprises

emails = ["george@gmail.com", "jason@outlook.com", "deborah@outlook.com", "andrea@outlook.com", "max@gmail.com", "peter@gmail.com", "sherry@yahoo.com", "rod@outlook.com"]
# Initialize the email_provider_name : number_of_occurance dictionary
mail_count = dict()
for mail in emails:
    # Split email address with "@"
    name_and_email = mail.split("@")
    # Get the second element of the obtained by the split() function, it's the email provider's name
    email_provider = name_and_email[1]
    # See if it exists in the dictionary. If exists, increment it's value by 1; if not, initialize
    # it's value to 1
    if email_provider in mail_count:
        mail_count[email_provider] += 1
    else:
        mail_count[email_provider] = 1

# Print the result according to mail_count dictionary, in a form similar to 
# outlook.com comprises xxx of the email market
# gmail.com comprises yyy of the email market
# etc.
for mail, count in mail_count.items():
    print("{email} comprises {ratio} of the email market".format(email=mail, ratio=count/len(emails)))