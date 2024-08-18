import pets

def main():
    pet = pets.Pet("shepard","bob",130,"brown")
    print("pet:\nname:",pet.get_name(),"weight:", pet.get_weight())
    
    # pet.feed(1800)
    # print("pet:\nname:",pet.name,"weight:", pet.__weight)
    
    # pet.walk(1.5)
    # print("pet:\nname:",pet.name,"weight:", pet.__weight)
    
    # pet.__weight = -100
    # print("pet:\nname:",pet.name,"weight:", pet.__weight)
main()