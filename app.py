#BMI Calculator

def calc(w,h):
    return w / (h ** 2)

def find(bmi):
     if bmi < 18.5:
        return "Underweight"
     elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
     elif 25 <= bmi < 29.9:
        return "Overweight"
     else:
        return "Obese"
 


w= float(input("Give me your weight :"))
h= float(input("Give me your height :"))
bmi= calc(w,h)
res= find(bmi)
print(res)