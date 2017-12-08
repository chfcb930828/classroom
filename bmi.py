def bmi(w,h):
    b = w/h/h
    print(b)
    if b < 18.5:
        print("体重偏轻")
    elif 18.5<=b<24:
        print("体重正常")
    else:
        print("体重偏重")

weight = float(input("您的体重是："))
height = float(input("您的身高是："))
bmi(weight,height)
