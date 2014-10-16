#Natural language interpretation

#Open sauce this fo sho.  No reason to reinvent the spaceship. http://nltk.github.com/


import nltk	

def langInterp(textInp):
	
	def isMove(tokens):
		#Determines if move is commanded in sentence
		check = 'move'
		if check in tokens:
			return True
		else:
			return False
	
	def deterDirect(tokens):
		defaultDirects = {'north','south','east','west','northeast','northwest','southeast','southwest'}
		#For each default direction, check if it exists in the tokens
		try:
			for idx,string in enumerate(defaultDirects):
				if string in tokens:
					return tokens[tokens.index(string)]
		except: 
			print 'Error, move direction not specified.'
			
	#Tokenize input		
	tokens = nltk.word_tokenize(textInp)
	#Lowercase everything for comparison purposes
	for idx,string in enumerate(tokens):
		tokens[idx] = string.lower()
	
	#taggedTokens = nltk.pos_tag(tokens)
	
	move = isMove(tokens)	#determine if input is a move
	if move: #if input is a move, determine direction of move
		action = 'move'
		direction = deterDirect(tokens)
		return [action,direction]


#Function Test
#[action,actionDescriptor] = langInterp('Move like a fucking hoss to the south.')
#print action
#print actionDescriptor	

