import pytest
import time


@pytest.mark.parallel
def test_1(page):
    page.goto("https://www.google.com")
    time.sleep(10)
    print("TEST 1 DONE")


@pytest.mark.parallel
def test_2(page):
    page.goto("https://www.wikipedia.org")
    time.sleep(10)
    print("TEST 2 DONE")


@pytest.mark.parallel
def test_3(page):
    page.goto("https://www.python.org")
    time.sleep(10)
    print("TEST 3 DONE")


#@pytest.mark.parallel
def test_4(page):
    page.goto("https://www.github.com")
    time.sleep(10)
    print("TEST 4 DONE")