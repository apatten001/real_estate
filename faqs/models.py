from django.db import models

# Create your models here.


class FrequentQuestions(models.Model):

    """
    Frequently asked questions
    """

    question = models.CharField(max_length=250)

    def __str__(self):
        return self.question


class FrequentQuestionsAnswers(models.Model):

    """
    Answers to the frequently asked questions.
    """

    question = models.ForeignKey(FrequentQuestions, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return self.answer



