from cmath import inf
import copy


class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn
        self.aug_conf_matrix = copy.deepcopy(self.conf_matrix)
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        # You should keep updating following variable with best string so far.
        self.best_state = None  
    
    def augment(self):
      self.aug_conf_matrix = dict()
      for c in self.alphabet:
        self.aug_conf_matrix[c] = list()
      for c in self.alphabet:
        for x in self.conf_matrix[c]:
          self.aug_conf_matrix[x].append(c)
      for c in self.alphabet:
        self.aug_conf_matrix[c].append(c)
      for c in self.alphabet:
        self.aug_conf_matrix[c] = (self.aug_conf_matrix[c], len(self.aug_conf_matrix[c]))

    def searchWords(self, idx, sentence, depth):
      currCost = inf
      word = sentence[idx]
      currWord = [i for i in word]
      l = len(word)
      #choose any depth nos from 0 to l-1
      for n in range(l**depth):
        params = []
        for i in range(depth):
          params.append(n%l)
          n//=l
        #iterate through all possible substitutions
        prod = 1
        for i in range(depth):
          prod*= self.aug_conf_matrix[word[params[i]]][1]
        for x in range(prod):
          indices = []
          for i in range(depth):
            indices.append(x%self.aug_conf_matrix[word[params[i]]][1])
            x//=self.aug_conf_matrix[word[params[i]]][1]
          newWord = [f for f in word]
          for i in range(depth):
            newWord[params[i]] = self.aug_conf_matrix[word[params[i]]][0][indices[i]]
          sentence[idx] = ''.join(newWord)
          newCost = self.cost_fn(' '.join(sentence))
          if (newCost < currCost):
            
            currWord = newWord
            currCost = newCost
      sentence[idx] = ''.join(currWord)
      return currCost    
    def searchSentence(self, sentence, depth):
      l = len(sentence)
      for idx in range(l):
        self.searchWords(idx, sentence, depth)

    def search(self, start_state):
        """
        :param start_state: str Input string with spelling errors
        """
        sentence = start_state
        # You should keep updating self.best_state with best string so far.
        # self.best_state = start_state
        self.augment()
        for i in range(1, 5):
          sentence = start_state.split()
          self.searchSentence(sentence,i)
          self.best_state = ' '.join(sentence)
          sentence = start_state
          
        
        







        