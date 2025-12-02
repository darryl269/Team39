from .utils import get_var

class RoleDependency:

    def __init__(self, students_count: int, roles_count: int, role: int, dependencies: set[int]):
        """
        Creates a role dependency. This role can only be given to a student,
        if all the roles in ``dependencies`` are given to a student.
        :param role: the role
        :param dependencies: the roles, on which said role is dependent
        """
        self.students_count = students_count
        self.roles_count = roles_count
        self.role = role
        self.dependencies = dependencies

    def get_clauses(self):
        clauses = []
        for dependent_role in self.dependencies:
            clauses += self._dependency_clauses(dependent_role)
        return clauses

    def _dependency_clauses(self, dependent_role):
        clauses = self._no_student_for_role(self.role)
        for i in range(0, len(clauses)):
            clauses[i] = clauses[i] + self._at_least_one_student_for_role(dependent_role)
        return clauses

    def _at_least_one_student_for_role(self, role):
        clause = []
        for s in range(0, self.students_count):
            clause.append(get_var(s, role))
        return clause

    def _no_student_for_role(self, role):
        clauses = []
        for s in range(0, self.students_count):
            clauses.append([-1*get_var(s, role)])
        return clauses
