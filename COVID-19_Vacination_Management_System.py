# Function to register patients
def new_patient_registration():
    # opens the 'patient.txt' file to see how many patients have registered to be used as their patient ID
    with open('patient.txt') as patient_file:
        words = patient_file.readlines()
        if len(words) == 0:
            count = 1
        else:
            lst = []
            for lines in words:
                lst.append(lines)
            count=len(lst)+1
    print('\n'+'='*100)
    # gets the patient's contact number and also works as a sentinel control loop to see if they want to continue or not
    patient_contact = str(input('\nEnter your contact number(enter -1 to exit): '))
    if patient_contact != '-1':
        while patient_contact != '-1':
            # Initializes the vaccine name to an empty string
            vaccine_name= ''
            # Verifies the contact number entered by the patient based of the length of the phone number
            while True:
                if len(patient_contact)<8 or len(patient_contact)>13:
                    patient_contact= str(input('\nPlease enter a valid contact number. For example, 017XXXXXXX [enter -1 to exit]: '))
                    continue
                break
            email = str(input('\nEnter your email: '))
            # Verifies the email of the patient, this is because all email addresses have the letter '@'
            while '@' not in email:
                email= str(input('\nPlease enter a valid email address: '))
            # gets patient's vaccine center of choice
            choice = input('\nWhich vaccination center would you like to go to? Enter 1 if you would like to go to Vaccination Center 1 and enter 2 if you would like to go to Vaccination Center 2 : ')
            # Ensures that patient only enters 1 or 2
            while choice != '1' and choice != '2':
                choice = input('\nPlease enter the number 1 for VC1 or enter the number 2 for VC2. Do not enter letters, words or sentences : ')
            vc_chosen = choice
            # gets patient name
            name = str(input('\nEnter your name: '))
            # Verifies patient name by the length of the name, if the patient enters nothing, then they would have to enter again
            while len(name)==0:
                name = str(input('\nPlease enter your real name: '))
            # Verifies the age of the patient by using a loop and also ensures that the patient does not enter arbitrary age number.
            while True:
                try:
                    ask_age=int(input('\nEnter your age: '))
                    if ask_age <= 0: 
                        continue
                    elif ask_age>122:
                        print('\nThe oldest person alive is only 122 years old. Please enter a valid age')
                        continue
                    break
                except:
                    continue
            age = ask_age
            # shows the patient the option of the vaccine they can choose from their age
            if age > 45:
                while vaccine_name != 'AF' and vaccine_name != 'BV' and vaccine_name != 'DM' and vaccine_name != 'EC' :
                    vaccine_name= input(f"\nYour vaccine options are 'AF', 'BV', 'DM' or 'EC'. Enter your vaccine code of choice: ")
                    vaccine_name = str(vaccine_name.upper())
            elif age >= 18 and age <= 45:
                while vaccine_name != 'AF' and vaccine_name != 'BV' and vaccine_name != 'CZ'  and vaccine_name != 'DM' and vaccine_name != 'EC' :
                    vaccine_name= input(f"\nYour vaccine options are 'AF', 'BV', 'CZ', 'DM' or 'EC'. Enter your vaccine code of choice: ")
                    vaccine_name = str(vaccine_name.upper())
            elif age >= 12 and age <18:
                while vaccine_name != 'AF':
                    vaccine_name= input(f"\nYour vaccine options are 'AF'. Enter 'AF' if you wish to receive the 'AF' vaccine: ")
                    vaccine_name = str(vaccine_name.upper())
            else:
                print(f"\nYou are too young and not eligible to receive the vaccine")
            vaccine_chosen = vaccine_name
            # gets patient height
            if age>=12:
                while True:
                    try:
                        ask_height=float(input('\nEnter your height in meters: '))
                        break
                    except:
                        continue
                height= ask_height
                # gets patient weight while ensuring they don't enter arbitrary weight number such as 1000kg. Because it doesn't make sense for a human weight a ton.
                while True:
                    try:
                        ask_weight=float(input('\nEnter your weight in kilograms: '))
                        if ask_weight<25:
                            print('\nYour weight shows that you are severely underweight')
                            print("\nIn that case you can't receive the vaccine unless you enter your proper weight in kilograms")
                            continue
                        elif ask_weight>600:
                            print('\nYou are severely overweight')
                            print('\nEven the heaviest man alive is only 595kg, Please enter your actual weight in kilograms')
                            continue
                        break
                    except:
                        continue
                weight= ask_weight
                blood_type = ''
                # gets and verifies patient blood type based of the 4 existing blood type
                while blood_type != 'A' and blood_type !='B' and blood_type !='AB' and blood_type !='O':
                    get_blood = input('\nEnter your bloodtype(A, B, AB or O): ')
                    blood_type = get_blood.upper() 
                # adds leading zeroes to the number of the patient until its 8 digits long. For example, if the patient number is 5, then the string output would be 00000005
                idNum = str(count).zfill(8) 
                # shows the patient their unique id number
                print(f"\nYour unique ID number is {idNum}.")
                # increases the counter that counts the number of patient by 1
                count+=1
                # appends the information of the patient to the 'patient.txt' file
                with open('patient.txt','a') as patient_file:
                    patient_file.write(f"Patient ID Number: {idNum}, Vaccination Center chosen: {vc_chosen}, Vaccine chosen: {vaccine_chosen}, Patient Name: {name}, Patient Contact Number: {patient_contact}, Patient Email: {email}, Patient blood type: {blood_type}, Patient Height: {height}m, Patient Weight: {weight}kg")
                    patient_file.write("\n")
            print('\n'+'='*100)
            # asks for the next patient's contact number
            patient_contact = str(input('\nEnter your contact number(enter -1 to exit): '))
            # option when the patient does not want to continue registering
    if patient_contact == '-1':
        print('\nThank you for registering, have a nice day\n')

# import date, timedelta and datetime from the datetime module
from datetime import date, timedelta, datetime

# function that administers vaccine to patients
def vaccine_administration():
    # blank_vaccination_file is a variable that is set to false at first
    # the purpose of this variable is to determine whether the 'vaccine.txt' file is empty or not
    # If it's empty then this function will transfer all the patient data from the 'patient.txt' file into the 'vaccination.txt' file
    # However if it's not empty then the function will use the data from 'vaccine.txt' file, sort it, add new data about the patient's vaccination details and transfer it into the 'vaccination.txt' file
    blank_vaccination_file = False
    with open('vaccination.txt','r') as vaccine_file:
        if vaccine_file.read() == '':
            blank_vaccination_file = True
    print('\n'+'='*100)
    # this is the empty list in which the data of the patient taken from the 'vaccination.txt' will be appended to
    vaccine_info_lst=[]
    # Opens the 'patient.txt' file and make each data obtained more readable by using built-in methods such as replace and split
    with open('patient.txt') as patient_file:
        for line in patient_file.readlines():
            newline = line.replace(',','')
            vaccine_info_lst.append(newline.split())
    # gets the patient's patient ID and ensures that patient does not type random words
    while True:
        try:
            get_patient_id = int(input('\nEnter your patient ID(enter -1 to exit): '))
            break
        except:
            continue
    while get_patient_id != -1:
        # a function that will be used to determine the date of either the patient's first dose or the upcoming next dose. 
        def time_for_vaccine(x):
            end_date = date.today() + timedelta(days = x)
            return end_date
        while True: 
            # determines whether the id entered by the patient matches the id that has been recorded in the 'patient.txt' file
            # If it doesn't match then the patient would have to enter their right patient id, if they can't remember or don't want to continue, they can exit by entering '-1'
            patient_id = str(get_patient_id).zfill(8)
            patient_present = False
            for i in range(len(vaccine_info_lst)):
                if patient_id in vaccine_info_lst[i]:
                    vaccine_chosen = vaccine_info_lst[i][10].replace(',','')
                    vaccine_center = vaccine_info_lst[i][7].replace(',','')
                    # remembers the index location of the patient
                    patient_index = i
                    patient_present = True
                    break
            if patient_present == True:
                break
            else:
                try:
                    get_patient_id = int(input('\nPlease enter a valid patient ID. If you do not have a patient ID, please register first(enter -1 to exit): '))
                    continue
                except:
                    continue 
        # tells the patient their patient id and what vaccine they have selected when they registered
        print(f"\nYour patient ID is {patient_id} and you have selected the {vaccine_chosen} vaccine")
        # gets the current date and turns it into a readable string
        today_date_string = datetime.strftime(datetime.now(),'%A, %d %B, %Y' )
        # when the patient's vaccine chosen isn't EC, the function asks the patient if they are selecting their first or second dose
        if vaccine_chosen != 'EC':
            get_dose_number = input('\nIs the vaccine that you are seeking to take your first dose or second dose? (Type 1 for first or 2 for second): ')
            while get_dose_number != '1' and get_dose_number != '2':
                get_dose_number = input('\nEnter 1 if you are seeking to take your first dose and enter 2 if you are seeking to take your second dose: ')
            dose_number = get_dose_number
            if dose_number == '1':
                # sets the status of the patient based on the dose they selected as well as telling them information about where they are going to receive their vaccine.
                status = 'COMPLETED-D1'
                print(f"\nYou are going to receive your first dose of vaccine at vaccination center {vaccine_center}. Please proceed to vaccination center {vaccine_center} to receive your first dose of {vaccine_chosen} vaccine")
                # gets the date of the second vaccine date of the patient based of what vaccine they have selected
                if vaccine_chosen == 'AF':
                    second_vaccine_date = time_for_vaccine(14)
                elif vaccine_chosen == 'BV':
                    second_vaccine_date = time_for_vaccine(21)
                elif vaccine_chosen == 'CZ':
                    second_vaccine_date = time_for_vaccine(21)
                elif vaccine_chosen == 'DM':
                    second_vaccine_date = time_for_vaccine(28)
                # changes the date into more easily readable string
                second_vaccine_date_string= datetime.strftime(second_vaccine_date, '%A, %d %B, %Y')
                # informs the patient when and where they should take their second vaccine
                print(f"\nYou should go to vaccination center {vaccine_center} on {second_vaccine_date_string} to get your second dose of {vaccine_chosen} vaccine.")
                # appends necessary information about the vaccine to the empty list that was created above
                vaccine_info_lst[patient_index].append(today_date_string)
                vaccine_info_lst[patient_index].append(second_vaccine_date_string)
                vaccine_info_lst[patient_index].append(status)
            elif dose_number == '2':
                status= 'COMPLETED'
                # gets the date of the patient's first dose of vaccine based of their vaccine choice
                if vaccine_chosen == 'AF':
                    first_vaccine_date = time_for_vaccine(-14)
                elif vaccine_chosen == 'BV':
                    first_vaccine_date = time_for_vaccine(-21)
                elif vaccine_chosen == 'CZ':
                    first_vaccine_date = time_for_vaccine(-21)
                elif vaccine_chosen == 'DM':
                    first_vaccine_date = time_for_vaccine(-28)
                # confirms whether the patient took their first vaccine on the date that was estimated, if they didn't take it on that date, they can enter the exact date of when they took their first vaccine
                while True:
                    first_date_confirmation = input(f"\nDid you take your first vaccine on {datetime.strftime(first_vaccine_date, '%A, %d %B, %Y')}?[Type 'Y' for yes and 'N' for no]: ").upper()
                    if first_date_confirmation == 'Y' or first_date_confirmation == 'N':
                        break
                    else:
                        continue
                if first_date_confirmation == 'N':
                    while True:
                        print(f"\nPlease enter the date when you taken your first {vaccine_chosen} vaccine in the format of DD/MM/YYYY")
                        print('\nYou only need to enter the date in numbers.For example, September would be 9. ')
                        vaccine_date = int(input('\nEnter date: '))
                        vaccine_month = int(input('\nEnter month: '))
                        vaccine_year= int(input('\nEnter year: '))
                        try:
                            first_vaccine_date = datetime(vaccine_year, vaccine_month, vaccine_date)
                            break
                        except:
                            continue
                # converts date obtained from the patient into readable string
                first_vaccine_date_string = datetime.strftime(first_vaccine_date, '%A, %d %B, %Y')
                # appends all the necessary information about the vaccine to the empty list that was created above
                vaccine_info_lst[patient_index].append(first_vaccine_date_string)
                vaccine_info_lst[patient_index].append(today_date_string)
                vaccine_info_lst[patient_index].append(status)
                # informs the patient on where they are going to receive their second dose of vaccine
                print(f"\nYou are going to receive your second dose of {vaccine_chosen} vaccine at vaccination center {vaccine_center}. Please proceed to vaccination center {vaccine_center} to receive your second dose of {vaccine_chosen} vaccine")      
        else:
            # this is for the patient that has chosen the 'EC' vaccine
            # their status is automatically completed because they only need 1 dose
            status= 'COMPLETED'
            # tells them where they are going to receive their dose of EC vaccine
            print(f"\nYou are going to receive your first and final dose of EC vaccine at vaccination center {vaccine_center}. Please proceed to vaccination center {vaccine_center} to receive your {vaccine_chosen} vaccine")      
            # appends the information that are important for the vaccine to the empty list created above
            vaccine_info_lst[patient_index].append(today_date_string)
            vaccine_info_lst[patient_index].append(status)
        # create a function that sorts lists based on the 4th element in each sublist
        # the fourth element was specifically chosen because the fourth element is the patient id, and since patient id are just numbers, they can be arranged in ascending order
        def sort(lst):
            lst.sort(key = lambda x : x[2])
            return lst
        # create a list that is a sorted version of the original list
        sorted_lst = sort(vaccine_info_lst)
        # checks whether the 'vaccination.txt' file is blank or not
        if blank_vaccination_file:
            # when the 'vaccination.txt' file is empty
            with open('vaccination.txt','w') as vaccination_file:
                for lst in sorted_lst:
                    try:
                        lst[32]
                        # determine the list in the sorted list that belongs to the patient, since additional data of the patient was added to the list, the lst is longer
                        # list that doesn't belong to the patient would have a length of 31
                        if lst[10] == 'EC':
                            vaccination_file.write(f"Patient ID: {lst[3]}, Vaccine Administered: {lst[10]}, Vaccine Center: {lst[7]}, Date of final vaccine: {lst[31]}, Status: {lst[32]}")
                            vaccination_file.write("\n")   
                        else:
                            vaccination_file.write(f"Patient ID: {lst[3]}, Vaccine Administered: {lst[10]}, Vaccine Center: {lst[7]}, Date of first vaccine: {lst[31]}, Status: {lst[33]}, Date of second vaccine: {lst[32]}")
                            vaccination_file.write("\n")    
                    except:
                        vaccination_file.write(f"Patient ID: {lst[3]}, Vaccine Administered: {lst[10]}, Vaccine Center: {lst[7]}, Date of first vaccine: Not Available, Status: NEW, Date of second vaccine: Not Available")
                        vaccination_file.write("\n")    
        else:
            # this part of the code will be executed when the 'vaccination.txt' file is not empty 
            updated_vaccination_lst = []
            # opens the 'vaccination.txt' file and make the data more readable by using built in methods such as replace and split
            with open('vaccination.txt') as vaccination_file:
                for line in vaccination_file.readlines():
                    newline = line.replace(',','')
                    # the new 'vaccination.txt' lines are appended to the new empty vaccination list
                    updated_vaccination_lst.append(newline.split())
            counter = 0
            for updated_lst in updated_vaccination_lst:
                # checks whether the 3rd index of updated list in updated vaccination list contains the patient id
                if updated_lst[2] == patient_id:
                    updated_vaccination_lst.pop(counter)
                counter +=1
                    # if it contains the patient id, then all data regarding the patient will be removed as it will be replaced by a newer version of the patient's data
            # create a string about the vaccine's information and patient information based on the dose number of vaccine that the patient chose
            if vaccine_chosen != 'EC':
                if dose_number == '1':
                    administer_new_patient = f"Patient ID: {patient_id}, Vaccine Administered: {vaccine_chosen}, Vaccine Center: {vaccine_center}, Date of first vaccine: {today_date_string}, Status: {status}, Date of second vaccine: {second_vaccine_date_string}".split()
                else: 
                    administer_new_patient = f"Patient ID: {patient_id}, Vaccine Administered: {vaccine_chosen}, Vaccine Center: {vaccine_center}, Date of first vaccine: {first_vaccine_date_string}, Status: {status}, Date of second vaccine: {today_date_string}".split()
            else:
                # this is for EC because EC vaccine only has 1 dose
                administer_new_patient = f"Patient ID: {patient_id}, Vaccine Administered: {vaccine_chosen}, Vaccine Center: {vaccine_center}, Date of first vaccine: {today_date_string}, Status: {status}, Date of second vaccine: Not Available".split()
            # the string is then appended to the updated vaccination list
            updated_vaccination_lst.append(administer_new_patient)
            # the list is then sorted
            sorted_updated_lst = sort(updated_vaccination_lst)
            with open('vaccination.txt', 'w') as vaccination_file:
                for lines in sorted_updated_lst:
                    try:
                        # lines[24] is to determine the data of the patient
                        lines[24]
                        # the information is then written to the 'vaccination.txt' file
                        vaccination_file.write(f"Patient ID: {lines[2]}, Vaccine Administered: {lines[5]}, Vaccine Center: {lines[8]}, Date of first vaccine: {lines[13]}, {lines[14]} {lines[15]}, {lines[16]}, Status: {lines[18]}, Date of second vaccine: {lines[23]}, {lines[24]} {lines[25]}, {lines[26]}")
                        vaccination_file.write("\n")   
                    except:
                        vaccination_file.write(f"Patient ID: {lines[2]}, Vaccine Administered: {lines[5]}, Vaccine Center: {lines[8]}, Date of first vaccine: Not Available, Status: NEW, Date of second vaccine: Not Available")
                        vaccination_file.write("\n")       
        # gets the patient's ID number
        while True:
            try:
                print('\n' +'='*100)
                get_patient_id = int(input('\nEnter your patient ID(enter -1 to exit): '))
                break
            except:
                continue

def search_patient_record():
    # gets patient ID number
    while True:
        try:
            get_patient_id = int(input('\nEnter your patient ID(enter -1 to exit): '))
            break
        except:
            continue
    while get_patient_id != -1:
        # add leading zeroes to patient id number
        patient_id = str(get_patient_id).zfill(8)
        # empty lists that will store data about the patient or the vaccine
        patient_record = []
        vaccine_record = []
        display_patient_record=[]
        display_vaccine_record=[]
        # opens the 'patient.txt' file and make the data more readable using built in functions such as split and replace
        with open('patient.txt') as patient_file:
            for line in patient_file.readlines():
                newline_patient = line.replace(',','')
                patient_record.append(newline_patient.split())
        # checks whether the patient id is in the list
        for patient_lst in patient_record:
            if patient_id in patient_lst:
                display_patient_record= patient_lst
                break
        # opens the 'vaccination.txt' file and make the data more readable using built in functions such as split and replace
        with open('vaccination.txt') as vaccination_file:
            for line in vaccination_file.readlines():
                newline_vaccine = line.replace(',','')
                vaccine_record.append(newline_vaccine.split())
        # split the list that contains the patient id in it's last 3 data
        for vaccine_lst in vaccine_record:
            if patient_id in vaccine_lst:
                display_vaccine_record= vaccine_lst[3:]
                break
        # initialize 2 empty phrases and two null values
        phrase1=''
        phrase2=''
        j=None
        l = None
        # loop over the length of the list that displays the patient's record
        for i in range(len(display_patient_record)):
            # change every data is in the list into a string
            word = str(display_patient_record[i])
            # add the word to one of the phrase
            phrase1+=word
            #  if i and j is the same value then add a comma to the phrase and set j to null
            #  if the last index of word is ':', add 1 to i and set the value to j
            if i==j:
                phrase1 += ','
                j = None
            phrase1+= ' '
            if word[-1] == ':':
                j=i+1
        # if the length of the vaccine record isn't 0 then loop over the length of the vaccine record and set every data to a string with the variable of word
        if len(display_vaccine_record) != 0:
            for k in range(len(display_vaccine_record)):
                word = str(display_vaccine_record[k])
                # add the string togethter using the variable phrase2
                phrase2+=word
                # if k is equal to l then add a comma and set l to null 
                if k==l:
                    phrase2 += ','
                    l= None
                phrase2+= ' '
                # if the last index of the word is ':', add 1 to k and set the value to l
                if word[-1] == ':':
                    l=k+1
        else:
            # if the length of the vaccine record is 0 then set phrase 2 with the phrase shown below
            phrase2 = f"Status: NEW"
            # print both phrases together 
        if len(display_patient_record)== 0 and len(display_vaccine_record)== 0:
            print('Patient not found')
        else:
            print(f"{phrase1}{phrase2}")
        # gets the patient id
        while True:
            try:
                get_patient_id = int(input('\nEnter your patient ID(enter -1 to exit): '))
                break
            except:
                continue
# gets statistical information on the patient vaccinated
def patient_statistical_information():
    # initialize the variables to 0 and set the lst to an empty list
    lst=[]
    count_VC1_D2=0
    count_VC1=0
    count_VC1_total=0
    count_VC2_D2 = 0
    count_VC2=0 
    count_VC2_total = 0
    # open the 'vaccination.txt' file and make it more readable using built in functions such as replace and split
    # the new data line is then appended to the list
    with open('vaccination.txt') as vaccination_file:
        for line in vaccination_file.readlines():
            newline = line.replace(',','')
            lst.append(newline.split())
    # counts the number of patient according to the VC number and the dose
    for lst_of_words in lst:
        if lst_of_words[8] == '1':
            if lst_of_words[18]=='COMPLETED':
                count_VC1+=1
            elif lst_of_words[18] == 'COMPLETED-D1':
                count_VC1_D2+=1
        else:
            if lst_of_words[18]=='COMPLETED':
                count_VC2+=1
            elif lst_of_words[18] == 'COMPLETED-D1':
                count_VC2_D2+=1
    # adds the total patient for each VC
    count_VC1_total=count_VC1+count_VC1_D2
    count_VC2_total= count_VC2+count_VC2_D2
    print('\n' + '='*100)
    # get the string with leading zeroes for each of the value
    count_VC1_str = str(count_VC1).zfill(4)
    count_VC1_D2_str = str(count_VC1_D2).zfill(4)
    count_VC1_total_str = str(count_VC1_total).zfill(4)
    count_VC2_str = str(count_VC2).zfill(4)
    count_VC2_D2_str = str(count_VC2_D2).zfill(4)
    count_VC2_total_str = str(count_VC2_total).zfill(4)
    # display the information in a table view
    print('\n\t\tStatistical information on Patients Vaccinated')
    print('\n\tNumber of patients waiting:', end='')
    print('\tNumber of patients completed:', end='')
    print('\tTotal:')
    print(f"VC1 \t\t{count_VC1_D2_str} \t\t\t\t {count_VC1_str} \t\t\t {count_VC1_total_str}")
    print(f"VC2 \t\t{count_VC2_D2_str} \t\t\t\t {count_VC2_str} \t\t\t {count_VC2_total_str}")
    print('\n' + '='*100)
    print(f"\nNumber of patient in Vaccination Center 1 who are waiting for their second dose: {count_VC1_D2}")
    print(f"\nNumber of patients in Vaccination Center 1 who has completed vaccination: {count_VC1}")
    print(f"\nTotal number of patients vaccinated in Vaccination Center 1: {count_VC1_total}")
    print(f"\nNumber of patient in Vaccination Center 2 who are waiting for their second dose: {count_VC2_D2}")
    print(f"\nNumber of patients in Vaccination Center 2 who has completed vaccination: {count_VC2}")
    print(f"\nTotal number of patients vaccinated in Vaccination Center 2: {count_VC2_total}")
    print('\n'+ '='*100)

def vaccination_management_system():
    choice = None
    # displays the options to the user and calls the function according to the needs of the patient
    while True:
        print('\n\t\tVaccination Management System Main Menu\n\n\t\tChoose a number below that suits your needs\n\n\t\t1. Register\n\n\t\t2. Administer a Vaccine\n\n\t\t3. Patient Record\n\n\t\t4. Statistical Information on Patients Vaccinated')
        choice = input('\nEnter 1 if you would like to register, enter 2 if you would like to be administered a vaccine, enter 3 if you would like to see your patient record or enter 4 if you would like to know about the statistical information on the patients vaccinated.Enter your choice: ')
        if choice== '1':
            new_patient_registration()
        elif choice == '2':
            vaccine_administration()
        elif choice == '3':
            search_patient_record()
        elif choice == '4':
            patient_statistical_information()
# calling the function
vaccination_management_system()