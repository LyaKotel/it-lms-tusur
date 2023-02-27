def responses_creator(item_ids):
    item_ids = [None] if item_ids is None else item_ids
    return list( (dict(item_id=item_id) for item_id in item_ids) )

print(responses_creator(['a', 10, responses_creator([1,2])]))