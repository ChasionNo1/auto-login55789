from pip._vendor.distlib.compat import raw_input

conntact = {}
conntact_list = []
while 1:
    conntact['name'] = raw_input("please input name:")
    conntact['phone'] = raw_input("please input phone number:")
    conntact_list.append(conntact)
    print(conntact_list)
    go_on = raw_input("continue?\n")
    if go_on == "yes":
        pass
    if go_on == "no":
        break
    else:
        print("you didn't say no\n")
i = 1
for conntact in conntact_list:
    print("%d: name=%s" % (i, conntact['name']))
    print("%d: phone=%s" % (i, conntact['phone']))
    i = i + 1
