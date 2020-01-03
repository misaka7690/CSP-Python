import sys
import re

sys.stdin = open("input.txt", "r")
P, H, L = 0, 1, 2


class Translator:
    def __init__(self): 
        self.markdown = []
        markdown = sys.stdin.read().split("\n\n")
        for i in range(len(markdown)):
            markdown[i] = markdown[i].strip("\n")
        for m in markdown:
            if len(m) > 0:
                self.markdown.append(m)

    # 判断区块类型
    def f1(self, s):
        if s[0] == "#":
            return H
        if s[0] == "*":
            return L
        return P

    # 转化H类型
    def f2(self, H):
        s = H.split(maxsplit=1)
        x = len(s[0])
        return f"<h{x}>{s[1]}</h{x}>"

    # 转化P类型
    def f3(self, P):
        return f"<p>{P}</p>"

    # 转化L类型
    def f4(self, L):
        L = L.split("\n")
        for i in range(len(L)):
            L[i] = L[i].strip("*")
            L[i] = L[i].strip()
            L[i] = f"<li>{L[i]}</li>"
        t = "\n".join(L)
        return f"<ul>\n{t}\n</ul>"

    # 对所有区块进行处理然后拼接起来
    def f5(self):
        ans = []
        for m in self.markdown:
            q = self.f1(m)
            if q == H:
                p = self.f2(m)
            elif q == P:
                p = self.f3(m)
            else:
                p = self.f4(m)

            ans.append(p)
        self.html = "\n".join(ans)

    # 将区块内转化
    def f6(self):
        def tmp1(matched):
            Text = matched.group("Text")
            Text = Text[1:-1]
            return f"<em>{Text}</em>"

        self.html = re.sub("(?P<Text>_.*?_)", tmp1, self.html)

        def tmp2(matched):
            Text = matched.group("Text")
            Text= Text[1:-1]
            Link = matched.group("Link")
            Link = Link[1:-1]
            return f'<a href="{Link}">{Text}</a>'
        self.html = re.sub('(?P<Text>[[].*?[]])(?P<Link>[(].*?[)])', tmp2, self.html)
        print(self.html)


translator = Translator()
translator.f5()
translator.f6()