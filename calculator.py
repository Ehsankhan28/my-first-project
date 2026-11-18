# ans=0
# has_run_before=False
# try:
#     while True:
#         if has_run_before:
#             print(f"\nCurrent answer:{ans}")
#         choice=input("Want old ans or try a new number (y/n):")
#         if choice.lower() =="y":
#             a=ans
#         else:
#             a=int(input("enter no:"))
#             operator=input("enter operator:(+,-,/,*)")
#             b=int(input("enter no:"))
#             if operator=="+":
#                 ans= (a+b)
#             elif operator=="-":
#                 ans= (a-b)
#             elif operator=="*":
#                 ans= (a*b)
#             elif operator=="/":
#                 ans= (a/b)
#             else:
#                 print("invalid input")
#                 continue
#             print("Result:",ans)
            
#             has_run_before=True
# except:
#     print("something went wrong")
# finally:
#     print(" Thanq Users for using my calculator ")

# markd=[80,75,91]
# markd[1]=82
# print(markd)

# markd[0:2]=[85,86]
# print(markd)

# nums=[1,2,3]
# nums.extend([4,5])
# print(nums)

# #organizer 
# guest_list = ["Dr. Ehsan Ali Khan", "Professor Jones"]

# guest_list.append("Miss Davis")

# students = ["Alex", "Jamie"]
# guest_list.extend(students)

# guest_list.insert(0, "Principal Green")


# print("Final Guest List:")
# for guest in guest_list:
#     print(guest)


# Digital Music Playlist


playlist = ["Song A", "Song B", "Song C", "Song D", "Song E"]

print("Initial Playlist:")
print(playlist)


playlist.remove("Song B")

print("\nAfter removing Song B:")
print(playlist)


played_song = playlist.pop()

print("\nSong played:", played_song)
print("Playlist after playing the last song:")
print(playlist)


del playlist[1]

print("\nAfter deleting Song C:")
print(playlist)


playlist.clear()

print("\nFinal Playlist:")
print(playlist)


 #sort and sorted 
numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)


numbers = [5, 2, 8, 1, 3]

new_list = sorted(numbers)

print(new_list)
print(numbers)



