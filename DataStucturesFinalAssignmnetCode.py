import datetime
import heapq

class SocialMediaPost:
    def __init__(self):
        self.posts = {}  # hash table for fast lookup by unique datetime value
        self.bst = []  # binary search tree for time range queries
        self.heap = []  # min-heap for prioritizing posts by views

    def add_post(self, datetime_value, post, person, views=0):
        datetime_obj = datetime.datetime.strptime(datetime_value, '%d/%m/%Y %H:%M') # Converts datetime string to datetime object
        post_obj = (datetime_obj, post, person, views) # Creating a tuple to represent the post

        # Add to hash table
        self.posts[datetime_obj] = post_obj # Storing the post in the dictionary for quick access by datetime

        # Add to binary search tree
        self.bst.append(post_obj) # Adding the post to the list (BST) for time range queries
        self.bst.sort(key=lambda x: x[0]) # Sorting the list based on datetime (ascending order)

        # Add to min-heap
        heapq.heappush(self.heap, (-views, datetime_obj, post, person)) # Pushing post details onto the min-heap with views as the priority (negative views for min-heap)

    def get_post_by_datetime(self, datetime_value):
        datetime_obj = datetime.datetime.strptime(datetime_value, '%d/%m/%Y %H:%M')  # Converting datetime string to datetime object
        if datetime_obj in self.posts:  # Checking if the datetime exists in the hash table
            return self.posts[datetime_obj] # Returning the post details if found
        return None  # Returning None if the datetime is not found

    def get_posts_in_time_range(self, start_datetime_value, end_datetime_value):
        start_datetime_obj = datetime.datetime.strptime(start_datetime_value, '%d/%m/%Y %H:%M') # Converting start datetime string to datetime object
        end_datetime_obj = datetime.datetime.strptime(end_datetime_value, '%d/%m/%Y %H:%M') # Converting end datetime string to datetime object

        posts = [post for post in self.bst if start_datetime_obj <= post[0] <= end_datetime_obj]  # Filtering posts within the specified time range
        return posts # Returning the list of filtered posts

    def get_post_with_most_views(self):
        if not self.heap:  # Checking if the min-heap is empty
            return None   # Returning None if the heap is empty
        return heapq.heappop(self.heap)[2:] # Popping and returning the post details with the most views (post content and user)


account = SocialMediaPost()  # Creating an instance of SocialMediaPost class

# Adding posts with specific datetime, content, user name , and number views
account.add_post('1/1/2024 08:30', 'Good morning', 'Mohammed', views=98)
account.add_post('4/1/2024 09:00', 'Eid Mubarak', 'Sara', views=20)
account.add_post('17/1/2024 15:00', 'Coffee dose', 'Ali', views=56)
account.add_post('10/1/2024 14:00', 'Rainy Day', 'Shamma', views=105)
account.add_post('13/1/2024 12:00', 'Ramadan Kareem', 'Noora', views=200)
account.add_post('7/1/2024 10:00', 'Family', 'Saif', views=50)

# Test Case 1
print("Test Case 1 Finds a post with unique datetime value :")
print(account.get_post_by_datetime('17/1/2024 15:00')[1:3])
print(account.get_post_by_datetime('7/1/2024 10:00')[1:3])
print(account.get_post_by_datetime('20/1/2024 12:00'))

# Test Case 2
print("\nTest Case 2 finds a post with a unique time range :")
print("\n[Range 1] from 1 january to 4 january ")
for post in account.get_posts_in_time_range('1/1/2024 00:00', '4/1/2024 23:59'):
    print(post[1:3])

print("\n[Range 2] from 10 january to 14 january ")
for post in account.get_posts_in_time_range('10/1/2024 00:00', '14/1/2024 23:59'):
    print(post[1:3])

print("\n[Range 3] from 4 january to 17 january ")
for post in account.get_posts_in_time_range('4/1/2024 00:00', '17/1/2024 23:59'):
    print(post[1:3])

# Test Case 3
print("\nTest Case 3 finds the post with the most views:")
print(account.get_post_with_most_views())