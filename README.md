# SSL_Project_Mini-game-hub
Mini Game Hub
Authors :
            Bhavya Machupalli
            Subha srivalli Athreyi Yanala

Mini Game Hub is a Two-user game platform built using Bash and Python
The system allows users to :
     Authenticate using a secure login system
     Select and play board games through a graphical interface
     Track results using a persistent leaderboard
     View game statistics and visualizations

In this folder you'll find 7 scripts
1) main.sh :- This is the entry point of the project.
              It handles user authentication by asking two players for their usernames and passwords, verifying or registering them securely using hashed passwords.
              Then launches the game engine by passing the authenticated usernames to game.py.
2) game.py :- This manages the game system after login.
              It shows the game menu, runs the selected game using a graphical interface (Pygame), records the result, displays the leaderboard and statistics,
              and allows players to play again or exit.
3) leaderboard.sh :- leaderboard.sh reads the game history file and calculates each player’s wins, losses,
                     and win/loss ratio, then displays a sorted leaderboard in the terminal.
4) users.tsv :- users.tsv stores registered user data.It keeps usernames along with their hashed passwords for authentication.
5) history.csv :- history.csv stores the results of all games played.Each entry records the winner, loser, date, and game name.
6) games/ :- contains 1. base_game.py ->  represents a generic 2 player,turn based board game.
                      2. tictactoe.py ->  It contains the implementation of the Tic-Tac-Toe game.
                      3. connect4.py  ->  It contains the implementation of the connect four game.
                      4. othello.py   ->  It contains the implementation of the Othello (Reversi) game.
7) report/ :- It contains the project report written in LaTeX.
               1. report.tex -> Project overview and features
                                Explanation of:
                                authentication system
                                base class and games
                                leaderboard and analytics
                                Libraries used
                                Problems faced and solutions
                                Improvements (what you’d do with more time)
                                References
               2. Makefile ->   It contains commands to compile the LaTeX report into a PDF.

To run these scripts use : bash <script_name>.sh
