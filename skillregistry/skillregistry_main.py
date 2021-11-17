import skillregistryfunctions as fd

loop = 'true'
while (loop == 'true'):
    username = input("Please enter your username: ")
    successful_login = 0
    for key, value in fd.skillRegister.items():
        if (username == key):
           successful_login = 1
           print("Logged in successfully as " + username)
           loop = 'false'
    if successful_login == 1:
        while True:
            print("WELCOME TO SKILLTECH")
            print("MY PROFILE")
            print('\n')
            print("1. View My Skills")
            print("2. Add Skills")
            print("3. Remove a Skill")
            print("4. Clear All Skills")
            print('\n')
            print("HELP OTHERS")
            print('\n')
            print("5. Provide Training")
            print("6. Provide Mentoring")
            print("7. Who Can I Help")
            print('\n')
            print("TRAINER & MENTORS")
            print('\n')
            print("8. People With My Skills")
            print("9. People With Other Skills")
            print("10. People With Extra Skills")
            print('\n')
            print("MY DEPENDENCIES")
            print('\n')
            print("11. For Team")
            print("12. For Organization")
            print('\n')
            print("SEARCH SKILLS")
            print('\n')
            print("13. Search People By Skill")
            print("14. Search Skill By People")
            print('\n')
            print("ACCOUNT")
            print('\n')
            print("15. Logout")
            print("16. Quit")
            choice = str(input("Enter your choice: "))
            if choice == '1':
                skills = fd.searchSkills(username.split())
                print("MySkills are: {}\n".format(str(skills)))
            elif choice == '2':
                new_skill = input("Enter the skills to be added: ")
                print(new_skill.split(','))
                new_skilladd = fd.addSkill(username,new_skill.split(','))
                print("The new skills are added. Now MySkills are: {}\n".format(fd.searchSkills(username.split())))
            elif choice == '3':
                remove_skill = input("Enter the skill to be removed: ")
                remove_skilllist = fd.removeSkill(username,remove_skill)
                print("The {} skill is removed. Now My Skills are: {}\n".format(remove_skill,fd.searchSkills(username.split())))
            elif choice == '4':
                clearskill = fd.clearallskills(username.split())
                print("All Skills are removed for me. Now My Skills are: {}\n".format(fd.searchSkills(username.split())))
            elif choice == '5':
                trainee_names = input("Enter the trainee names to whom training is provided: ")
                skill_names = input("Enter the skill names for which training is provided: ")
                providetraining = fd.provideTraining(trainee_names.split(','), skill_names.split(','))
                print("Skills are added for which training is provided: {}\n".format(fd.searchSkills(trainee_names.split(','))))
            elif choice == '6':
                trainee_names = input("Enter the trainee names to whom mentoring is provided: ")
                providementoring = fd.provideMentoring(username, trainee_names.split(','))
                print("Skills are added for trainees for whom mentoring is done: {}\n".format(fd.searchSkills(trainee_names.split(','))))
            elif choice == '7':
                traineesrequiringhelp = fd.whoCanIHelp(username)
                print("These are the trainees whom i can help: {}\n".format(traineesrequiringhelp))
            elif choice == '8':
                traineeshavingmyskills = fd.peopleWithMySkills(username)
                print("These are the people having my skills: {}\n".format(traineeshavingmyskills))
            elif choice == '9':
                pplwithotherskills = fd.peopleWithOtherSkills(username)
                print("These are the people having other skills than me: {}\n".format(pplwithotherskills))
            elif choice == '10':
                pplwithextraskills = fd.peoplewithextraskills(username)
                print("These are the people having extra skills than me: {}\n".format(pplwithextraskills))
            elif choice == '11':
                colleagues_names = input("Enter the colleagues names: ")
                mydepsdept = fd.myDependenciesindept(username, colleagues_names.split(','))
                print("These are the skills in my department having dependencies on me: {}\n".format(mydepsdept))
            elif choice == '12':
                mydeps = fd.myDependencies(username)
                print("These are the skills in organization having dependencies on me: {}\n".format(mydeps))
            elif choice == '13':
                skill_names = input("Enter the skill names to be searched for: ")
                ppl_with_skill = fd.searchPeople(skill_names.split(','))
                print("These are the people having the above mentioned skills: {}\n".format(ppl_with_skill))
            elif choice == '14':
                ppl_names = input("Enter the people names for which skills to be searched for: ")
                skillsppl = fd.searchSkills(ppl_names.split(','))
                print("These are the skills that above mentioned people have: {}\n".format(skillsppl))
            elif choice == '15':
                loop = 'true'
                print("Logging out Successfully\n\n")
                break
            elif choice == '16':
                loop = 'false'
                print("Quitting Successfully\n")
                break
            else:
                print("Wrong Choice\n")
    else:
        print("Incorrect Username entered")
        pass
