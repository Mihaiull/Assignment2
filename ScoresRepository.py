#colorama for making it fancy
from colorama import Fore, Style

#The class that has a list of scores and methods to manipulate it
class ScoresRepository:
    def __init__(self):
        self.scores = []
        self.scores_undo = []

    # Add a score to the list
    #@input: score - the score to be added
    def add_score(self, score):
        self.scores.append(score)
        self.scores_undo.append(self.scores[:])

    #My refusal to use a for led me to use a for
    #@input scores - a list of scores to be added
    def add_scores(self, scores):
        for i in range(len(scores)):
            self.scores.append(scores[i])
        self.scores_undo.append(self.scores[:])

    #Add a score at an index to the list
    #@input: index - the index where the score will be added
    #@input: score - the score to be added
    def add_score_at_index(self, index, score):
        self.scores.insert(index, score)
        self.scores_undo.append(self.scores[:])

    #Remove the score at an index:
    #@input index - the index of the score to be removed
    def remove_score_at_index(self, index):
        self.scores.pop(index)
        self.scores_undo.append(self.scores[:])

    #Remove the scores between two indexes:
    #@input index1 - the start index
    #@input index2 - the end index
    def remove_scores_between_indexes(self, index1, index2):
        for i in range(index2, index1-1, -1):
            self.scores.pop(i)
        self.scores_undo.append(self.scores[:])

    #Replace the score at given index:
    #@input index - the index of the score to be replaced
    #@input score - the new score
    def replace_score_at_index(self, index, score):
        self.scores[index] = score
        self.scores_undo.append(self.scores[:])
    
    #Get indexes with scores less than a value:
    #@input score - the value
    #@output indexes - the list of indexes with scores less than the value
    def get_indexes_with_scores_less_than(self, score):
        indexes = []
        for i in range(len(self.scores)):
            if self.scores[i] < score:
                indexes.append(i)
        return indexes
    
    #Get all indexes sorted by their score:
    #@output indexes - the list of indexes sorted by score
    def get_indexes_sorted_by_score(self):
        indexes = []
        for i in range(len(self.scores)):
            indexes.append(i)
        indexes.sort(key=lambda x: self.scores[x])
        return indexes
    
    #Get indexes with scores higher than a value and sorted:
    #@input score - the value
    #@output indexes - the list of indexes with scores higher than the value
    def get_indexes_with_scores_higher_than(self, score):
        indexes = []
        for i in range(len(self.scores)):
            if self.scores[i] > score:
                indexes.append(i)
        indexes.sort(key=lambda x: self.scores[x])
        return indexes
    
    #Get the average scores between two indexes:
    #@input index1 - the start index
    #@input index2 - the end index
    #@output average - the average of the scores between the indexes
    def get_average_scores_between_indexes(self, index1, index2):
        total = 0
        for i in range(index1, index2+1):
            total += self.scores[i]
        return round(total / (index2 - index1 + 1), 2)
    
    #Get the minimum score between two indexes:
    #@input index1 - the start index
    #@input index2 - the end index
    #@output minimum - the minimum score between the indexes
    def get_minimum_score_between_indexes(self, index1, index2):
        minimum = self.scores[index1]
        for i in range(index1, index2):
            if self.scores[i] < minimum:
                minimum = self.scores[i]
        return minimum
    
    #Get the scores of participants between two indexes that are multiples of a given value:
    #@input index1 - the start index
    #@input index2 - the end index
    #@input multiple - the value
    def get_scores_between_indexes_multiples_of(self, index1, index2, multiple):
        scores = []
        for i in range(index1, index2):
            if self.scores[i] % multiple == 0:
                scores.append(self.scores[i])
        return scores
    
    #Keep only participants with scores multiple of a value, removing the others:
    #@input multiple - the value
    def keep_only_scores_multiple_of(self, multiple):
        for i in range(len(self.scores)-1, -1, -1):
            if self.scores[i] % multiple != 0 or self.scores[i] < multiple or self.scores[i] == 0:
                del self.scores[i]
        self.scores_undo.append(self.scores[:])

    #Keep only participants with scores higher than a value, removing the other:
    #@input score - the value
    def keep_only_scores_higher_than(self, score):
        for i in range(len(self.scores)-1, -1, -1):
            if self.scores[i] <= score:
                del self.scores[i]
        self.scores_undo.append(self.scores[:])

    #UNDO:
    def undo(self):
        if len(self.scores_undo) == 0:
            print("Nothing to undo!")
        else:
            try:
                self.scores_undo.pop()
                self.scores.clear()
                for i in range(len(self.scores_undo[-1])):
                    self.scores.append(self.scores_undo[-1][i])
            except:
                print("Nothing to undo!")
    
    def read_list_from_file(self, filepath):
        with open(filepath, "r") as f:
            self.scores = [int(x) for x in f.read().split(",")]

    def write_list_to_file(self, filepath):
        with open(filepath, "w") as f:
            f.write(",".join([str(x) for x in self.scores]))

    def write_list_to_file(self):
        with open("output.txt", "w") as f:
            f.write(",".join([str(x) for x in self.scores]))
    def read_list_from_file(self):
        with open("input.txt", "r") as f:
            self.scores = [int(x) for x in f.read().split(",")]

    #Method to print the list of scores
    #@output: string - the string to be printed
    def __str__(self):
        string = "\n"
        string +="[ "
        for i in range(len(self.scores)):
            string +=Fore.GREEN + str(self.scores[i])
            string += " "
        string += Style.RESET_ALL
        string += "]"
        return string
