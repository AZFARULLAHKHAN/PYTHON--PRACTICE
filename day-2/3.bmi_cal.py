def bmi(weight,height):
    b=weight / (height ** 2)
    return["underweight" ,"normal weight" , "overweight", "obesity"][(b>30)+(b>25)+(b>18.5)]
print(bmi(70,5.5))