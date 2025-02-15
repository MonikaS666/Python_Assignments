class MulFunc():
    def SubfoldersInAI():
        lists=["Machine Learning","Natural Language Processing","Time Series Analysis","Deep Learning"]
        print("Subfields in AI are:")
        for temp in lists:
            print(temp)
    def OddEven():
        temp=int(input("Enter the number:"))
        temp1=temp
        if(temp%2==0):
            message=f"{temp1} is Even number"
        else:
            message=f"{temp1} is Odd number"
        return message
    def Eligible():
        Age=int(input("Your Age:"))
        Gender=input("Your Gender:")
        if(Age>=18 and Gender=="Female"):
            print("Eligible")
        elif(Age>=21 and Gender=="Male"):
            print("Eligible")
        else:
            print("Not Eligible")
    def Calculate_Total_Percent():
        Marks=[]
        for i in range(5):
            Mark=float(input(f"Subject{i+1}:"))
            Marks.append(Mark)
        Total=sum(Marks)
        Average=Total/len(Marks)
        print("Total:",int(Total))
        print("Percentage:",Average)
    def Triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        Area_formula=(Height*Breadth)/2
        print("Area formula=(Height*Breadth)/2")
        print("Area of triangle:",Area_formula)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        Perimeter_formula=Height1+Height2+Breadth
        print("Perimeter formula=Height1+Height1+Breadth")
        print("Perimeter of triangle:",Perimeter_formula)