from faker import Faker

def generate_random_name(human_sexuality = str) -> str:
    fake = Faker()
    name = ""
    if human_sexuality == "F"  : name += fake.first_name_female()
    else : name += fake.first_name_male()

    return name + " " + fake.last_name()