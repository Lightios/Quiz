from screens.test_screen import TestScreen
from screens.categories_loader import questions, categories
from widgets.answer import Answer
import random


class CategoriesScreen(TestScreen):
    def __init__(self, **kwargs):
        self.questions = questions
        self.categories = categories

        super().__init__(**kwargs)

    def update_labels(self):
        for answer in self.ALL_ANSWERS:
            self.ids[answer].set_color()

        self.current_question = random.choice(self.questions)

        self.ids.contents.text = self.current_question.contents

        draw_list = [0, 1, 2, 3, 4]
        categories = [self.current_question.category]

        while len(categories) < 5:
            new_category = random.choice(self.categories)

            if new_category not in categories:
                categories.append(new_category)

        for answer in self.ALL_ANSWERS:
            index = random.choice(draw_list)
            text = categories[index]
            self.ids[answer].set_parameters(text, False)
            self.ids[answer].answer_index = index
            draw_list.remove(index)

    def check_condition(self):
        return self.selected_answer == self.current_question.category

    def mark_condition(self, answer: Answer):
        return answer.answer_index == 0
