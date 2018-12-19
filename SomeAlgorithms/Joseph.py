'''
Joseph Problem Destription
People are standing in a circle waiting to be executed. Counting begins at a 
specified point in the circle and proceeds around the circle in a specified 
direction. After a specified number of people are skipped, the next person is 
executed. The procedure is repeated with the remaining people, starting with 
the next person, going in the same direction and skipping the same number of
people, until only one person remains, and is freed.
'''

People_Count = input("please input the count of attending people: ")
Skip_num = input("please input the number to skip a person: ")

#init the circle:
Joseph_circle = range(People_Count)
print Joseph_circle

#processing the circulation:
current_skip = 0
current_index = -1
current_count = 0
while current_skip < People_Count:
 current_index += 1
 # reset index while reaching the end 
 if (current_index == People_Count ):
  current_index = 0
 if(Joseph_circle[current_index] < 0):
  continue
 else :
  current_count += 1
  if(current_count % Skip_num == 0):
   Joseph_circle[current_index] = -1
   current_skip += 1
   print " the skip people is : " + str(current_index+1)


