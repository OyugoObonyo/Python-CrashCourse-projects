"""
A class should have one and only one job/responsibility. If a class
has more than one responsibilty, it becfomes coupled and changing on responsbility,
leads to changing another responsibility
"""
# Example1 without SRP

# class  User:
#     def __init__(self, name: str):
#         self.name = name
#     
#     def get_name(self) -> str:
#         pass
# 
#     def save(self, user):
#         pass

"""
The class above handles both user properties and user DB Managaement.
If we make changes to the dB management functions, we'll have to make changes to DB
properties too
"""

# Example with SRP

# class User:
#     def __init__(self, name: str):
#             self.name = name
#     
#     def get_name(self):
#         pass
# 
# 
# class UserDB:
#     def get_user(self, id) -> User:
#         pass
# 
#     def save(self, user: User):
#         pass

"""
User properties and user database management are now decoupled therefore making
it easier to make changes if we desire to 
"""