import quiz

def test_add_question():
    q = "What is the capital of France?"
    a = "Paris"
    quiz.add_question(q, a)
    assert quiz.questions == {q: a}

def test_get_question():
    quiz.questions = {"What is the capital of France?": "Paris",
                      "What is the tallest mountain in the world?": "Mount Everest"}
    q = quiz.get_question()
    assert q in quiz.questions.keys()

def test_check_answer():
    quiz.questions = {"What is the capital of France?": "Paris",
                      "What is the tallest mountain in the world?": "Mount Everest"}
    q = "What is the capital of France?"
    a = "Paris"
    assert quiz.check_answer(q, a) == True
    a = "London"
    assert quiz.check_answer(q, a) == False

if __name__ == "__main__":
    test_add_question()
    test_get_question()
    test_check_answer()
    print("All tests passed!")
