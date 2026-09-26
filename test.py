
from cutsmlist import custmanager

passed = 0
failed = 0


def check(condition, pass_msg, fail_msg):
    global passed, failed
    if condition:
        print(f"PASSED: {pass_msg}")
        passed += 1
    else:
        print(f"FAILED: {fail_msg}")
        failed += 1


def tesddvalidc():
    cm = custmanager()
    cm.addcust("Shrishti", "2", "shrishti@gmail.com")
    check(len(cm.customers) == 1,
          "valid customer added",
          "customer was not added correctly")


def tesaem():
    cm = custmanager()
    cm.addcust("Test", "1", "notanemail")
    check(len(cm.customers) == 0,
          "invalid email rejected",
          "invalid email was added anyway")


def tespeo():
    cm = custmanager()
    cm.addcust("Test", "-3", "test@example.com")
    check(len(cm.customers) == 0,
          "invalid number of people rejected",
          "invalid people count was added anyway")


def tesname():
    cm = custmanager()
    cm.addcust("", "1", "test@example.com")
    check(len(cm.customers) == 0,
          "empty name rejected",
          "empty name was added anyway")


def teseargot():
    cm = custmanager()
    cm.addcust("Test User", "1", "test@example.com")
    result = cm.searchcust(1)
    check(result is not None and result.name == "Test User",
          "search found the correct customer",
          "search did not return the correct customer")


def tessearnotgot():
    cm = custmanager()
    result = cm.searchcust(999)
    check(result is None,
          "search correctly returned nothing for a missing ID",
          "search returned something for a missing ID")


def tesdelcust():
    cm = custmanager()
    cm.addcust("Test User", "1", "test@example.com")
    cm.deletecust(1)
    check(len(cm.customers) == 0,
          "customer deleted successfully",
          "customer was not deleted")


def tesbalcal():
    cm = custmanager()
    cm.addcust("Test User", "1", "test@example.com")
    customer = cm.searchcust(1)
    customer.due = 5000
    customer.paid = 2000
    check(customer.balance() == 3000,
          "balance calculated correctly",
          "balance calculation is wrong")


tesddvalidc()
tesaem()
tespeo()
tesname()
teseargot()
tessearnotgot()
tesdelcust()
tesbalcal()
print("\n----------------------------")
print(f"TOTAL: {passed + failed} tests | PASSED: {passed} | FAILED: {failed}")
if failed == 0:
    print("ALL TESTS PASSED - system is working correctly!")
else:
    print("SOME TESTS FAILED - check the messages above.")