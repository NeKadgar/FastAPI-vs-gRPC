# gRPC
## Setup
Install the dependencies:
```bash
$ python -m pip install --upgrade pip
$ python -m pip install grpcio
$ python -m pip install grpcio-tools
```
## Performance

Everything below dont make a lot of sence because sometimes CPU goes to 100%, sometimes only 60% and after few reruns
100%

#### Hello \<Name>
time displays 1000 responses of Hello \<Name>

|           | 1 client      | 10 clients    | 50 clients    |
|-----------|---------------|---------------|---------------|
| 1 worker  | 0.4-0.53 sec  | 0.32-0.43 sec | 0.34-0.5 sec  |
| 2 workers | 0.41-0.45 sec | 0.34-0.40 sec | 0.34-0.37 sec |
| 4 workers | 0.4-0.6 sec   | 0.34-0.36 sec | 0.34-0.41 sec  |

#### Add user

time displays 100 added users

|           | 1-50 clients  |
|-----------|---------------|
| 1 worker  | 0.72-0.83 sec |
| 2 workers | error         |

#### Auth user
time displays 1000 auth requests

|           | 1 client     | 10 clients    | 50 clients   |
|-----------|--------------|---------------|--------------|
| 1 worker  | 2.67-3.5 sec | 2.67-2.77 sec | 2.95-3.3 sec |
| 2 workers | 3-3.25 sec   | 3.1-3.5 sec   | 3.5-5.1 sec  |
| 4 workers | 2.42-3.3 sec | 2.74-3.6 sec  | 2.5-3.2 sec  |

### Conclusion
GIL exists, time of all operations with database pretty random, sometimes it's 1.8 sec, sometimes (same code, another run) time is 6 sec. 

# FastAPI

## Setup
Install the dependencies:
```bash
$ pip install fastapi
$ pip install "uvicorn[standard]"
```
## Performance



