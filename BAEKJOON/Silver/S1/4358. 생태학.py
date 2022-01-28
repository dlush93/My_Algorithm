import sys
input = sys.stdin.readline

trees = dict()
whole_cnt = 0
while True:
   name = input().rstrip()
   if not name:
       break
   if name not in trees:
       trees[name] = 1
   else:
       trees[name] += 1
   whole_cnt += 1
tree_list = sorted(trees.items())
for val in tree_list:
    tree, cnt = val
    print(f'{tree} {cnt/whole_cnt*100:.4f}')