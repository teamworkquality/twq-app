API:

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