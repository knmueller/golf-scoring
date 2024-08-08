function mark_cell_for_team(team_score, p1_cell, p1_score, p2_cell, p2_score) {
    if (p1_score == team_score) {
        p1_cell.style.backgroundColor = "lightgreen"
    }

    if (p2_score == team_score) {
        p2_cell.style.backgroundColor = "lightgreen"
    }
}

function highlight_champ_table() {
    var champ_table = document.getElementById("champ-match");

    team1_match_score = 0
    team2_match_score = 0

    // Add color to title cell in handicap rows
    champ_table.rows[1].cells[0].style.backgroundColor = "lightblue";
    champ_table.rows[6].cells[0].style.backgroundColor = "pink";

    // loop through hole 1 to hole18
    for (let hole_idx = 1; hole_idx < champ_table.rows[0].cells.length; hole_idx++) {

        // Add color to handicap rows
        champ_table.rows[1].cells[hole_idx].style.backgroundColor = "lightblue";
        champ_table.rows[6].cells[hole_idx].style.backgroundColor = "pink";

        // get player scores for this hole
        var p1_cell = champ_table.rows[2].cells[hole_idx];
        var p1_score = p1_cell.innerHTML;
        var p2_cell = champ_table.rows[3].cells[hole_idx];
        var p2_score = p2_cell.innerHTML;
        var team1_score = 100;
        if (p1_score && p2_score) {
            team1_score = Math.min(p1_score, p2_score);
        } else if (p1_score) {
            team1_score = p1_score;
        } else if (p2_score) {
            team1_score = p2_score;
        }

        var p3_cell = champ_table.rows[4].cells[hole_idx];
        var p3_score = p3_cell.innerHTML;
        var p4_cell = champ_table.rows[5].cells[hole_idx];
        var p4_score = p4_cell.innerHTML;
        var team2_score = 100;
        if (p3_score && p4_score) {
            team2_score = Math.min(p3_score, p4_score)
        } else if (p3_score) {
            team2_score = p3_score;
        } else if (p4_score) {
            team2_score = p4_score;
        }

        if (p1_score || p2_score || p3_score || p4_score) {
            if (team1_score == team2_score) {
                mark_cell_for_team(team1_score, p1_cell, p1_score, p2_cell, p2_score)
                mark_cell_for_team(team2_score, p3_cell, p3_score, p4_cell, p4_score)
                team1_match_score += 1
                team2_match_score += 1
            } else if (team1_score < team2_score) {
                mark_cell_for_team(team1_score, p1_cell, p1_score, p2_cell, p2_score)
                team1_match_score += 2
            } else {
                mark_cell_for_team(team2_score, p3_cell, p3_score, p4_cell, p4_score)
                team2_match_score += 2
            }
        }
    }

    var tr = champ_table.tHead.children[0];
    var th = document.createElement(f'th');
    th.className = "table__cell";
    th.innerHTML = "Match Score";
    tr.appendChild(th);

    var team1_score_cell = champ_table.rows[2].insertCell(-1);
    team1_score_cell.className = "table__cell"
    team1_score_cell.innerHTML = team1_match_score;

    var team2_score_cell = champ_table.rows[4].insertCell(-1);
    team2_score_cell.className = "table__cell"
    team2_score_cell.innerHTML = team2_match_score;

    if (team1_match_score == team2_match_score) {
        team1_score_cell.style.backgroundColor = "yellow"
        team2_score_cell.style.backgroundColor = "yellow"
    } else if (team1_match_score > team2_match_score) {
        team1_score_cell.style.backgroundColor = "green"
        team1_score_cell.style.color = "white"
    } else {
        team2_score_cell.style.backgroundColor = "green"
        team1_score_cell.style.color = "white"
    }

    team1_score_cell.style.textAlign = "center";
    team2_score_cell.style.textAlign = "center";
}
