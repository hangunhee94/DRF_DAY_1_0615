def homework(num1, num2 , *args, **kwargs):
    print(f"num1 : {num1}")
    print(f"num2 : {num2}")
    print(args)
    print(kwargs)
    return

homework(1, 2, 3, 4, 5, 11, 22, 3, 2, num3=11, num4=21, num5=35)

