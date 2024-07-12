# Task 1: Email Extraction Enhancement
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, extraexample3@gmail.com"
# By ?! essentially means to print all except for where exclude is mentioned in the email. {2,6} gives a range for the domain so that we can't have one shorter than
# 2 characters and can't have one longer than 6. .co is the shortest example and .letter would be an example of the longest. Obviously not a domain but yeah.
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@(?!exclude)\b[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b', text) 
print(emails)
