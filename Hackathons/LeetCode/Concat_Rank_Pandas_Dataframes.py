# Find people who have the most friends and the count of their friends 

def find_most_friends(request_accepted):
    friend_count = {}
    for row in request_accepted:
        friend_count[row['requester_id']] = friend_count.get(row['requester_id'], 0) + 1
        friend_count[row['accepter_id']] = friend_count.get(row['accepter_id'], 0) + 1
    max_friends = max(friend_count.values())
    result = [{'id': k, 'num': v} for k, v in friend_count.items() if v == max_friends]
    return result

if __name__ == '__main__':
    request_accepted = [
        {'requester_id': 1, 'accepter_id': 2, 'accept_date': '2016/06/03'},
        {'requester_id': 1, 'accepter_id': 3, 'accept_date': '2016/06/08'},
        {'requester_id': 2, 'accepter_id': 3, 'accept_date': '2016/06/08'},
        {'requester_id': 3, 'accepter_id': 4, 'accept_date': '2016/06/09'},
    ]
    print(find_most_friends(request_accepted))
