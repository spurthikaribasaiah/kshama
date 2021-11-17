skillRegister = {
    "John" : {"HTML5","CSS","JavaScript","JQuery","Angular","React"},
    "Smith" : {"Azure Devops","Adobe XD","Java","C#"},
    "Boult" : {"Mongo DB","Fresh Chat","Android","Python","Whimsical"},
    "Will" : {"Swagger","CMS","Visual Studio","TFS","PostMan"},
    "Ethan" : {"Burp","CSS","Adobe XD","Java","Python","PostMan"},
    "Mike" : {"JavaScript","jQuery","React"},
    "Daniel" : {"HTML5","CSS","JavaScript","jQuery","Angular","React","Azure Devops","Adobe XD","Java","C#"}
}

def searchSkills(names):
   result = {}
   for name in names:
      for key, value in skillRegister.items():
         if key == name:
            result.update({key:value})

   return result

def searchPeople(skillset):
    spresult = {}
    for skill in skillset:
        ppllist = []
        for key, value in skillRegister.items():
            if skill in value:
                ppllist.append(key)
        spresult.update({skill: ppllist})

    return spresult

def addSkill(name,skill):
    for key, value in skillRegister.items():
        if key == name:
           value.update(skill)

    return skillRegister

def removeSkill(name, skill):
    for key, value in skillRegister.items():
        if key == name and skill in value:
            value.discard(skill)

    return skillRegister

def clearallskills(names):
    for name in names:
        for key, value in skillRegister.items():
            if key == name:
                value.clear()

    return skillRegister

def provideTraining(traineeNames,skill):
    for name in traineeNames:
        for key, value in skillRegister.items():
            if key == name:
                value.update(skill)

    return skillRegister

def provideMentoring(myName,traineeNames):
    for key, value in skillRegister.items():
        if key == myName:
           myskills = value
    for trainee in traineeNames:
        for key, value in skillRegister.items():
            if key == trainee:
                new_value = value.union(myskills)
                value.clear()
                value.update(new_value)

    return skillRegister

def whoCanIHelp(myName):
    for key, value in skillRegister.items():
        if key == myName:
           myskills = value
    traineenamesrequiringhelp = {}
    for key, value in skillRegister.items():
        if key != myName:
           skillcount = 0
           for skill in myskills:
               if skill not in value:
                   skillcount = skillcount + 1
           traineenamesrequiringhelp.update({key:skillcount})

    return traineenamesrequiringhelp

def peopleWithMySkills(myName):
    for key, value in skillRegister.items():
        if key == myName:
           myskills = value
    traineenameshavingmyskills = {}
    for key, value in skillRegister.items():
        if key != myName:
           skillcount = 0
           for skill in myskills:
               if skill in value:
                   skillcount = skillcount + 1
           traineenameshavingmyskills.update({key:skillcount})

    return traineenameshavingmyskills

def peopleWithOtherSkills(myName):
    for key, value in skillRegister.items():
        if key == myName:
           myskills = value
    peoplewithotherskills = {}
    for key, value in skillRegister.items():
        if key != myName:
           skillcount = 0
           for skill in value:
               if skill not in myskills:
                   skillcount = skillcount + 1
           peoplewithotherskills.update({key: skillcount})

    return peoplewithotherskills

def peoplewithextraskills(myName):
    for key, value in skillRegister.items():
        if key == myName:
           myskills = value
    peoplewithextraskill = {}
    for key, value in skillRegister.items():
        if key != myName:
            skillcount = 0
            newskillcount = 0
            for skill in myskills:
                if skill not in value:
                    skillcount = skillcount + 1
            if skillcount == 0:
                for new_skill in value:
                    if new_skill not in myskills:
                        newskillcount = newskillcount + 1
                peoplewithextraskill.update({key : newskillcount})

    return peoplewithextraskill


def myDependencies(myName):
    for key, value in skillRegister.items():
        if key == myName:
           myskills = value
    allskilllist = set()
    mydependencies = set()
    for key, value in skillRegister.items():
        if key != myName:
            allskilllist.update(value)
    for skill in myskills:
        if skill not in allskilllist:
            mydependencies.add(skill)

    return mydependencies

def myDependenciesindept(myName,deptlist):
    for key, value in skillRegister.items():
        if key == myName:
           myskills = value
    deptallskilllist = set()
    deptmydependencies = set()
    for key, value in skillRegister.items():
        if key != myName and key in deptlist:
            deptallskilllist.update(value)
    for skill in myskills:
        if skill not in deptallskilllist:
            deptmydependencies.add(skill)

    return deptmydependencies
