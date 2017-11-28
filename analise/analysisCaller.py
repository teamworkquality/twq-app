import numpy as np
import analyse as ana

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

# Examples below
data = np.array([[
[0,4,5,5,5,2,2,4,1,5,5,1,5,4,5,4,5,4,5,5,4,5,2,4,5,5,5,5,5,5,2,4,5,5,5,5,1,4,5,5,4,5,5,5,5,5,5,5,5,1,5,5,5,5,5,5,5,5,5,5,5,5],
[1,5,5,4,4,2,2,4,1,5,5,4,5,5,5,5,4,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,1,5,5,5,5,5,5,4,5,5,5,5,5,1,5,5,5,5,5,5,5,5,5,5,5,5],
[2,5,4,4,4,5,3,5,5,4,5,3,4,4,5,5,5,4,5,4,3,3,3,3,4,2,5,4,5,4,5,4,3,5,5,5,2,5,4,5,5,5,5,5,5,5,5,5,5,1,5,5,5,5,5,5,5,5,5,5,3,5],
[3,4,5,4,5,5,3,5,3,4,3,5,3,4,5,5,5,4,5,4,5,5,4,4,4,4,3,4,5,5,5,4,5,5,4,5,5,5,4,4,5,4,4,4,5,5,5,4,5,2,5,5,4,5,5,4,5,4,4,5,5,4]
],
[
[4,5,5,4,4,4,4,4,4,5,5,4,5,4,4,5,5,5,5,4,4,5,4,4,4,5,5,4,5,5,4,5,4,5,4,5,4,4,4,5,5,4,4,4,5,5,5,5,5,4,5,5,5,5,5,5,5,5,4,5,3,3],
[5,4,5,5,5,3,4,4,3,5,4,4,4,5,5,5,5,5,5,5,5,5,5,5,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,3,5,5,5,4,5,5,5,5,4,5,3,3],
[6,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,4,5,5,4,5,4,4,4,4,4,4,4,5,5,4,5,5,3,5,5,5,4,4,5,5,4,5,5,4,4,5,4,4,3,4,5,4,4,4,5,4,5,5,5,3,4],
[7,5,5,5,5,2,4,5,1,5,5,3,4,5,5,5,5,4,5,3,5,5,3,4,5,5,5,5,5,5,5,4,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,3],
[8,4,5,4,4,4,4,4,3,4,5,5,5,4,4,5,5,4,5,5,4,4,2,3,4,4,5,5,5,5,4,4,5,4,5,5,4,5,5,4,4,5,5,4,5,5,5,5,5,3,4,4,5,4,5,4,5,4,5,5,5,3],
[9,5,5,5,5,5,4,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,1,5,5,5,4,4,5,5,3,5,3,5,5,5,5,5,5,3,5],
[10,4,5,5,5,4,5,5,5,5,5,5,4,4,5,5,4,5,5,5,5,5,1,4,4,5,4,4,5,4,5,5,5,5,5,5,5,5,4,4,5,5,5,5,5,5,5,4,4,2,4,4,4,4,4,5,4,4,5,5,4,4],
[11,3,3,3,3,4,4,3,3,3,3,5,4,3,3,4,4,3,4,4,3,4,4,2,2,2,4,2,3,3,4,3,2,5,4,4,3,2,3,4,4,4,4,4,3,4,4,4,4,3,4,4,3,4,5,4,4,4,4,4,3,3],
[12,4,4,4,5,3,4,4,1,5,5,4,5,5,5,5,5,4,5,5,5,5,5,4,5,3,5,5,5,5,5,4,4,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,3,5,4,5,4,5,5,5,5,5,5,2,5]
],
[
[13,4,4,4,4,2,2,4,2,5,4,2,4,3,3,4,4,4,4,4,3,5,2,4,4,3,4,3,4,4,3,3,4,5,5,5,2,4,2,4,5,4,4,4,4,5,5,4,5,3,4,4,4,4,4,4,5,4,4,5,4,3],
[14,5,5,5,5,2,1,2,2,5,5,3,5,4,5,5,5,5,4,3,4,5,3,3,5,4,5,5,5,5,4,5,5,5,5,5,4,3,4,5,5,5,5,5,4,5,5,5,5,4,5,4,5,5,5,5,5,5,4,3,3,4],
[15,5,5,3,4,1,4,4,1,4,4,1,4,5,5,5,5,5,5,4,2,4,3,4,2,4,5,4,5,4,2,5,4,5,4,5,5,4,5,4,5,5,5,5,4,5,5,4,3,5,5,5,4,5,5,5,5,5,5,4,4,4],
[16,5,4,3,5,3,2,3,3,4,2,2,5,3,4,4,4,4,4,4,4,5,3,4,4,3,5,4,5,4,3,3,4,5,5,5,3,4,4,4,4,3,4,4,4,4,5,4,4,3,3,4,4,4,4,4,5,5,3,4,4,4],
[17,4,4,4,4,2,4,4,3,5,4,4,4,4,4,5,4,5,4,5,4,5,5,4,4,5,4,4,5,5,5,4,4,5,3,5,5,4,4,4,5,5,2,4,5,5,4,4,5,1,4,5,4,5,5,5,5,5,4,4,5,4],
[18,4,3,3,4,3,2,4,2,4,4,3,3,4,4,4,4,5,4,3,3,4,3,3,4,4,5,4,5,4,4,4,4,3,4,4,4,4,4,4,5,3,5,5,3,4,4,4,4,5,4,4,5,4,4,4,4,4,5,4,5,4],
[19,5,4,4,4,2,1,2,2,5,4,4,4,4,5,5,4,4,4,5,5,5,4,2,4,4,5,4,5,5,4,5,5,5,5,5,4,4,5,5,5,5,4,4,5,5,5,4,4,3,4,4,5,5,5,4,5,5,5,5,4,4],
[20,4,4,5,5,2,2,5,2,5,5,3,5,3,4,5,5,5,5,5,4,5,2,2,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,4,5,5,5,4,4,4,5,5,5,3,4,4,5,4,5,5,5,4,4,4,3,4],
[21,5,4,4,4,2,1,4,2,5,4,4,4,4,4,5,4,4,4,4,4,5,4,4,4,4,3,4,5,4,4,4,4,5,5,5,4,5,4,3,5,5,5,5,5,4,5,4,4,1,4,5,4,4,4,4,5,4,5,4,3,4],
[22,4,3,4,4,2,1,2,3,5,5,3,3,4,5,5,5,4,5,5,5,4,5,4,4,2,4,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,3,5,5,5,2,4,5,5,4,4,5,5,5,4,5,4,5],
[23,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,5,4,4,4,5,5,4,5,5,5,5,5]
],
[
[24,5,5,2,5,5,1,5,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,5,5,5,5,5,5,5,5,5,3,5,5,5,5,5,5,5,5],
[25,4,4,2,4,2,4,4,2,4,4,2,2,4,4,4,5,4,5,4,2,4,4,4,2,2,4,4,4,4,2,2,4,5,5,5,2,4,4,4,5,4,4,4,4,4,5,2,4,2,4,4,4,4,4,4,5,4,4,4,4,4],
[26,5,5,4,5,4,2,5,2,4,5,5,5,5,5,5,5,5,5,5,4,5,5,4,4,4,5,4,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,4,4,5,5,5,5,5,5,5,4,5],
[27,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,4,5,5,5,4,5,5,5,5,4,5,5,5],
[28,4,5,4,4,2,2,4,1,4,4,2,4,4,4,4,5,4,4,4,4,4,2,4,4,5,4,4,5,5,2,4,4,5,5,5,2,4,4,4,4,5,5,5,4,5,5,4,4,4,4,4,4,4,5,4,5,4,4,4,4,5],
[29,5,3,3,4,5,4,5,4,5,3,4,4,5,5,4,5,5,5,5,4,4,2,4,4,4,5,4,5,4,5,4,4,5,5,5,5,5,3,4,5,3,5,4,5,4,5,5,5,3,5,4,5,4,5,5,5,5,5,5,3,3],
[30,5,3,3,3,4,4,5,3,4,3,5,4,4,4,4,4,4,4,4,3,5,4,2,3,3,5,3,5,4,5,4,3,5,4,4,2,4,3,4,5,5,4,5,4,4,5,4,5,4,4,5,5,4,5,4,5,4,5,4,4,4],
[31,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
[32,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,5,5,4,5,4,5,5,5,5,5,5,5,5]
],
[
[33,5,4,4,5,4,5,5,5,5,5,5,5,4,4,5,5,5,5,4,5,5,5,4,4,4,5,3,5,5,5,5,4,5,5,5,5,5,5,5,4,5,5,5,5,5,4,3,4,1,5,5,4,4,5,5,4,4,5,4,4,4],
[34,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,3,1,5,4,5,3,3,4,5,5,5,3,3,5],
[35,5,5,3,1,3,1,4,1,5,5,5,5,5,5,5,5,2,3,5,3,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,1,5,3,4,5,5,3,3,5,5,5,3,3,1,4,5,5,4,5,4,5,3,5,5,1,5],
[36,5,3,3,4,2,3,4,3,5,5,5,5,5,4,5,5,4,4,4,4,5,4,4,4,4,4,3,5,4,4,4,4,4,4,4,4,4,4,3,4,4,2,3,3,4,4,3,3,2,3,4,4,5,4,4,5,4,4,4,3,3],
[37,5,1,1,5,4,2,5,1,5,5,4,5,5,5,4,5,5,5,5,5,5,4,5,4,5,5,5,5,5,4,5,5,5,5,5,4,4,4,4,5,5,3,4,5,5,5,1,2,1,5,5,4,3,5,3,5,4,5,4,5,5],
[38,5,5,5,4,5,5,5,5,5,5,4,5,4,5,4,5,5,5,5,5,5,5,4,4,4,5,5,5,5,4,5,5,5,5,5,5,5,4,5,5,5,5,5,4,5,5,4,5,4,4,5,4,5,5,5,5,5,5,5,5,5]
],
[
[39,4,4,4,5,3,2,4,2,4,1,2,4,5,4,4,4,4,5,4,3,5,4,3,4,4,5,4,4,4,3,4,3,5,5,5,4,3,3,4,5,4,4,4,4,5,4,4,4,2,4,5,4,4,4,4,5,5,5,4,4,3],
[40,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,3,5,5,5,5,5,5,5,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,1,3,3],
[41,4,4,3,5,3,2,4,3,4,3,2,3,2,4,4,4,4,3,4,4,4,3,4,2,4,3,4,4,4,3,4,4,5,3,3,3,2,3,3,4,4,3,4,4,4,3,4,4,1,3,4,3,3,4,4,4,3,4,4,3,4]
],
[
[42,5,4,5,5,1,1,5,2,5,5,2,4,4,5,5,4,4,4,4,5,4,2,5,4,5,4,4,4,4,2,4,4,2,5,5,2,5,5,4,5,5,5,4,4,5,5,4,4,5,4,5,4,5,5,5,5,4,5,5,4,3],
[43,5,5,4,4,4,3,5,5,4,5,5,5,4,5,4,4,5,1,5,5,5,2,4,4,5,5,5,5,5,5,5,5,5,5,5,5,4,3,5,5,5,5,4,5,4,5,4,4,4,5,4,5,5,5,4,5,5,5,4,4,5],
[44,5,4,5,5,4,3,5,2,5,2,5,5,3,4,4,4,4,3,4,3,5,3,3,3,5,5,3,5,4,4,5,3,5,4,5,4,4,2,4,4,5,4,4,4,5,3,4,5,2,4,5,4,4,4,4,5,5,4,5,2,4],
[45,5,4,3,4,4,4,4,2,4,5,4,4,4,4,4,4,4,4,4,4,5,4,2,4,5,4,4,4,4,4,4,4,4,5,5,4,4,4,4,4,5,5,5,4,4,5,4,4,4,4,4,4,4,4,4,5,4,4,4,4,4]
],
[
[46,4,5,5,5,5,4,5,1,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,5,5,5,4,5,5,5,5,5,5,5,5],
[47,5,4,4,4,5,2,4,4,5,3,4,3,4,3,4,4,5,4,5,4,5,4,4,3,4,4,3,5,4,5,5,4,4,4,5,4,4,3,4,5,5,4,4,5,5,5,3,3,2,5,4,4,4,5,4,5,4,5,4,4,3],
[48,4,4,4,4,2,2,5,3,4,4,4,4,4,5,5,4,4,5,4,4,5,2,4,4,4,4,4,5,5,4,5,5,5,4,5,3,5,5,4,5,5,4,4,5,4,5,3,3,3,4,5,3,4,5,5,4,5,4,4,4,4],
[49,5,5,5,5,5,5,5,2,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,4,5,5,5,5,5,5,5,4,4,5,5,5,5,5,5,5,5,5,5,5],
[50,5,5,5,5,5,4,5,2,5,4,5,5,5,5,5,5,5,5,5,5,5,4,4,4,5,5,3,5,4,5,5,4,5,5,5,5,5,3,5,5,5,4,3,5,4,4,4,4,2,5,5,5,5,5,5,5,5,5,5,3,4]
],
[
[51,5,5,5,5,5,2,5,1,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,5,5,5,5,5,3,5,4,5,5,5,5,5,5,5,5,5,4,5,5,4,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5],
[52,5,5,5,5,5,4,4,4,5,4,5,4,5,5,5,5,5,5,5,4,5,5,4,4,4,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,4,5,4,4,5,5,4,5,5,5,5,5,5,5,5],
[53,3,4,3,2,2,4,4,4,4,5,2,4,3,2,4,5,4,5,4,5,4,4,4,2,2,4,5,4,5,2,4,4,5,3,5,2,5,4,4,4,4,5,5,4,3,5,4,3,2,3,2,3,4,3,3,5,3,2,4,3,4],
[54,4,4,2,3,4,2,3,4,4,4,4,5,4,4,5,4,4,5,4,4,5,4,2,3,4,4,4,4,4,4,4,4,5,5,4,4,4,4,4,4,4,1,3,5,5,5,4,4,2,4,4,5,4,4,4,4,4,5,5,4,3],
[55,5,5,5,5,5,1,4,1,4,4,5,5,5,4,5,5,4,5,5,4,5,5,5,5,4,3,4,5,4,1,4,5,5,5,5,5,5,5,5,4,5,4,4,4,4,5,5,5,2,5,5,4,5,4,5,5,4,5,5,3,4]
]])


ci = np.array([[0,9,"comunicacao"],[10,13,"coordenacao"],[14,20, 'suporte_mutuo'],[21,24,'esforco'],[25,34,'coesao'],[35,37,'balanco'],[38,40,'satis.'],[41,45,'aprendizagem'],[46,55,'efetividade'],[56,60, 'eficiencia']])
# teamData = createReport(0, data, ci)
# print(teamData)
companyData, companyTeamsData = createReport(1, data, ci)
print(companyData)
# print(companyTeamsData)
