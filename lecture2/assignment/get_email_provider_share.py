# Given a list of email addresses, count the number of 
# each email provider by taking the suffix of the email
# address, and calculate the share of markets that this 
# email provider comprises

emails = ["george@gmail.com", "jason@outlook.com", "deborah@outlook.com", "andrea@outlook.com", "max@gmail.com", "peter@gmail.com", "sherry@yahoo.com", "rod@outlook.com"]
# Initialize the email_provider_name : number_of_occurance dictionary
mail_count = dict()
for mail in emails:
    # Split email address with "@"
    # YOUR CODE HERE
    # Get the second element of the obtained by the split() function, it's the email provider's name
    # YOUR CODE HERE
    # See if it exists in the dictionary. If exists, increment it's value by 1; if not, initialize
    # it's value to 1
    # YOUR CODE HERE

# Print the result according to mail_count dictionary, in a form similar to 
# outlook.com comprises xxx of the email market
# gmail.com comprises yyy of the email market
# etc.
# YOUR CODE HERE