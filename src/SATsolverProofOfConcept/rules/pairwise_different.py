from .utils import get_var

class PairwiseDifferent:
    def __init__(self, students_count, roles_count):
        self.students_count = students_count
        self.roles_count = roles_count

    def get_clauses(self):
        clauses = []
        for role in range(self.roles_count):
            for student in range(self.students_count):
                clauses += self._role_exclusivity(student, role)
        return clauses

    def _role_exclusivity(self, student, role):
        clauses = []
        for h in range(0, self.students_count):
            if h != student:
                clauses.append([
                    -1*get_var(student, role),
                    -1*get_var(h, role)
                ])
        return clauses