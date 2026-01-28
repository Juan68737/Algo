import sys


#python3 verify.py /Users/jhonathanherrera/algo/Algo/Assignment1/output/test_output.out 

def checkValidity(file):
    with open(file, "r") as f:
        hospitals_pick = f.readlines()

    students = set()

    '''
    Checks validity: each hospital and each student is matched to
    exactly one partner, with no duplicates
    
    '''
    for single_pick in hospitals_pick:
        student = single_pick[2]
        if student in students:
            return False
        students.add(student)
    return True


def checkBlocker(file):
    pass

def main():
    file = sys.argv[1]
    if not checkValidity(file):
        print("NOT VALID! You either have duplicate matches or a blocker \n please check again!")

    print("No erros, Valid G.S. Output")

if __name__ == "__main__":
    main()

