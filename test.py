def say_scores(score0, score1):
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    
def announce_lead_changes(last_leader=None):
    def say_announce(score0, score1):
        nonlocal last_leader
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
    return say_announce
    
def both(f, g):
    def say(score0, score1):
        nonlocal f, g
        f(score0, score1)
        g(score0, score1)
    return say
    
h=both(say_scores, announce_lead_changes())
h(10,0)
h(10,6)
h(6,17)