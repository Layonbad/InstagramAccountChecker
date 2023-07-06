# Import instaloader package
import instaloader

# creating an Instaloader() object
ig=instaloader.Instaloader()

# getting the instagram username as input from user
username=input("Enter your Instagram username: ")

# Fetching the details of provided username from instagram
profile=instaloader.Profile.from_username(ig.context, username)

# Printing the fetched details and storing the profile pic
print("Username: ", profile.username)
print("Number of Posts Uploaded: ", profile.mediacount)
print(profile.username + "is having" + str(profile.followers) + " followers.")
print(profile.username + "is having" + str(profile.followees) + " people")
print("Bio: " + profile.biography)
instaloader.Instaloader().download_profile(username, profile_pic_only=True)