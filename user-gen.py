import sys
import re
# defined a function called checkargs. It looks at the system arguments passed at the CLI. IF there isn't at least 2 arguments then it shows the usage. If its more than 3, ti also shows an error and exits cleanly. 

# this takes the ppervious version and adds the ability to append an email to the names using the CLI
# NOV 20 11:51PM -  added ful_email, and luf_email.  This is underscores between names
#nov 20 12:17 made edits to tool menu. added lazy approach to adding - to CLI argument selection.
#NOV 21 2013: 145AM-  Adding lowercase support to all lists
# nov 21 - 242AM- added additional error correction for domain.  must contain @ and contain at leat 3 characters
def checkargs():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print "Target UserName Generator  ( TUG )  v06"
        print  "  "
        print "usage:  %s names.txt -FLAG [@email.com]" % (sys.argv[0])
        print "        "
        print  " GENERATE LIST WITHOUT EMAIL"
        print  " -lnfn  is  LastnameFirstname  -- DoeJohn"
        print  " -fnln  is FirstnameLastname  -- JohnDoe"
        print  " -filn  is FirstinitialLastname -- JDoe"
        print  " -lifn  is LastinitialFirstname -- DJohn "
        print  " -fdl   is firstname DOT lastname -- John.Doe " 
        print  " -ldf   is lastname DOT firstname -- Doe.John "
        print  " -ful   is firstname _ lastname -- John_Doe "
        print  " -luf   is lastname _ firstname -- Doe_John "
        print  " -all   prints all combinations -- ALL "
        print  "  "
        print  "example:  %s names.txt -FLAG" % (sys.argv[0])
        print   "    "
        print  " GENERATE LIST WITH EMAIL  "
        print   "-lnfn_email   is LastNameFirstname@acme.com -- doejohn@acme.com"            
        print   "-fnln_email   is FirstNameLastName@acme.com -- johndoe@acme.com"
        print   "-filn_email   is FirstInitialLastname@acme.com  -- jdoe@acme.com"
        print   "-lifn_email   is LastInitialFirstname@acme.com  -- djohn@acme.com"
        print   "-fdl_email    is Firstname DOT Lastname@acme.com --  john.doe@acme.com"
        print   "-ldf_email    is Lastname DOT Firstname@acme.com -- doe.john@acme.com"
        print   "-ful_email    is Firstname_Lastname@acme.com  --  john_doe@acme.com"
        print   "-luf_email    is Lastname_firstname@acme.com  --  doe_john@acme.com "
        print   "-all_email    is ALL NAMING CONVENTIONS @acme.com ---- "
        print    "  " 
        print  "example  %s names.txt -FLAG_email @acme.com" % (sys.argv[0])
        print  "   "
        print  "NOTE: Input text file should be in 'firstname lastname' format. Only tested on linux text files."
        sys.exit(0)
checkargs()




# nov 21 12:44AM - added this error check if user entered  (python script.py 1)
def checkinputfile():
    if len(sys.argv[1]) < 4:
        print "ERROR WITH INPUT FILE.   Usage: %s inputfile.txt FLAGS (email)" % (sys.argv[0]) 
        sys.exit(0)
checkinputfile()

# NOV 21 2013- 1:19am-  Decided to add a basic ERROR check for the domain when its used
def checkdomain():
    if len(sys.argv[3]) < 5 or len(sys.argv[3]) ==0:
        print "ERROR WITH DOMAIN NAME.  TOO SHORT--"
        sys.exit(0)  # had to add this exit command or it would keep going and not print the code
#checkdomain() # caused errors with only generating user list and domain didnt exist
# ended up adding checkdomain() in the actual function call so its only called if domain is specificed.

#print sys.argv[3]

# funtion to open a file passed at the command line. This is a text files with (firstname lastname). Its opened in 'r' (read only)
def call_lnfn():
    f = open(sys.argv[1], 'r')
    for line in f:
        first_name, last_name = line.strip().split()
        print (first_name.lower()) + (last_name.lower()) # NOV 21-1242AM-  added lower functonality
       #print(s.lower())
def call_fnln():
    f = open(sys.argv[1], 'r')
    for line in f:
        first_name, last_name = line.strip().split()
        print (last_name.lower()) + (first_name.lower())

def call_filn():
    f = open(sys.argv[1], 'r')
    for line in f:
        first_name, last_name = line.strip().split()
        print (first_name[0].lower()) + (last_name.lower())

def call_lifn():
    f = open(sys.argv[1], 'r')
    for line in f:
        first_name, last_name = line.strip().split()
        print (last_name[0].lower()) + (first_name.lower())

def call_all():
    f = open(sys.argv[1], 'r')
    for line in f:
        first_name, last_name = line.strip().split()
        print (first_name.lower()) + (last_name.lower())
        print (last_name.lower()) + (first_name.lower())
        print (first_name[0].lower()) + (last_name.lower())
        print (last_name[0].lower()) + (first_name.lower())

def call_fdl():
    f = open(sys.argv[1], 'r')
    for line in f:
        first_name, last_name = line.strip().split()
        print (first_name.lower()) + "." + (last_name.lower())    

def call_ldf():
    f = open(sys.argv[1], 'r')
    for line in f:
        first_name, last_name = line.strip().split()
        print (last_name.lower()) + "." + (first_name.lower())

def call_ful():
    f = open(sys.argv[1], 'r')
    for line in f:
       first_name, last_name = line.strip().split()
       print (first_name.lower()) + "_" + (last_name.lower())

def call_luf():
    f = open(sys.argv[1], 'r')
    for line in f:
       first_name, last_name = line.strip().split()
       print (last_name.lower()) + "_" + (first_name.lower())
# END standard username funtions



# start email functions
def call_lnfn_email():
    checkdomain()
    f = open(sys.argv[1], 'r')
    for line in f:
        first_name, last_name = line.strip().split()
        print (last_name.lower()) + (first_name.lower()) + sys.argv[3] 

def call_fnln_email():
     checkdomain()
     f = open(sys.argv[1], 'r')
     for line in f:
        first_name, last_name = line.strip().split()
        print (first_name.lower()) + (last_name.lower()) + sys.argv[3]

def call_filn_email():
     checkdomain()
     f = open(sys.argv[1], 'r')
     for line in f:
        first_name, last_name = line.strip().split()
        print (first_name[0].lower()) + (last_name.lower()) + sys.argv[3]

def call_lifn_email():
     checkdomain()
     f = open(sys.argv[1], 'r')
     for line in f:
        first_name, last_name = line.strip().split()
        print (last_name[0].lower()) + (first_name.lower()) + sys.argv[3]

def call_fdl_email():
     checkdomain()
     f = open(sys.argv[1], 'r')
     for line in f:
        first_name, last_name = line.strip().split()
        print (first_name.lower()) + "." + (last_name.lower()) + sys.argv[3]

def call_ldf_email():
     checkdomain()
     f = open(sys.argv[1], 'r')
     for line in f:
       first_name, last_name = line.strip().split()
       print (last_name.lower()) + "." + (first_name.lower()) + sys.argv[3]

def call_all_email():
    checkdomain() 
    f = open(sys.argv[1], 'r')
    for line in f:
       first_name, last_name = line.strip().split()
       print (last_name.lower()) + (first_name.lower()) + sys.argv[3]
       print (first_name.lower()) + (last_name.lower()) + sys.argv[3]
       print (first_name[0].lower()) + (last_name.lower()) + sys.argv[3]
       print (last_name[0].lower()) + (first_name.lower()) + sys.argv[3]
       print (first_name.lower()) + "." + (last_name.lower()) + sys.argv[3]
       print (last_name.lower()) + "." + (first_name.lower()) + sys.argv[3]

def call_ful_email():
    checkdomain()
    f = open(sys.argv[1], 'r')
    for line in f:
       first_name, last_name = line.strip().split()
       print (first_name.lower()) + "_" + (last_name.lower()) + sys.argv[3]

def call_luf_email():
    checkdomain()
    f = open(sys.argv[1], 'r')
    for line in f:
       first_name, last_name = line.strip().split()
       print (last_name.lower()) + "_" + (first_name.lower()) + sys.argv[3]




# start logic that looks at the cli argumment passed to determine which list combination to print
#@nov 20 2013-  lazy coder approach.  added "-" in front on names instead of making a real menu.
#nov 21 1:15AM - decided to fix my lazy approach and also add both  flag and -flag.
def logic():
    if sys.argv[2] == "-lnfn":
            call_lnfn()
    elif sys.argv[2] == "lnfn":
            call_lnfn()
    elif sys.argv[2] == "-fnln":
         call_fnln() 
    elif sys.argv[2] == "fnln":
            call_fnln()
    elif sys.argv[2] == "-filn":
            call_filn()
    elif sys.argv[2] == "filn":
            call_filn()
    elif sys.argv[2] == "-lifn":
            call_lifn()
    elif sys.argv[2] == "lifn":
            call_lifn()
    elif sys.argv[2] == "-all":
            call_all()
    elif sys.argv[2] == "all":
            call_all()
    elif sys.argv[2] == "-fdl":
            call_fdl()
    elif sys.argv[2] == "fdl":
            call_fdl()
    elif sys.argv[2] == "-ldf":
            call_ldf()
    elif sys.argv[2] == "ldf":
            call_ldf()
    elif sys.argv[2] == "-ful":
            call_ful()
    elif sys.argv[2] == "ful":
            call_ful()
    elif sys.argv[2] == "-luf":
            call_luf()
    elif sys.argv[2] == "-luf":
            call_luf()
    elif sys.argv[2] == "-lnfn_email":
            call_lnfn_email()
    elif sys.argv[2] == "lnfn_email":
            call_lnfn_email()
    elif sys.argv[2] == "-fnln_email":
            call_fnln_email()
    elif sys.argv[2] == "fnln_email":
            call_fnln_email()
    elif sys.argv[2] == "-filn_email":
            call_filn_email()
    elif sys.argv[2] == "filn_email":
            call_filn_email()
    elif sys.argv[2] == "-lifn_email":
            call_lifn_email()
    elif sys.argv[2] == "lifn_email":
            call_lifn_email()
    elif sys.argv[2] == "-fdl_email":
            call_fdl_email()
    elif sys.argv[2] == "fdl_email":
            call_fdl_email()
    elif sys.argv[2] == "-ldf_email":
            call_ldf_email()
    elif sys.argv[2] == "ldf_email":
            call_ldf_email()
    elif sys.argv[2] == "-all_email":
            call_all_email()
    elif sys.argv[2] == "all_email":
            call_all_email()
    elif sys.argv[2] == "-ful_email":
            call_ful_email()
    elif sys.argv[2] == "ful_email":
            call_ful_email()
    elif sys.argv[2] == "-luf_email":
            call_luf_email()
    elif sys.argv[2] == "luf_email":
            call_luf_email()
    elif len(sys.argv[2]) == 1:
        print "INVALID CONVERSION TYPE FLAG.....Bro "
    else:
        print "ERROR 5: UNKNOWN FLAG.  Try using -FLAG"
        sys.exit(0)
logic()
