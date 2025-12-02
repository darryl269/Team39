from .utils import get_var

class EssentialRoles:
    def __init__(self, students_count: int, essential_roles: list[int]):
        self.students_count = students_count
        self.essential_roles = essential_roles

    def get_clauses(self):
        clauses = []
        for role in self.essential_roles:
            clauses.append(self._role_must_be_occupied(role))
        return clauses

    def _role_must_be_occupied(self, role):
        clause = []
        for student in range(0, self.students_count):
            clause.append(get_var(student, role))
        return clause