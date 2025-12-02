from inputs_for_role_assignment import InputsForRoleAssignment
from rules.role_dependency import RoleDependency
from rules.utils import get_var


class InputInterpreter:
    def __init__(self, inputs: InputsForRoleAssignment):
        self._id_to_student = {}
        self._student_to_id = {}
        self._id_to_role = {}
        self._role_to_id = {}
        for student_id, student in enumerate(inputs.get_students()):
            self._id_to_student[student_id] = student
            self._student_to_id[student] = student_id
        for role_id, role in enumerate(inputs.get_roles()):
            self._id_to_role[role_id] = role
            self._role_to_id[role] = role_id

        self.students_count = len(inputs.get_students())
        self.roles_count = len(inputs.get_roles())
        self.essential_roles = self._get_essential_roles_as_int_list(inputs.get_essential_roles())
        self.role_dependency_rules = self._get_role_dependency_rules(inputs.get_role_dependencies())
        self.vetoes = self._interpret_vetoes(inputs.get_vetoes())

    def _get_essential_roles_as_int_list(self, essential_roles: set[str]):
        return [
            self.get_id_from_role(r) for r in essential_roles
        ]

    def _get_role_dependency_rules(self, role_dependencies: dict[str, set[str]]):
        return [
            RoleDependency(
                self.students_count,

                self.roles_count,
                self.get_id_from_role(r),
                set(self._get_ids_from_roles(role_dependencies.get(r)))
            )
            for r in role_dependencies.keys()
        ]

    def _interpret_vetoes(self, vetoes: dict[str, set[str]]):
        output = []
        for student in vetoes.keys():
            for vetoed_roles in self._get_ids_from_roles(vetoes.get(student)):
                output.append(-1 * get_var(self.get_id_from_student(student), vetoed_roles))
        return output

    def get_student_from_id(self, student_id):
        return self._id_to_student[student_id]

    def get_id_from_student(self, student):
        return self._student_to_id[student]

    def get_role_from_id(self, role_id):
        return self._id_to_role[role_id]

    def _get_ids_from_roles(self, roles):
        return [
            self.get_id_from_role(r) for r in roles
        ]

    def get_id_from_role(self, role):
        return self._role_to_id[role]

