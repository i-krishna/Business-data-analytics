# Count the number of server replacements when a server encountered three consecutive "error" logs.

import os
from collections import defaultdict, deque

def countFaults(n, logs):
    # Write your code here
    server_status = defaultdict(deque)
    replacements = 0

    for log in logs:
        server_id, status = log.split()
        
        # Maintain a queue of the last 3 statuses for the server
        server_status[server_id].append(status)
        if len(server_status[server_id]) > 3:
            server_status[server_id].popleft()
        
        # Check if the server logs three consecutive "error"s
        if list(server_status[server_id]) == ["error", "error", "error"]:
            replacements += 1
            server_status[server_id].clear()  # Reset the server's status after replacement
    
    return replacements

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    logs_count = int(input().strip())
    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    result = countFaults(n, logs)
    fptr.write(str(result) + '\n')
    fptr.close()
