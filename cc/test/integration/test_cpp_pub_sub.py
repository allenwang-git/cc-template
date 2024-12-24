import pytest
import time
import subprocess

@pytest.mark.timeout(60)
def test_python_pub_sub():
    pub_cmd = ["./cc/cc_pub"]
    sub_cmd = ["./cc/cc_sub"]

    sub = subprocess.Popen(sub_cmd, stdout=subprocess.PIPE, text=True)
    time.sleep(0.5)
    pub = subprocess.Popen(pub_cmd, stdout=subprocess.PIPE, text=True)

    # run the test for a while
    time.sleep(2)

    # terminate processes
    pub.wait()
    sub.wait()

    # check logs
    assert (
        "Write sample: [userID: 1, message: Hello World]" in pub.stdout.read()
    ), "Publisher did not send correct data."
    assert (
        "Message received: [userID: 1, message: Hello World]" in sub.stdout.read()
    ), "Subscriber did not receive correct data."

