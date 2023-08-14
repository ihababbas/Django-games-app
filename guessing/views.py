from django.shortcuts import render
from random import randint

def guessing_game(request):
    if request.method == 'POST':
        guessed_number = int(request.POST['guessed_number'])
        number_to_guess = request.session.get('number_to_guess')
        count = request.session.get('count', 5)
        score = request.session.get('score', 0)
        
        if guessed_number == number_to_guess:
            score += count * 2
            result = f"Congratulations! You guessed the number {number_to_guess}. Your score is {score}."
            number_to_guess = randint(1, 20)
            count = 5
        elif guessed_number > number_to_guess:
            result = f"Your guess is too high. {count - 1} rounds left."
            count -= 1
        else:
            result = f"Your guess is too low. {count - 1} rounds left."
            count -= 1
        
        request.session['number_to_guess'] = number_to_guess
        request.session['count'] = count
        request.session['score'] = score
    else:
        number_to_guess = randint(1, 20)
        request.session['number_to_guess'] = number_to_guess
        request.session['count'] = 5
        request.session['score'] = 0
        result = "Welcome to the Guessing Game!"
    
    context = {
        'result': result,
        'score': request.session['score'],
        'count': request.session['count'],
        'number_to_guess': request.session['number_to_guess']
    }
    
    return render(request, 'game.html', context)
