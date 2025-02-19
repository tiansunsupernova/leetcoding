class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for x in asteroids:
            keep_x = True
            while st and x < 0 and st[-1] > 0:
                if st[-1] + x < 0: 
                    st.pop()
                elif st[-1] + x == 0:
                    st.pop()
                    keep_x = False
                    break
                else:
                    keep_x = False
                    break
            if keep_x: st.append(x)
        return st                        

