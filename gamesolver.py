# API

# pos represents the current state of the game
# move represents an action to be taken that can alter the game board

class FourToZeroGame:
	"""
	Game: 4 to 0
	Players: 2
	Objective: Each player chooses to subtract either 1 or 2 from the current number,
	starting at 4, before passing the new number onto the other player.
	The player that *receives* the number 0 from the last player loses.
	"""
	def initial_pos():
		return 4

	# makes the move
	def do_move(pos, move):
		return pos + move

	def lost(pos):
		return pos == 0

	# all {valid, legal, legit, possible} moves from the current point in the game
	def gen_moves(pos):
		if FourToZeroGame.lost(pos):
		    return []
		elif pos == 1:
			return [-1]
		else:
			return [-1, -2]

	# evaluates the immediate situation, by checking whether (and if so, how) the current game is finished
	def primitive(pos):
		return LOSS if FourToZeroGame.lost(pos) else UNDECIDED

# Solver

WIN = 'W' # forces the opponent into a loss
LOSS = 'L' # no way to win against opponent
TIE = 'T' # no more moves but no decisive winner
DRAW = 'D' # the game as entered a cycle
UNDECIDED = 'U' # the game is not over yet

# dfs traversal of game tree
def solve(game):
	def after(pos):
		return [game.do_move(pos, move) for move in game.gen_moves(pos)]

	explore = [game.initial_pos()]
	frontier = []
	known = {} # outcomes

	while len(explore)+len(frontier) > 0:
		if len(explore) > 0:
			pos = explore.pop(0) # dequeue
			e = game.primitive(pos)
			if e == UNDECIDED:
				if pos not in frontier:
					frontier.append(pos)
					explore = after(pos)+explore
			else:
				known[pos] = e
		else:
			pos = frontier.pop()
			if pos in known: # already determined
				continue
			tied, drew = False, False
			for next in after(pos):
				if known[next] == LOSS:
					known[pos] = WIN
					break
				elif known[next] == TIE:
					tied = True
				elif known[next] == DRAW:
					drew = True
			if pos not in known:
				known[pos] = TIE if tied else DRAW if drew else LOSS

	return known[game.initial_pos()]

print (solve(FourToZeroGame))