class Army(object):

    def __init__(self,population=10000,enemy=10000,strategy=None):
        self._population = population
        self._enemy = enemy
        self._strategy = strategy if strategy else Attacking
    
    @property
    def population(self):
        return self._population

    @population.setter
    def population(self,population):
        self._population = population

    def __repr__(self):
        return "我方人数：{0} -- 敌方人数:{1} , 我方决定使用策略--{2}".format(self._population,self._enemy,self._strategy(self._enemy))


def Surronding(army):
    return "围攻"

def Attacking(army):
    return "正面强攻"

def Spliting(army):
    return "迂回策应"


def main():
    troopA = Army(strategy=Spliting)
    print(troopA)

if __name__ == '__main__':
    main()