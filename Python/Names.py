#part1

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for i in students:
    print i['first_name'], i['last_name']

#Part II

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

i=1
print "Students"
for key in users['Students']:
     print i, "-", key['first_name'], key['last_name']," - ", (len(key['first_name']) + len(key['last_name']))
     i +=1
     
i=1    
print "Instructors"
for key in users['Instructors']:
     print i, "-", key['first_name'], key['last_name']," - ", (len(key['first_name']) + len(key['last_name']))
     i +=1