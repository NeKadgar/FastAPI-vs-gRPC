import grpc
from concurrent import futures
import threading
from services import services_pb2_grpc, services_pb2
import time
import datetime
from models import db, user

MAX_WORKERS = 4
db_session = next(db.get_session())


class Greeter(services_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()

    def SayHello(self, request, context):
        self.counter += 1
        if self.counter > 1000:
            print(f"1000 HelloWorlds in {time.time() - self.last_print_time} seconds")
            self.last_print_time = time.time()
            self.counter = 0
        return services_pb2.HelloReply(message=f'Hello {request.name}')


class UserService(services_pb2_grpc.UserServiceServicer):
    def __init__(self):
        self.user_counter = 0
        self.auth_user = 0
        self.last_print_time = time.time()

    def AddUser(self, request, context):
        self.user_counter += 1
        new_user = user.User(
            first_name=request.first_name,
            last_name=request.last_name,
            age=request.age
        )
        db_session.add(new_user)
        db_session.commit()
        if self.user_counter > 100:
            print(f"100 Users in {time.time() - self.last_print_time} seconds")
            self.last_print_time = time.time()
            self.user_counter = 0
        return services_pb2.AddUserResponse(token=f"{new_user.last_name}_{new_user.first_name}", user_id=new_user.id)

    def AuthUser(self, request, context):
        self.auth_user += 1
        current_user = db_session.query(user.User).filter_by(
            first_name=request.first_name,
            last_name=request.last_name,
            age=request.age
        ).first()
        if not current_user:
            return services_pb2.AuthUserResponse(
                token="",
                server_time=str(datetime.datetime.now())
            )
        if self.auth_user > 1000:
            print(f"1000 Auth in {time.time() - self.last_print_time} seconds")
            self.last_print_time = time.time()
            self.auth_user = 0
        return services_pb2.AuthUserResponse(
            token=f"{current_user.last_name}_{current_user.first_name}",
            server_time=str(datetime.datetime.now())
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_WORKERS))
    services_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    services_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print(f"Server Running : threadcount {threading.active_count()}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    # db_session = next(db.get_session())
    # db_session.rollback()
    serve()
