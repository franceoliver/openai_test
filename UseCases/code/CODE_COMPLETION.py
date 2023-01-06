# Template https://plainenglish.io/blog/generate-python-code-with-openai-codex-api-9617f8acd7bd
# offical doc https://beta.openai.com/docs/guides/code/best-practices

import os
import openai

openai.api_key = "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"

prompt = """SELECT DISTINCT department.name
FROM department
JOIN employee ON department.id = employee.department_id
JOIN salary_payments ON employee.id = salary_payments.employee_id
WHERE salary_payments.date BETWEEN '2020-06-01' AND '2020-06-30'
GROUP BY department.name
HAVING COUNT(employee.id) > 10;
-- Explanation of the above query in human readable format"""

response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=prompt,
            temperature=0,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)

print(response['choices'][0]['text'])