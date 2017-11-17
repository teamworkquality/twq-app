import numpy as np
from analise import analyse as ana
# import analyse as ana

'''
createReport(flag, construct_data, construct_info, normality_significance = 0.05)

flag is 0 or 1
construct_data is a numpy array which has a different format depending on the flag used (see below for details). All the answers must range from 1 to 5. All answers that are negative must already have their absolute value, i.e., if an answer has value 1 but is a negative answer, it's value in the matrix must be 5.
construct_info has the following format:
[
	[first answer index for construct 1 (int), last answer index for construct 1 (int), construct name (string)], 
	[first answer index for construct 2 (int), last answer index for construct 2 (int), construct name (string)], 
	...
	[first answer index for construct N (int), last answer index for construct N (int), construct name (string)], 
]
normality_significance will help determine how reliable the normality calculation must be.

if flag = 0, a team dataset(each person's answers and id) must be provided
	construct_data will have the format:
		[
			[person1 id, person1 answer 1, person1 answer 2, ..., person1 answer m],
			[person2 id, person2 answer 1, person2 answer 2, ..., person2 answer m],
			...
			[personN id, personN answer1, personN answer 2, ..., personN answer m]
		]
else if flag = 1, a company dataset (each team's person's answers and id) must be provided
	construct_data will have the format (similar to the previous one, but each team is put separetely in a single numpy array):
		[
			[
				[person1 id, person1 answer 1, person1 answer 2, ..., person1 answer m],
				[person2 id, person2 answer 1, person2 answer 2, ..., person2 answer m],
				...
				[personN id, personN answer1, personN answer 2, ..., personN answer m]
			]

			[
				[personG id, personG answer 1, personG answer 2, ..., personG answer m],
				[personG+1 id, personG+1 answer 1, personG+1 answer 2, ..., personG+1 answer m],
				...
				[personG+C id, personG+C answer1, personG+C answer 2, ..., personG+C answer m]
			]
		]

The function returns a list of data that has different formats depending on the flag used.
if flag = 0
	A list of lists, containing the information for the provided team dataset in the following format:
		[[construct1 mean, construct1 alpha], [construct2 mean, construct2 alpha], ..., [constructN mean, constructN alpha]]

if flag = 1
	A list containing 2 other lists. The first list with the information regarding the company, with the following format:
		[[[construct1 mean, construct1 alpha], [construct2 mean, construct2 alpha], ..., [constructN mean, constructN alpha]],
		[Constructs correlation array for the company]* ,  icc for the company ]
	The second list contains lists similar to when flag = 1, but for all teams:
		[
			[construct1Team1 mean, construct1Team1 alpha], [construct2Team1 mean, construct2Team1 alpha], ...,
			[constructNTeam1 mean, constructNTeam1 alpha]
			[construct1Team2 mean, construct1Team2 alpha], [construct2Team2 mean, construct2Team2 alpha], ...,
			[constructNTeam2 mean, constructNTeam2 alpha]
			...
			[construct1TeamM mean, construct1TeamM alpha], [construct2TeamM mean, construct2TeamM alpha], ...,
			[constructNTeamM mean, constructNTeamM alpha]
		]
	* See table 6 in "Teamwork quality and project success in software development A survey of agile development teams".
	Note that, unlike table 6, the calculated correlation has the lower triangle mirrored to the upper triangle in the matrix.
	
''' 

class person:
	def __init__(self, personId, answers):
		self.personId = personId
		self.answers = answers

class constructInfo:

	def __init__(self, firstQuestionIndex, lastQuestionIndex, constructName):
		self.firstQuestionIndex = firstQuestionIndex
		self.lastQuestionIndex = lastQuestionIndex
		self.constructName = constructName

class construct:

	def __init__(self, constructInfo, people):
		self.constructInfo = constructInfo
		self.constructSize = int(constructInfo.lastQuestionIndex) - int(constructInfo.firstQuestionIndex) + 1
		self.constructData = np.empty((0,self.constructSize), int)
		self.calculatedData = False
		for person in people:
			self.constructData = np.vstack((self.constructData, person.answers[int(self.constructInfo.firstQuestionIndex):(int(self.constructInfo.lastQuestionIndex) + 1)]))
		
	def calculateConstructData(self):
		if not self.calculatedData:
			self.mean = self.constructData.mean()
			self.alpha = ana.cronbach(np.array(self.constructData))
			self.calculatedConstructData = np.array([self.mean, self.alpha])
			self.calculatedData = True

class team:

	def __init__(self, people, constructsInfo):
		self.constructs = np.array([])
		self.people = list()
		for p in people:
			personId = p[0]
			personAnswers = p[1:]
			newPerson = person(personId, personAnswers)
			self.people.append(newPerson)

		for constructInfo in constructsInfo:
			newConstruct = construct(constructInfo, self.people)
			self.constructs = np.append(self.constructs, newConstruct)


	def getCalculatedData(self):
		
		returnArray = list()
		for construct in self.constructs:
			if not construct.calculatedData:
				construct.calculateConstructData()
			returnArray.append(construct.calculatedConstructData)
		return returnArray

class company:

	def __init__(self, teamsPeople, constructsInfo, normality_significance):

		self.teams = list()
		self.people = list()
		answersCount = len(teamsPeople[0][0])
		self.data = np.empty((0,answersCount-1), int)
		self.constructs = list()
		self.normality_significance = normality_significance
		for teamPeople in teamsPeople:
			t = team(teamPeople, constructsInfo)
			self.teams.append(t)

			self.people.extend(t.people)
			for person in t.people:
				self.data = np.vstack((self.data, person.answers))

		for constructInfo in constructsInfo:
			newConstruct = construct(constructInfo, self.people)
			self.constructs.append(newConstruct)

	def getCalculatedData(self):
		returnArray = list()
		constructsMeans = np.array([])
		companyCalculatedData = list()

		for construct in self.constructs:
			if not construct.calculatedData:
				construct.calculateConstructData()
			companyCalculatedData.append(construct.calculatedConstructData)
			constructsMeans = np.append(constructsMeans, construct.mean)

		teamsConstructsCalculatedData = list()

		correlationData = np.empty((0, len(self.constructs)), float)

		for t in self.teams:
			teamData = t.getCalculatedData()
			teamsConstructsCalculatedData.append(t.getCalculatedData())
			for person in t.people:
				personConstructsMeans = list()
				for c in self.constructs:
					answersArray = np.array(person.answers[int(c.constructInfo.firstQuestionIndex):int(c.constructInfo.lastQuestionIndex) + 1])
					constructMean = answersArray.mean()
					personConstructsMeans.append(constructMean)
				correlationData = np.vstack((correlationData, np.array(personConstructsMeans)))

		self.w, self.p_value = ana.shapiro_wilk(self.data)
		if(self.p_value < self.normality_significance):
			self.correlation = ana.pearson(correlationData)
		else:
			self.correlation = ana.spearman(correlationData)
		self.icc = ana.icc3_k(self.data)

		companyCalculatedData.append(self.correlation)
		companyCalculatedData.append(self.icc)
		
		returnArray = [companyCalculatedData, teamsConstructsCalculatedData]
		return returnArray


def createReport(flag, construct_data, construct_info, normality_significance = 0.05):
	constructsInfo = np.array([])
	for constructI in construct_info:
		firstI = constructI[0]
		lastI = constructI[1]
		name = constructI[2]
		newConstructInfo = constructInfo(firstI, lastI, name)
		constructsInfo = np.append(constructsInfo, newConstructInfo)

	if(flag == 0):
		t = team(construct_data, constructsInfo)
		tData = t.getCalculatedData()
		# verification if each construct from team is reportable by checking cronbach's alpha
		tData = [{ "results": construct, "reportable": isConstructReportable(construct[1]) } for construct in tData]
		return tData
		# return t.getCalculatedData()

	else: 
		c = company(construct_data, constructsInfo, normality_significance)
		cData, cTeamsData = c.getCalculatedData()
		# verification if each construct from company (and also for each team in company) is reportable by checking cronbach's alpha
		cData = [{ "results": construct, "reportable": isConstructReportable(construct[1]) } for construct in cData[:len(cData) - 2]] + cData[len(cData) - 2:]
		cTeamsData = [[{ "results": construct, "reportable": isConstructReportable(construct[1]) } for construct in team] for team in cTeamsData]
		return [cData, cTeamsData]
		# return c.getCalculatedData()

def isConstructReportable(cronbachAlpha):
	return cronbachAlpha >= 0.7

''' Examples below
data = np.array([
    [1,9,2,5,8,7],
    [2,6,1,3,2,8],
    [3,8,4,6,8,3],
    [4,7,1,2,6,2],
    [5,10,5,6,9,1],
    [6,6,2,4,7,0]
])

data2 = np.array([
		[
			[1,9,2,5,8,7],
			[2,6,1,3,2,8],
			[3,8,4,6,8,3],
			[4,7,1,2,6,2],
			[5,10,5,6,9,5],
			[6,6,2,4,7,4]
		],
		[
			[7,3,2,9,8,2],
			[8,4,1,3,4,3],
			[9,5,4,7,5,6],
			[10,2,2,3,6,0]
		]
	])

ci = np.array([[0,1,"c1"],[2,4,"c2"]])

teamData = createReport(0, data, ci)
print(teamData)
companyData, companyTeamsData = createReport(1, data2, ci)
print(companyData)
print(companyTeamsData)
'''