# Lang agent implemented in Google ADK

This repository contains a simple Google ADK agent which acts as Korean quiz partner.
It assumes the user is an English-speaking Korean language student, and generates quizzes to test your knowledge.
It also grades & provides feedback on your answers to help you improve.

## Running the agent locally

To run the agent locally, simply run in your terminal:

```$ make run```

Or, to use the interactive ADK web UI, run:

```$ make web```

## Running the evaluation suite

The agent has basic agent monitoring configured via evalsets. To run these evaluations, run:

```$ make eval```