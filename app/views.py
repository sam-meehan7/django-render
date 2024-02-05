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

        # Use the answer_question function to process the question
        answer, vector_results = answer_question(question)

        # Update the context with the results
        context['answer'] = answer
        context['question'] = question
        context['vector_results'] = vector_results

    # Render the template with the context
    return render(request, 'app/query_form.html', context)
