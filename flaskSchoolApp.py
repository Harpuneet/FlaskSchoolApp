'''
  flaskSchoolApp.py - For parsing school data
'''

from flask import Flask, render_template, jsonify
import requests, csv

app = Flask(__name__)

@app.route('/api/schools/<int:school_id>', methods=['GET'])
def get_schoolsData(school_id):
	
	school_data = {"schoolId":None, "name": "", "telephone": None, "fax": None, "email": "", "principal": "", "schoolWebsite": "", "street": "", "suburb": "", "city": "", "postalAddress1": "", "postalAddress2": "", "postalAddress3": "", "postalCode": None, "urbanArea": "", "schoolType": "", "definition": "", "authority": "", "genderOfStudents": "", "territorialAuthorityWithAucklandLocalBoard": "", "regionalCouncil": "", "ministryOfEducationLocalOffice": "", "educationRegion": "", "generalElectorate": "", "maoriElectorate": "", "censusAreaUnit": "", "ward": "", "longitude": None , "latitude": None, "decile": None, "totalSchoolRoll": None, "europeanPakeha": None, "maori": None, "pasifika": None, "asian": None, "MELAA": None, "other": None, "internationalStudents": None}

	try:
		school_directory_url = 'https://www.educationcounts.govt.nz/__data/assets/file/0003/62571/Directory-School-Current.csv'
		headers              = {'content-type': 'text/plain; charset=utf-8'}
		result               = requests.get(school_directory_url)
		reader = csv.reader((result.text).split('\n'), delimiter=',')
		for row in reader:
			if (row[0].strip()).isdigit() and int(row[0].strip()) == int(school_id):
				school_data["schoolId"]                       				= int(row[0])
				school_data["name"]                           				= row[1]
				school_data["telephone"]                      				= row[2]
				school_data["fax"]                            				= row[3]
				school_data["email"]						  				= row[4]
				school_data["principal"]					  				= row[5]
				school_data["schoolWebsite"]				  				= row[6]
				school_data["street"]						  				= row[7]
				school_data["suburb"]						  				= row[8]
				school_data["city"] 						  				= row[9]
				school_data["postalAddress1"] 			      				= row[10]
				school_data["postalAddress2"] 				  				= row[11]
				school_data["postalAddress3"]				  				= row[12]
				school_data["postalCode"] 					  				= row[13]
				school_data["urbanArea"] 					  				= row[14]
				school_data["schoolType"]     				  				= row[15]
				school_data["definition"] 					  				= row[16]
				school_data["authority"] 					  			  	= row[17]
				school_data["genderOfStudents"]				  			  	= row[18]
				school_data["territorialAuthorityWithAucklandLocalBoard"] 	= row[19]
				school_data["regionalCouncil"] 				  				= row[20]
				school_data["ministryOfEducationLocalOffice"]				= row[21]
				school_data["educationRegion"] 				  				= row[22]
				school_data["generalElectorate"] 			  				= row[23]
				school_data["maoriElectorate"] 				  				= row[24]
				school_data["censusAreaUnit"]      			  				= row[25]
				school_data["ward"] 						  				= row[26]
				school_data["longitude"] 					  				= float(row[27])
				school_data["latitude"] 					  				= float(row[28])
				school_data["decile"] 						  				= int(row[29])
				school_data["totalSchoolRoll"]   			  				= int(row[30])
				school_data["europeanPakeha"] 				  				= int(row[31])
				school_data["maori"]  						  				= int(row[32])
				school_data["pasifika"] 					  				= int(row[33])
				school_data["asian"]   						  				= int(row[34])
				school_data["MELAA"] 						  				= int(row[35])
				school_data["internationalStudents"] 		  				= int(row[36])

				return jsonify(school_data)

	except Exception, e:
		return "Couldn't find school id " + str(school_id)
		
	# return render_template('index.html')

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8008)