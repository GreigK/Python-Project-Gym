from models.activity import Activity
from models.member import Member
from models.booking import Booking

import repositories.activity_repository as activity_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
activity_repository.delete_all()
member_repository.delete_all()


member1 = Member('Billy Bob')
member_repository.save(member1)

member2 = Member('John Smith')
member_repository.save(member2)

member3 = Member('Jane Doe')
member_repository.save(member3)

activity1 = Activity('Spin Class', 'Cardio')
activity_repository.save(activity1)

activity2 = Activity('Aquafit', 'Swimming')
activity_repository.save(activity2)

booking1 = Booking(member1, activity1, 'Why didnt i just cycle outside')
booking_repository.save(booking1)

booking2 = Booking(member3, activity1, 'bike only had one peddle')
booking_repository.save(booking2)

booking3 = Booking(member1, activity2, 'big fan, cya next week')
booking_repository.save(booking3)

booking4 = Booking(member2, activity2, 'turns out its in the deep end, bring a float')
booking_repository.save(booking4)
