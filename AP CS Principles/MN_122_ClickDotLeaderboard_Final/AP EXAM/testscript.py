items = ["sword","shield","healthpotion","healthpotion","hamburger"]
health = 100
def requestitems():
    print(items)

def usehealthpotion():
    global health
    for x in items:
        if x == "healthpotion":
            print('used healthpotion, health increased by 50.')
            health += 50
            break
usehealthpotion()