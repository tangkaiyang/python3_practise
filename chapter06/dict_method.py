a = dict()
a = {'booby1':{"company": "imooc"},
     "bobby2": {"company": "imooc"}
     }
# clear
# a.clear()
# pass

# 浅拷贝 修改new_dict会影响到a,直接将bobby1的值指向{"company":"imooc"}
# copy, 返回浅拷贝
# new_dict = a.copy()
# new_dict["bobby1"]["company"] = "imooc3"

import copy
new_dict = copy.deepcopy(a)
new_dict["bobby1"]["company"] = "imooc3"


# fromkeys
new_list = ["bobby1", "bobby2"]

new_dict = dict.fromkeys(new_list, {"company": "imooc"})

# new_dict["bobby"]
new_dict.get("bobby", {}) # 避免使用不存在的key导致报错

for key, value in new_dict.items():
    print(key, value)

# setdefault 取值加设置值
default_value = new_dict.setdefault("bobby", "imooc")

# update 将iterable合并
new_dict.update({"bobby": "imooc"})

# 传入iterable
new_dict.update(bobby = "imooc", bobby3 = "imooc")

new_dict.update([("bobby", "imooc"), ("bobby3", "imooc")])
new_dict.update((("bobby", "imooc"), ("bobby3", "imooc")))
