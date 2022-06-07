[![Tests](https://github.com/CallThemHunter/SuperAutoPetsAI/actions/workflows/test-SAP-app.yml/badge.svg?event=push)](https://github.com/CallThemHunter/SuperAutoPetsAI/actions/workflows/test-SAP-app.yml)

Super Auto Pets AI

This project has 3 major components:

- Game Engine
- Reinforcement Learning AI
- Selenium Webdriver

The engine mimics the engine which
drives the game Super Auto Pets (c. Team
Wood Games) as best as I could determine
through reverse engineering the logic
behind the game mechanics.

The engine is to support save and load states
through the OpenAI Gym API. Outputs are
non-deterministic but discrete.

The RL AI is to be trained on artificial
matches generated within this project's
game engine. The AI incrementally learns
how to play the game, eventually becoming
skilled.

The webdriver is to be an implementation of the
AI, used so players may play against the
AI in the real game. Image analysis is
used to convert the game image to the
state representation used by the AI and
project's engine, and the webdriver performs
the actions based on the AI's decisions.