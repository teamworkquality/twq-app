API:

function createReport(flag, answers_data, construct_data) {
	flag: 
		0 if creating report for one team; 
		1 if creating report for one company;
	answers_data: 
		if flag 0, data is a numpy array like [[answers for Q1], [answers for Q2], ..., [answers for Qn]];
		if flag 1, data is a numpy array like [[Team 1], [Team 2], ..., [Team i]] where each [Team i] is like
		[[answers for Q1], [answers for Q2], ..., [answers for Qn]];
	construct_data:
		a numpy array where each element is the construct of question like [Q1 construct, Q2 construct, ..., Qn construct]
}


