from collections import defaultdict, deque
import sys
import time
import random
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

with open(sys.argv[1], "r") as f:
    n = int(f.readline().strip())
    data = [[int(x) for x in line.strip().split()] for line in f]

# Example input

data2 = [
    [1, 2, 3],  # hospital 1 prefs
    [1, 2, 3],  # hospital 2 prefs
    [2, 3, 1],  # hospital 3 prefs
    [2, 1, 3],  # student 1 prefs
    [3, 1, 2],  # student 2 prefs
    [1, 2, 3]   # student 3 prefs
]


person = defaultdict(list)
hospitals = defaultdict(list)

index = 1
for i in range(n):
    hospitals[index] = [[s, True] for s in data[i]]  # change here
    index += 1

index = 1
for i in range(n, 2 * n):
    person[index] = [[h, True] for h in data[i]]  # change here
    index += 1

free = {}

for i in range(n):
    free[i + 1] = True

studentMatch = {i: None for i in range(1, n+1)}   # student -> hospital
hospitalMatch = {i: None for i in range(1, n+1)}  # hospital -> student


"""
# Initialized
person["Xavier"] = [["Shands", True], ["North", True], ["Vetrans", True]]
person["Yancey"] = [["North", True], ["Shands", True], ["Vetrans", True]]
person["Zeus"] = [["Shands", True], ["North", True], ["Vetrans", True]]

hospitals["Shands"] = [["Yancey", True], ["Xavier", True], ["Zeus", True]]
hospitals["North"] = [["Shands", True], ["Yancey", True], ["Zeus", True]]
hospitals["Vetrans"] = [["Xavier", True], ["Yancey", True], ["Zeus", True]]

free = {
    "Xavier": True,
    "Yancey": True,
    "Zeus": True
}

applicants = deque(["Xavier", "Yancey", "Zeus"])
unmatchedHospital = deque(["Shands", "North", "Vetrans"])


studentMatch = defaultdict(str)
hosptialMatch = defaultdict(str)

students = {
        "Xavier": ["Shands", "North", "Vetrans"],
        "Yancey": ["North", "Shands", "Vetrans"],
        "Zeus": ["Shands", "North", "Vetrans"]
    }
hospitals = {
    "Shands": ["Yancey", "Xavier", "Zeus"],
     "North": ["Xavier", "Yancey", "Zeus"],
    "Vetrans": ["Xavier", "Yancey", "Zeus"]
}


def initialize():

    for student in students:
        studentMatch[student] = " "

    for hosptial in hospitals:
        hosptialMatch[hosptial] = " "


initialize()
"""


def assign(h, a):
    studentMatch[a[0]] = h
    hospitalMatch[h] = a[0]
    free[a[0]] = False


def swap(h, a):
    oldHospital = studentMatch[a[0]]
    studentMatch[a[0]] = h
    hospitalMatch[h] = a[0]
    hospitalMatch[oldHospital] = None
    unmatchedHospital.append(oldHospital)


unmatchedHospital = deque(hospitals.keys())

# If the students have the ranking
ranking = defaultdict(dict)

for student, prefernces in person.items():
    for rank, (hospital, _) in enumerate(prefernces):
        ranking[student][hospital] = rank


def gs(unmatchedHospital):
    while unmatchedHospital:

        hospital = unmatchedHospital.popleft()
        hospitalList = hospitals[hospital]  # -> we get the list

        # applicant = 1st applicant on h's list to whom hospital has not been matched
        # applicant = hospitalList.pop(0)
        applicant = None
        for student in hospitalList:
            if student[1] == True:
                applicant = student
                student[1] = False
                break

        # if there is no applicant
        # this means they all have been matched, so we continue
        if applicant is None:
            continue

        # get the current hospital that the applicant is matched to
        student = applicant[0]
        currentHospital = studentMatch[student]

        if free[student]:
            assign(hospital, applicant)
        # elif a prefers h to her/his current assignment h':
        elif ranking[student][hospital] < ranking[student][currentHospital]:
            swap(hospital, applicant)
        else:
            # a rejects h
            unmatchedHospital.append(hospital)


start1 = time.perf_counter()
gs(unmatchedHospital)
end1 = time.perf_counter()
for k, v in hospitalMatch.items():
    print(f"{k} {v}\n")

# -------------------------------------------------------------------------------------
print(f"Timer for G.S if :{(end1-start1):.10f}")
# TaskB

# Check Validity


def checkValidity(hospitalMatch, studentMatch, n):

    matchedStudents = set()

    for h in range(1, n + 1):
        if hospitalMatch[h] is None:
            return False

        student = hospitalMatch[h]

        if student in matchedStudents:
            return False

        matchedStudents.add(student)

    for s in range(1, n + 1):
        if studentMatch[s] is None:
            return False

    if len(matchedStudents) != n:
        return False

    return True

    '''
    Checks validity: each hospital and each student is matched to
    exactly one partner, with no duplicates
    
    '''

    '''
    for _,a in hospitalMatch.items():
        if a in students:
            return False
        students.add(a)
    return True
    '''


def checkStability(hosptialMatch, studentMatch, hospitals, ranking):
    for h in hospitals:
        currentStudent = hospitalMatch[h]

        for s, _ in hospitals[h]:

            if s == currentStudent:
                break

            currentHospital = studentMatch[s]

            if ranking[s][h] < ranking[s][currentHospital]:
                return False

    return True


if checkValidity(hospitalMatch, studentMatch, n):
    print("No errors, Valid G.S. Output")
else:
    print("NOT VALID! You have duplicate matches \n please check again!")

if checkStability(hospitalMatch, studentMatch, hospitals, ranking):
    print("No errors, Valid G.S. Output")
else:
    print("NOT STABLE! You have a blocker \n please check again!")

# print(person)
# print("-")
# print(hospitals)
# print("-")

# print(studentMatch)
# print("-")

# print(hospitalMatch)
