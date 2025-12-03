def get_actual_essential_roles(essential_roles: set[str],
                               role_dependencies: dict[str, set[str]]):
    output = essential_roles
    for role in essential_roles:
        if role in role_dependencies.keys():
            output = output.union(role_dependencies.get(role))
    return output


def validate_inputs(essential_roles: set[str] | None, role_dependencies: dict[str, set[str]] | None,
                    roles: set[str], student_names: set[str]):
    if any([role not in roles for role in essential_roles]):
        raise ValueError("All roles from essential_roles must be in roles!")
    if len(roles) < len(student_names):
        raise ValueError("There are more students than there are roles. Impossible assignment.")
    if len(student_names) < len(essential_roles):
        raise ValueError("There are more essential roles than students. Impossible assignment.")
    if len(student_names) < len(get_actual_essential_roles(essential_roles, role_dependencies)):
        raise ValueError("There are more essential roles and roles, which these roles depend on, combined, "
                         "than there are students. Try checking the dependencies of roles set as essential. "
                         "Impossible assignment.")


class InputsForRoleAssignment:
    """
    This class is a capsule for all the needed inputs for roles assignment.
    """
    def __init__(self,
                 student_names: set[str],
                 roles: set[str],
                 essential_roles: set[str] = None,
                 vetoes: dict[str, set[str]] = None,
                 role_dependencies: dict[str, set[str]] = None):
        validate_inputs(essential_roles, role_dependencies, roles, student_names)

        self._student_names = student_names
        self._roles = roles
        self._essential_roles = essential_roles
        self._vetoes = vetoes
        self._role_dependencies = role_dependencies

    def get_roles(self) -> set[str]:
        return self._roles

    def get_students(self) -> set[str]:
        return self._student_names

    def get_essential_roles(self) -> set[str]:
        return self._essential_roles

    def get_role_dependencies(self) -> dict[str, set[str]]:
        return self._role_dependencies

    def get_vetoes(self) -> dict[str, set[str]]:
        return self._vetoes