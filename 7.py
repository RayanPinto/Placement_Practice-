hee=[
    "1.Visibility",
    "2.flexiblity",
    "3.error prevention",
    "4.user control",
    "5.help",
    "6.recogniton",
    "7.Ui",
    "8.design",
    "9.Consistency",
    "10.navgiation"
]
rts=[]
for h in hee:
    print(h)
    while True:
        rt=int(input("Enter your choice"))
        if rt.isdigit() and 1<=rt<=5:
            rts.append(rt)
            break
        else:
            print("error")
        print()
avg=sum(rts)/len(rts)
if avg>=4.5:
    