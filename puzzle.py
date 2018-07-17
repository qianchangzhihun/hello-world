# This is a interesting code to help you forget your troubles

from sys import argv

script, user_name = argv
prompt = '>'

print "%s,Do you have troubles in your daily life?" % user_name
print "yes or no?"
ans1 = raw_input(prompt)


if ans1 == "yes":
    print "Can you fix it by yourself? %s" % user_name
    print "yes or no?"
    ans2 = raw_input(prompt)
    if ans2 == "yes":
        print "TMD! Why do you need to worry about it?" 
    else:
        print "TMD! Why do you need to worry about it?" 
else:
    print "TMD! Why do you need to worry about it?" 
