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

# Example input
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
