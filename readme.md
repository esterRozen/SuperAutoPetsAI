[![Tests](https://github.com/CallThemHunter/SuperAutoPetsAI/actions/workflows/test-SAP-app.yml/badge.svg?event=push)](https://github.com/CallThemHunter/SuperAutoPetsAI/actions/workflows/test-SAP-app.yml)

Super Auto Pets AI

This project has 3 major components:

- Game Engine (90% complete, 320 of 340 tests completed)
- Reinforcement Learning AI
    - DQN Complete
    - AQN In Progress
    - A2C In Progress
    - A3C In Progress
    - Future Revisions TBD
- Selenium Webdriver (to be completed)

The game engine mimics the engine which drives the strategy
auto-battler game Super Auto Pets (c. Team Wood Games) as near
as I could through reverse engineering the minutiae of the logic
behind the game mechanics.

The engine has its own program interface with intuitive controls
analogous to the discrete actions possible in the real game.
Results are non-deterministic but discrete. The program interface
has a builtin save and load method for easily changing contexts.

The engine is also packaged as an Open AI Gym environment.

Three RL AIs are to be trained on this game, one DQN, one AQN,
and one A3C network.

The webdriver is to be an implementation of the AI, used so
players may play against the AI in the real game in the 1v1
versus mode. Image analysis is used to convert the game image
to the state representation used by the AI and project's engine,
and the webdriver performs the actions based on the AI's decisions.

The image analysis will be completed using numerous fixed position crops
followed by basic feature matching to determine which unit is in which
position, if it is holding an item, and what its stats are.