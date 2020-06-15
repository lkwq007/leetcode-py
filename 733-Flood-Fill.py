class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        height=len(image)
        width=len(image[0])
        if height<1 or width<1:
            return image
        color=image[sr][sc]
        if color==newColor:
            return image
        def dfs(y,x):
            if y>=0 and y<height and x>=0 and x<width and image[y][x]==color:
                image[y][x]=newColor
                dfs(y,x+1)
                dfs(y,x-1)
                dfs(y+1,x)
                dfs(y-1,x)
        dfs(sr,sc)
        return image