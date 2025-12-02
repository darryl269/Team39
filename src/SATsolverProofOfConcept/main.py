from students_role_assignment_calculator import StudentsRoleAssignmentCalculator
from inputs_for_role_assignment import InputsForRoleAssignment

student_names = {
    "Jena", "Anna", "Anja", "Tom", "Tim", "Tommy"
}
roles = {
    "Role1", "Role2", "Role3", "Role4", "Role5", "Role6",
    "Role7", "Role8", "Role9", "Role10", "Role11", "Role12"
}
essential_roles = {
    "Role3", "Role5", "Role12"
}
role_dependencies = {
    "Role1": {"Role2", "Role4"},
    "Role12": {"Role11"}
}
vetoes = {
    "Jena": {"Role1"}
}
assignment_inputs = InputsForRoleAssignment(
    student_names,
    roles,
    essential_roles=essential_roles,
    role_dependencies=role_dependencies,
    vetoes=vetoes
)
calculator = StudentsRoleAssignmentCalculator(assignment_inputs)
role_assignments = calculator.get_role_assignments()
role_assignments.pretty_print()
