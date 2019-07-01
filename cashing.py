import requests
import json
import os.path

course_list=[]
def get_course_data(api):
	if os.path.exists("courses_data.json"):
		myFile=open("courses_data.json","r")
		data1=myFile.read()
		dict_data=json.loads(data1)
		inside_data=dict_data["availableCourses"]
		count=0
		for index in inside_data:
		    course_name = index["name"]
		    course_id = index["id"]
		    course_list.append(course_id)
		    print str(count)+" ",course_name,course_id
		    count=count+1
	else:		
		response=requests.get(api)	
		course_data=response.json()	
		course_json_file=open("courses_data.json","w")
		string_data=json.dumps(course_data)	
		course_json_file.write(string_data)
url="http://saral.navgurukul.org/api/courses"
get_course_data(url)

user_input=input("enter your choice to anyone id:-")
user_id=course_list[user_input]
print user_id

def exersice_fun(api2): 
	filename="file/excersice"+str(user_id)+".json"
	if os.path.exists(filename):
		course_json_file=open(filename,"r")
		data1=course_json_file.read()
		dict_data1=json.loads(data1)
		inside_data=dict_data1["data"]
		return inside_data
	else:
		exersice_data=requests.get(api2)
		excersiceData=exersice_data.json()
		json_file1=open(filename,"w")
		string_data=json.dumps(excersiceData)
		json_file1.write(string_data)
		json_file1.close()
		return filename
url2=url+"/"+str(user_id) + "/" +"exercises"
inside_data1 = exersice_fun(url2)

child_list=[]
def childExerciseData():
	count=0
	for index in inside_data1:
		child_list.append(index["id"])
		print str(count),"parentChldExercise:",index["name"],index["id"]
		inside_data2= index["childExercises"]
		count1=0
		for index1 in inside_data2:
			print "\t",str(count1), "childExersice:",index1["name"],index1["id"]
			count1=count1+1
		count=count+1
	return child_list
child_list=childExerciseData()

slug_list=[]
def child_exersice(user_childExersice):
	childExercises=0
	for index in inside_data1: 
		# print type(inside_data)
		count=0
		childExercises=child_list[user_childExersice]
		if childExercises==index["id"]:
			slug_list.append(index["slug"])
			print str(count),index["name"]
			child_ex = index["childExercises"]
			count1=count+1
			for index1 in child_ex:
				slug_list.append(index1["slug"])
				print str(count1),index1["name"],index1["id"]
				count1 = count1+1
				count=count+1
	return slug_list

slug_input=input("enter the childExercise which slug you want:")
slug_list=child_exersice(slug_input)

user_slug=input("enter your slug_index")
get_slug=slug_list[user_slug]
		
def child_fun(api3):
	slug_file="slug/slugExercise"+str(get_slug)+".json"
	if os.path.exists(slug_file):
		if get_slug!=None:
			if slug_list[user_slug] != []:
				course_json_file=open(slug_file,"r")
				data1=course_json_file.read()
				dict_data1=json.loads(data1)
				inside_data=dict_data1["content"]
				print inside_data
	else:
		exersice_data=requests.get(api3)
		exersiceData=exersice_data.json()
		json_file1=open(slug_file,"w")
		string_data=json.dumps(exersiceData)
		json_file1.write(string_data)
		json_file1.close()
url3="http://saral.navgurukul.org/api/courses"+"/"+str(user_id)+"/"+"exercise"+"/"+"getBySlug?slug="+str(get_slug)
child_fun(url3)

