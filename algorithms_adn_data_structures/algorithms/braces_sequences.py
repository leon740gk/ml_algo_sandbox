from data_structures.my_stack import MyStack


def is_braces_sequence_correct(sequence: str) -> bool:
    """
    Check if braces sequence is correct
    :param sequence: string of braces
    :return: True or False
    """
    stack = MyStack()
    for brace in sequence:
        if brace not in "()[]":
            continue
        if brace in "([":
            stack.push(brace)
        else:
            if stack.is_empty():
                return False
            left_brace = stack.pop()
            right_brace = ")" if left_brace == "(" else "]"
            if right_brace != brace:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    sequence_1 = "((([[]])))[]()"
    sequence_2 = "((sd(sdc[[]]sdc))sdc)[g]efc(erevce)"
    sequence_3 = "([)]"
    sequence_4 = "["
    sequence_5 = ")"
    sequences = [
        sequence_1,
        sequence_2,
        sequence_3,
        sequence_4,
        sequence_5
    ]
    correct_answers = [True, True, False, False, False]
    for i, sequence in enumerate(sequences):
        result = is_braces_sequence_correct(sequence)
        assert result == correct_answers[i], \
            f"result: {result}, correct_answer: {correct_answers[i]}, on i {i}"
