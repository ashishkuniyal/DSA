class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        ans=[]
        i,j=0,0
        UP,RIGHT,DOWN,LEFT=0,1,2,3
        direction=RIGHT
        up_wall=0
        right_wall=n
        left_wall=-1
        down_wall=m
        while len(ans)!=m*n:
            if direction==RIGHT:
                while j<right_wall:
                    ans.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                right_wall-=1
                direction=DOWN
            elif direction==DOWN:
                while i<down_wall:
                    ans.append(matrix[i][j])
                    i+=1
                i,j=i-1,j-1
                down_wall-=1
                direction=LEFT
            elif direction==LEFT:
                while j>left_wall:
                    ans.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                left_wall+=1
                direction=UP
            else:
                while i>up_wall:
                    ans.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                up_wall+=1
                direction=RIGHT
        return ans




        