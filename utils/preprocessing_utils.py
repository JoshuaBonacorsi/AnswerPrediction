def apply_answers(example):
    try : 
        x = int(example['Answer_start'][1:-1])
    except :
        x = None
    example['answers'] = {"text":[example['Answer_text'][1:-1]],'answer_start':[x]}
    return example

def preprocess_function(data):
    data = data.map(apply_answers)
    data = data.rename_column("Paragraph", "context")
    data = data.rename_column("Question", "question")
    data = data.remove_columns("Answer_text")
    data = data.remove_columns("Theme")
    data = data.remove_columns("Answer_possible")
    data = data.remove_columns("Answer_start")
    new_column = [str(i) for i in range(len(data))]
    data = data.add_column("id", new_column)
    return(data)