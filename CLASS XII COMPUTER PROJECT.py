# CONNECTION

import mysql.connector as c
a=c.connect(host="localhost",user="root",password="whis",database="prisonmanagement")
if a.is_connected():
    print("connected")
    cur=a.cursor()
    
# CONNECTION COMPLETE

while True:
    print("Enter 1 to work with CONVICTS table")
    print("Enter 2 to work with STAFF table")
    print("Enter 3 to work with INCARCERATED_WORKERS table")
    print("Enter 4 to work with PAROLES table")
    print("Enter 5 to work with VISITORS table")
    print("Enter 6 for reports")
    print("Enter 7 to exit")
    Menu1=int(input("Enter numeric value according to your need above"))
    print()

    # CONVICTS TABLE
    
    if Menu1==1:
        print("Enter 1 if you wish to enter a record")
        print("Enter 2 if you wish to delete records/a convict is being released")
        print("Enter 3 if you wish to update a record")
        print("Enter 4 if you wish to display records")
        print("Enter 5 if you wish to go back")
        print()
        while True:
            print("Enter 0 to see TABLE-CONVICTS options again")
            Menu2=int(input("Enter your desired action from above menu->"))
            print()
            if Menu2==0:
                print("Enter 1 if you wish to enter a record")
                print("Enter 2 if you wish to delete a record")
                print("Enter 3 if you wish to update a record")
                print("Enter 4 if you wish to display records")
                print("Enter 5 if you wish to go back")
                print()

# INSERTING VALUES

            elif Menu2==1:
                while True:
                    Confirm_Insert_Convicts=int(input("Enter 1 if you wish to insert a record. Enter 0 to go back"))
                    print()
                    if Confirm_Insert_Convicts==0:
                        print()
                        break
                    elif Confirm_Insert_Convicts==1:
                        Convicts_ID = int(input("Enter Convict's ID "))
                        Convicts_Name = input("Enter Convict's Full Name ")
                        Convicts_Crime = input("Enter Convict's Crime ")
                        Convicts_Level = int(input("Enter Convict's Security Level [1/2/3] "))
                        Convicts_Date = input("Enter Date of Booking [YYYY-MM-DD] ")
                        Convicts_Sentence = int(input("Enter the number of years sentences"))
                        Convicts_Address = input("Enter the Convict's address")
                        Convicts_Contact = int(input("Enter the Convict's contact number"))
                        print()
                        
# ENSURING THAT INPUT IS VALID
                        
                        cur.execute("Select C_ID from convicts")
                        INVALID_ID=cur.fetchall()
                        INVALID=(0,)
                        for i in INVALID_ID:
                            i2=i
                            INVALID=INVALID+i2
                        cur.execute("Select C_Name from convicts")
                        INVALID_NAME=cur.fetchall()
                        INVALID_N=()
                        for i in INVALID_NAME:
                            i2=i
                            INVALID_N=INVALID_N+i2
                        if Convicts_ID in INVALID:
                            print("This ID already exists, the next id is->",INVALID[-1]+1)
                            print()
                        elif Convicts_Name=="" or Convicts_Crime=="" or Convicts_Date=="" or Convicts_Address=="":
                            print("No field should be left empty!")
                        elif Convicts_ID>=INVALID[-1]+2:
                            print("This ID is beyond the sequence, the next id is->",INVALID[-1]+1)
                            print()
                        elif len(Convicts_Date) != 10:
                            print("Invalid amount of characters in date, ensure you are following the format [YYYY-MM-DD]")
                            print()
                        elif Convicts_Date[4]!="-" or Convicts_Date[7]!="-":
                            print("Invalid date format, please separate terms using dashes [YYYY-MM-DD].")
                            print()
                        elif int(Convicts_Date[5])==1 and int(Convicts_Date[6])>2 or int(Convicts_Date[8])>3 or int(Convicts_Date[8])==3 and int(Convicts_Date[9])>1:
                            print("Invalid Date")
                        elif Convicts_Level>3 or Convicts_Level<1:
                            print("Security level must be 1,2 or 3")
                            print()
                        elif len(Convicts_Name)>25:
                            print("Name is too long [Max 25 characters]")
                            print()
                        elif len(Convicts_Crime)>40:
                            print("Crime details too long [Max 40 characters]")
                            print()
                        elif Convicts_Sentence<0:
                            print("Enter a valid sentence period!")
                        elif len(Convicts_Address)>30:
                            print("Address too long")
                        elif len(str(Convicts_Contact)) != 10:
                            print("Invalid contact number, it must be of 10 digits")
                        else:
                            cur.execute("INSERT INTO convicts VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(Convicts_ID, Convicts_Name, Convicts_Crime, Convicts_Level, Convicts_Date,Convicts_Sentence,Convicts_Address,Convicts_Contact))
                            a.commit()
                            print("Record entered---->","| ID->",Convicts_ID,"| Name->",Convicts_Name,"| Crime->",Convicts_Crime,"| Security Level->",Convicts_Level, " |Booking Date->",Convicts_Date,"|Sentence Period->",Convicts_Sentence," |Address->",Convicts_Address," |Contact->",Convicts_Contact)
                            print()
                            break
                    else:
                        print("Invalid input")
                        print()

# DELETE RECORDS AND ENSURING THAT THE INPUT EXISTS IN THE TABLE
    
            elif Menu2==2:
                cur.execute("Select C_ID from convicts")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to delete records!")
                    print()
                else:
                    while True:
                        print("Enter 1 if you wish to delete all records from table")
                        print("Enter 2 if you wish to delete a range of records using convict ID")
                        print("Enter 3 if you wish to delete a record via Convict's ID")
                        print("Enter 4 if you wish to delete a record via Convict's Name")
                        print("Enter 5 if you wish to remove a convict's record and add them to releases table via Convict's ID")
                        print("Enter 6 if you wish to go back")
                        Convicts_Delete_Choice=int(input("Enter your choice here"))
                        print()
                        if Convicts_Delete_Choice==1:
                            while True:
                                CONFIRMATION=int(input("Enter 1 to confirm deletion of all records. Enter 0 to go back"))
                                print()
                                if CONFIRMATION==1:
                                    cur.execute("Delete from convicts")
                                    a.commit()
                                    print("All records deleted from convicts table")
                                    print()
                                    break
                                elif CONFIRMATION==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Delete_Choice==2:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 to go back"))
                                if Confirm==1:
                                    Convicts_Delete_Range_Start=int(input("Enter the convict ID for start value of deletion of range. Must be smaller than end value"))
                                    Convicts_Delete_Range_End=int(input("Enter the convict ID for end value of deletion of range."))
                                    print()
                                    if Convicts_Delete_Range_Start<1:
                                        print("Start ID must be greater than or equal to 1")
                                        print()
                                    elif Convicts_Delete_Range_Start>Convicts_Delete_Range_End:
                                        print("Start value must be smaller than end value")
                                        print()
                                    else:
                                        cur.execute("Delete from convicts where C_ID between %s and %s",(Convicts_Delete_Range_Start,Convicts_Delete_Range_End))
                                        a.commit()
                                        print("Given range of records have been deleted")
                                        print()
                                        break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Delete_Choice==3:
                            Convicts_Delete_ID=int(input("Enter the convict's ID whose record you wish to delete"))
                            cur.execute("Select C_ID from convicts")
                            INVALID_ID=cur.fetchall()
                            INVALID=()
                            for i in INVALID_ID:
                                i2=i
                                INVALID=INVALID+i2
                            if Convicts_Delete_ID not in INVALID:
                                print("This Convict ID does not exist")
                                print()
                            else:
                                cur.execute("Select C_Name from convicts where C_ID = %s",(Convicts_Delete_ID,))
                                Convicts_C_Name_Delete_ID=cur.fetchall()
                                cur.execute("Delete from convicts where C_ID = %s", (Convicts_Delete_ID,))
                                a.commit()
                                for i in Convicts_C_Name_Delete_ID:
                                    Convicts_C_Name_Delete_ID_Output=i
                                print("Record of convict with Convict ID",Convicts_Delete_ID,"is deleted.")
                                print("Convict with Convict ID",Convicts_Delete_ID,"is",Convicts_C_Name_Delete_ID_Output[0])
                                print()
                                break
                        elif Convicts_Delete_Choice==4:
                            Convicts_Delete_Name=input("Enter the full name of the convict whose record you wish to delete")
                            print
                            cur.execute("Select C_Name from convicts")
                            VALID_NAME=cur.fetchall()
                            VALID=()
                            for i in VALID_NAME:
                                VALID+=i
                            if Convicts_Delete_Name not in VALID:
                                print("The entered name may have an error or the said person does not have a record")
                                print()
                            else:
                                cur.execute("Select C_ID from convicts where C_Name = %s",(Convicts_Delete_Name,))
                                Convicts_C_ID_Delete_Name=cur.fetchall()
                                cur.execute("Delete from convicts where C_Name = %s",(Convicts_Delete_Name,))
                                a.commit()
                                for i in Convicts_C_ID_Delete_Name:
                                    Convicts_C_ID_Delete_Name_Output=i
                                print(Convicts_Delete_Name, "'s record has been removed. Their C_ID is->",Convicts_C_ID_Delete_Name_Output[0])
                                print()
                                break
                        elif Convicts_Delete_Choice==5:
                            Convicts_Delete_ID=int(input("Enter the convict's ID who has been released"))
                            Convicts_C_Sentence2_Delete_ID=input("Enter release date [YYYY-MM-DD] format")
                            if len(Convicts_C_Sentence2_Delete_ID) != 10:
                                print("Invalid amount of characters in date, ensure you are following the format [YYYY-MM-DD]")
                                print()
                            elif Convicts_C_Sentence2_Delete_ID[4]!="-" or Convicts_C_Sentence2_Delete_ID[7]!="-":
                                print("Invalid date format, please separate terms using dashes [YYYY-MM-DD].")
                                print()
                            elif int(Convicts_C_Sentence2_Delete_ID[5])==1 and int(Convicts_C_Sentence2_Delete_ID[6])>2 or int(Convicts_C_Sentence2_Delete_ID[8])>3 or int(Convicts_C_Sentence2_Delete_ID[8])==3 and int(Convicts_C_Sentence2_Delete_ID[9])>1:
                                print("Invalid Date, check the month and day")
                            else:
                                cur.execute("Select C_ID from convicts")
                                INVALID_ID=cur.fetchall()
                                INVALID=()
                                for i in INVALID_ID:
                                    i2=i
                                    INVALID=INVALID+i2
                                if Convicts_Delete_ID not in INVALID:
                                    print("This Convict ID does not exist")
                                    print()
                                else:
                                    cur.execute("Select C_Name from convicts where C_ID = %s",(Convicts_Delete_ID,))
                                    Convicts_C_Name_Delete_ID=cur.fetchall()
                                    cur.execute("Select Booking_Date from convicts where C_ID=%s",(Convicts_Delete_ID,))
                                    Convicts_C_Book_Delete_ID=cur.fetchall()
                                    cur.execute("Select Years_Sentenced from convicts where C_ID=%s",(Convicts_Delete_ID,))
                                    Convicts_C_Sentence_Delete_ID=cur.fetchall()
                                    cur.execute("Select Release_Number from releases")
                                    Rnum=cur.fetchall()
                                    Rnum2=()
                                    for i in Rnum:
                                        Rnum2+=i
                                    if Rnum2==():
                                        Convicts_Delete_Number=1
                                    else:
                                        Convicts_Delete_Number=Rnum2[-1]+1
                                    cur.execute("Insert into releases values(%s,%s,%s,%s,%s)",(Convicts_Delete_Number,Convicts_C_Name_Delete_ID[0][0],Convicts_C_Book_Delete_ID[0][0],Convicts_C_Sentence2_Delete_ID,Convicts_C_Sentence_Delete_ID[0][0]))
                                    cur.execute("Delete from convicts where C_ID = %s", (Convicts_Delete_ID,))
                                    a.commit()
                                    for i in Convicts_C_Name_Delete_ID:
                                        Convicts_C_Name_Delete_ID_Output=i
                                    print("Record of convict with Convict ID",Convicts_Delete_ID,"is deleted.")
                                    print()
                                    break
                        elif Convicts_Delete_Choice==6:
                            print()
                            break
                        else:
                            print("Invalid input")
                            print()
                            
# UPDATE RECORDS AND CHECKING IF THE UPDATE IS VALID
    
            elif Menu2==3:
                cur.execute("Select C_ID from convicts")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to update records!")
                    print()
                else:
                    print("Enter 1 if you wish to update convict ID")
                    print("Enter 2 if you wish to update convict name")
                    print("Enter 3 if you wish to update crime")
                    print("Enter 4 if you wish to update security level")
                    print("Enter 5 if you wish to update booking date")
                    print("Enter 6 if you wish to update Address")
                    print("Enter 7 if you wish to update Contact")
                    print("Enter 8 if you wish to go back")
                    print()
                    while True:
                        print("Enter 0 if you wish to see UPDATE options again")
                        Convicts_Update=int(input("Enter your choice"))
                        print()
                        if Convicts_Update==8:
                            print()
                            break
                        elif Convicts_Update==0:
                            print("Enter 1 if you wish to update convict ID")
                            print("Enter 2 if you wish to update convict name")
                            print("Enter 3 if you wish to update crime")
                            print("Enter 4 if you wish to update security level")
                            print("Enter 5 if you wish to update booking date")
                            print("Enter 6 if you wish to update Address")
                            print("Enter 7 if you wish to update Contact")
                            print("Enter 8 if you wish to go back")
                            print()
                        elif Convicts_Update==1:
                            Convicts_Update_C_ID_Old=int(input("Enter the convict ID you wish to update"))
                            print()
                            cur.execute("Select C_ID from convicts")
                            INVALID_ID=cur.fetchall()
                            INVALID=()
                            for i in INVALID_ID:
                                i2=i
                                INVALID=INVALID+i2
                            if Convicts_Update_C_ID_Old not in INVALID:
                                print("This Convict ID does not exist")
                                print()
                            else:
                                Convicts_Update_C_ID_New=int(input("Enter the updated convict ID"))
                                cur.execute("Select C_ID from convicts")
                                INVALID_ID=cur.fetchall()
                                INVALID=()
                                for i in INVALID_ID:
                                    i2=i
                                    INVALID+=i2
                                if Convicts_Update_C_ID_New in INVALID:
                                    print("This Convict ID already exists")
                                    print()
                                elif Convicts_Update_C_ID_New<0:
                                    print("Convict ID must be positive!")
                                    print()
                                elif Convicts_Update_C_ID_New>INVALID[-1]+1:
                                    print("The maximum value you may update convict ID to is",INVALID[-1]+1)
                                    print()
                                elif str(Convicts_Update_C_ID_New)=="":
                                    print("You didn't input an ID!")
                                else:
                                    cur.execute("Update convicts set C_ID = %s where C_ID = %s",(Convicts_Update_C_ID_New,Convicts_Update_C_ID_Old))
                                    a.commit()
                                    print("The convict's convict ID has been updated from",Convicts_Update_C_ID_Old,"to",Convicts_Update_C_ID_New)
                                    print()
                        elif Convicts_Update==2:
                            Convicts_Update_Name_Old=input("Enter the convict name you wish to update")
                            print()
                            cur.execute("Select C_Name from convicts")
                            INVALID_NAME=cur.fetchall()
                            INVALID=()
                            for i in INVALID_NAME:
                                i2=i
                                INVALID=INVALID+i2
                            if Convicts_Update_Name_Old not in INVALID:
                                print("This convict name does not exist")
                                print()
                            else:
                                Convicts_Update_Name_New=input("Enter the updated convict name")
                                cur.execute("Select C_Name from convicts")
                                INVALID_Name=cur.fetchall()
                                INVALID=()
                                for i in INVALID_Name:
                                    i2=i
                                    INVALID+=i2
                                if len(Convicts_Update_Name_New)>25:
                                    print("Convict name must be less than 25 characters")
                                    print()
                                elif Convicts_Update_Name_New=="":
                                    print("You didn't enter a new name!")
                                else:
                                    cur.execute("Update convicts set C_Name = %s where C_Name = %s",(Convicts_Update_Name_New,Convicts_Update_Name_Old))
                                    a.commit()
                                    cur.execute("Select C_Name from paroles")
                                    Newname=cur.fetchall()
                                    Newname2=()
                                    for i in Newname:
                                        Newname2+=i
                                    if Convicts_Update_Name_Old in Newname2:
                                        cur.execute("Update paroles set C_Name = %s where C_Name = %s",(Convicts_Update_Name_New,Convicts_Update_Name_Old))
                                    cur.execute("Select C_Name from incarcerated_workers")
                                    Newname=cur.fetchall()
                                    Newname2=()
                                    for i in Newname:
                                        Newname2+=i
                                    if Convicts_Update_Name_Old in Newname2:
                                        cur.execute("Update incarcerated_workers set C_Name = %s where C_Name = %s",(Convicts_Update_Name_New,Convicts_Update_Name_Old))
                                    cur.execute("Select Visiting from visitors")
                                    Newname=cur.fetchall()
                                    Newname2=()
                                    for i in Newname:
                                        Newname2+=i
                                    if Convicts_Update_Name_Old in Newname2:
                                        cur.execute("Update visitors set visiting = %s where visiting = %s",(Convicts_Update_Name_New,Convicts_Update_Name_Old))
                                    a.commit()
                                    print("The convict's convict name has been updated from",Convicts_Update_Name_Old,"to",Convicts_Update_Name_New)
                                    print()
                        elif Convicts_Update==3:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Convicts_Update_Crime_Old=int(input("Enter the convicts ID whose crime you wish to update"))
                                    print()
                                    cur.execute("Select C_ID from convicts")
                                    INVALID_ID=cur.fetchall()
                                    INVALID=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALID=INVALID+i2
                                    if Convicts_Update_Crime_Old not in INVALID:
                                        print("This convict ID does not exist")
                                        print()
                                    else:
                                        Convicts_Update_Crime_New=input("Enter the new register of the convict's crime with the provided ID")
                                        print()
                                        if len(Convicts_Update_Crime_New)>40:
                                            print("Crime is too long")
                                            print()
                                        elif Convicts_Update_Crime_New=="":
                                            print("You didn't enter a crime")
                                        else:
                                            cur.execute("Update convicts set Crime = %s where C_ID = %s",(Convicts_Update_Crime_New,Convicts_Update_Crime_Old))
                                            a.commit()
                                            print("The crime of given ID",Convicts_Update_Crime_Old,"has been updated to->",Convicts_Update_Crime_New)
                                            print()
                                            break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Update==4:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Convicts_Update_Sec_Old=int(input("Enter the convicts ID whose security level you wish to update"))
                                    print()
                                    cur.execute("Select C_ID from convicts")
                                    INVALID_ID=cur.fetchall()
                                    INVALID=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALID=INVALID+i2
                                    if Convicts_Update_Sec_Old not in INVALID:
                                        print("This convict ID does not exist")
                                        print()
                                    else:
                                        Convicts_Update_Sec_New=int(input("Enter the new security level of convict with the provided ID"))
                                        print()
                                        if Convicts_Update_Sec_New>3 or Convicts_Update_Sec_New<1:
                                            print("Security level must be 1,2 or 3")
                                            print()
                                        elif str(Convicts_Update_Sec_New)=="":
                                            print("You didn't enter a security level!")
                                        else:
                                            cur.execute("Update convicts set Security_Level = %s where C_ID = %s",(Convicts_Update_Sec_New,Convicts_Update_Sec_Old))
                                            a.commit()
                                            print("The security level of given ID",Convicts_Update_Sec_Old,"has been updated to->",Convicts_Update_Sec_New)
                                            print()
                                            break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Update==5:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Convicts_Update_Date_Old=int(input("Enter the convicts ID whose booking date you wish to update"))
                                    print()
                                    cur.execute("Select C_ID from convicts")
                                    INVALID_ID=cur.fetchall()
                                    INVALID=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALID=INVALID+i2
                                    if Convicts_Update_Date_Old not in INVALID:
                                        print("This convict ID does not exist")
                                        print()
                                    else:
                                        Convicts_Update_Date_New=input("Enter the new booking date of the given convict ID")
                                        print()
                                        if len(Convicts_Update_Date_New)<10 or len(Convicts_Update_Date_New)>10:
                                            print("Invalid amount of characters date, ensure you are following the format [YYYY-MM-DD]")
                                            print()
                                        elif int(Convicts_Update_Date_New[5])>1 or int(Convicts_Update_Date_New[5])==1 and int(Convicts_Update_Date_New[6])>2 or Convicts_Update_Date_New[4]!="-" or Convicts_Update_Date_New[7]!="-":
                                            print("Invalid date, follow the format please or check that date exists.")
                                            print()
                                        else:
                                            cur.execute("Update convicts set Booking_Date = %s where C_ID = %s",(Convicts_Update_Date_New,Convicts_Update_Date_Old))
                                            a.commit()
                                            cur.execute("select C_ID from paroles")
                                            Bupdate=cur.fetchall()
                                            Bupdate2=()
                                            for i in Bupdate:
                                                Bupdate2+=i
                                            for j in Bupdate2:
                                                if Convicts_Update_Date_Old==j:
                                                    cur.execute("Update paroles set Booking_Date = %s where C_ID = %s",(Convicts_Update_Date_New,Convicts_Update_Date_Old))
                                                    a.commit()
                                            print("The booking date of given ID",Convicts_Update_Date_Old,"has been updated to->",Convicts_Update_Date_New)
                                            print()
                                            break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Update==6:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Convicts_Update_Address_Old=int(input("Enter the convicts ID whose Address you wish to update"))
                                    print()
                                    cur.execute("Select C_ID from convicts")
                                    INVALID_ID=cur.fetchall()
                                    INVALID=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALID=INVALID+i2
                                    if Convicts_Update_Address_Old not in INVALID:
                                        print("This convict ID does not exist")
                                        print()
                                    else:
                                        while True:
                                            Convicts_Update_Address_New=input("Enter the updated address")
                                            if len(Convicts_Update_Address_New)>30:
                                                print("Address too long")
                                                print()
                                            elif Convicts_Update_Address_New=="":
                                                print("You didn't enter an address!")
                                                print()
                                            else:
                                                cur.execute("Update convicts set Address = %s where C_ID = %s",(Convicts_Update_Address_New,Convicts_Update_Address_Old))
                                                a.commit()
                                                print("Address updated")
                                                print()
                                                break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Update==7:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Convicts_Update_Contact_Old=int(input("Enter the convicts ID whose Contact you wish to update"))
                                    print()
                                    cur.execute("Select C_ID from convicts")
                                    INVALID_ID=cur.fetchall()
                                    INVALID=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALID=INVALID+i2
                                    if Convicts_Update_Contact_Old not in INVALID:
                                        print("This convict ID does not exist")
                                        print()
                                    else:
                                        while True:
                                            Convicts_Update_Contact_New=int(input("Enter the updated contact"))
                                            if len(str(Convicts_Update_Contact_New))!=10:
                                                print("Contact number should be exactly 10 digits!")
                                                print()
                                            else:
                                                cur.execute("Update convicts set Contact = %s where C_ID = %s",(Convicts_Update_Contact_New,Convicts_Update_Contact_Old))
                                                a.commit()
                                                print("Contact updated")
                                                print()
                                                break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        else:
                            print("Invalid input")
                            print()
                            
# DISPLAYING RECORDS AND ENSURING INPUT MAKES SENSE
    
            if Menu2==4:
                cur.execute("Select C_ID from convicts")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to display records!")
                    print()
                else:
                    print("Enter 1 to check records of all convicts")
                    print("Enter 2 to check record of specific convict ID")
                    print("Enter 3 to check record of specific convict name")
                    print("Enter 4 to check records from given range of convict IDs")
                    print("Enter 5 to go back")
                    print()
                    while True:
                        print("Enter 0 to see CONVICTS SELECT options")
                        Convicts_Select_Option=int(input("Enter your choice"))
                        print()
                        if Convicts_Select_Option==0:
                            print("Enter 1 to check records of all convicts")
                            print("Enter 2 to check record of specific convict ID")
                            print("Enter 3 to check record of specific convict name")
                            print("Enter 4 to check records from given range of convict IDs")
                            print("Enter 5 to go back")
                            print()
                        elif Convicts_Select_Option==5:
                            print("Going back")
                            print()
                            break
                        elif Convicts_Select_Option==1:
                            cur.execute("Select * from convicts")
                            Convicts_Select_All=cur.fetchall()
                            print("Table format-> Convict ID, Convict Name, Crime, Security Level, Booking Date","Years sentenced","Address","Contact")
                            print()
                            i=1
                            for convict in Convicts_Select_All:
                                  print("Entry",i,"->   ",end="")
                                  print(convict[0]," - ",end="")
                                  print(convict[1]," - ",end="")
                                  print(convict[2]," - ",end="")
                                  print(convict[3]," - ",end="")
                                  print(convict[4]," - ",end="")
                                  print(convict[5]," - ",end="")
                                  print(convict[6]," - ",end="")
                                  print(convict[7])
                                  print()
                                  i+=1
                        elif Convicts_Select_Option==2:
                            while True:
                                Convicts_Select_Single_ID=int(input("Enter the convict ID whose record you wish to see"))
                                cur.execute("Select C_ID from convicts")
                                INVALID_ID=cur.fetchall()
                                INVALID=()
                                for i in INVALID_ID:
                                    i2=i
                                    INVALID=INVALID+i2
                                if INVALID==():
                                    print("No records exist")
                                elif Convicts_Select_Single_ID in INVALID:
                                    cur.execute("Select * from convicts where C_ID = %s",(Convicts_Select_Single_ID,))
                                    Convicts_Select_All=cur.fetchall()
                                    print("Table format-> Convict ID, Convict Name, Crime, Security Level, Booking Date","Years sentenced","Address","Contact")
                                    print()
                                    i=1
                                    for convict in Convicts_Select_All:
                                          print("Entry",i,"->   ",end="")
                                          print(convict[0]," - ",end="")
                                          print(convict[1]," - ",end="")
                                          print(convict[2]," - ",end="")
                                          print(convict[3]," - ",end="")
                                          print(convict[4]," - ",end="")
                                          print(convict[5]," - ",end="")
                                          print(convict[6]," - ",end="")
                                          print(convict[7])
                                          print()
                                          i+=1
                                    print()
                                    break
                                else:
                                    print("This ID does not exist")
                                    print()
                        elif Convicts_Select_Option==3:
                            Convicts_Select_Single_Name=input("Enter the convict name whose record you wish to see")
                            print()
                            cur.execute("Select C_Name from convicts")
                            INVALID_NAME=cur.fetchall()
                            INVALID=()
                            for i in INVALID_NAME:
                                i2=i
                                INVALID=INVALID+i2
                            if Convicts_Select_Single_Name in INVALID:
                                cur.execute("Select * from convicts where C_Name = %s",(Convicts_Select_Single_Name,))
                                Convicts_Select_All=cur.fetchall()
                                print("Table format-> Convict ID, Convict Name, Crime, Security Level, Booking Date","Years sentenced","Address","Contact")
                                print()
                                i=1
                                for convict in Convicts_Select_All:
                                    print("Entry",i,"->   ",end="")
                                    print(convict[0]," - ",end="")
                                    print(convict[1]," - ",end="")
                                    print(convict[2]," - ",end="")
                                    print(convict[3]," - ",end="")
                                    print(convict[4]," - ",end="")
                                    print(convict[5]," - ",end="")
                                    print(convict[6]," - ",end="")
                                    print(convict[7])
                                    print()
                                    i+=1
                                print()
                            else:
                                print("This name does not exist")
                                print()
                        elif Convicts_Select_Option==4:
                             Convicts_Select_Range_Start=int(input("Enter convict ID for start value of range"))
                             Convicts_Select_Range_End=int(input("Enter convict ID for end value of range"))
                             print()
                             if Convicts_Select_Range_Start<0:
                                print("Start value must be 1 or more")
                                print()
                             elif Convicts_Select_Range_Start>Convicts_Select_Range_End:
                                 print("Start value must be less than end value")
                             else:
                                 cur.execute("Select * from convicts where C_ID between %s and %s",(Convicts_Select_Range_Start,Convicts_Select_Range_End))
                                 Convicts_Select_All=cur.fetchall()
                                 print("Table format-> Convict ID, Convict Name, Crime, Security Level, Booking Date","Years sentenced","Address","Contact")
                                 print()
                                 i=1
                                 for convict in Convicts_Select_All:
                                    print("Entry",i,"->   ",end="")
                                    print(convict[0]," - ",end="")
                                    print(convict[1]," - ",end="")
                                    print(convict[2]," - ",end="")
                                    print(convict[3]," - ",end="")
                                    print(convict[4]," - ",end="")
                                    print(convict[5]," - ",end="")
                                    print(convict[6]," - ",end="")
                                    print(convict[7])
                                    print()
                                    i+=1
                        else:
                            print("Invalid input")
                            print()
            elif Menu2==5:
                print()
                break
            elif Menu2 not in (0,1,2,3,4,5):
                print("Invalid input")
                print()

# STAFF TABLE

    elif Menu1==2:
        print("Enter 1 if you wish to enter a record")
        print("Enter 2 if you wish to delete a record/all records")
        print("Enter 3 if you wish to update a record")
        print("Enter 4 if you wish to display records")
        print("Enter 5 if you wish to see all staff's salaries")
        print("Enter 6 if you wish to go back")
        print()
        while True:
            print("Enter 0 to see TABLE-STAFF options again")
            Menu2=int(input("Enter your desired action from above menu->"))
            print()
            if Menu2==0:
                print("Enter 1 if you wish to enter a record")
                print("Enter 2 if you wish to delete a record")
                print("Enter 3 if you wish to update a record")
                print("Enter 4 if you wish to display records")
                print("Enter 5 if you wish to see all staff's salaries")
                print("Enter 6 if you wish to go back")
                print()
                
# INSERTION OF RECORDS

            elif Menu2==1:
                while True:
                    Confirm_Insert_Staff=int(input("Enter 1 if you wish to insert a record. Enter 0 to go back"))
                    print()
                    if Confirm_Insert_Staff==0:
                        print()
                        break
                    elif Confirm_Insert_Staff==1:
                        Staff_ID = int(input("Enter Staff's ID "))
                        Staff_Name = input("Enter Staff's Full Name ")
                        Staff_Designation = input("Enter Staff's Designation ")
                        Staff_Shift = input("Enter Staff's Shift [Day,Evening,Night] ")
                        Staff_Date = input("Enter Date of Join [YYYY-MM-DD] ")
                        Staff_Sal = int(input("Enter salary"))
                        print()
                        
# ENSURING THAT INPUT IS VALID

                        cur.execute("Select S_ID from staff")
                        INVALID_ID=cur.fetchall()
                        INVALIDS=(0,)
                        for i in INVALID_ID:
                            i2=i
                            INVALIDS=INVALIDS+i2
                        cur.execute("Select S_Name from staff")
                        INVALID_NAME=cur.fetchall()
                        INVALID_NS=()
                        for i in INVALID_NAME:
                            i2=i
                            INVALID_NS=INVALID_NS+i2
                        if Staff_ID in INVALIDS:
                            print("This ID already exists, the next id is->",INVALIDS[-1]+1)
                            print()
                        elif Staff_Name=="" or Staff_Designation=="" or Staff_Shift=="" or Staff_Date=="":
                            print("No field should be left empty!")
                            print()
                        elif Staff_ID>=INVALIDS[-1]+2:
                            print("This ID is beyond the sequence, the next id is->",INVALIDS[-1]+1)
                            print()
                        elif len(Staff_Date)<10 or len(Staff_Date)>10:
                            print("Invalid amount of characters date, ensure you are following the format [YYYY-MM-DD]")
                            print()
                        elif int(Staff_Date[5])>1 or int(Staff_Date[5])==1 and int(Staff_Date[6])>2 or Staff_Date[4]!="-" or Staff_Date[7]!="-":
                            print("Invalid date, follow the format please or check that date exists.")
                            print()
                        elif len(Staff_Name)>25:
                            print("Name is too long [Max 25 characters]")
                            print()
                        elif len(Staff_Designation)>20:
                            print("Designation too long [Max 20 characters]")
                            print()
                        elif len(Staff_Shift)>15:
                            print("Shift details too long [Max 15 characters]")
                            print()
                        else:
                            cur.execute("INSERT INTO staff VALUES (%s,%s,%s,%s,%s)",(Staff_ID, Staff_Name, Staff_Designation, Staff_Shift, Staff_Date))
                            a.commit()
                            cur.execute("INSERT INTO staff_salaries VALUES (%s,%s,%s)",(Staff_ID,Staff_Sal,Staff_Date))
                            a.commit()
                            print("Record entered---->","| ID->",Staff_ID,"| Name->",Staff_Name,"| Designation->",Staff_Designation,"| Shift->",Staff_Shift,"| Join Date->",Staff_Date)
                            print()
                            break
                    else:
                        print("Invalid input")
                        print()
                        
# DELETION OF RECORDS

            elif Menu2==2:
                cur.execute("Select S_ID from staff")
                INVALID_ID=cur.fetchall()
                INVALIDS=()
                for i in INVALID_ID:
                    i2=i
                    INVALIDS=INVALIDS+i2
                if INVALIDS==():
                    print("Enter records before attempting to delete records!")
                    print()
                else:
                    while True:
                        print("Enter 1 if you wish to delete all records from table")
                        print("Enter 2 if you wish to delete a range of records using staff ID")
                        print("Enter 3 if you wish to delete a record via staff ID")
                        print("Enter 4 if you wish to delete a record via staff name")
                        print("Enter 5 if you wish to go back")
                        Staff_Delete_Choice=int(input("Enter your choice here"))
                        print()
                        if Staff_Delete_Choice==1:
                            while True:
                                CONFIRMATION=int(input("Enter 1 to confirm deletion of all records. Enter 0 to go back"))
                                print()
                                if CONFIRMATION==1:
                                    cur.execute("Delete from staff")
                                    a.commit()
                                    print("All records deleted from staff table")
                                    print()
                                    break
                                elif CONFIRMATION==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Staff_Delete_Choice==2:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 to go back"))
                                if Confirm==1:
                                    Staff_Delete_Range_Start=int(input("Enter the Staff ID for start value of deletion of range. Must be smaller than end value"))
                                    Staff_Delete_Range_End=int(input("Enter the Staff ID for end value of deletion of range."))
                                    print()
                                    if Staff_Delete_Range_Start<1:
                                        print("Start ID must be greater than or equal to 1")
                                        print()
                                    elif Staff_Delete_Range_Start>Staff_Delete_Range_End:
                                        print("Start value must be smaller than end value")
                                        print()
                                    else:
                                        cur.execute("Delete from staff where S_ID between %s and %s",(Staff_Delete_Range_Start,Staff_Delete_Range_End))
                                        a.commit()
                                        print("Given range of records have been deleted")
                                        print()
                                        break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Staff_Delete_Choice==3:
                            Staff_Delete_ID=int(input("Enter the staff ID whose record you wish to delete"))
                            cur.execute("Select S_ID from staff")
                            INVALID_ID=cur.fetchall()
                            INVALIDS=()
                            for i in INVALID_ID:
                                i2=i
                                INVALIDS=INVALIDS+i2
                            if Staff_Delete_ID not in INVALIDS:
                                print("This staff ID does not exist")
                                print()
                            else:
                                cur.execute("Select S_Name from staff where S_ID = %s",(Staff_Delete_ID,))
                                Staff_S_Name_Delete_ID=cur.fetchall()
                                cur.execute("Delete from staff where S_ID = %s",(Staff_Delete_ID,))
                                a.commit()
                                for i in Staff_S_Name_Delete_ID:
                                    Staff_S_Name_Delete_ID_Output=i
                                print("Record of staff with Staff ID",Staff_Delete_ID,"is deleted.")
                                print("Staff with Staff ID",Staff_Delete_ID,"is",Staff_S_Name_Delete_ID_Output[0])
                                print()
                                break
                        elif Staff_Delete_Choice==4:
                            Staff_Delete_Name=input("Enter the full name of the staff member whose record you wish to delete")
                            print()
                            cur.execute("Select S_Name from staff")
                            VALID_NAME=cur.fetchall()
                            VALIDS=()
                            for i in VALID_NAME:
                                VALIDS+=i
                            if Staff_Delete_Name not in VALIDS:
                                print("The entered name may have an error or the said person does not have an entry")
                                print()
                            else:
                                cur.execute("Select S_ID from staff where S_Name = %s",(Staff_Delete_Name,)                                )
                                Staff_S_ID_Delete_Name=cur.fetchall()
                                cur.execute("Delete from staff where S_Name = %s",(Staff_Delete_Name,))
                                a.commit()
                                for i in Staff_S_ID_Delete_Name:
                                    Staff_S_ID_Delete_Name_Output=i
                                print(Staff_Delete_Name,"'s record has been removed. Their S_ID is->",Staff_S_ID_Delete_Name_Output[0])
                                print()
                                break
                        elif Staff_Delete_Choice==5:
                            print()
                            break
                        else:
                            print("Invalid input")
                            print()
                            
# UPDATING RECORDS

            elif Menu2==3:
                cur.execute("Select S_ID from staff")
                INVALID_ID=cur.fetchall()
                INVALIDS=()
                for i in INVALID_ID:
                    i2=i
                    INVALIDS=INVALIDS+i2
                if INVALIDS==():
                    print("Enter records before attempting to update records!")
                    print()
                else:
                    print("Enter 1 if you wish to update staff ID")
                    print("Enter 2 if you wish to update staff name")
                    print("Enter 3 if you wish to update designation")
                    print("Enter 4 if you wish to update shift")
                    print("Enter 5 if you wish to update join date")
                    print("Enter 6 if you wish to update salary")
                    print("Enter 7 if you wish to go back")
                    print()
                    while True:
                        print("Enter 0 if you wish to see UPDATE options again")
                        Staff_Update=int(input("Enter your choice"))
                        print()
                        if Staff_Update==7:
                            print()
                            break
                        elif Staff_Update==0:
                            print("Enter 1 if you wish to update staff ID")
                            print("Enter 2 if you wish to update staff name")
                            print("Enter 3 if you wish to update designation")
                            print("Enter 4 if you wish to update shift")
                            print("Enter 5 if you wish to update join date")
                            print("Enter 6 if you wish to update salary")
                            print("Enter 7 if you wish to go back")
                            print()
                            
# UPDATE STAFF ID

                        elif Staff_Update==1:
                            Staff_Update_S_ID_Old=int(input("Enter the staff ID you wish to update"))
                            cur.execute("Select S_ID from staff")
                            INVALID_ID=cur.fetchall()
                            INVALIDS=()
                            for i in INVALID_ID:
                                i2=i
                                INVALIDS=INVALIDS+i2
                            if Staff_Update_S_ID_Old not in INVALIDS:
                                print("This staff ID does not exist")
                                print()
                            else:
                                Staff_Update_S_ID_New=int(input("Enter the updated staff ID"))
                                cur.execute("Select S_ID from staff")
                                INVALID_ID=cur.fetchall()
                                INVALIDS=()
                                for i in INVALID_ID:
                                    i2=i
                                    INVALIDS+=i2
                                if Staff_Update_S_ID_New in INVALIDS:
                                    print("This Staff ID already exists")
                                    print()
                                elif Staff_Update_S_ID_New<0:
                                    print("Staff ID must be positive!")
                                    print()
                                elif Staff_Update_S_ID_New>INVALIDS[-1]+1:
                                    print("The maximum value you may update staff ID to is",INVALIDS[-1]+1)
                                    print()
                                else:
                                    cur.execute("Update staff set S_ID = %s where S_ID = %s",(Staff_Update_S_ID_New,Staff_Update_S_ID_Old))
                                    a.commit()
                                    print("The staff's ID has been updated from",Staff_Update_S_ID_Old,"to",Staff_Update_S_ID_New)
                                    print()
                                    
# UPDATE STAFF NAME

                        elif Staff_Update==2:
                            Staff_Update_Name_Old=input("Enter the staff name you wish to update")
                            cur.execute("Select S_Name from staff")
                            INVALID_NAME=cur.fetchall()
                            INVALIDS=()
                            for i in INVALID_NAME:
                                i2=i
                                INVALIDS=INVALIDS+i2
                            if Staff_Update_Name_Old not in INVALIDS:
                                print("This staff name does not exist")
                                print()
                            else:
                                Staff_Update_Name_New=input("Enter the updated staff name")
                                cur.execute("Select S_Name from staff")
                                INVALID_Name=cur.fetchall()
                                INVALIDS=()
                                for i in INVALID_Name:
                                    i2=i
                                    INVALIDS+=i2
                                if len(Staff_Update_Name_New)>25:
                                    print("Staff name must be less than 25 characters")
                                    print()
                                else:
                                    cur.execute("Update staff set S_Name = %s where S_Name = %s",(Staff_Update_Name_New,Staff_Update_Name_Old))
                                    a.commit()
                                    print("The staff's name has been updated from",Staff_Update_Name_Old,"to",Staff_Update_Name_New)
                                    print()

    # UPDATE DESIGNATION
    
                        elif Staff_Update==3:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Staff_Update_Designation_Old=int(input("Enter the staff ID whose designation you wish to update"))
                                    cur.execute("Select S_ID from staff")
                                    INVALID_ID=cur.fetchall()
                                    INVALIDS=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALIDS=INVALIDS+i2
                                    if Staff_Update_Designation_Old not in INVALIDS:
                                        print("This staff ID does not exist")
                                        print()
                                    else:
                                        Staff_Update_Designation_New=input("Enter the new designation of the staff with the provided ID")
                                        print()
                                        if len(Staff_Update_Designation_New)>20:
                                            print("Designation is too long")
                                            print()
                                        else:
                                            cur.execute("Update staff set Designation = %s where S_ID = %s",(Staff_Update_Designation_New,Staff_Update_Designation_Old))
                                            a.commit()
                                            print("The designation of given ID",Staff_Update_Designation_Old,"has been updated to->",Staff_Update_Designation_New)
                                            print()
                                            break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                                    
# UPDATE SHIFT

                        elif Staff_Update==4:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Staff_Update_Shift_Old=int(input("Enter the staff ID whose shift you wish to update"))
                                    cur.execute("Select S_ID from staff")
                                    INVALID_ID=cur.fetchall()
                                    INVALIDS=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALIDS=INVALIDS+i2
                                    if Staff_Update_Shift_Old not in INVALIDS:
                                        print("This staff ID does not exist")
                                        print()
                                    else:
                                        Staff_Update_Shift_New=input("Enter the new register of the staff's shift with the provided ID")
                                        print()
                                        if len(Staff_Update_Shift_New)>15:
                                            print("Shift details is too long")
                                            print()
                                        else:
                                            cur.execute("Update staff set Shift = %s where S_ID = %s",(Staff_Update_Shift_New,Staff_Update_Shift_Old))
                                            a.commit()
                                            print("The shift of given ID",Staff_Update_Shift_Old,"has been updated to->",Staff_Update_Shift_New)
                                            print()
                                            break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                                    
# UPDATE JOIN DATE

                        elif Staff_Update==5:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Staff_Update_Date_Old=int(input("Enter the staff ID whose join date you wish to update"))
                                    cur.execute("Select S_ID from staff")
                                    INVALID_ID=cur.fetchall()
                                    INVALIDS=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALIDS=INVALIDS+i2
                                    if Staff_Update_Date_Old not in INVALIDS:
                                        print("This staff ID does not exist")
                                        print()
                                    else:
                                        Staff_Update_Date_New=input("Enter the new join date of the given staff ID")
                                        print()
                                        if len(Staff_Update_Date_New)<10 or len(Staff_Update_Date_New)>10:
                                            print("Invalid amount of characters date, ensure you are following the format [YYYY-MM-DD]")
                                            print()
                                        elif int(Staff_Update_Date_New[5])>1 or int(Staff_Update_Date_New[5])==1 and int(Staff_Update_Date_New[6])>2 or Staff_Update_Date_New[4]!="-" or Staff_Update_Date_New[7]!="-":
                                            print("Invalid date, follow the format please or check that date exists.")
                                            print()
                                        else:
                                            cur.execute("Update staff set Join_Date = %s where S_ID = %s",(Staff_Update_Date_New,Staff_Update_Date_Old))
                                            a.commit()
                                            cur.execute("Update staff_salaries set Join_Date= %s where S_ID = %s",(Staff_Update_Date_New,Staff_Update_Date_Old))
                                            a.commit()
                                            print("The join date of given ID",Staff_Update_Date_Old,"has been updated to->",Staff_Update_Date_New)
                                            print()
                                            break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                                    
# UPDATE SALARY

                        elif Staff_Update==6:
                            Staff_Update_S_IDD_Old=int(input("Enter the staff ID you wish to update"))
                            cur.execute("Select S_ID from staff")
                            INVALID_ID=cur.fetchall()
                            INVALIDS=()
                            for i in INVALID_ID:
                                i2=i
                                INVALIDS=INVALIDS+i2
                            if Staff_Update_S_IDD_Old not in INVALIDS:
                                print("This staff ID does not exist")
                                print()
                            else:
                                Staff_Sal_Upd=int(input("Enter new salary for specified ID"))
                                cur.execute("Update staff_salaries set salary = %s where S_ID = %s",(Staff_Sal_Upd,Staff_Update_S_IDD_Old))
                                a.commit()
                                print()
                        else:
                            print("Invalid input")
                            print()
                            
# DISPLAY RECORDS FROM TABLE

            elif Menu2==4:
                cur.execute("Select S_ID from staff")
                INVALID_ID=cur.fetchall()
                INVALIDS=()
                for i in INVALID_ID:
                    i2=i
                    INVALIDS=INVALIDS+i2
                if INVALIDS==():
                    print("Enter records before attempting to display records!")
                    print()
                else:
                    print("Enter 1 to check records of all staff")
                    print("Enter 2 to check record of specific staff ID")
                    print("Enter 3 to check record of specific staff name")
                    print("Enter 4 to check records from given range of staff IDs")
                    print("Enter 5 to go back")
                    print()
                    while True:
                        print("Enter 0 to see STAFF SELECT options")
                        Staff_Select_Option=int(input("Enter your choice"))
                        print()
                        if Staff_Select_Option==0:
                            print("Enter 1 to check records of all staff")
                            print("Enter 2 to check record of specific staff ID")
                            print("Enter 3 to check record of specific staff name")
                            print("Enter 4 to check records from given range of staff IDs")
                            print("Enter 5 to go back")
                            print()
                        elif Staff_Select_Option==5:
                            print("Going back")
                            print()
                            break
                        
# DISPLAY ALL

                        elif Staff_Select_Option==1:
                            cur.execute("Select * from staff")
                            Staff_Select_All=cur.fetchall()
                            print("Table format-> Staff ID, Staff Name, Designation, Shift, Join Date")
                            print()
                            i=1
                            for staff in Staff_Select_All:
                                print("Entry",i,"->   ",end="")
                                print(staff[0]," - ",end="")
                                print(staff[1]," - ",end="")
                                print(staff[2]," - ",end="")
                                print(staff[3]," - ",end="")
                                print(staff[4])
                                print()
                                i+=1
                                
# DISPLAY SINGLE ID

                        elif Staff_Select_Option==2:
                            while True:
                                Staff_Select_Single_ID=int(input("Enter the staff ID whose record you wish to see"))
                                cur.execute("Select S_ID from staff")
                                INVALID_ID=cur.fetchall()
                                INVALIDS=()
                                for i in INVALID_ID:
                                    i2=i
                                    INVALIDS=INVALIDS+i2
                                if INVALIDS==():
                                    print("No records exist")
                                elif Staff_Select_Single_ID in INVALIDS:
                                    cur.execute("Select * from staff where S_ID = %s",(Staff_Select_Single_ID,))
                                    Staff_Select_Single=cur.fetchall()
                                    print("Table format-> Staff ID, Staff Name, Designation, Shift, Join Date")
                                    print()
                                    for staff in Staff_Select_Single:
                                        print("Entry of ID",Staff_Select_Single_ID,"->   ",end="")
                                        print(staff[0]," - ",end="")
                                        print(staff[1]," - ",end="")
                                        print(staff[2]," - ",end="")
                                        print(staff[3]," - ",end="")
                                        print(staff[4])
                                    print()
                                    break
                                else:
                                    print("This ID does not exist")
                                    print()
                                    
# DISPLAY SINGLE NAME

                        elif Staff_Select_Option==3:
                            Staff_Select_Single_Name=input("Enter the staff name whose record you wish to see")
                            print()
                            cur.execute("Select S_Name from staff")
                            INVALID_NAME=cur.fetchall()
                            INVALIDS=()
                            for i in INVALID_NAME:
                                i2=i
                                INVALIDS=INVALIDS+i2
                            if Staff_Select_Single_Name in INVALIDS:
                                cur.execute("Select * from staff where S_Name = %s",(Staff_Select_Single_Name,))
                                Staff_Select_Single=cur.fetchall()
                                print("Table format-> Staff ID, Staff Name, Designation, Shift, Join Date")
                                print()
                                for staff in Staff_Select_Single:
                                    print("Entry of",Staff_Select_Single_Name,"->   ",end="")
                                    print(staff[0]," - ",end="")
                                    print(staff[1]," - ",end="")
                                    print(staff[2]," - ",end="")
                                    print(staff[3]," - ",end="")
                                    print(staff[4])
                                print()
                                break
                            else:
                                print("This name does not exist")
                                print()
                                
# DISPLAY RANGE

                        elif Staff_Select_Option==4:
                            Staff_Select_Range_Start=int(input("Enter staff ID for start value of range"))
                            Staff_Select_Range_End=int(input("Enter staff ID for end value of range"))
                            print()
                            if Staff_Select_Range_Start<0:
                                print("Start value must be 1 or more")
                                print()
                            elif Staff_Select_Range_Start>Staff_Select_Range_End:
                                print("Start value must be less than end value")
                                print()
                            else:
                                cur.execute("Select * from staff where S_ID between %s and %s",(Staff_Select_Range_Start,Staff_Select_Range_End))
                                Staff_Select_All=cur.fetchall()
                                print("Table format-> Staff ID, Staff Name, Designation, Shift, Join Date")
                                print()
                                i=1
                                for staff in Staff_Select_All:
                                    print("Entry",i,"->   ",end="")
                                    print(staff[0]," - ",end="")
                                    print(staff[1]," - ",end="")
                                    print(staff[2]," - ",end="")
                                    print(staff[3]," - ",end="")
                                    print(staff[4])
                                    print()
                                    i+=1
                        else:
                            print("Invalid input")
                            print()
            elif Menu2==5:
                cur.execute("Select S_ID from staff")
                INVALID_ID=cur.fetchall()
                INVALIDS=()
                for i in INVALID_ID:
                    i2=i
                    INVALIDS=INVALIDS+i2
                if INVALIDS==():
                    print("Enter records before attempting to display salary records!")
                    print()
                else:
                    cur.execute("Select * from staff_salaries")
                    salaries=cur.fetchall()
                    print("Table format-> Staff ID, Salary, Join Date")
                    j=1
                    for i in salaries:
                        print("Entry",j,"->   ",end="")
                        print(i[0]," - ",end="")
                        print(i[1]," - ",end="")
                        print(i[2])
                        print()
                        j+=1
            elif Menu2==6:
                print("Going back")
                print()
                break
            else:
                print("Invalid input")
                print()
            
# iNCARCERATED_WORKERS TABLE

    if Menu1==3:
        print("Enter 1 if you wish to enter a record")
        print("Enter 2 if you wish to delete record of fired worker")
        print("Enter 3 if you wish to display records")
        print("Enter 4 if you wish to update a record")
        print("Enter 5 if you wish to go back")
        print()
        while True:
            print("Enter 0 to see TABLE-INCARCERATED WORKERS options again")
            Menu2=int(input("Enter your desired action from above menu->"))
            print()
            if Menu2==0:
                print("Enter 1 if you wish to enter a record")
                print("Enter 2 if you wish to delete record of fired worker")
                print("Enter 3 if you wish to display records")
                print("Enter 4 if you wish to update a record")
                print("Enter 5 if you wish to go back")
                print()
            elif Menu2==1:
                while True:
                    Confirm_Insert_Convicts=int(input("Enter 1 if you wish to insert a record. Enter 0 to go back"))
                    print()
                    if Confirm_Insert_Convicts==0:
                        print()
                        break
                    elif Confirm_Insert_Convicts==1:
                        Convicts_ID = int(input("Enter Convict's ID "))
                        Convicts_Department = input("Enter Convict's Department")
                        Convicts_Date = input("Enter Date of Assignment [YYYY-MM-DD] ")
                        Convicts_Wage = int(input("Enter Convict's wage"))
                        print()
                        
# ENSURING THAT INPUT IS VALID
                        
                        cur.execute("Select C_ID from incarcerated_workers")
                        INVALID_ID=cur.fetchall()
                        INVALID=(0,)
                        for i in INVALID_ID:
                            i2=i
                            INVALID=INVALID+i2
                        cur.execute("Select C_ID from convicts")
                        INVALID_IDD=cur.fetchall()
                        INVALIDD=(0,)
                        for i in INVALID_IDD:
                            i2=i
                            INVALIDD=INVALIDD+i2
                        if Convicts_ID in INVALID:
                            print("This ID already exists")
                            print()
                        elif Convicts_ID not in INVALIDD:
                            print("This ID doesn't exist in convicts")
                        elif Convicts_Department=="" or Convicts_Date=="":
                            print("No field should be left empty!")
                        elif len(Convicts_Date) != 10:
                            print("Invalid amount of characters in date, ensure you are following the format [YYYY-MM-DD]")
                            print()
                        elif Convicts_Date[4]!="-" or Convicts_Date[7]!="-":
                            print("Invalid date format, please separate terms using dashes [YYYY-MM-DD].")
                            print()
                        elif int(Convicts_Date[5])==1 and int(Convicts_Date[6])>2 or int(Convicts_Date[8])>3 or int(Convicts_Date[8])==3 and int(Convicts_Date[9])>1:
                            print("Invalid Date")
                        elif len(Convicts_Department)>20:
                            print("Department too long [Max 20 characters]")
                            print()
                        elif Convicts_Wage<0:
                            print("Enter a valid Wage!")
                        else:
                            cur.execute("select C_Name from convicts where C_ID = %s",(Convicts_ID,))
                            namework=cur.fetchall()
                            Convicts_Name=namework[0][0]
                            cur.execute("INSERT INTO incarcerated_workers VALUES (%s,%s,%s,%s,%s)",(Convicts_ID, Convicts_Name, Convicts_Department, Convicts_Date,Convicts_Wage))
                            a.commit()
                            print("Record entered---->","| ID->",Convicts_ID,"| Name->",Convicts_Name,"| Department->",Convicts_Department, " |Assignment Date->",Convicts_Date,"|Wage->",Convicts_Wage)
                            print()
                            break
                    else:
                        print("Invalid input")
                        print()
                        
# DELETE

            elif Menu2==2:
                cur.execute("Select C_ID from incarcerated_workers")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to delete records!")
                    print()
                else:
                    while True:
                        print("Enter 1 if you wish to delete all records from table")
                        print("Enter 2 if you wish to delete a range of records using convict ID")
                        print("Enter 3 if you wish to delete a record via Convict's ID")
                        print("Enter 4 if you wish to delete a record via Convict's Name")
                        print("Enter 5 if you wish to go back")
                        Convicts_Delete_Choice=int(input("Enter your choice here"))
                        print()
                        if Convicts_Delete_Choice==1:
                            while True:
                                CONFIRMATION=int(input("Enter 1 to confirm deletion of all records. Enter 0 to go back"))
                                print()
                                if CONFIRMATION==1:
                                    cur.execute("Delete from incarcerated_workers")
                                    a.commit()
                                    print("All records deleted from incarcerated_workers table")
                                    print()
                                    break
                                elif CONFIRMATION==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Delete_Choice==2:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 to go back"))
                                if Confirm==1:
                                    Convicts_Delete_Range_Start=int(input("Enter the convict ID for start value of deletion of range. Must be smaller than end value"))
                                    Convicts_Delete_Range_End=int(input("Enter the convict ID for end value of deletion of range."))
                                    print()
                                    if Convicts_Delete_Range_Start<1:
                                        print("Start ID must be greater than or equal to 1")
                                        print()
                                    elif Convicts_Delete_Range_Start>Convicts_Delete_Range_End:
                                        print("Start value must be smaller than end value")
                                        print()
                                    else:
                                        cur.execute("Delete from incarcerated_workers where C_ID between %s and %s",(Convicts_Delete_Range_Start,Convicts_Delete_Range_End))
                                        a.commit()
                                        print("Given range of records have been deleted")
                                        print()
                                        break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Delete_Choice==3:
                            Convicts_Delete_ID=int(input("Enter the convict's ID whose record you wish to delete"))
                            cur.execute("Select C_ID from incarcerated_workers")
                            INVALID_ID=cur.fetchall()
                            INVALID=()
                            for i in INVALID_ID:
                                i2=i
                                INVALID=INVALID+i2
                            if Convicts_Delete_ID not in INVALID:
                                print("This Convict ID does not exist")
                                print()
                            else:
                                cur.execute("Select C_Name from incarcerated_workers where C_ID = %s",(Convicts_Delete_ID,))
                                Convicts_C_Name_Delete_ID=cur.fetchall()
                                cur.execute("Delete from incarcerated_workers where C_ID = %s", (Convicts_Delete_ID,))
                                a.commit()
                                for i in Convicts_C_Name_Delete_ID:
                                    Convicts_C_Name_Delete_ID_Output=i
                                print("Record of convict with Convict ID",Convicts_Delete_ID,"is deleted.")
                                print("Convict with Convict ID",Convicts_Delete_ID,"is",Convicts_C_Name_Delete_ID_Output[0])
                                print()
                                break
                        elif Convicts_Delete_Choice==4:
                            Convicts_Delete_Name=input("Enter the full name of the convict whose record you wish to delete")
                            print
                            cur.execute("Select C_Name from incarcerated_workers")
                            VALID_NAME=cur.fetchall()
                            VALID=()
                            for i in VALID_NAME:
                                VALID+=i
                            if Convicts_Delete_Name not in VALID:
                                print("The entered name may have an error or the said person does not have a record")
                                print()
                            else:
                                cur.execute("Select C_ID from incarcerated_workers where C_Name = %s",(Convicts_Delete_Name,))
                                Convicts_C_ID_Delete_Name=cur.fetchall()
                                cur.execute("Delete from incarcerated_workers where C_Name = %s",(Convicts_Delete_Name,))
                                a.commit()
                                for i in Convicts_C_ID_Delete_Name:
                                    Convicts_C_ID_Delete_Name_Output=i
                                print(Convicts_Delete_Name, "'s record has been removed. Their C_ID is->",Convicts_C_ID_Delete_Name_Output[0])
                                print()
                                break
                        elif Convicts_Delete_Choice==5:
                            print()
                            break
                    else:
                        print("Invalid input")
                        print()

# DISPALYING RECORDS

            if Menu2==3:
                cur.execute("Select C_ID from incarcerated_workers")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to display records!")
                    print()
                else:
                    print("Enter 1 to check records of all workers")
                    print("Enter 2 to check record of specific convict ID")
                    print("Enter 3 to check record of specific worker name")
                    print("Enter 4 to check records from given range of convict IDs")
                    print("Enter 5 to go back")
                    print()
                    while True:
                        print("Enter 0 to see CONVICTS SELECT options")
                        Convicts_Select_Option=int(input("Enter your choice"))
                        print()
                        if Convicts_Select_Option==0:
                            print("Enter 1 to check records of all workers")
                            print("Enter 2 to check record of specific convict ID")
                            print("Enter 3 to check record of specific worker name")
                            print("Enter 4 to check records from given range of convict IDs")
                            print("Enter 5 to go back")
                            print()
                        elif Convicts_Select_Option==5:
                            print("Going back")
                            print()
                            break
                        elif Convicts_Select_Option==1:
                            cur.execute("Select * from incarcerated_workers")
                            Convicts_Select_All=cur.fetchall()
                            print("Table format-> Convict ID, Convict Name, Department,Assignment Date,Wages")
                            print()
                            i=1
                            for convict in Convicts_Select_All:
                                  print("Entry",i,"->   ",end="")
                                  print(convict[0]," - ",end="")
                                  print(convict[1]," - ",end="")
                                  print(convict[2]," - ",end="")
                                  print(convict[3]," - ",end="")
                                  print(convict[4])
                                  print()
                                  i+=1
                        elif Convicts_Select_Option==2:
                            while True:
                                Convicts_Select_Single_ID=int(input("Enter the convict ID whose record you wish to see"))
                                cur.execute("Select C_ID from incarcerated_workers")
                                INVALID_ID=cur.fetchall()
                                INVALID=()
                                for i in INVALID_ID:
                                    i2=i
                                    INVALID=INVALID+i2
                                if INVALID==():
                                    print("No records exist")
                                elif Convicts_Select_Single_ID in INVALID:
                                    cur.execute("Select * from incarcerated_workers where C_ID = %s",(Convicts_Select_Single_ID,))
                                    Convicts_Select_All=cur.fetchall()
                                    print("Table format-> Convict ID, Convict Name, Department,Assignment Date,Wages")
                                    print()
                                    i=1
                                    for convict in Convicts_Select_All:
                                          print("Entry",i,"->   ",end="")
                                          print(convict[0]," - ",end="")
                                          print(convict[1]," - ",end="")
                                          print(convict[2]," - ",end="")
                                          print(convict[3]," - ",end="")
                                          print(convict[4])
                                          print()
                                          i+=1
                                    print()
                                    break
                                else:
                                    print("This ID does not exist")
                                    print()
                        elif Convicts_Select_Option==3:
                            Convicts_Select_Single_Name=input("Enter the convict name whose record you wish to see")
                            print()
                            cur.execute("Select C_Name from incarcerated_workers")
                            INVALID_NAME=cur.fetchall()
                            INVALID=()
                            for i in INVALID_NAME:
                                i2=i
                                INVALID=INVALID+i2
                            if Convicts_Select_Single_Name in INVALID:
                                cur.execute("Select * from incarcerated_workers where C_Name = %s",(Convicts_Select_Single_Name,))
                                Convicts_Select_All=cur.fetchall()
                                print("Table format-> Convict ID, Convict Name, Department,Assignment Date,Wages")
                                print()
                                i=1
                                for convict in Convicts_Select_All: 
                                    print("Entry",i,"->   ",end="")
                                    print(convict[0]," - ",end="")
                                    print(convict[1]," - ",end="")
                                    print(convict[2]," - ",end="")
                                    print(convict[3]," - ",end="")
                                    print(convict[4])
                                    print()
                                    i+=1
                                print()
                            else:
                                print("This name does not exist")
                                print()
                        elif Convicts_Select_Option==4:
                             Convicts_Select_Range_Start=int(input("Enter convict ID for start value of range"))
                             Convicts_Select_Range_End=int(input("Enter convict ID for end value of range"))
                             print()
                             if Convicts_Select_Range_Start<0:
                                print("Start value must be 1 or more")
                                print()
                             elif Convicts_Select_Range_Start>Convicts_Select_Range_End:
                                 print("Start value must be less than end value")
                             else:
                                 cur.execute("Select * from incarcerated_workers where C_ID between %s and %s",(Convicts_Select_Range_Start,Convicts_Select_Range_End))
                                 Convicts_Select_All=cur.fetchall()
                                 print("Table format-> Convict ID, Convict Name, Department,Assignment Date,Wages")
                                 print()
                                 i=1
                                 for convict in Convicts_Select_All:
                                     print("Entry",i,"->   ",end="")
                                     print(convict[0]," - ",end="")
                                     print(convict[1]," - ",end="")
                                     print(convict[2]," - ",end="")
                                     print(convict[3]," - ",end="")
                                     print(convict[4])
                                     print()
                                     i+=1
                        else:
                            print("Invalid input")
                            print()

# UPDATE IN WORKERS TABLE

            if Menu2==4:
                cur.execute("Select C_ID from incarcerated_workers")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to display records!")
                    print()
                else:
                    print("Enter 1 to update Assignment Date of worker")
                    print("Enter 2 to update Department of worker")
                    print("Enter 3 to update wage of worker")
                    print("Enter 4 to go back")
                    print()
                    while True:
                        print("Enter 0 to see CONVICTS SELECT options")
                        Convicts_Select_Option=int(input("Enter your choice"))
                        print()
                        if Convicts_Select_Option==0:
                            print("Enter 1 to update Assignment Date of worker")
                            print("Enter 2 to update Department of worker")
                            print("Enter 3 to update wage of worker")
                            print("Enter 4 to go back")
                            print()
                        elif Convicts_Select_Option==1:
                            Convicts_Update_Date_Old=int(input("Enter the convicts ID whose assignment date you wish to update"))
                            print()
                            cur.execute("Select C_ID from incarcerated_workers")
                            INVALID_ID=cur.fetchall()
                            INVALID=()
                            for i in INVALID_ID:
                                i2=i
                                INVALID=INVALID+i2
                                if Convicts_Update_Date_Old not in INVALID:
                                    print("This convict ID does not exist")
                                    print()
                                else:
                                    Convicts_Update_Date_New=input("Enter the new Assignment date of the given convict ID")
                                    print()
                                    if len(Convicts_Update_Date_New)<10 or len(Convicts_Update_Date_New)>10:
                                        print("Invalid amount of characters date, ensure you are following the format [YYYY-MM-DD]")
                                        print()
                                    elif int(Convicts_Update_Date_New[5])>1 or int(Convicts_Update_Date_New[5])==1 and int(Convicts_Update_Date_New[6])>2 or Convicts_Update_Date_New[4]!="-" or Convicts_Update_Date_New[7]!="-":
                                        print("Invalid date, follow the format please or check that date exists.")
                                        print()
                                    else:
                                        cur.execute("Update incarcerated_workers set Assignment_Date = %s where C_ID = %s",(Convicts_Update_Date_New,Convicts_Update_Date_Old))
                                        a.commit()
                        elif Convicts_Select_Option==2:
                            Convicts_Update_Date_Old=int(input("Enter the convicts ID whose department you wish to update"))
                            print()
                            cur.execute("Select C_ID from incarcerated_workers")
                            INVALID_ID=cur.fetchall()
                            INVALID=()
                            for i in INVALID_ID:
                                i2=i
                                INVALID=INVALID+i2
                                if Convicts_Update_Date_Old not in INVALID:
                                    print("This convict ID does not exist")
                                    print()
                                else:
                                    New_Dept=input("Enter the new department of the convict")
                                    if len(New_Dept)>20:
                                        print("Department name too long!")
                                    else:
                                        cur.execute("Update incarcerated_workers set Department = %s where C_ID = %s",(New_Dept,Convicts_Update_Date_Old))
                                        a.commit()
                        elif Convicts_Select_Option==3:
                            Convicts_Update_Date_Old=int(input("Enter the convicts ID whose department you wish to update"))
                            print()
                            cur.execute("Select C_ID from incarcerated_workers")
                            INVALID_ID=cur.fetchall()
                            INVALID=()
                            for i in INVALID_ID:
                                i2=i
                                INVALID=INVALID+i2
                                if Convicts_Update_Date_Old not in INVALID:
                                    print("This convict ID does not exist")
                                    print()
                                else:
                                    New_Wage=int(input("Enter the new wage of the convict"))
                                    if New_Wage<0:
                                        print("Enter a valid wage amount!")
                                    else:
                                        cur.execute("Update incarcerated_workers set Wage = %s where C_ID = %s",(New_Wage,Convicts_Update_Date_Old))
                                        a.commit()
                        elif Convicts_Select_Option==4:
                            print("Going back")
                            print()
                            break
            elif Menu2==5:
                print()
                break
            elif Menu2 not in (0,1,2,3,4,5):
                print("Invalid input")
                print()

# PAROLES TABLE

    if Menu1==4:
        print("Enter 1 if you wish to enter a record")
        print("Enter 2 if you wish to delete record of parole")
        print("Enter 3 if you wish to display records")
        print("Enter 4 if you wish to go back")
        print()
        while True:
            print("Enter 0 to see TABLE-PAROLES options again")
            Menu2=int(input("Enter your desired action from above menu->"))
            print()
            if Menu2==0:
                print("Enter 1 if you wish to enter a record")
                print("Enter 2 if you wish to delete record of fired worker")
                print("Enter 3 if you wish to display records")
                print("Enter 4 if you wish to go back")
                print()
            elif Menu2==1:
                while True:
                    Confirm_Insert_Convicts=int(input("Enter 1 if you wish to insert a record. Enter 0 to go back"))
                    print()
                    if Confirm_Insert_Convicts==0:
                        print()
                        break
                    elif Confirm_Insert_Convicts==1:
                        Convicts_ID = int(input("Enter Convict's ID "))
                        Convicts_Date = input("Enter Date of parole [YYYY-MM-DD] ")

# ENSURING THAT INPUT IS VALID
                        
                        cur.execute("Select C_ID from paroles")
                        INVALID_ID=cur.fetchall()
                        INVALID=(0,)
                        for i in INVALID_ID:
                            i2=i
                            INVALID=INVALID+i2
                        cur.execute("Select C_Name from paroles")
                        INVALID_NAME=cur.fetchall()
                        INVALID_N=()
                        for i in INVALID_NAME:
                            i2=i
                            INVALID_N=INVALID_N+i2
                        cur.execute("Select C_ID from convicts")
                        INVALID_IDD=cur.fetchall()
                        INVALIDD=(0,)
                        for i in INVALID_IDD:
                            i2=i
                            INVALIDD=INVALIDD+i2
                        if Convicts_ID in INVALID:
                            print("This ID already exists.")
                            print()
                        elif Convicts_ID not in INVALIDD:
                            print("This ID doesn't exist in convicts")
                        elif Convicts_Date=="":
                            print("Date should not be left empty!")
                        elif len(Convicts_Date) != 10:
                            print("Invalid amount of characters in date, ensure you are following the format [YYYY-MM-DD]")
                            print()
                        elif Convicts_Date[4]!="-" or Convicts_Date[7]!="-":
                            print("Invalid date format, please separate terms using dashes [YYYY-MM-DD].")
                            print()
                        elif int(Convicts_Date[5])==1 and int(Convicts_Date[6])>2 or int(Convicts_Date[8])>3 or int(Convicts_Date[8])==3 and int(Convicts_Date[9])>1:
                            print("Invalid Date")
                        else:
                            cur.execute("Select Booking_Date from convicts where C_ID=%s",(Convicts_ID,))
                            B_Date=cur.fetchall()
                            cur.execute("Select C_Name from convicts where C_ID=%s",(Convicts_ID,))
                            Convicts_Name=cur.fetchall()
                            cur.execute("INSERT INTO paroles VALUES (%s,%s,%s,%s)",(Convicts_ID, Convicts_Name[0][0], B_Date[0][0], Convicts_Date))
                            a.commit()
                            print("Record entered---->","| ID->",Convicts_ID,"| Name->",Convicts_Name[0][0], " |Booking Date->",B_Date[0][0],"|Parole Date->",Convicts_Date)
                            print()
                            break
                    else:
                        print("Invalid input")
                        print()
                        
# DELETE

            elif Menu2==2:
                cur.execute("Select C_ID from paroles")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to delete records!")
                    print()
                else:
                    while True:
                        print("Enter 1 if you wish to delete all records from table")
                        print("Enter 2 if you wish to delete a range of records using convict ID")
                        print("Enter 3 if you wish to delete a record via Convict's ID")
                        print("Enter 4 if you wish to delete a record via Convict's Name")
                        print("Enter 5 if you wish to go back")
                        Convicts_Delete_Choice=int(input("Enter your choice here"))
                        print()
                        if Convicts_Delete_Choice==1:
                            while True:
                                CONFIRMATION=int(input("Enter 1 to confirm deletion of all records. Enter 0 to go back"))
                                print()
                                if CONFIRMATION==1:
                                    cur.execute("Delete from paroles")
                                    a.commit()
                                    print("All records deleted from paroles table")
                                    print()
                                    break
                                elif CONFIRMATION==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Delete_Choice==2:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 to go back"))
                                if Confirm==1:
                                    Convicts_Delete_Range_Start=int(input("Enter the convict ID for start value of deletion of range. Must be smaller than end value"))
                                    Convicts_Delete_Range_End=int(input("Enter the convict ID for end value of deletion of range."))
                                    print()
                                    if Convicts_Delete_Range_Start<1:
                                        print("Start ID must be greater than or equal to 1")
                                        print()
                                    elif Convicts_Delete_Range_Start>Convicts_Delete_Range_End:
                                        print("Start value must be smaller than end value")
                                        print()
                                    else:
                                        cur.execute("Delete from paroles where C_ID between %s and %s",(Convicts_Delete_Range_Start,Convicts_Delete_Range_End))
                                        a.commit()
                                        print("Given range of records have been deleted")
                                        print()
                                        break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Delete_Choice==3:
                            Convicts_Delete_ID=int(input("Enter the convict's ID whose record you wish to delete"))
                            cur.execute("Select C_ID from paroles")
                            INVALID_ID=cur.fetchall()
                            INVALID=()
                            for i in INVALID_ID:
                                i2=i
                                INVALID=INVALID+i2
                            if Convicts_Delete_ID not in INVALID:
                                print("This Convict ID does not exist")
                                print()
                            else:
                                cur.execute("Select C_Name from paroles where C_ID = %s",(Convicts_Delete_ID,))
                                Convicts_C_Name_Delete_ID=cur.fetchall()
                                cur.execute("Delete from paroles where C_ID = %s", (Convicts_Delete_ID,))
                                a.commit()
                                for i in Convicts_C_Name_Delete_ID:
                                    Convicts_C_Name_Delete_ID_Output=i
                                print("Record of convict with Convict ID",Convicts_Delete_ID,"is deleted.")
                                print("Convict with Convict ID",Convicts_Delete_ID,"is",Convicts_C_Name_Delete_ID_Output[0])
                                print()
                                break
                        elif Convicts_Delete_Choice==4:
                            Convicts_Delete_Name=input("Enter the full name of the convict whose record you wish to delete")
                            print
                            cur.execute("Select C_Name from paroles")
                            VALID_NAME=cur.fetchall()
                            VALID=()
                            for i in VALID_NAME:
                                VALID+=i
                            if Convicts_Delete_Name not in VALID:
                                print("The entered name may have an error or the said person does not have a record")
                                print()
                            else:
                                cur.execute("Select C_ID from paroles where C_Name = %s",(Convicts_Delete_Name,))
                                Convicts_C_ID_Delete_Name=cur.fetchall()
                                cur.execute("Delete from paroles where C_Name = %s",(Convicts_Delete_Name,))
                                a.commit()
                                for i in Convicts_C_ID_Delete_Name:
                                    Convicts_C_ID_Delete_Name_Output=i
                                print(Convicts_Delete_Name, "'s record has been removed. Their C_ID is->",Convicts_C_ID_Delete_Name_Output[0])
                                print()
                                break
                        elif Convicts_Delete_Choice==5:
                            print()
                            break
                    else:
                        print("Invalid input")
                        print()

# DISPALYING RECORDS

            if Menu2==3:
                cur.execute("Select C_ID from paroles")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to display records!")
                    print()
                else:
                    print("Enter 1 to check records of all workers")
                    print("Enter 2 to check record of specific convict ID")
                    print("Enter 3 to check record of specific convict name")
                    print("Enter 4 to check records from given range of convict IDs")
                    print("Enter 5 to go back")
                    print()
                    while True:
                        print("Enter 0 to see INCARECERATED WORKERS SELECT options")
                        Convicts_Select_Option=int(input("Enter your choice"))
                        print()
                        if Convicts_Select_Option==0:
                            print("Enter 1 to check records of all workers")
                            print("Enter 2 to check record of specific convict ID")
                            print("Enter 3 to check record of specific worker name")
                            print("Enter 4 to check records from given range of convict IDs")
                            print("Enter 5 to go back")
                            print()
                        elif Convicts_Select_Option==5:
                            print("Going back")
                            print()
                            break
                        elif Convicts_Select_Option==1:
                            cur.execute("Select * from paroles")
                            Convicts_Select_All=cur.fetchall()
                            print("Table format-> Convict ID, Convict Name, Booking Date, Parole Date")
                            print()
                            i=1
                            for convict in Convicts_Select_All:
                                  print("Entry",i,"->   ",end="")
                                  print(convict[0]," - ",end="")
                                  print(convict[1]," - ",end="")
                                  print(convict[2]," - ",end="")
                                  print(convict[3])
                                  print()
                                  i+=1
                        elif Convicts_Select_Option==2:
                            while True:
                                Convicts_Select_Single_ID=int(input("Enter the convict ID whose record you wish to see"))
                                cur.execute("Select C_ID from paroles")
                                INVALID_ID=cur.fetchall()
                                INVALID=()
                                for i in INVALID_ID:
                                    i2=i
                                    INVALID=INVALID+i2
                                if INVALID==():
                                    print("No records exist")
                                elif Convicts_Select_Single_ID in INVALID:
                                    cur.execute("Select * from paroles where C_ID = %s",(Convicts_Select_Single_ID,))
                                    Convicts_Select_All=cur.fetchall()
                                    print("Table format-> Convict ID, Convict Name, Booking Date, Parole Date")
                                    print()
                                    i=1
                                    for convict in Convicts_Select_All:
                                        print("Entry",i,"->   ",end="")
                                        print(convict[0]," - ",end="")
                                        print(convict[1]," - ",end="")
                                        print(convict[2]," - ",end="")
                                        print(convict[3])
                                    print()
                                    i+=1
                                    break
                                else:
                                    print("This ID does not exist")
                                    print()
                        elif Convicts_Select_Option==3:
                            Convicts_Select_Single_Name=input("Enter the convict name whose record you wish to see")
                            print()
                            cur.execute("Select C_Name from paroles")
                            INVALID_NAME=cur.fetchall()
                            INVALID=()
                            for i in INVALID_NAME:
                                i2=i
                                INVALID=INVALID+i2
                            if Convicts_Select_Single_Name in INVALID:
                                cur.execute("Select * from paroles where C_Name = %s",(Convicts_Select_Single_Name,))
                                Convicts_Select_All=cur.fetchall()
                                print("Table format-> Convict ID, Convict Name, Booking Date, Parole Date")
                                print()
                                i=1
                                for convict in Convicts_Select_All:
                                    print("Entry",i,"->   ",end="")
                                    print(convict[0]," - ",end="")
                                    print(convict[1]," - ",end="")
                                    print(convict[2]," - ",end="")
                                    print(convict[3])
                                    print()
                                    i+=1
                            else:
                                print("This name does not exist")
                                print()
                        elif Convicts_Select_Option==4:
                             Convicts_Select_Range_Start=int(input("Enter convict ID for start value of range"))
                             Convicts_Select_Range_End=int(input("Enter convict ID for end value of range"))
                             print()
                             if Convicts_Select_Range_Start<0:
                                print("Start value must be 1 or more")
                                print()
                             elif Convicts_Select_Range_Start>Convicts_Select_Range_End:
                                 print("Start value must be less than end value")
                             else:
                                 cur.execute("Select * from paroles where C_ID between %s and %s",(Convicts_Select_Range_Start,Convicts_Select_Range_End))
                                 Convicts_Select_All=cur.fetchall()
                                 print("Table format-> Convict ID, Convict Name, Booking Date, Parole Date")
                                 print()
                                 i=1
                                 for convict in Convicts_Select_All:
                                     print("Entry",i,"->   ",end="")
                                     print(convict[0]," - ",end="")
                                     print(convict[1]," - ",end="")
                                     print(convict[2]," - ",end="")
                                     print(convict[3])
                                     print()
                                     i+=1   
                        else:
                            print("Invalid input")
                            print()
            elif Menu2==4:
                print("Going back")
                print()
                break
            elif Menu2 not in  (0,1,2,3,4):
                print("Invalid input")
                print()
    elif Menu1==5:
        print("Enter 1 if you wish to enter a record")
        print("Enter 2 if you wish to delete records")
        print("Enter 3 if you wish to update a record")
        print("Enter 4 if you wish to display all visit records")
        print("Enter 5 if you wish to go back")
        print()
        while True:
            print("Enter 0 to see TABLE VISITORS options again")
            Menu2=int(input("Enter your desired action from above menu->"))
            print()
            if Menu2==0:
                print("Enter 1 if you wish to enter a record")
                print("Enter 2 if you wish to delete a record")
                print("Enter 3 if you wish to update a record")
                print("Enter 4 if you wish to display all visit records")
                print("Enter 5 if you wish to go back")
                print()
                
# INSERTING VALUES
    
            elif Menu2==1:
                while True:
                    Confirm_Insert_Convicts=int(input("Enter 1 if you wish to insert a record. Enter 0 to go back"))
                    print()
                    if Confirm_Insert_Convicts==0:
                        print()
                        break
                    elif Confirm_Insert_Convicts==1:
                        Convicts_ID = int(input("Enter the visit number "))
                        Convicts_Name = input("Enter the visitor's Full Name ")
                        Convicts_Level = int(input("Enter the ID of the convict being visited "))
                        Convicts_Date = input("Enter Date of Visiting [YYYY-MM-DD]")
                        Convicts_Contact=int(input("Enter the visitor's contact number"))
                        print()
                        
                        # ENSURING THAT INPUT IS VALID
                        cur.execute("Select VIsit_Number from visitors")
                        INVALID_ID=cur.fetchall()
                        INVALID=(0,)
                        for i in INVALID_ID:
                            i2=i
                            INVALID=INVALID+i2
                        cur.execute("Select C_ID from convicts")
                        INVID=cur.fetchall()
                        INVI=()
                        for j in INVID:
                            INVI+=j
                        if Convicts_Level not in INVI:
                            print("That Convict ID doesn't exist in Convicts table")
                            print()
                        elif Convicts_ID in INVALID:
                            print("This ID already exists, the next id is->",INVALID[-1]+1)
                            print()
                        elif Convicts_Name=="" or Convicts_Date=="":
                            print("No field should be left empty!")
                        elif Convicts_ID>=INVALID[-1]+2:
                            print("This ID is beyond the sequence, the next id is->",INVALID[-1]+1)
                            print()
                        elif len(Convicts_Date) != 10:
                            print("Invalid amount of characters in date, ensure you are following the format [YYYY-MM-DD]")
                            print()
                        elif Convicts_Date[4]!="-" or Convicts_Date[7]!="-":
                            print("Invalid date format, please separate terms using dashes [YYYY-MM-DD].")
                            print()
                        elif int(Convicts_Date[5])==1 and int(Convicts_Date[6])>2 or int(Convicts_Date[8])>3 or int(Convicts_Date[8])==3 and int(Convicts_Date[9])>1:
                            print("Invalid Date")
                        elif len(Convicts_Name)>25:
                            print("Visitor name is too long [Max 25 characters]")
                            print()
                        elif len(str(Convicts_Contact)) != 10:
                            print("Invalid contact number, it must be of 10 digits")
                        else:
                            cur.execute("select C_Name from convicts where C_ID=%s",(Convicts_Level,))
                            name=cur.fetchall()
                            cur.execute("INSERT INTO visitors VALUES (%s,%s,%s,%s,%s,%s)",(Convicts_ID, Convicts_Name, name[0][0], Convicts_Level, Convicts_Date,Convicts_Contact))
                            a.commit()
                            print("Record entered---->","| ID->",Convicts_ID,"| Name->",Convicts_Name,"| Convict visiting->",name[0][0],"| Convict ID->",Convicts_Level, " |Visiting Date->",Convicts_Date," |Visitor contact->",Convicts_Contact)
                            print()
                            break
                    else:
                        print("Invalid input")
                        print()
            elif Menu2==2:
                cur.execute("Select visit_number from visitors")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to delete records!")
                    print()
                else:
                    while True:
                        print("Enter 1 if you wish to delete all records from table")
                        print("Enter 2 if you wish to delete a range of records using visit number")
                        print("Enter 3 if you wish to delete a record via visit number")
                        print("Enter 4 if you wish to delete a record via visitor's Name")
                        print("Enter 5 if you wish to go back")
                        Convicts_Delete_Choice=int(input("Enter your choice here"))
                        print()
                        if Convicts_Delete_Choice==1:
                            while True:
                                CONFIRMATION=int(input("Enter 1 to confirm deletion of all records. Enter 0 to go back"))
                                print()
                                if CONFIRMATION==1:
                                    cur.execute("Delete from visitors")
                                    a.commit()
                                    print("All records deleted from visitors table")
                                    print()
                                    break
                                elif CONFIRMATION==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Delete_Choice==2:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 to go back"))
                                if Confirm==1:
                                    Convicts_Delete_Range_Start=int(input("Enter the visit number for start value of deletion of range. Must be smaller than end value"))
                                    Convicts_Delete_Range_End=int(input("Enter the visit number for end value of deletion of range."))
                                    print()
                                    if Convicts_Delete_Range_Start<1:
                                        print("Start value must be greater than or equal to 1")
                                        print()
                                    elif Convicts_Delete_Range_Start>Convicts_Delete_Range_End:
                                        print("Start value must be smaller than end value")
                                        print()
                                    else:
                                        cur.execute("Delete from visitors where visit_number between %s and %s",(Convicts_Delete_Range_Start,Convicts_Delete_Range_End))
                                        a.commit()
                                        print("Given range of records have been deleted")
                                        print()
                                        break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Delete_Choice==3:
                            Convicts_Delete_ID=int(input("Enter the visit number whose record you wish to delete"))
                            cur.execute("Select visit_number from visitors")
                            INVALID_ID=cur.fetchall()
                            INVALID=()
                            for i in INVALID_ID:
                                i2=i
                                INVALID=INVALID+i2
                            if Convicts_Delete_ID not in INVALID:
                                print("This visit number does not exist")
                                print()
                            else:
                                cur.execute("Delete from visitors where visit_number = %s", (Convicts_Delete_ID,))
                                a.commit()
                                for i in Convicts_C_Name_Delete_ID:
                                    Convicts_C_Name_Delete_ID_Output=i
                                print("Record of visit number",Convicts_Delete_ID,"is deleted.")
                                print()
                                break
                        elif Convicts_Delete_Choice==4:
                            Convicts_Delete_Name=input("Enter the full name of the visitor whose record you wish to delete")
                            print
                            cur.execute("Select visitor_Name from visitors")
                            VALID_NAME=cur.fetchall()
                            VALID=()
                            for i in VALID_NAME:
                                VALID+=i
                            if Convicts_Delete_Name not in VALID:
                                print("The entered name may have an error or the said person does not have a record")
                                print()
                            else:
                                cur.execute("Select visit_number from visitors where Visitor_Name = %s",(Convicts_Delete_Name,))
                                Convicts_C_ID_Delete_Name=cur.fetchall()
                                cur.execute("Delete from visitors where Visitor_Name = %s",(Convicts_Delete_Name,))
                                a.commit()
                                for i in Convicts_C_ID_Delete_Name:
                                    Convicts_C_ID_Delete_Name_Output=i
                                print(Convicts_Delete_Name, "'s record has been removed. Their visit_number is->",Convicts_C_ID_Delete_Name_Output[0])
                                print()
                                break
                        elif Convicts_Delete_Choice==5:
                            print()
                            break
                        else:
                            print("Invalid input")
                            print()
       
# UPDATE RECORDS AND CHECKING IF THE UPDATE IS VALID

            elif Menu2==3:
                cur.execute("Select Visit_Number from visitors")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to update records!")
                    print()
                else:
                    print("Enter 1 if you wish to update visitor name")
                    print("Enter 2 if you wish to update the convict ID of the convict being visited")
                    print("Enter 3 if you wish to update visit date")
                    print("Enter 4 if you wish to update Contact")
                    print("Enter 5 if you wish to go back")
                    print()
                    while True:
                        print("Enter 0 if you wish to see UPDATE options again")
                        Convicts_Update=int(input("Enter your choice"))
                        print()
                        if Convicts_Update==8:
                            print()
                            break
                        elif Convicts_Update==0:
                            print("Enter 1 if you wish to update visitor name")
                            print("Enter 2 if you wish to update the convict ID of the convict being visited")
                            print("Enter 3 if you wish to update visit date")
                            print("Enter 4 if you wish to update Contact")
                            print("Enter 5 if you wish to go back")
                            print()
                        elif Convicts_Update==1:
                            Visitors_Update_Name_sitors_Update_Name_Old=input("Enter the visitor name you wish to update")
                            print()
                            cur.execute("Select Visitor_Name from visitors")
                            INVALID_NAME=cur.fetchall()
                            INVALID=()
                            for i in INVALID_NAME:
                                i2=i
                                INVALID=INVALID+i2
                            if Visitors_Update_Name_Old not in INVALID:
                                print("This visitor name does not exist")
                                print()
                            else:
                                Visitors_Update_Name_New=input("Enter the updated visitor name")
                                cur.execute("Select Visitor_Name from visitors")
                                INVALID_Name=cur.fetchall()
                                INVALID=()
                                for i in INVALID_Name:
                                    i2=i
                                    INVALID+=i2
                                if len(Visitors_Update_Name_New)>25:
                                    print("VIsitor name must be less than 25 characters")
                                    print()
                                elif Visitors_Update_Name_New=="":
                                    print("You didn't enter a new name!")
                                else:
                                    cur.execute("Update visitors set Visitor_Name = %s where Visitor_Name = %s",(Visitors_Update_Name_New,Visitors_Update_Name_Old))
                                    a.commit()
                                    print("The Visitor's name has been updated from",Visitors_Update_Name_Old,"to",Visitors_Update_Name_New)
                                    print()
                        elif Convicts_Update==2:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    C_Visit=int(input("Enter the visit number where you wish to update convict ID"))
                                    print()
                                    cur.execute("Select Visit_Number from visitors")
                                    INVALID_ID=cur.fetchall()
                                    INVALID=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALID=INVALID+i2
                                    if C_Visit not in INVALID:
                                        print("This visit number does not exist")
                                        print()
                                    else:
                                        C_Visit_New=int(input("Enter the updated convict ID"))
                                        cur.execute("select C_ID from convicts")
                                        invalidids=cur.fetchall()
                                        invalidids2=()
                                        for i in invalidids:
                                            invalidids2+=i
                                        if C_Visit_New not in invalidids2:
                                            print("This convict id doesn't exist in convicts table!")
                                        else:
                                            cur.execute("update visitors set C_ID = %s where visit_number = %s",(C_Visit_New,C_Visit))
                                            cur.execute("select C_Name from convicts where C_ID = %s",(C_Visit_New,))
                                            newname=cur.fetchall()
                                            cur.execute("update visitors set visiting = %s where visit_number = %s",(newname[0][0],C_Visit))
                                            a.commit()
                                            break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Update==3:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Convicts_Update_Date_Old=int(input("Enter the visit number where you wish to update visiting date"))
                                    print()
                                    cur.execute("Select visit_number from visitors")
                                    INVALID_ID=cur.fetchall()
                                    INVALID=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALID=INVALID+i2
                                    if Convicts_Update_Date_Old not in INVALID:
                                        print("This visit number does not exist")
                                        print()
                                    else:
                                        Convicts_Update_Date_New=input("Enter the new visiting date of the given visit number")
                                        print()
                                        if len(Convicts_Update_Date_New)<10 or len(Convicts_Update_Date_New)>10:
                                            print("Invalid amount of characters date, ensure you are following the format [YYYY-MM-DD]")
                                            print()
                                        elif int(Convicts_Update_Date_New[5])>1 or int(Convicts_Update_Date_New[5])==1 and int(Convicts_Update_Date_New[6])>2 or Convicts_Update_Date_New[4]!="-" or Convicts_Update_Date_New[7]!="-":
                                            print("Invalid date, follow the format please or check that date exists.")
                                            print()
                                        else:
                                            cur.execute("Update visitors set Date = %s where visit_number = %s",(Convicts_Update_Date_New,Convicts_Update_Date_Old))
                                            a.commit()
                                            print("The visit date of given visit number",Convicts_Update_Date_Old,"has been updated to->",Convicts_Update_Date_New)
                                            print()
                                            break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                                else:
                                    print("Invalid input")
                                    print()
                        elif Convicts_Update==4:
                            while True:
                                Confirm=int(input("Enter 1 to continue, enter 0 if you wish to go back"))
                                print()
                                if Confirm==1:
                                    Convicts_Update_Contact_Old=int(input("Enter the visit number where you wish to update Contact"))
                                    print()
                                    cur.execute("Select Visit_number from visitors")
                                    INVALID_ID=cur.fetchall()
                                    INVALID=()
                                    for i in INVALID_ID:
                                        i2=i
                                        INVALID=INVALID+i2
                                    if Convicts_Update_Contact_Old not in INVALID:
                                        print("This visit numbr does not exist")
                                        print()
                                    else:
                                        while True:
                                            Convicts_Update_Contact_New=int(input("Enter the updated contact"))
                                            if len(str(Convicts_Update_Contact_New))!=10:
                                                print("Contact number should be exactly 10 digits!")
                                                print()
                                            else:
                                                cur.execute("Update visitors set Contact = %s where Visit_number = %s",(Convicts_Update_Contact_New,Convicts_Update_Contact_Old))
                                                a.commit()
                                                print("Contact updated")
                                                print()
                                                break
                                elif Confirm==0:
                                    print("Going back")
                                    print()
                                    break
                        elif Convicts_Update==5:
                            print("Going back")
                            print()
                            break
                        else:
                            print("Invalid input")
                            print()
            elif Menu2==4:
                cur.execute("Select Visit_Number from visitors")
                INVALID_ID=cur.fetchall()
                INVALID=()
                for i in INVALID_ID:
                    i2=i
                    INVALID=INVALID+i2
                if INVALID==():
                    print("Enter records before attempting to update records!")
                    print()
                else:
                    cur.execute("Select * from visitors")
                    Convicts_Select_All=cur.fetchall()
                    print("Table format-> Visit number, Visitor Name, Visiting, Convict ID, Date of visiting, Visitor's contact")
                    print()
                    i=1
                    for convict in Convicts_Select_All:
                        print("Entry",i,"->   ",end="")
                        print(convict[0]," - ",end="")
                        print(convict[1]," - ",end="")
                        print(convict[2]," - ",end="")
                        print(convict[3]," - ",end="")
                        print(convict[4]," - ",end="")
                        print(convict[5])
                        print()
                        i+=1
            elif Menu2==5:
                print("Going back")
                print()
                break

#REPORTS MENU
            
    elif Menu1==6:
        while True:
            print("Enter 1 to see how many convicts are currently in prison")
            print("Enter 2 to see how many staff members are currently working in prison")
            print("Enter 3 to see average salaries of staff members")
            print("Enter 4 to see average wage of all incarcerated workers")
            print("Enter 5 to see how many incarcerated workers are currently working")
            print("Enter 6 to see how many total visits have taken place")
            print("Enter 7 to see how many visits a convict has got via convict ID")
            print("Enter 8 to see how many guards are currently working")
            print("Enter 9 to see how many convicts have been released")
            print("Enter 10 to see how many paroles are currently active")
            print("Enter 11 to go back")
            Menu3=int(input("Enter your choice from above"))
            print()
            if Menu3==1:
                cur.execute("select count(C_ID) from convicts")
                out=cur.fetchone()
                if out==():
                    print("No prisoners currently in prison")
                    print()
                else:
                    print(out[0], "prisoners are currently in prison")
                    print()
            elif Menu3==2:
                cur.execute("select count(S_ID) from staff")
                out=cur.fetchone()
                if out==():
                    print("No staff members currently working in prison")
                    print()
                else:
                    print(out[0], "staff members are currently working in prison")
                    print()
            elif Menu3==3:
                cur.execute("select avg(salary) from staff_salaries")
                out=cur.fetchone()
                if out==():
                    print("No staff members currently working in prison, hence no salaries")
                    print()
                else:
                    print(out[0], "is the average salary of all workers")
                    print()
            elif Menu3==4:
                cur.execute("select avg(wage) from incarcerated_workers")
                out=cur.fetchone()
                if out==():
                    print("No incarcerated workers currently in prison")
                    print()
                else:
                    print(out[0], "is the average wage of incarcerated workers in prison")
                    print()
            elif Menu3==5:
                cur.execute("select count(C_ID) from incarcerated_workers")
                out=cur.fetchone()
                if out==():
                    print("No incarcerated workers currently in prison")
                    print()
                else:
                    print(out[0], "incarcerated workers are currently in prison")
                    print()
            elif Menu3==6:
                cur.execute("select count(visit_number) from visitors")
                out=cur.fetchone()
                if out==():
                    print("No visits have taken palce")
                    print()
                else:
                    print(out[0], "visits have taken place")
                    print()
            elif Menu3==7:
                ConvictV = int(input("Enter the convict ID of the convict whose number of visits you wish to see"))
                print()
                cur.execute("select count(*) from visitors where C_ID=%s", (ConvictV,))
                visits = cur.fetchone()
                visits2=visits[0]
                if visits2>0:
                    print("Number of visits of the given convict ID is", visits2)
                    print()
                else:
                    print("No visits found for the convict with given convict ID")
                    print()
            elif Menu3==8:
                cur.execute("select count(S_ID) from staff where Designation='Guard'")
                out=cur.fetchone()
                if out==():
                    print("No guards currently working in prison")
                    print()
                else:
                    print(out[0], "guards are currently working in prison")
                    print()
            elif Menu3==9:
                cur.execute("select count(Release_Number) from releases")
                out=cur.fetchone()
                if out==():
                    print("No releases as of yet")
                    print()
                else:
                    print(out[0], "releases have taken place")
                    print()
            elif Menu3==10:
                cur.execute("select count(C_ID) from paroles")
                out=cur.fetchone()
                if out==():
                    print("No paroles currently active")
                    print()
                else:
                    print(out[0], "paroles are currently active")
                    print()
            elif Menu3==11:
                print("Going back")
                print()
                break
            else:
                print("Invalid input")
                print()
    elif Menu1==7:
        print("Exitting")
        print()
        break
    elif Menu1 not in (1,2,3,4,5,6,7):
        print("Invalid input")
        print()

# END OF CODE, ENDING CONNECTION

a.close()


