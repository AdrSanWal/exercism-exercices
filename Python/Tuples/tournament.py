data = {0: {'win': {'MP': 1, 'W': 1, 'D': 0, 'L': 0, 'P': 3},
            'draw': {'MP': 1, 'W': 0, 'D': 1, 'L': 0, 'P': 1},
            'loss': {'MP': 1, 'W': 0, 'D': 0, 'L': 1, 'P': 0}
            },
        1: {'win': {'MP': 1, 'W': 0, 'D': 0, 'L': 1, 'P': 0},
            'draw': {'MP': 1, 'W': 0, 'D': 1, 'L': 0, 'P': 1},
            'loss': {'MP': 1, 'W': 1, 'D': 0, 'L': 0, 'P': 3}
            }}


def stats_to_row(team, stats):
    first, last = f"{team}{(31 - len(team))*' '}", ""
    for stat in stats.values():
        last += f"|{'  ' if len(str(stat)) == 1 else ' '}{stat} "
    return [first + last[:-1]]


def tally(rows):
    table = [f"Team{27*' '}| MP |  W |  D |  L |  P"]
    teams_stats = {}
    for row in rows:
        match = row.split(';')
        *teams, result = match
        for i, team in enumerate(teams):
            if team in teams_stats:
                teams_stats[team] = {x: teams_stats[team][x] + data[i][result][x]
                                     for x in teams_stats[team]}
            else:
                teams_stats[team] = data[i][result]
    sorted_stats = sorted(teams_stats, key=lambda x: (-teams_stats[x]['P'], x))

    for t in sorted_stats:
        table.extend(stats_to_row(t, teams_stats[t]))

    return table
