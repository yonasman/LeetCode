class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            p1,p2 = 0, len(image[i]) - 1
            while(p1 <= p2):
                image[i][p1],image[i][p2] = 1- image[i][p2],1 - image[i][p1]
                p1 += 1
                p2 -= 1
        return image