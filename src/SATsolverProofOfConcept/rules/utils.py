VAR_BASE = 10000

def get_var(student_num: int, role_num: int):
    if student_num > 99 or student_num < 0:
        raise ValueError("student_num must be in the range 0 to 99 (both ends inclusive)")
    if role_num > 99 or student_num < 0:
        raise ValueError("role_num must be in the range 0 to 99 (both ends inclusive)")
    return VAR_BASE + student_num*100 + role_num

def interpret_model(model):
    for number, assignment in enumerate(model):
        if assignment:
            student_number = str(number)[1:3]
            role_number = str(number)[3:]
            print(f"student {student_number} is assigned role {role_number}")
