from client import SagaOrchestrator

def main():
    print("=== Saga Pattern Orchestrator ===")
    saga = SagaOrchestrator()
    steps = [
        {"name": "book_hotel", "success": True},
        {"name": "reserve_rental_car", "success": True},
        {"name": "charge_customer_card", "success": False}
    ]

    res = saga.run_saga(steps)
    print("Saga Execution Result:", res)
    assert res["saga_completed"] is False
    assert res["failed_step"] == "charge_customer_card"
    assert "reserve_rental_car_COMPENSATED" in res["compensations_triggered"]

    print("Saga Orchestrator verified successfully!")

if __name__ == "__main__":
    main()
