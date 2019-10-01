

def singleton(cls):
    __instances = {}

    def get_instance():
        if cls not in __instances:
            __instances[cls] = cls()
        return get_instance


@singleton
class MySingleton:
    x = 5

    def foo(self):
        pass


instance = MySingleton()
print(instance.x)

instance2 = MySingleton()
instance2.x = 15

print(instance2.x)
print(instance.x)
