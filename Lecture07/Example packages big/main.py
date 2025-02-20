# Module - main.

from packages.bank import exports as be, logic as bl, stats as bs
from packages.CRM import exports as ce, logic as cl, stats as cs

def main():
    bs.stat()
    bl.add(123)
    bl.change(321)
    bl.delete(453)
    bl.show()
    li = [1,23,4,3,3,435,34,53]
    be.export(li)

    print()
    print("part 2")
    cs.stat()
    cl.add(123)
    cl.change(321)
    cl.delete(453)
    cl.show()
    li = [1,23,4,3,3,435,34,53]
    ce.export(li)


if __name__ == "__main__":
    print("main.py has been started")
    main()
