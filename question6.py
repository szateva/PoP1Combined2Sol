def generate_sentences(subjects, predicates, objects):
    subjects.sort()
    predicates.sort()
    objects.sort()
    sents = ""
    for s in subjects:
        for p in predicates:
            for o in objects:
                sents+= s + " " + p + " " + o + ". "
    return sents[:-1]

