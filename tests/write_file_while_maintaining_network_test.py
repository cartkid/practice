import src.write_file_while_maintaining_network as wfwmn
import pytest

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_main():
    await wfwmn.main()
    whole_file: str = ""
    expected: str = "Hello world!"
    with open("new_file.txt", mode="r") as f:
        whole_file = f.read()
    assert whole_file == expected
