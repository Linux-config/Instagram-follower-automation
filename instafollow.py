import time
from random import randint

def follow(profile_url):
    # Simulate following the profile
    time.sleep(randint(1, 3))  # Simulate human-like delay
    return True

def get_followers(profile_url, amount):
    print("Getting followers for profile:", profile_url)
    success_count = 0
    for _ in range(amount):
        if follow(profile_url):
            success_count += 1
    print("Finished getting", success_count, "followers.")

# Take user input for profile URL and number of followers
profile_url = input("Enter the profile URL: ")
amount = int(input("Enter the number of followers you want to add: "))

# Get followers for the specified profile
get_followers(profile_url, amount)
