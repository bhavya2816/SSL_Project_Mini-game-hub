#!/bin/bash
# This script displays the leaderboard of the game.
#it reads the winner's name and the game played from the history.csv file and displays it in a formatted manne
echo "--------------------------------------------------------"
awk -F',' '

{if ($5=="Connect4"){
wins_Connect4[$1]++
losses_Connect4[$2]++
}

if ($5=="Tic Tac Toe"){
wins_tictactoe[$1]++
losses_tictactoe[$2]++
}

if ($5=="Othello"){
wins_othello[$1]++
losses_othello[$2]++
}

players[$1]=1
players[$2]=1
}

END{
    
    for (player in players){
        wc= (player in wins_Connect4) ? wins_Connect4[player] : 0
        lc= (player in losses_Connect4) ? losses_Connect4[player] : 0
        wt= (player in wins_tictactoe) ? wins_tictactoe[player] : 0
        lt= (player in losses_tictactoe) ? losses_tictactoe[player] : 0
        wo= (player in wins_othello) ? wins_othello[player] : 0
        lo= (player in losses_othello) ? losses_othello[player] : 0

        if (lc==0) {
        wc_lc_ratio="ND"
        }else {
        wc_lc_ratio = (wc/lc)
         }

        if (lt==0) {
        wt_lt_ratio="ND"
        }else {
        wt_lt_ratio = (wt/lt)
         }

        if (lo==0) {
        wo_lo_ratio="ND"
        }else {
        wo_lo_ratio = (wo/lo)
         }
        if (!(lc==0 && wc==0)){
        printf "%s ,Connect4, %d , %d , %s\n",player,wc,lc,wc_lc_ratio}
        if (!(lo==0 && wo==0)){        
        printf "%s ,Othello, %d , %d , %s\n",player,wo,lo,wo_lo_ratio}
        if (!(lt==0 && wt==0)){
        printf "%s ,Tic Tac Toe, %d , %d , %s\n",player,wt,lt,wt_lt_ratio}
    }
}' history.csv |{
    if [ "$1" = "1" ]; then
        sort -t',' -k1
    elif [ "$1" = "2" ];then
        sort -t',' -gr -k3
    elif [ "$1" = "3" ];then
        sort -t',' -gr -k4
    else
        sort -t',' -gr -k5 
    fi
}| column -t -s',' -N "Player,Game,Wins,Losses,W/L"

echo "------------------------------------------------------"