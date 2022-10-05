"""
This is a simple Email slicer
that will slice the email as name and domain
for e.g., xyz@abc.com
output ans = [xyz, abc.com]
Explaination = ans[0] is name and ans[1] is domain
"""

def Slicer(email :str)->list:
    ans = []#this is the returning value

    value = ''

    for i in email:
        if i == "@":#when tackel @ just we had completed the name part
            ans.append(value)
            value = ''
        else:
            value += i
    ans.append(value)#add the last past or domail part
    return ans





ans = Slicer("xyz@outlook.com")

print(ans)
