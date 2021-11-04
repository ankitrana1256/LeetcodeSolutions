class Solution:
    def sumNumbers(root) -> int:
        if not root: return 0
        
        output = []
        
        def pre(node, sofar):
            if not node.left and not node.right:
                output.append("".join(sofar+[str(node.val)]))
                
            if node.left: pre(node.left,sofar+[str(node.val)])
            if node.right: pre(node.right,sofar+[str(node.val)])
                
        pre(root,[])
        
        return sum([int(x) for x in output])
    
root = [1,2,3]
a = Solution.sumNumbers(root)
print(a)