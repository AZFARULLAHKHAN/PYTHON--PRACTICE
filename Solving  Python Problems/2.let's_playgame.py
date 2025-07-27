"""Let's play! You have to return which player won! In case of a draw return Draw!.

Examples (Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!" """
#solution:

def rps(p1, p2):
    if p1 not in ("rock", "paper", "scissors") or p2 not in ("rock", "paper", "scissors"):
        return "Invalid input."
    if p1 == p2:
        return "Draw!"
    if (p1, p2) in [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]:
        return "Player 1 won!"
    return "Player 2 won!"
p1=input("ENTER PLAYER 1 CHOICE (rock,paper,scissors): ").lower()
p2=input("ENTER PLAYER 2 CHOICE (rock,paper,scissors: ").lower()
print("THE RESULT IS:",rps(p1, p2))
