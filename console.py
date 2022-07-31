import pdb

from models.booking import Booking
import repositories.booking_repository as booking_repository

from models.member import Member
import repositories.member_repository as member_repository

from models.activity import Activity
import repositories.activity_repository as activity_repository

from models.activity_type import ActivityType
import repositories.activity_type_repository as activity_type_repository

booking_repository.delete_all()
member_repository.delete_all()
activity_repository.delete_all()
activity_type_repository.delete_all()



member_1 = Member("Billy Bob")
member_repository.save(member_1)

member_2 = Member("John Smoth")
member_repository.save(member_2)

member_3 = Member("Jane Doe")
member_repository.save(member_3)

member_4 = Member("Paddy Pimblett")
member_repository.save(member_4)

activity_type_1 = ActivityType("endurance")
activity_type_repository.save(activity_type_1)

activity_type_2 = ActivityType("strength")
activity_type_repository.save(activity_type_2)

activity_type_3 = ActivityType("flexibility")
activity_type_repository.save(activity_type_3)

activity_1 = Activity("Aquafit", activity_type_2)
activity_repository.save(activity_1)

activity_2 = Activity("Spin class", activity_type_1)
activity_repository.save(activity_2)

booking_1 = Booking(member_2, activity_2)
booking_repository.save(booking_1)

booking_2 = Booking(member_3, activity_1)
booking_repository.save(booking_2)

booking_3 = Booking(member_3, activity_2)
booking_repository.save(booking_3)

booking_4 = Booking(member_4, activity_2)
booking_repository.save(booking_4)

