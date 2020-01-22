class Solution(object):
    # My solution
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral_order_boi = []
        
        while len(matrix) > 0:
            # append top numbers
            try:
                for number in matrix[0]:
                    spiral_order_boi.append(number)
                del matrix[0]
            except:
                pass
            # append right numbers 
            try:
                for row in matrix:
                    spiral_order_boi.append(row[-1])
                    del row[-1]
            except:
                pass
            # append bottom numbers in reverse order
            try:
                last_row = matrix[len(matrix) - 1][::-1]
                for number in last_row:
                    spiral_order_boi.append(number)
                del matrix[-1]
            except:
                pass
            try:
                # append left numbers in reverse order
                left_numbers = []
                for row in matrix:
                    left_numbers.append(row[0])
                    del row[0]
                left_numbers = left_numbers[::-1]
                for number in left_numbers:
                    spiral_order_boi.append(number)
            except:
                pass
        return spiral_order_boi
        
    def spiralOrderEfficient(self, matrix):
        return list(self.spiral(matrix))
        
    def spiral(self, matrix):
        if matrix:
            yield from matrix.pop(0) 
            yield from self.spiral(list(zip(*matrix))[::-1])