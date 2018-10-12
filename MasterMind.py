import discord
client = discord.Client()
token = 'NTAwNDI5NjI1NzQzMTE0Mjgy.DqKvlQ.NGhVWALQt8wHAUiz5-FJJRgowPE'

class MasterMind:

    def game(self,word):
        init_string = "`"
        for char in word:
            init_string += "_ "
        init_string += "`"
        guesses = 0
        correct_placement = 0
        while correct_placement != len(word):
            guess = self.parse_next_word(len(word))
            results = self.score_word(word, guess)
            correct_placement = results[0]
            correct_number = results[1]
            self.send_guess_result('`'+guess+' '+str(correct_placement)+'|'+str(correct_number))
            guesses += 1
        return "you won in "+str(guesses)+" guesses"

    def score_word(self, word, guess):
        correct_placement = 0
        correct_number = 0
        for i in range(len(guess)):
            if guess[i] in word:
                correct_number += 1
            if guess[i] == word[i]:
                correct_placement += 1
        return [correct_placement, correct_number]

    def parse_next_word(self, word_len):
        return

    def send_guess_result(self, guess_results):
        return
