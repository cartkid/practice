import asyncio
import pytest
import threading
import time


def write_some_file():
    time.sleep(2)
    print(f"sync code running in {threading.get_ident()}")
    with open("new_file.txt", mode="w") as f:
        f.write("Hello world!")
    time.sleep(2)
    print("done writing")


def print_some_file():
    time.sleep(1)
    print(f"sync code running in {threading.get_ident()}")
    with open("new_file.txt", mode="r") as f:
        print(f.read())
    print("done reading")


# def test_write_some_file():
#     whole_file: str = ""
#     expected: str = "Hello world!"
#     with open("new_file.txt", mode="r") as f:
#         whole_file = f.read()
#     assert whole_file == expected


async def main():
    for x in range(15):
        print(
            f"{x}... currently running {threading.get_ident()}: {time.clock_gettime(0)}"
        )
        if x == 1:
            loop = asyncio.get_event_loop()
            loop.create_task(asyncio.to_thread(write_some_file))
        if x == 10:
            loop = asyncio.get_event_loop()
            loop.create_task(asyncio.to_thread(print_some_file))
        await asyncio.sleep(1)


asyncio.run(main())

pytest.main()
