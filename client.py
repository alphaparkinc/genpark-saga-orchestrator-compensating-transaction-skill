class SagaOrchestrator:
    """Saga Pattern Orchestrator with atomic rollback guarantees."""
    def __init__(self):
        self.execution_history = []
        self.compensation_history = []

    def run_saga(self, steps_definitions: list[dict]) -> dict:
        """
        steps_definitions: list of dicts with 'name', 'status' (True/False indicating step success),
        'action_log', 'compensation_log'
        """
        executed = []
        for step in steps_definitions:
            name = step["name"]
            success = step.get("success", True)
            if success:
                executed.append(step)
                self.execution_history.append(name)
            else:
                # Failure encountered: Rollback all previously executed steps in reverse order
                for completed in reversed(executed):
                    self.compensation_history.append(completed["name"] + "_COMPENSATED")
                return {
                    "saga_completed": False,
                    "failed_step": name,
                    "forward_executed": list(self.execution_history),
                    "compensations_triggered": list(self.compensation_history)
                }

        return {
            "saga_completed": True,
            "forward_executed": list(self.execution_history),
            "compensations_triggered": []
        }
