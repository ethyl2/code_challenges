"""
From Kapil Sharma's lecture 6-23-2020
"Write a code to provide the total number of activities in the last 5 minutes."

More info: Assume that an app has a logging system that logs when users click on links, log in, register, etc.,
and each of those is logged as a separate event.

My solution uses the deque object in python (https://docs.python.org/2/library/collections.html) to store activities.
Calling the clean_out_storage() pops off the activities older than 5 minutes from the deque.
Calling find_num_activities_last_5_mins() calls that method and then returns the size of the deque.
"""
from collections import deque
from datetime import datetime


class Activity:
    def __init__(self, timestamp, activity_type, user_id):
        self.timestamp = timestamp
        self.activity_type = activity_type
        self.user_id = user_id


class Activities:
    def __init__(self):
        self.storage = deque()
        self.delta_amount = 1000  # used to make past activity timestamps

    # Gets rid of any activities that are older than 5 minutes ago.
    def clean_out_storage(self):
        current_timestamp = datetime.timestamp(datetime.now())
        while len(self.storage) > 0 and current_timestamp - self.storage[0].timestamp > 300:
            self.storage.popleft()

    # This is the method to call to provide the solution to the coding challenge
    def find_num_activities_last_5_mins(self):
        self.clean_out_storage()
        return len(self.storage)

    # Before an activity is added, might as well clean out the storage too (although not necessary)
    def store_activity(self, activity):
        self.clean_out_storage()
        self.storage.append(activity)

    # Create an activity that happened in the present moment
    def create_activity(self, activity_type, user_id):
        if not activity_type or not user_id:
            print("activity_type and user_id is required")
            return None
        current_timestamp = datetime.timestamp(datetime.now())
        return Activity(current_timestamp, activity_type, user_id)

    # Create an activity that happened in the past (for testing purposes)
    def create_past_activity(self, activity_type, user_id):
        if not activity_type or not user_id:
            print("activity_type and user_id is required")
            return None

        current_timestamp = datetime.timestamp(datetime.now())
        past_timestamp = current_timestamp - self.delta_amount
        # Each past activity created will be slightly less old than the prev one
        self.delta_amount -= 1
        return Activity(past_timestamp, activity_type, user_id)

# Testing


a = Activities()

act01 = a.create_past_activity('register', 789)
act02 = a.create_past_activity('login', 789)
act03 = a.create_past_activity('register', 678)
act04 = a.create_past_activity('click link 1', 789)
act05 = a.create_past_activity('logout', 789)

a.store_activity(act01)
a.store_activity(act02)
a.store_activity(act03)
a.store_activity(act04)
a.store_activity(act05)

print(a.find_num_activities_last_5_mins())  # 0

act1 = a.create_activity('register', 123)
act2 = a.create_activity('login', 123)
act3 = a.create_activity('register', 456)
act4 = a.create_activity('click link 1', 123)
act5 = a.create_activity('logout', 123)

a.store_activity(act1)
a.store_activity(act2)
a.store_activity(act3)
a.store_activity(act4)
a.store_activity(act5)

print(a.find_num_activities_last_5_mins())  # 5
