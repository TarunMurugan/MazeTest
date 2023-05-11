import API
import sys

class MazeSolve:

    def __init__(self):
        #y-->,x--down
        self.flood=[[14,13,12,11,10,9,8,7,7,8,9,10,11,12,13,14],
                    [13,12,11,10,9,8,7,6,6,7,8,9,10,11,12,13],
                    [12,11,10,9,8,7,6,5,5,6,7,8,9,10,11,12],
                    [11,10,9,8,7,6,5,4,4,5,6,7,8,9,10,11],
                    [10,9,8,7,6,5,4,3,3,4,5,6,7,8,9,10],
                    [9,8,7,6,5,4,3,2,2,3,4,5,6,7,8,9],
                    [8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8],
                    [7,6,5,4,3,2,1,0,0,1,2,3,4,5,6,7],
                    [7,6,5,4,3,2,1,0,0,1,2,3,4,5,6,7],
                    [8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8],
                    [9,8,7,6,5,4,3,2,2,3,4,5,6,7,8,9],
                    [10,9,8,7,6,5,4,3,3,4,5,6,7,8,9,10],
                    [11,10,9,8,7,6,5,4,4,5,6,7,8,9,10,11],
                    [12,11,10,9,8,7,6,5,5,6,7,8,9,10,11,12],
                    [13,12,11,10,9,8,7,6,6,7,8,9,10,11,12,13],
                    [14,13,12,11,10,9,8,7,7,8,9,10,11,12,13,14]]


        self.queue=[]
        self.walls=[]
        self.orientation=1 #1-right, 2-down , 3-left, 4-up
        self.orient_list={1:[0,1],2:[1,0],3:[0,-1],4:[-1,0]}
        self.wall_flag=0
        self.current_cell=[0,0]
        self.flooded=[]

    def log(self,string): #only for simulating
        sys.stderr.write("{}\n".format(string))
        sys.stderr.flush()


    def index_2d(self,myList, v):    #check
        for i, x in enumerate(myList):
            if v in x:
                return [i, x.index(v)]
    
    def neighbour(self,cell):
        if 15>cell[0]>0 and 15>cell[1]>0:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]-1],[cell[0]-1,cell[1]],[cell[0],cell[1]+1]]
        elif cell[0]==0 and 15>cell[1]>0:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]-1],[cell[0],cell[1]+1]]
        elif cell[0]==15 and 15>cell[1]>0:
            neighbours=[[cell[0],cell[1]-1],[cell[0]-1,cell[1]],[cell[0],cell[1]+1]]
        elif 15>cell[0]>0 and cell[1]==0:
            neighbours=[[cell[0]+1,cell[1]],[cell[0]-1,cell[1]],[cell[0],cell[1]+1]]
        elif 15>cell[0]>0 and cell[1]==15:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]-1],[cell[0]-1,cell[1]]]
        elif cell[0]==0 and cell[1]==0:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]+1]]
        elif cell[0]==15 and cell[1]==15:
            neighbours=[[cell[0],cell[1]-1],[cell[0]-1,cell[1]]]    
        elif cell[0]==0 and cell[1]==15:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]-1]]
        elif cell[0]==15 and cell[1]==0:
            neighbours=[[cell[0]-1,cell[1]],[cell[0],cell[1]+1]]
        return neighbours




    def neighbour_accesible(self,cell):
        if 15>cell[0]>0 and 15>cell[1]>0:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]-1],[cell[0]-1,cell[1]],[cell[0],cell[1]+1]]
        elif cell[0]==0 and 15>cell[1]>0:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]-1],[cell[0],cell[1]+1]]
        elif cell[0]==15 and 15>cell[1]>0:
            neighbours=[[cell[0],cell[1]-1],[cell[0]-1,cell[1]],[cell[0],cell[1]+1]]
        elif 15>cell[0]>0 and cell[1]==0:
            neighbours=[[cell[0]+1,cell[1]],[cell[0]-1,cell[1]],[cell[0],cell[1]+1]]
        elif 15>cell[0]>0 and cell[1]==15:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]-1],[cell[0]-1,cell[1]]]
        elif cell[0]==0 and cell[1]==0:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]+1]]
        elif cell[0]==15 and cell[1]==15:
            neighbours=[[cell[0],cell[1]-1],[cell[0]-1,cell[1]]]    
        elif cell[0]==0 and cell[1]==15:
            neighbours=[[cell[0]+1,cell[1]],[cell[0],cell[1]-1]]
        elif cell[0]==15 and cell[1]==0:
            neighbours=[[cell[0]-1,cell[1]],[cell[0],cell[1]+1]]

        neighbours=[i for i in neighbours if [i,cell] not in self.walls and [cell,i] not in self.walls]

        # for i in neighbours:
        #     if [cell,i] in self.walls:
        #         neighbours.remove(i)     
        return neighbours

    def floodfill(self):
        self.log("queue:{}".format(self.queue))
        cell=self.queue.pop()
        neighbours=self.neighbour_accesible(cell)
        self.log("floodfill:accessible:{}".format(neighbours))
        # self.log("floodfill:neightbours:{}".format(neighbours))
        
        # for i in neighbours:
        #     if [cell,i] in self.walls:
        #         neighbours.remove(i)
        
        neighbour_vals=[self.flood[i[0]][i[1]] for i in neighbours]
        if self.flood[cell[0]][cell[1]]<=min(neighbour_vals):
            self.flood[cell[0]][cell[1]]=min(neighbour_vals)+1
                # self.log(self.flood[0])
                # self.log(self.flood[1])
                # self.log(self.flood[2])
                # self.log(self.flood[3])
                # self.log(self.flood[4])
                # self.log(self.flood[5])
                # self.log(self.flood[6])
                # self.log(self.flood[7])
                # self.log(self.flood[8])
                # self.log(self.flood[9])
                # self.log(self.flood[10])
                # self.log(self.flood[11])
                # self.log(self.flood[12])
                # self.log(self.flood[13])
                # self.log(self.flood[14])
                # self.log(self.flood[15])
            self.queue=neighbours+self.queue
            
                
            
    def floodfillqueue(self,cell):
        self.queue.insert(0,cell)
        i=1
        while self.queue!=[]:
            self.floodfill()
            # self.log("floodfillqueue:iteration:{}".format(i))

            i+=1   
       





    #make only unique values, pairs get registered multiple times
    def walldetected(self,abs_orientation):  #1-right, 2-down , 3-left, 4-up
        
        cell=self.current_cell
        self.log("walldetect:abs orient of wall:{},cell:{}".format(abs_orientation,cell))
        if abs_orientation==1 and cell[1]!=15:
            if [cell,[cell[0],cell[1]+1]] not in self.walls or [[cell[0],cell[1]+1],cell] not in self.walls:
                self.walls.append([cell,[cell[0],cell[1]+1]]) 
            # self.walls.append([[cell[0],cell[1]+1],cell])
        elif abs_orientation==3 and cell[1]!=0:
            if [cell,[cell[0],cell[1]-1]] not in self.walls or [[cell[0],cell[1]-1],cell] not in self.walls:
                self.walls.append([cell,[cell[0],cell[1]-1]])
            # self.walls.append([[cell[0],cell[1]-1],cell])
        elif abs_orientation==4 and cell[0]!=0:
            if [cell,[cell[0]-1,cell[1]]] not in self.walls or [[cell[0]-1,cell[1]],cell] not in self.walls:
                self.walls.append([cell,[cell[0]-1,cell[1]]])
            # self.walls.append([[cell[0]-1,cell[1]],cell])
        elif abs_orientation==2 and cell[0]!=15:
            if [cell,[cell[0]+1,cell[1]]] not in self.walls or [[cell[0]+1,cell[1]],cell] not in self.walls:
                self.walls.append([cell,[cell[0]+1,cell[1]]])
            # self.walls.append([[cell[0]+1,cell[1]],cell])

    def next_cell(self,cell,ignore=[]):
        self.log("next_cell:ignore:{}".format(ignore))
        neighbours=[i for i in self.neighbour(cell) if i not in ignore]
        # for i in neighbours:
        #     if [cell,i] in self.walls:
        #         neighbours.remove(i)
        neighbour_values=[self.flood[i][j] for [i,j] in neighbours]
        # self.log("neighbours:{}".format(neighbours))
        indices=[i for i in range(len(neighbour_values)) if neighbour_values[i]==min(neighbour_values)]
        for i in indices:
            if [neighbours[i][0]-cell[0],neighbours[i][1]-cell[1]]==self.orient_list[self.orientation]:
                index=i
                break
            else:
                index=indices[0]
        next_cell=neighbours[index]
        if [cell,next_cell] not in self.walls and [next_cell,cell] not in self.walls:
            if self.flood[cell[0]][cell[1]]<=self.flood[next_cell[0]][next_cell[1]]:
                self.floodfillqueue(cell)
            return next_cell
        else:
            self.floodfillqueue(cell)
            ignore.append(next_cell)
            return self.next_cell(cell,ignore)
        
    
    def wall_data(self):

        if API.wallLeft():
            abs_orient_wall=self.orientation-1 if self.orientation!=1 else 4 
            self.walldetected(abs_orient_wall)
            self.log("wall left")
        if API.wallRight():
            abs_orient_wall=self.orientation+1 if self.orientation!=4 else 1 
            self.walldetected(abs_orient_wall)
            self.log("wall right")
        if API.wallFront():
            self.walldetected(self.orientation)
            self.log("wall front")


    def move(self,to_cell):
        diff=[to_cell[0]-self.current_cell[0],to_cell[1]-self.current_cell[1]]#1-right, 2-down , 3-left, 4-up
        cell_next_orientation=[i for i in self.orient_list if self.orient_list[i]==diff][0]
        orientation_diff=cell_next_orientation-self.orientation
        self.log("move:next_oreint:{}".format(cell_next_orientation))
        self.log("move:self_oreint:{}".format(self.orientation))
        self.log("move:oreint_diff:{}".format(orientation_diff))
        if orientation_diff==0:
            API.moveForward()
        elif orientation_diff==1 or orientation_diff==-3:
            API.turnRight()
            API.moveForward()
        elif orientation_diff==-1 or orientation_diff==3:
            API.turnLeft()
            API.moveForward()
        elif orientation_diff==2 or orientation_diff==-2:
            API.turnRight()
            API.turnRight()
            API.moveForward()
        self.current_cell=to_cell
        self.orientation+=orientation_diff
        self.log(self.flood[0])
        self.log(self.flood[1])
        self.log(self.flood[2])
        self.log(self.flood[3])
        self.log(self.flood[4])
        self.log(self.flood[5])
        self.log(self.flood[6])
        self.log(self.flood[7])
        self.log(self.flood[8])
        self.log(self.flood[9])
        self.log(self.flood[10])
        self.log(self.flood[11])
        self.log(self.flood[12])
        self.log(self.flood[13])
        self.log(self.flood[14])
        self.log(self.flood[15]) 


    def combined(self):
        self.log("Running...")
        API.setColor(0, 0, "G")
        API.setText(0, 0, "abc")
        while self.flood[self.current_cell[0]][self.current_cell[1]]!=0:
            self.log("current_cell:{}".format(self.current_cell))
            self.wall_data()
            self.log("walls:{}".format(self.walls))
            move_to=self.next_cell(self.current_cell,[])
            self.log("combined:moveto:{}".format(move_to))
            self.move(move_to)

    

if __name__ == "__main__":
    object=MazeSolve()
    object.combined()
    object.log(object.flood)
    object.log(object.walls)
   


        









