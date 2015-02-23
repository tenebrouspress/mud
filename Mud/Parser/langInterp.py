#Natural language interpretation

#Open sauce this fo sho.  No reason to reinvent the spaceship. http://nltk.github.com/


import nltk

def langInterp(textInp):

        def isMove(tokens):
                #Determines if move is commanded in sentence
                checks = ['move', 'go', 'walk', 'run']
                move = False
                for check in checks:
                        if check in tokens:
                                move = True
                return move

        def isLook(tokens):
                #Determines if look is commanded in sentence
                checks = ['look']
                look = False
                for check in checks:
                        if check in tokens:
                                look = True
                return look

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

        if isMove(tokens): #if input is a move, determine direction of move
                action = 'move'
                direction = deterDirect(tokens)
                return [action,direction]

        if isLook(tokens): #if input is a move, determine direction of move
                action = 'look'
                direction = deterDirect(tokens)
                return [action,direction]

#Function Test
#[action,actionDescriptor] = langInterp('Move like a fucking hoss to the south.')
#print action
#print actionDescriptor
