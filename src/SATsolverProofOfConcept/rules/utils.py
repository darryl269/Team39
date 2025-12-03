VAR_BASE = 10000

def get_var(student_num: int, role_num: int) -> int:
    """
    Returns a variable in propositional logic represented as a 5-digit integer that starts with '1'.

    The next two digits after the leading one represent the student's number (0 to 99, both ends
    inclusive).

    The last two digits after that represent the role number assigned to that student (0 to 99,
    both ends inclusive).

    As an example, 12345 says that student number 23 is assigned role 45.

    :param student_num: the student's number (0 to 99, both inclusive)
    :param role_num: the role number (0 to 99, both inclusive)
    :return: the variable in propositional logic
    """
    if student_num > 99 or student_num < 0:
        raise ValueError("student_num must be in the range 0 to 99 (both ends inclusive)")
    if role_num > 99 or student_num < 0:
        raise ValueError("role_num must be in the range 0 to 99 (both ends inclusive)")
    return VAR_BASE + student_num * 100 + role_num


def interpret_model(model):
    """
    Prints the result of the SAT solver, which is formally called a model, in a human-readable
    format.

    :param model: the model / result from the solver
    """
    for number, assignment in enumerate(model):
        if assignment:
            student_number = str(number)[1:3]
            role_number = str(number)[3:]
            print(f"student {student_number} is assigned role {role_number}")
