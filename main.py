# emails.txt contains all emails to check for its validility. res.txt will contain the result of the validility check.
# Please seperate all emails in emails.txt by a new line with no additional characters

# If error is given, in project directory, use 'pip install verify_email' in shell
from verify_email import verify_email

# Clear contents of output file
open('res.txt', 'w').close()

# Initialize I/O files
rawEmails = open('emails.txt', 'r').read().split('\n')
isValidEmails = open('res.txt', 'a')

# Loop through each email in input file
for x in range(0, len(rawEmails)):
	# Write each emails valid status into output file
	isValidEmails.write(rawEmails[x] + ': ' + str(verify_email(rawEmails[x])) + '\n')

	# Print percentage of completion by dividing current email with total amount of emails and print current email (ex. 0.1% - 1. 0.1% = 10%, with '- 1' being the first email)
	prnt = str(x / len(rawEmails))[:4] + '% - ' + str(x + 1)
	print(prnt)

print('-----COMPLETE-----')

# Save/close file
isValidEmails.close()
