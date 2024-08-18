def convert_height(height_in_inches):
    inches = (height_in_inches) % 12
    feet = int(((height_in_inches)-inches)/12)
    print("Your hieght is ",feet,"' ",inches,'"',sep="")

def before(alphabet):
    print(chr(ord(alphabet)-1),"\n",chr(ord(alphabet)-2),"\n",chr(ord(alphabet)-3),sep="")
def main():
    # convert_height(int(input("Enter height in inches:\n")))
    before(input("Enter alphabet:\n"))
main()