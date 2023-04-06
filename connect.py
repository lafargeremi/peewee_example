import datetime

from models import *
from database import database


#%% Print users in DB
with database:
    users = User.select()
    for user in users:
        print(user.surname)

#%% Select and print all user of group A
with database:
    users = User.select().where(User.group == "A")
    for user in users:
        print(user.surname)

#%% Should fail because user already exist.
with database:
    users = User.create(surname="User3", group="B")
    an_instruction = Instructions.create(user=User)

#%% Create an instruction for a user.
with database:
    user_1_user = User.select().where(User.surname == "User1").get()
    print(user_1_user.surname)
    ring_roll_machine = Machine.select().where(Machine.name == "Ring Rolling Machine").get()
    print(ring_roll_machine.name)
    an_instruction = Instructions.create(user=user_1_user, machine=ring_roll_machine, date=datetime.date.today())
    an_instruction.save()

#%% Print the instructions
with database:
    instructions = Instructions.select().where(Instructions.machine == ring_roll_machine)
    for an_instruction in instructions:
        print(f"{an_instruction.user.surname} receive Instruction on the {an_instruction.date}")
