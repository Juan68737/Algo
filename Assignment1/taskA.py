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
unmatched_hospital = deque(["Shands", "North", "Vetrans"])


def assign(h, a):
    pass


def swap(h, a):
    pass


perfer = dict()

while unmatched_hospital:

    hospital = unmatched_hospital.popleft()
    hospital_list = hospitals[hospital]  # -> we get the list
    applicant = lol
    # while True:
    #    a = applicants.pop()

    if free[applicant]:
        assign(hospital, applicant)
    elif not free[applicant] and perfer[applicant] == hospital:
        swap(hospital, applicant)
    else:
        continue
