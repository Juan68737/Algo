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
'''

studentMatch = defaultdict(int)
hosptialMatch = defaultdict(int)

n = 3

data = [
    [1, 2, 3],  # hospital 1 prefs
    [2, 3, 1],  # hospital 2 prefs
    [2, 1, 3],  # hospital 3 prefs
    [2, 1, 3],  # student 1 prefs
    [1, 2, 3],  # student 2 prefs
    [1, 2, 3]   # student 3 prefs
]

person = defaultdict(list)
hospitals = defaultdict(list)


def initialize():
    
    
    for student in person.keys():
        studentMatch[student] = " "

    for hosptial in hospitals.keys():
        hosptialMatch[hosptial] = " "
    
    index = 1
    for i in range(n):
        hospitals[index] = [[s, True] for s in data[i]]
        index += 1

    index = 1
    for i in range(n, 2 * n):
        person[index] = [[h, True] for h in data[i]]
        index += 1

    free = {}

    for i in range(n):
        free[i + 1] = True

initialize()

#If the students have the ranking
ranking = defaultdict(dict)

for student_index_id, hospital_list in person.items():
    #hospital, unassigned = hospital_list
    ranking[student_index_id] = {v[0]: i +1 for i,v in enumerate(hospital_list)}

unmatched_hospital = deque(hospitals.keys())

def test():
    for k,v in ranking.items():
        print(f"{k} prefers this list order: {v.keys()}\n")

    for k,v in person.items():
        print(f"{k} prefers this list order: {v}\n")

    for k,v in hospitals.items():
        print(f"{k} prefers this list order: {v}\n")
    
    print("Hospitals in Queue\n")
    print(unmatched_hospital)

#test()

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

    if studentMatch[applicant] == 0:
        assign(hospital, applicant)
    elif a prefers h to her/his current assignment h':
        swap(hospital, applicant)
    else:
        reject(hospital)

