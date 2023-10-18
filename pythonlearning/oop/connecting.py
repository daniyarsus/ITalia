from worker import Worker

person = Worker(0, 0, 0, False)
person.set_worker(input(), input(), input(), bool(input()))
print(person.get_worker())