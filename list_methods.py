"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type == 1:test
       express_queue.append(person_name)
       return express_queue
    elif ticket_type == 0:
        normal_queue.append(person_name)
        return normal_queue


def find_my_friend(queue, friend_name):
    return queue.index(friend_name)


def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue
    


def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):
    return queue.count(person_name)


def remove_the_last_person(queue):
    last_person = queue[-1]
    queue.remove(last_person)
    return last_person


def sorted_names(queue):
    return sorted(queue)
