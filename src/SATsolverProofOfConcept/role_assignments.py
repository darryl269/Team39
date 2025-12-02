from input_interpreter import InputInterpreter


class RoleAssignments:
    def __init__(self, input_interpreter: InputInterpreter, model=None, conflicts=None):
        self.input_interpreter = input_interpreter
        self.model = model
        self.conflicts = conflicts

    def pretty_print(self):
        if self.model is None:
            print(f"No solution found")
        if self.conflicts is not None:
            print("Conflict(s) found:")
            self._pretty_print_conflicts(self.conflicts)

        for i, truth_val in enumerate(self.model):
            if truth_val:
                self._pretty_print_assignment(i)

    def _pretty_print_assignment(self, i):
        student = self.input_interpreter.get_student_from_id(int(str(i)[1:3]))
        role = self.input_interpreter.get_role_from_id(int(str(i)[3:]))
        print(f"{student} is assigned {role}")

    def _pretty_print_conflicts(self, conflicts):
        print(conflicts)
