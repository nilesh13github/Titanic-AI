import re

def fix_sql_spacing(query):
    # Add a space after commas if missing
    query = re.sub(r',(\S)', r', \1', query)

    # Add spaces between camelCase or numbers and letters
    query = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', query)
    query = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', query)

    # Fix missing space inside SQL functions like COUNT (*)
    query = re.sub(r'(\b[A-Z]+\b) \(', r'\1(', query)

    # List of SQL keywords
    keywords = ['SELECT', 'FROM', 'WHERE', 'GROUP BY', 'ORDER BY', 'HAVING', 'JOIN', 
                'ON', 'AS', 'AND', 'OR', 'NOT', 'SUM', 'COUNT', 'BY']

    # Ensure keywords are properly spaced
    for keyword in keywords:
        query = re.sub(r'(?i)(\b' + keyword.replace(" ", r"\s+") + r'\b)(\S)', r'\1 \2', query)
        query = re.sub(r'(\S)(\b' + keyword.replace(" ", r"\s+") + r'\b)', r'\1 \2', query)

    # Ensure proper spacing for multi-word keywords (GROUP BY, ORDER BY)
    query = re.sub(r'(?i)\b(GROUP|ORDER)\s*BY\b', r'\1 BY', query)

    # Fix cases where a number sticks to a keyword (like 0GROUP BY)
    query = re.sub(r'(\d)(GROUP|ORDER|HAVING|JOIN|ON|BY)', r'\1 \2', query, flags=re.IGNORECASE)

    # Fix missing space between functions and FROM, GROUP BY, etc.
    query = re.sub(r'(\))(\bFROM\b|\bGROUP BY\b|\bORDER BY\b)', r'\1 \2', query, flags=re.IGNORECASE)

    # Remove extra spaces
    query = re.sub(r'\s+', ' ', query).strip()

    return query

# Test case
print(fix_sql_spacing("SELECT age, COUNT (*) as frequency FROM Observation WHERE sex_id = 0GROUP BY age"))
