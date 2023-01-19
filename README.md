# Bulk Email Verifier

Verify the existence and activity of email accounts/addresses.

## Prerequisites

[Python 3.7+](https://www.python.org/downloads/) required.
`verify_email` module required.

## Usage
 1. Do `pip install verify_email` in the project directory if not done
    already.
 2. Insert all email addresses to be verified in `emails.txt`. **Make sure that the emails are all spelled correctly and each email is separated be a new line with no additional characters or spaces at the end or beginning of each line.** The project comes with example emails in `emails.txt` as an example on how exactly they should be formatted.
 3. Run `python main.py` and wait until the process is complete. The output is in the newly created file `res.txt` after the process is completed. **The file will be updated at the end of the whole process and each result is not appended live right after each email is verified.**
