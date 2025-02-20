# Module - main.

from package_bank import exports as be, logic as bl, stats as bs

def main():
    bs.stat()
    bl.add(123)
    bl.change(321)
    bl.delete(453)
    bl.show()
    li = [1,23,4,3,3,435,34,53]
    be.export(li)

if __name__ == "__main__":
    print("main.py has been started")
    main()
