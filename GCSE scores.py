import os

def menu():
    choice = 0
    while choice < 1 or choice > 6:
         print("Please choose an option:")
         print('1 - Create New File')
         print('2 - Add New Test Scores')
         print('3 - View All Student files')
         print('4 - View All Scores And Grades For Student')
         print('5 - Search For Grade In Subject')
         print('6 - Search For Grade In Subject For One Student')
         print()
         choice = int(input('enter choice: '))
    return choice

def newFile():
    name=input('enter first name: ')
    name2=input('enter surname: ')
    name3=name2+' '+name+'.txt'
    print(name3)
    new = False
    try:
        with open(name3, mode = 'r', encoding ='utf-8') as my_file:
            name3 = my_file.read().splitlines()
    except FileNotFoundError:
        new = True
        print('File Does Not Exist, We Will Start Taking Details Now')
        
    if new == True:
        subject=input('enter subject: ')
        marks=int(input('enter number of marks: '))
        pmarks=int(input('enter maximum number of possible marks: '))
        grade,percent=gradecalc(marks,pmarks)
        marks=str(marks)
        pmarks=str(pmarks)
        percent=str(percent)
        grade=str(grade)
        details=name2+','+name+','+subject+','+marks+','+pmarks+','+percent+','+grade
        print(details)
        with open(name3, mode='a',encoding='utf-8')as my_file:  
           name3=my_file.write(details+'\n')
        main()
        
    elif new == False:
        print('file already exists, please select option 2')
        print()
        input('press enter to return to menu')
        print()
        main()

def newScores():
    name=input('enter first name: ')
    name2=input('enter surname: ')
    name3=name2+' '+name+'.txt'
    print(name3)
    try:
        with open(name3, mode = 'r', encoding ='utf-8') as my_file:
            subject=input('enter subject: ')
        marks=int(input('enter number of marks: '))
        pmarks=int(input('enter maximum number of possible marks: '))
        grade,percent=gradecalc(marks,pmarks)
        marks=str(marks)
        pmarks=str(pmarks)
        percent=str(percent)
        grade=str(grade)
        name3=str(name3)
        add=name2+','+name+','+subject+','+marks+','+pmarks+','+percent+','+grade
        print(add)
        print(name3)
        with open(name3, mode='a',encoding='utf-8')as my_file:  
           ToAdd=my_file.write(add+'\n')
        main()

    except FileNotFoundError:
        print('file does not exist, please select option 1')
        print()
        input('press enter to return to menu')
        print()
        main()
    
        subject=input('enter subject: ')
        marks=int(input('enter number of marks: '))
        pmarks=int(input('enter maximum number of possible marks: '))
        grade,percent=gradecalc(marks,pmarks)
        marks=str(marks)
        pmarks=str(pmarks)
        percent=str(percent)
        grade=str(grade)
        name3=str(name3)
        details=name2+','+name+','+marks+','+pmarks+','+percent+'%'+','+grade
        print(details)
        print(name3)
        with open(name3, mode='a',encoding='utf-8')as my_file:  
           name3=my_file.write(details+'\n')
        main()

def viewAll():
    print()
    print('All Student Files: ')
    print()
    files = os.listdir()
    index=0
    while index < len(files):
        filename = files[index]
        if filename.endswith('.txt'):
            print(filename)
        index += 1
    print()
    input('press enter to return to menu')
    print()
    main()
        
def gradecalc(marks,pmarks):
    grade=0
    percent=marks/pmarks
    percent=percent*100
    if percent <10:
        grade='F'
    elif percent <20:
        grade=1
    elif percent <30:
        grade=2
    elif percent <40:
        grade=3
    elif percent <50:
        grade=4
    elif percent <60:
        grade=5
    elif percent <70:
        grade=6
    elif percent <80:
        grade=7
    elif percent <90:
        grade=8
    else:
        grade=9
        
    percent=percent
    percent=round(percent)
    print(percent,grade)
    return grade,percent

def viewGrades():
    name=input('enter first name: ')
    name2=input('enter surname: ')
    name3=name2+' '+name+'.txt'
    try:
        with open(name3, mode = 'r', encoding ='utf-8') as my_file:
            studentResults = my_file.read().splitlines()
            print()
        print('***Here are the results for:',name, name2,'***')
        print()
        totalResult = 0
        totalGrade = 0
        for counter in range(len(studentResults)):
            result = studentResults[counter].split(',')
            totalResult = totalResult + int(result[5])
            totalGrade = totalGrade + int(result[6])
            counter = counter + 1
            print('\t******************************************')
            print('\t\tSubject:',result[2])
            print('\t\tScore:',result[3],'out of:',result[4])
            print('\t\t',result[5],'%')
            print('\t\tGrade:',result[6])
            print('\t******************************************')
            print()
                  
        avgResult = totalResult / counter
        avgGrade = totalGrade / counter
        avgGrade = int(avgGrade)
        avgResult=round(avgResult)
        print('***Here Are The Statistics for:', name, name2,'***')
        print('\tAverage %:',avgResult)
        print('\tAverage Grade:',avgGrade)
        print()
        input('press enter to return to menu')
        print()
        main()
                  
                
    except FileNotFoundError:
        print('file does not exist, please select option 1')
        print()
        input('press enter to return to menu')
        print()
        main()

def veiwSub():
    sub=input('enter subject: ')
    files = os.listdir()
    index=0
    while index < len(files):
        filename = files[index]
        if filename.endswith('.txt'):
            with open(filename, mode = 'r', encoding ='utf-8') as my_file:
                studentResults = my_file.read().splitlines()
                print()
                print('***Here are the results for:',filename,'in',sub,'***')
                print()
                totalResult = 0
                totalGrade = 0
                for counter in range(len(studentResults)):
                    result = studentResults[counter].split(',')
                    if result[2] == sub:
                        totalResult = totalResult + int(result[5])
                        totalGrade = totalGrade + int(result[6])
                        counter = counter + 1
                        print('\t******************************************')
                        print('\t\tSubject:',result[2])
                        print('\t\tScore:',result[3],'out of:',result[4])
                        print('\t\t',result[5],'%')
                        print('\t\tGrade:',result[6])
                        print('\t******************************************')
                        print()
                              
                avgResult = totalResult / counter
                avgGrade = totalGrade / counter
                avgGrade = int(avgGrade)
                avgResult=round(avgResult)
                print('***Here Are The Statistics for:',filename,'***')
                print('\tAverage %:',avgResult)
                print('\tAverage Grade:',avgGrade)
                print()
                    
                index += 1
    input('press enter to return to menu')
    print()
    main()  

def veiwSubOne():
    name=input('enter first name: ')
    name2=input('enter surname: ')
    name3=name2+' '+name+'.txt'
    sub=input('enter subject: ')
    try:
        with open(name3, mode = 'r', encoding ='utf-8') as my_file:
            studentResults = my_file.read().splitlines()
            print()
        print('***Here are the results for:',name, name2,'in',sub,'***')
        print()
        totalResult = 0
        totalGrade = 0
        for counter in range(len(studentResults)):
            result = studentResults[counter].split(',')
            if result[2] == sub:
                totalResult = totalResult + int(result[5])
                totalGrade = totalGrade + int(result[6])
                counter = counter + 1
                print('\t******************************************')
                print('\t\tSubject:',result[2])
                print('\t\tScore:',result[3],'out of:',result[4])
                print('\t\t',result[5],'%')
                print('\t\tGrade:',result[6])
                print('\t******************************************')
                print()
                  
        avgResult = totalResult / counter
        avgGrade = totalGrade / counter
        avgGrade = int(avgGrade)
        avgResult=round(avgResult)
        print('***Here Are The Statistics for:', name, name2,'in',sub,'***')
        print('\tAverage %:',avgResult)
        print('\tAverage Grade:',avgGrade)
        print()
        input('press enter to return to menu')
        print()
        main()
                  
                
    except FileNotFoundError:
        print('file does not exist, please select option 1')
        print()
        input('press enter to return to menu')
        print()
        main()
     


def main():
    print('Welcome To Student Scores Interface')
    print()
    choice=menu()
    if choice == 1:
        newFile()
    elif choice == 2:
        newScores()
    elif choice == 3:
        viewAll()
    elif choice == 4:
        viewGrades()
    elif choice == 5:
        veiwSub()
    elif choice == 6:
        veiwSubOne()
    else:
        print('ERROR')
        menu()

main()
