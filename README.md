# bmo

A research project for learning chess AI implementation.

BMO _Bishop Moves Only_ named in part after _Bishop_ the "artificial person" character in the movie _Aliens_ and the friendly computer character from animated series _Adventure Time_. 

## Plan

* [ ] Basic infrastructure for programmatic gameplay
    * [ ] initiating, playing and saving games
    * [ ] integration with chess board ui
    * [ ] reading and writing standard protocols for moves and board states
* [ ] Implement various chess playing algorithms 
* [ ] Build a tournament system to pit bots against each other
* [ ] Integrating with online chess services like [LiChess](https://lichess.org)
* [ ] Maybe integrate historic computer chess programs (e.g. Sargon)
* [ ] Train an AI neural network using play against existing implementations (and self-play)

## Existing Protocols

* [SAN](https://www.chessprogramming.org/Algebraic_Chess_Notation#SAN) (Standard Algebraic Notation) describes chess moves using ASCII
* [FEN](https://www.chessprogramming.org/Forsyth-Edwards_Notation) (Forsyth-Edwards Notation) and its successor [EPN](https://www.chessprogramming.org/Extended_Position_Description) (Extended Position Description) both define a board state using ASCII
* [PGN](https://www.chessprogramming.org/Portable_Game_Notation) (Portable Game Notation) see standard [implementation guide](https://github.com/fsmosca/PGN-Standard) 

## Chess Bots Online

Integrating BMO with online service would enable testing and training against interested human players and other bots.

[LiChess](https://lichess.org) embraces properly registered chess bots but [chess.com](https://chess.com/) does not. The article [Programming a Chess bot for chess.com](https://medium.com/swlh/programming-a-chess-bot-for-chess-com-fa6bd7e1da76) explains how to hack the web interface to integrate a bot to achieve this in order to play exclusively against other bots.

The strongest Chess AI bots seem to be [AlphaZero](https://en.wikipedia.org/wiki/AlphaZero) and [Stockfish](https://stockfishchess.org/).

## Resources

* [Chess Symbols in Unicode](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode)
* [Analysis of Artificial Intelligence in Chess](https://astrakhan.consulting/blog/analysis-of-artificial-intelligence-in-chess/)
* [Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2020/), Harvard University's course, available to outsiders through OpenCourseWare.



