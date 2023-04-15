from otree.api import *


doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'adamu_farida'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age', min=17)
    gender = models.StringField(
        choices=[['male', 'male'], ['female', 'female'], ['none binary', 'none binary']],
        label='What is your gender',
        widget=widgets.RadioSelect
    )
    Question1 = models.StringField(
         label='What product was advertised?'
    )
    Question2 = models.StringField(
         label='What colours can you remember from the brand?'
    )
    Question3 = models.StringField(
        label='Describe the brand in one word.'
    )
    Question4 = models.StringField(
        label='What do you like or dislike the most about the ad?'
    )
    branduse1 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5']],
        label='On a scale of 1-5, 1 being the lowest, how likely are you to use this brand?',
        widget=widgets.RadioSelect
    )
    branduse2 = models.StringField(
        choices=[['1', '1'], ['2', '2'], ['3', '3'], ['4', '4'], ['5', '5']],
        label='On a scale of 1-5, 1 being the lowest, How likely are you to recommend our brand to your friends?',
        widget=widgets.RadioSelect
    )

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'Question1', 'Question2', 'Question3', 'Question4', 'branduse1', 'branduse2']

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

page_sequence = [MyPage, Results]
