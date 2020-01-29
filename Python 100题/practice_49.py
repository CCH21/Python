def fun(s):
    if len(s) & 1 != 0:                         # 如果表达式长度为奇数，表达式无效
        return False
    stack = []                                  # 初始化栈
    mapping = {")": "(", "]": "[", "}": "{"}    # 建立哈希映射
    for char in s:                              # 一次处理表达式的每个括号
        if char in mapping:
            # 如果遇到闭括号，检查栈顶元素
            # 如果是一个相同类型的开括号，将它从栈中弹出并继续处理
            # 否则，表达式无效
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:                                   # 如果遇到开括号，推到栈上，稍后处理
            stack.append(char)
    return not stack                            # 如果到最后栈中仍然有元素，表达式无效；反之，表达式有效


bracket = input()
print(fun(bracket))
