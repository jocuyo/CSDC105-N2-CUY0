 # Author          : Josephine Cuyo
 # Course and Year : 2nd Year BS-IT
 # Filename        : cuyo_e3.py
 # Description     : Python program that accepts two arguments, the activity or sector and the quarantine classification, that prints the corresponding restriction to the corresponding arguments.
 # Honor Code      : I have not given nor received any unathorized help in
 #                   completing this exercise. I am also well aware of the 
 #                   policies stipulated in the AdNU student handbook.

program = input("Usage: ")
first = input("Activity or sector: ")
second = input("Quarantine classification: ")

if (program == './cuyo_e3.py'):         # program name
    if (first == 'people' or first == 'People' or first == 'PEOPLE'):       # for the people
        if (second == 'ecq' or second == 'Ecq' or second == 'ECQ'):         # quarantine classification
            print("100% stay at home except for workers in offices or industries permitted to operate")
        elif (second == 'mecq'or second == 'Mecq' or second == 'MECQ'):
            print("100% stay at home\n", "Restricted movement, only for accessing essential goods and services\n", "Exception for workers in offices or industries permitted to operate\n", "Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home\n")
        elif (second ==  'gcq'or second == 'Gcq' or second == 'GCQ'):
            print("Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home")
        elif (second == 'mgcq'or second == 'Mgcq' or second == 'MGCQ'):
            print("Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home")
        else:
            print("Error: Invalid input")

    elif (first == 'transport' or first == 'Transport' or first == 'TRANSPORT'):    # for transportation
        if (second == 'ecq' or second == 'Ecq' or second == 'ECQ'):     # quarantine classification
            print("No domestic flights, with limited international flights\n", "Public transportation is not allowed\n", "Shuttle services for employees of permitted offices or establishments, as well as point-to-point transport service, granted permission to operate by the government, with healthcare workers and other frontliners given priority\n")
        elif (second == 'mecq'or second == 'Mecq' or second == 'MECQ'):
            print("No domestic flights, with limited international flights\n","Controlled inbound flights\n", "No inter-island travel\n", "Public transportation is not allowed\n","Private transportation such as company shuttles and personal vehicles allowed subject to the guidelines provided by the Department of Transportation (DOTr)\n", "Biking and non-motorized transport encouraged\n")
        elif (second ==  'gcq'or second == 'Gcq' or second == 'GCQ'):
            print("Public transport is allowed with strict social distancing\n", "Inter-island travel from GCQ to GCQ allowed with safety protocols\n")
        elif (second == 'mgcq'or second == 'Mgcq' or second == 'MGCQ'):
            print("Public transport is allowed with strict social distancing\n", "Inter-island travel from GCQ to GCQ allowed with safety protocols\n")
        else:
            print("Error: Invalid input")

    elif (first == 'gatherings' or first == 'Gatherings' or first == 'GATHERINGS'):     # for gatherings
        if (second == 'ecq' or second == 'Ecq' or second == 'ECQ'):                     # quarantine classification
            print("Mass gatherings are not allowed\n", "Only mass gatherings that are essential for the provision of government services or authorized humanitarian activities permitted\n")
        elif (second == 'mecq'or second == 'Mecq' or second == 'MECQ'):
            print("Highly restricted (maximum of 5)\n","Non-essential work gatherings are prohibited\n")
        elif (second ==  'gcq'or second == 'Gcq' or second == 'GCQ'):
            print("Gatherings are limited to not more than ten (10) persons\n","Non-essential work gatherings are prohibited\n")
        elif (second == 'mgcq'or second == 'Mgcq' or second == 'MGCQ'):
            print("Fifty percent (50%) of the seating or venue capacity for movie screenings, concerts, sporting events, and other entertainment activities, religious services, and work conferences\n")
        else:
            print("Error: Invalid input")               # if argument cannot be found
    
    elif (first == 'schools' or first == 'Schools' or first == 'SCHOOLS'):          # for schools
        if (second == 'ecq' or second == 'Ecq' or second == 'ECQ'):                 # quarantine classification
            print("School premises are closed")
        elif (second == 'mecq'or second == 'Mecq' or second == 'MECQ'):
            print("School premises are closed")
        elif (second ==  'gcq'or second == 'Gcq' or second == 'GCQ'):
            print("Skeletal workforce permitted in schools\n","Face-to-face or in-person classes are suspended\n")
        elif (second == 'mgcq'or second == 'Mgcq' or second == 'MGCQ'):
            print("Limited face-to-face or in-person classes may be conducted; strict compliance with minimum public health standards and consultations with local government units (LGUs) and guidelines set by the Commission on Higher Education (CHED)\n")
        else:
            print("Error: Invalid input")               # if argument cannot be found

    elif (first == 'work' or first == 'Work' or first == 'WORK'):           # for work
        if (second == 'ecq' or second == 'Ecq' or second == 'ECQ'):         # quarantine classification
            print("Select industry workers permitted")
        elif (second == 'mecq'or second == 'Mecq' or second == 'MECQ'):
            print("Essential industries permitted to work at full capacity, with others operating at a fifty percent (50%) capacity\n","Work-from-home and other flexible work arrangements encouraged")
        elif (second ==  'gcq'or second == 'Gcq' or second == 'GCQ'):
            print("Alternative work arrangements")
        elif (second == 'mgcq'or second == 'Mgcq' or second == 'MGCQ'):
            print("Full operating capacity for work in all public and private offices\n","Alternative work arrangements for persons who are sixty (60) years old and above, or those with other health risks\n")
        else:
            print("Error: Invalid input")           # if argument cannot be found

    elif (first == 'government' or first == 'Government' or first == 'GOVERNMENT'):        # for government
        if (second == 'ecq' or second == 'Ecq' or second == 'ECQ'):                         # quarantine classification
            print("Skeletal workforce onsite\n","Work from home arrangements\n")
        elif (second == 'mecq'or second == 'Mecq' or second == 'MECQ'):
            print("Skeletal workforce onsite\n","Work from home arrangements\n")
        elif (second ==  'gcq'or second == 'Gcq' or second == 'GCQ'):
            print("Work in all government offices under alternative work arrangements\n")
        elif (second == 'mgcq'or second == 'Mgcq' or second == 'MGCQ'):
            print("Work in government offices may be at full operational capacity, or under alternative work arrangements\n")
        else:
            print("Error: Invalid input")       # if argument cannot be found

    else:
        print("Error: Invalid input")           # if argumrnt cannot be found

else:                   # if argument cannot be found
    print("Error: Invalid input")

