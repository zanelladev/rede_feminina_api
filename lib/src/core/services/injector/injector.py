class Injector:
    _registry = {}

    @staticmethod
    def register(class_type, instance):
        Injector._registry[class_type] = instance

    @staticmethod
    def retrieve(class_type):
        return Injector._registry.get(class_type)
