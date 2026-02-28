# Lang agent implemented in Google ADK

This repository contains a simple Google ADK agent which acts as Korean quiz partner.
It assumes the user is an English-speaking Korean language student, and generates quizzes to test your knowledge.
It also grades & provides feedback on your answers to help you improve.

## Agent architecture

![Lang agent architecture](/lang_agent/images/lang_agent_diagram.png)

1. The agent consists of a quiz agent (root_agent) which generates quiz questions based on the user's initial input.
2. The quiz agent then collects the user's answers and saves them to state, at which point it calls the review_agent tool to grade the user's answers.
3. The quiz agent then summarises this feedback for the user to learn from & improve.

## Running the agent locally

To run the agent locally, simply run in your terminal:

```$ make run```

Or, to use the interactive ADK web UI, run:

```$ make web```

## Running the evaluation suite

The agent has basic agent monitoring configured via evalsets. To run these evaluations, run:

```$ make eval```