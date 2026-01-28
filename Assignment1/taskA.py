from collections import defaultdict, deque

'''
Initialize each person and hospital to be free.

while (some hospital is free and hasn’t been matched/assigned
       to every applicant) {

    Choose such a hospital h
    a = 1st applicant on h's list to whom h has not been matched

    if (a is free)
        assign h and a
    else if (a prefers h to her/his current assignment h')
        assign a and h, and h' has a slot free
    else
        a rejects h
}

'''

'''
person = defaultdict(list)
hospitals = defaultdict(list)

#Initialized 
person["Xavier"] = [["Shands",True], ["North", True], ["Vetrans",True]]
person["Yancey"] = [["North",True], ["Shands", True], ["Vetrans",True]]
person["Zeus"] = [["Shands",True], ["North", True], ["Vetrans",True]]

hospitals["Shands"] = [["Yancey",True], ["Xavier", True], ["Zeus",True]]
hospitals["North"] = [["Shands",True], ["Yancey", True], ["Zeus",True]]
hospitals["Vetrans"] = [["Xavier",True], ["Yancey", True], ["Zeus",True]]

free = {
    "Xavier" : True,
    "Yancey" : True,
    "Zeus" : True
}

applicants = deque(["Xavier", "Yancey", "Zeus"])
unmatched_hospital = deque(["Shands", "North", "Vetrans"])
'''
studentMatch = defaultdict(str)
hosptialMatch = defaultdict(str)

students = {
        "Xavier" : ["Shands", "North","Vetrans"],
        "Yancey" : ["North", "Shands", "Vetrans"],
        "Zeus" : ["Shands", "North", "Vetrans"]
    }
hospitals = {
    "Shands" : ["Yancey", "Xavier","Zeus"],
     "North" : ["Xavier", "Yancey", "Zeus"],
    "Vetrans" : ["Xavier", "Yancey", "Zeus"]
}

def initialize():
    
    for student in students:
        studentMatch[student] = " "

    for hosptial in hospitals:
        hosptialMatch[hosptial] = " "

initialize()

#If the students have the ranking
ranking = defaultdict(dict)

for student, hospital_list in students.items():
    ranking[student] = {v: i +1 for i,v in enumerate(hospital_list)}


unmatched_hospital = deque(hospitals.keys())

def assign(h, a):
    studentMatch[a] = h
    hosptialMatch[h] = a

def swap(h,a):
    
    pass

def reject(h):
    unmatched_hospital.append(h)

while unmatched_hospital:

    hospital = unmatched_hospital.popleft()
    
    applicant = 1st applicant on h's list to whom hospital has not been matched

    if studentMatch[applicant] == " ":
        assign(hospital, applicant)
    elif a prefers h to her/his current assignment h':
        swap(hospital, applicant)
    else:
        reject(hospital)



