# Description #
# Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

# Examples:
# balanced_parens(0) => [""]
# balanced_parens(1) => ["()"]
# balanced_parens(2) => ["()()","(())"]
# balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]


def balanced_parens(n):
    poss = []
    def form(curr, open_count, close_count): #forms under the condition that the sum = 2*n
        if close_count > open_count: #fail
            return
        if close_count+open_count == 2*n:
            poss.append(''.join(curr))
            return
        if open_count < n: #idea is to first generate n 'open parantheses' followed by n 'close parentheses' and discover other combi from there
            curr.append('(')
            form(curr, open_count+1, close_count)
            curr.pop()
        if close_count < open_count: 
            curr.append(')')
            form(curr, open_count, close_count+1)
            curr.pop()
        return
    form([], 0, 0)
    return poss
