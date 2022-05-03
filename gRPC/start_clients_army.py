from multiprocessing import Process
import client


def get_users() -> list:
    with open("users.txt", "r") as file:
        return [user.split(":") for user in file.read().split("\n")]


if __name__ == "__main__":
    COUNT = 10
    PROCESSES = {}
    users = get_users()
    USERS_PER_CLIENT = 10000 // COUNT
    for x in range(COUNT):
        # PROCESSES[x] = Process(target=client.run)
        PROCESSES[x] = Process(target=client.create_users,
                               args=(users[USERS_PER_CLIENT * x: USERS_PER_CLIENT * (x + 1)], ))

    for x in range(COUNT):
        PROCESSES[x].start()
