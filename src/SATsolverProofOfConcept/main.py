from pycryptosat import Solver
from rules.exactly_one_role import ExactlyOneRolePerStudent
from rules.pairwise_different import PairwiseDifferent
from rules.essential_roles import EssentialRoles
from rules.utils import interpret_model
from rules.role_dependency import RoleDependency

roles = {"Role1", "Role2", "Role3",
         "Role4", "Role5", "Role6",
         "Role7", "Role8", "Role9"}
essential_roles = {"Role1, Role2, Role3"}
student_data = {
    "Student1" : {
        "Vetoes": ""
    },
    "Student2": {
        "Vetoes": "Role1"
    },
    "Student3": {
        "Vetoes": "Role1"
    }
}

role_count = 100
student_count = 8
if role_count < student_count:
    raise ValueError("There are more students than roles. Impossible")
if student_count < len(essential_roles):
    raise ValueError("There are less students than essential roles. Impossible.")

rules = [
    ExactlyOneRolePerStudent(student_count, role_count),
    PairwiseDifferent(student_count, role_count),
    EssentialRoles(student_count, [99]),
    RoleDependency(student_count, role_count, 99, {98, 97, 96, 95})
]

# Something I found during testing:
# If an ESSENTIAL role is dependent on other roles. The real set of essential roles
# is the union of the previous essential_roles set and the set of dependencies.

solver = Solver()
for rule in rules:
    solver.add_clauses(rule.get_clauses())

sat, model = solver.solve()
if not sat:
    print(f"conflict: {solver.get_conflict()}")
else:
    interpret_model(model)
