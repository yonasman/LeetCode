class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for img in image:
            p1 = 0
            p2 = len(img) - 1
            while(p1 <= p2): 
                img[p1], img[p2] = 1- img[p2],1- img[p1]
                p1 += 1
                p2 -= 1
        return image