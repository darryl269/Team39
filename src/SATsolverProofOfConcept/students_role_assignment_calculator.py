from inputs_for_role_assignment import InputsForRoleAssignment
from role_assignments import RoleAssignments
from pycryptosat import Solver
from rules.exactly_one_role import ExactlyOneRolePerStudent
from rules.pairwise_different import PairwiseDifferent
from rules.essential_roles import EssentialRoles
from input_interpreter import InputInterpreter


class StudentsRoleAssignmentCalculator:

    def __init__(self, inputs_for_role_assignment: InputsForRoleAssignment):
        self.interpreted_input = InputInterpreter(inputs_for_role_assignment)
        self.role_count = self.interpreted_input.roles_count
        self.student_count = self.interpreted_input.students_count
        self.essential_roles = self.interpreted_input.essential_roles
        self.role_dependencies = self.interpreted_input.role_dependency_rules
        self.vetoes = self.interpreted_input.vetoes

        self.solver = Solver()
        for r in [
            ExactlyOneRolePerStudent(self.student_count, self.role_count),
            PairwiseDifferent(self.student_count, self.role_count),
            EssentialRoles(self.student_count, self.essential_roles),
        ] + self.role_dependencies:
            self.solver.add_clauses(r.get_clauses())

    def get_role_assignments(self) -> RoleAssignments:
        sat, model = self.solver.solve(assumptions=self.vetoes)
        if not sat:
            return RoleAssignments(self.interpreted_input, conflicts=self.solver.get_conflict())
        else:
            return RoleAssignments(self.interpreted_input, model=model)

