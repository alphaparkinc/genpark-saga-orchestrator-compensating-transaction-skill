import sys
import json
from client import SagaOrchestrator

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "run_saga":
        saga = SagaOrchestrator()
        return saga.run_saga(params.get("steps", []))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
