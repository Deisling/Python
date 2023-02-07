




def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address,
    }
    return record

user1 = create_record("Vasya", "+79277677131", "Samara")
user2 = create_record("Vasya", "+79272640485", "Moscow")



print(user1)
print(user2)


def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagrajdaetsya madaliyu " + medal)


give_award("Za Berlin", "vasya", "petya")
give_award("Za London", "petya", "alexander", "valintin")

