from .utils import get_var

class ExactlyOneRolePerStudent:
    def __init__(self, num_of_students, num_of_roles):
        self.students_count = num_of_students
        self.roles_count = num_of_roles

    def get_clauses(self):
        return self._at_least_one_role() + self._at_most_one_role()

    def _at_least_one_role(self):
        clauses = []
        for s in range(0, self.students_count):
            clauses.append(self._at_least_one_role_for_student(s))
        return clauses

    def _at_least_one_role_for_student(self, student: int):
        clause = []
        for r in range(0, self.roles_count):
            clause.append(get_var(student, r))
        return clause

    def _at_most_one_role(self):
        clauses = []
        for s in range(0, self.students_count):
            for r in range(0, self.roles_count):
                clauses += self._exclusivity(s, r)
        return clauses

    def _exclusivity(self, student: int, role: int):
        clauses = []
        for other_role in range(0, self.roles_count):
            if other_role != role:
                clauses.append([
                    -1*get_var(student, role),
                    -1*get_var(student, other_role)
                ])
        return clauses