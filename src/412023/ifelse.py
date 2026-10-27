score = 50

if score >= 90:
    level = "A"
elif score >= 80:
    level = "B"
elif score >= 70:
    level = "C"
else:
    level = "D"

match level:
    case "A":
        print("A級")
    case "B":
        print("B級")
    case "C":
        print("C級")
    case _:
        print("不及格")