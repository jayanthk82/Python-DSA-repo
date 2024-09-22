class mergesort:
    def __init__(self,list):
        self.list = list
        self.sort()

    def sort(self):
        print("before sort",self.list)
        self.merge_sort(0,len(self.list)-1)
        self.display()

    def merge_sort(self,lower,upper):

        if lower < upper:
            mid = ((lower+upper)//2)
            self.merge_sort(lower,mid)
            self.merge_sort(mid+1,upper)
            self.merge(lower,mid,upper)


    def merge(self,lower,mid,upper):

        i=lower
        j=mid+1
        templist=list()

        while i<=mid and j<=upper:

            if(self.list[i]<self.list[j]):
                templist.append(self.list[i])
                i+=1
            else:
                templist.append(self.list[j])
                j+=1

        
        while j<=upper:
            templist.append(self.list[j])
            j+=1

       
        while i<=mid:
            templist.append(self.list[i])
            i+=1

        for i in range(len(templist)):
            self.list[lower+i] = templist[i]
    def display(self):
        print("aftersort",self.list)



                

