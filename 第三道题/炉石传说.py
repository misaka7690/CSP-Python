n=int(input())

class TwoHero:
    def __init__(self):
        self.First_Hero=[0,30]
        self.Second_Hero=[0,30]
        self.Winner=None
        self.First_Attendants=[]
        self.Second_Attendants=[]

    def First_summon(self,p,a,h):
        # m=len(self.First_Attendants)
        # if p==m+1:
        #     self.First_Attendants.append([a,h])
        # else:
        #     self.First_Attendants.insert(p-1,[a,h])
        self.First_Attendants.insert(p-1,[a,h])
    
    def Second_summon(self,p,a,h):
        self.Second_Attendants.insert(p-1,[a,h])

    def First_Attack(self,first_index,second_index):
        if  second_index:
            attacker=self.First_Attendants[first_index-1]
            defender=self.Second_Attendants[second_index-1]

            attacker[1]-=defender[0]
            defender[1]-=attacker[0]

            if attacker[1]<=0:
                self.First_Attendants.pop(first_index-1)
            else:
                self.First_Attendants[first_index-1]=attacker
            
            if defender[1]<=0:
                self.Second_Attendants.pop(second_index-1)
            else:
                self.Second_Attendants[second_index-1]=defender
        else:
            attacker=self.First_Attendants[first_index-1]
            defender=self.Second_Hero

            attacker[1]-=defender[0]
            defender[1]-=attacker[0]

            if attacker[1]<=0:
                self.First_Attendants.pop(first_index-1)
            else:
                self.First_Attendants[first_index-1]=attacker
            
            if defender[1]<=0:
                self.Winner='First'
            else:
                self.Second_Hero=defender

    def Second_Attack(self,second_index,first_index):
        if  first_index:
            attacker=self.Second_Attendants[second_index-1]
            defender=self.First_Attendants[first_index-1]

            attacker[1]-=defender[0]
            defender[1]-=attacker[0]

            if attacker[1]<=0:
                self.Second_Attendants.pop(second_index-1)
            else:
                self.Second_Attendants[second_index-1]=attacker
            
            if defender[1]<=0:
                self.First_Attendants.pop(first_index-1)
            else:
                self.First_Attendants[first_index-1]=defender
        else:
            attacker=self.Second_Attendants[second_index-1]
            defender=self.First_Hero

            attacker[1]-=defender[0]
            defender[1]-=attacker[0]

            if attacker[1]<=0:
                self.Second_Attendants.pop(second_index-1)
            else:
                self.Second_Attendants[second_index-1]=attacker

            if defender[1]<=0:
                self.Winner='Second'
            else:
                self.First_Hero=defender


    def report(self):
        if self.Winner==None:
            print(0)
        else:
            if self.Winner=='First':
                print(1)
            else:
                print(-1)
        
        print(self.First_Hero[1])

        t1=[]
        for tmp in self.First_Attendants:
            t1.append(tmp[1])
        
        print(str(len(t1))+' '+' '.join(map(str,t1)))

        print(self.Second_Hero[1])

        t2=[]
        for tmp in self.Second_Attendants:
            t2.append(tmp[1])
        
        print(str(len(t2))+' '+' '.join(map(str,t2)))


persons=TwoHero()
flag=1
for i in range(n):
    text=input().split()
    if len(text)==1:
        flag=0 if flag==1 else 1
    if text[0]=='summon':
        p=int(text[1])
        a=int(text[2])
        h=int(text[3])
        if flag:
            persons.First_summon(p,a,h)
        else:
            persons.Second_summon(p,a,h)
    if text[0]=='attack':
        aer=int(text[1])
        der=int(text[2])
        if flag:
            persons.First_Attack(aer,der)
        else:
            persons.Second_Attack(aer,der)

persons.report()