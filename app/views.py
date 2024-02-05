from django.shortcuts import render
from .query_vector import answer_question  # Make sure this is the correct path to your function
import random

# Define an array of fun facts
fun_facts = [
    "DoneDeal has over 70,000 cars for sale!",
    "DoneDeal has over 15,000 electric and hybrid cars for sale!"
]

def index(request):
    context = {
        'answer': None,
        'question': '',
        'vector_results': None,
        'fun_fact': random.choice(fun_facts),  # Select a random fun fact
    }

    if request.method == 'POST':
        # Get the question from the form input
        question = request.POST.get('question')

        answer, vector_results = answer_question(question)

        # Process the answer into structured data
        answer_sections = answer.split('\n\n')  # Split the answer by two newlines
        structured_answer = []
        for i in range(0, len(answer_sections), 2):
            if i + 1 < len(answer_sections):
                structured_answer.append({
                    'make_model': answer_sections[i].strip(),
                    'summary': answer_sections[i + 1].strip()
                })

        # Update the context with the structured answer
        context['answer'] = structured_answer
        context['question'] = question
        context['vector_results'] = vector_results

    # Render the template with the context
    return render(request, 'app/query_form.html', context)
