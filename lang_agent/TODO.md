1. Simplify agent architecture: root agent becomes quiz agent, review agent as tool *
    - Instruct quiz agent to rephrase review agent's feedback to speak directly to the student
2. Add main.py runner *
3. Add diagram of agent structure to root *
4. Update tools to use dynamic, persistent data
5. Add dynamic error log / test scenario collection

# 1. Create DB *
# 2. Add initial documents (grammar rules) *
# 3. Add tool method to read ranked grammar rules from DB (initially hardcode DB, then look to dependency inject via ToolContext) *
# 4. Add tool method to update existing grammar rule most recently tested (epoch time int) *
# 5. Update agent prompt to prioritise grammar rules which haven't been tested recently *
# 6. Update get_grammar_history to take an int number of questions
# 7. Add tool method to add grammar rules to DB
# 8. Add to root_agent prompt to be able to teach new grammar rules (based on whats not in the db already) - then add them to the pool
