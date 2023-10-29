from colorama import Fore, Style

class ScoresRepository:
    def __init__(self):
        self.scores = []
        self.scores_undo = []

    # Add a score to the list
    def add_score(self, score):
        self.scores_undo.append(self.scores[:])
        self.scores.append(score)
    def add_scores(self, scores):
        self.scores_undo.append(self.scores[:])
        for i in range(len(scores)):
            self.scores.append(scores[i])
    #Add a score at an index to the list
    def add_score_at_index(self, index, score):
        self.scores_undo.append(self.scores[:])
        self.scores.insert(index, score)

    #Remove the score at an index:
    def remove_score_at_index(self, index):
        self.scores_undo.append(self.scores[:])
        self.scores.pop(index)
    #Remove the scores between two indexes:
    def remove_scores_between_indexes(self, index1, index2):
        self.scores_undo.append(self.scores[:])
        for i in range(index2, index1-1, -1):
            self.scores.pop(i)
    #Replace the score at given index:
    def replace_score_at_index(self, index, score):
        self.scores_undo.append(self.scores[:])
        self.scores[index] = score
    
    #Get indexes with scores less than a value:
    def get_indexes_with_scores_less_than(self, score):
        indexes = []
        for i in range(len(self.scores)):
            if self.scores[i] < score:
                indexes.append(i)
        return indexes
    #Get all indexes sorted by their score:
    def get_indexes_sorted_by_score(self):
        indexes = []
        for i in range(len(self.scores)):
            indexes.append(i)
        indexes.sort(key=lambda x: self.scores[x])
        return indexes
    #Get indexes with scores higher than a value and sorted:
    def get_indexes_with_scores_higher_than(self, score):
        indexes = []
        for i in range(len(self.scores)):
            if self.scores[i] > score:
                indexes.append(i)
        indexes.sort(key=lambda x: self.scores[x])
        return indexes
    
    #Get the average scores between two indexes:
    def get_average_scores_between_indexes(self, index1, index2):
        total = 0
        for i in range(index1, index2+1):
            total += self.scores[i]
        return round(total / (index2 - index1), 2)
    #Get the minimum score between two indexes:
    def get_minimum_score_between_indexes(self, index1, index2):
        minimum = self.scores[index1]
        for i in range(index1, index2):
            if self.scores[i] < minimum:
                minimum = self.scores[i]
        return minimum
    
    #Get the scores of participants between two indexes
    #that are multiples of a given value:
    def get_scores_between_indexes_multiples_of(self, index1, index2, multiple):
        scores = []
        for i in range(index1, index2):
            if self.scores[i] % multiple == 0:
                scores.append(self.scores[i])
        return scores
    
    #Keep only participants with scores multiple of a value, removing the others:
    def keep_only_scores_multiple_of(self, multiple):
        self.scores_undo.append(self.scores[:])
        for i in range(len(self.scores)):
            if self.scores[i] % multiple != 0:
                self.scores.pop(i)
    #Keep only participants with scores higher than a value, removing the other:
    def keep_only_scores_higher_than(self, score):
        self.scores_undo.append(self.scores[:])
        for i in range(len(self.scores)):
            if self.scores[i] <= score:
                self.scores.pop(i)
    #UNDO:
    def undo(self):
        if len(self.scores_undo) == 0:
            print("Nothing to undo!")
        else:
            try:
                self.scores_undo.pop()
                self.scores = []
                for i in range(len(self.scores_undo[-1])):
                    self.scores.append(self.scores_undo[-1][i])
            except:
                print("Nothing to undo!")

    def __str__(self):
        string = "\n"
        string +="[ "
        for i in range(len(self.scores)):
            string +=Fore.GREEN + str(self.scores[i])
            string += " "
        string += Style.RESET_ALL
        string += "]"
        return string
