import os
import time
import random
import string
import grpc
from services import services_pb2, services_pb2_grpc

LETTERS = string.ascii_letters


def get_random_string():
    return ''.join(random.choice(LETTERS) for i in range(10))


def close(channel):
    """Close the channel"""
    channel.close()


def create_users(users):
    counter = 0
    with grpc.insecure_channel('localhost:9999') as channel:
        stub = services_pb2_grpc.UserServiceStub(channel)
        for user in users:
            fname, lname, age = user
            response = stub.AddUser(services_pb2.AddUserRequest(
                first_name=fname,
                last_name=lname,
                age=int(age)
            ))
            counter = counter + 1
            if counter % 100 == 0:
                print(f"token: {response.token}, id: {response.user_id}")


def auth_user(users):
    counter = 0
    with grpc.insecure_channel('localhost:9999') as channel:
        stub = services_pb2_grpc.UserServiceStub(channel)
        for user in users:
            fname, lname, age = user
            response = stub.AuthUser(services_pb2.AddUserRequest(
                first_name=fname,
                last_name=lname,
                age=int(age)
            ))
            counter = counter + 1
            if counter % 1000 == 0:
                print(f"token: {response.token}, id: {response.server_time}")


def run():
    pid = os.getpid()
    counter = 0
    with grpc.insecure_channel('localhost:9999') as channel:
        stub = services_pb2_grpc.GreeterStub(channel)
        while True:
            try:
                start = time.time()

                response = stub.SayHello(services_pb2.HelloRequest(name=get_random_string()))
                counter = counter + 1
                if counter % 1000 == 0:
                    print(
                        "%.4f : resp=%s : procid=%i"
                        % (time.time() - start, response.message, pid)
                    )
                # time.sleep(0.001)
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(close)
                exit()


if __name__ == "__main__":
    # run()
    with open("users.txt", "r") as file:
        users = [user.split(":") for user in file.read().split("\n")]
    # print(users)
    # create_users(users)
    auth_user(users)
