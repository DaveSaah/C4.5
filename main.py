from c45 import C45

c1 = C45("data/iris/iris.data", "data/iris/iris.names")
# c1 = C45(
#     "data/breast_cancer/breast_cancer.data", "data/breast_cancer/breast_cancer.names"
# )
c1.fetchData()
c1.preprocessData()
c1.generateTree()
c1.printTree()
